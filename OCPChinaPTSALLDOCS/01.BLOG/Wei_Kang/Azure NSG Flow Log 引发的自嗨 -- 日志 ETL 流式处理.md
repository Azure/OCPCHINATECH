上一篇中我们已经完成了事件驱动的日志注入的事件驱动的部分，本篇我们继续介绍关于由事件驱动产生的增量 NSG Flow Log 如何进行 ETL 处理，然后流式的方式注入到 Data Explorer 分析引擎中。我们先来回顾一下整体架构图，当 NSG Flow Log 的日志事件产生后，我们通过调用 Function 服务来进行对日志的 ETL 然后再写入到 EventHub 以流式的方式注入到 Data Explorer。

![images](https://github.com/JanlenHu/OCPChinaPTSALLDOCS/blob/master/01.BLOG/images/Azure%20NSG%20Flow%20Log%20引发的自嗨%20--%20日志%20ETL%20流式处理1.png)


当 Event Grid 产生 Blob event 后会通过 Webhook 的方式来调用 Function 服务，在 Function 服务中通过 Severless Code 来实现 ETL 的逻辑。这里的 ETL 逻辑比较简单，每个增量的日志内 Flow Log 是以嵌套的方式出现的，我们需要将 Log 进行扁平化操作，抽取每一个叶子节点日志，并将这些日志送入的 Event Hub 实现流化。

我们来看一下 NSG Flow Log 的格式，其中 Records 数组中以每分钟为单位增量产生该分钟内产生的 Flow Log，日志的数据结构中 flowTuples 是叶子节点，记录着匹配 NSG 规则的的具体 Flow 的信息（如时间戳，源 IP，目的 IP，源端口，目的端口，包统计信息，字节统计信息等），在扁平化操作中把每一个 Flow 的信息抽取出来然后注入到 Event Hub 即可，如果我们需要对原有的 Flow Log 信息做补充，也可以在这里做操作（如追加 IP 地址的 Geo 属性等）。
```
{
    "records": [
        {
            "time": "2018-11-13T12:00:35.3899262Z",
            "systemId": "a0fca5ce-022c-47b1-9735-89943b42f2fa",
            "category": "NetworkSecurityGroupFlowEvent",
            "resourceId": "/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/FABRIKAMRG/PROVIDERS/MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/FABRIAKMVM1-NSG",
            "operationName": "NetworkSecurityGroupFlowEvents",
            "properties": {
                "Version": 2,
                "flows": [
                    {
                        "rule": "DefaultRule_DenyAllInBound",
                        "flows": [
                            {
                                "mac": "000D3AF87856",
                                "flowTuples": [
                                    "1542110402,94.102.49.190,10.5.16.4,28746,443,U,I,D,B,,,,",
                                    "1542110424,176.119.4.10,10.5.16.4,56509,59336,T,I,D,B,,,,",
                                    "1542110432,167.99.86.8,10.5.16.4,48495,8088,T,I,D,B,,,,"
                                ]
                            }
                        ]
                    },
                    {
                        "rule": "DefaultRule_AllowInternetOutBound",
                        "flows": [
                            {
                                "mac": "000D3AF87856",
                                "flowTuples": [
                                    "1542110377,10.5.16.4,13.67.143.118,59831,443,T,O,A,B,,,,",
                                    "1542110379,10.5.16.4,13.67.143.117,59932,443,T,O,A,E,1,66,1,66",
                                    "1542110379,10.5.16.4,13.67.143.115,44931,443,T,O,A,C,30,16978,24,14008",
                                    "1542110406,10.5.16.4,40.71.12.225,59929,443,T,O,A,E,15,8489,12,7054"
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        {
            "time": "2018-11-13T12:01:35.3918317Z",
            "systemId": "a0fca5ce-022c-47b1-9735-89943b42f2fa",
            "category": "NetworkSecurityGroupFlowEvent",
            "resourceId": "/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/FABRIKAMRG/PROVIDERS/MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/FABRIAKMVM1-NSG",
            "operationName": "NetworkSecurityGroupFlowEvents",
            "properties": {
                "Version": 2,
                "flows": [
                    {
                        "rule": "DefaultRule_DenyAllInBound",
                        "flows": [
                            {
                                "mac": "000D3AF87856",
                                "flowTuples": [
                                    "1542110437,125.64.94.197,10.5.16.4,59752,18264,T,I,D,B,,,,",
                                    "1542110475,80.211.72.221,10.5.16.4,37433,8088,T,I,D,B,,,,",
                                    "1542110487,46.101.199.124,10.5.16.4,60577,8088,T,I,D,B,,,,",
                                    "1542110490,176.119.4.30,10.5.16.4,57067,52801,T,I,D,B,,,,"
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        ...
```
在前面介绍 Blob Event 时候介绍到，事件消息中的 contentLength 字段是一个累计值，表示当前 Blob 的总大小，所以实际上 Flow Log 的每分钟的增量是前后两次事件 contentLength 字段的插值。而 Function 服务是一个无状态的服务，所以这里我们借助 Azure Table 服务来做每次 Flow Log 处理偏移量的持久化，当新的 Flow Log 事件产生时，通过从 Azure Table 中读取前序偏移量从而计算出差值。下面是 Function 中托管的 Python Code 示例，创建 Function 服务时，大家注意创建 Consumption Model 计费模式，计算算力按照计算时长收费，处理完毕资源释放，持久化在外部来实现。
```
import json
import logging

import azure.functions as func
from azure.storage.blob.baseblobservice import BaseBlobService
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from pandas import DataFrame
from pandas.io.json import json_normalize
from azure.eventhub import EventHubClient, Sender, EventData

# Download Raw NSG Flow Log String
def downloadblobblock(accountname, accountkey, containername, blobname, startpoint, endpoint):
    base_blob_service = BaseBlobService(accountname, accountkey)
    blockstring = base_blob_service.get_blob_to_bytes(containername, blobname, start_range=startpoint, end_range=endpoint).content.decode('ASCII')
    return blockstring

# Flatten NSG Flow Log and Stream to EventHub
def ingestlogentry(logblockstring, eventhubaddr, evenhubaccount, eventhubaccesskey):
    logblockjson = json.loads(logblockstring)
    logblockdf = json_normalize(logblockjson)
    logblocknormalizejson = json.loads(logblockdf.to_json(orient='records'))
    logingest = logblocknormalizejson[0]['properties.flows']
    eventhubclient = EventHubClient(eventhubaddr, debug=False, username=evenhubaccount, password=eventhubaccesskey)
    eventhubsender = eventhubclient.add_sender(partition="0")
    eventhubclient.run()

    ruleloop = len(logingest)
    for i in range(ruleloop):
        output = logblocknormalizejson[0]
        output.pop('properties.flows')
        output.pop('properties.Version')
        #print(logingest[i])
        rule = logingest[i].get('rule')
        output['rule'] = rule
        flows = logingest[i].get('flows')
        flowsloop = len(flows)
        for j in range(flowsloop):
            #print(flows[j])
            mac = flows[j].get('mac')
            output['mac'] = mac
            flowtuples = flows[j].get('flowTuples')
            flowtuplesloop = len(flowtuples)
            for k in range(flowtuplesloop):
                #print(flowtuples[k])
                output['flowtuples'] = flowtuples[k]
                logging.info('Send an event: %s', output)
                eventhubsender.send(EventData(json.dumps(output)))

def main(event: func.EventGridEvent):
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)

    blobaccount = 'Put Your Blob Account Name Here'
    blobaccesskey = 'Put Your Blob Account Access Key Here'
    blobcontainername ='insights-logs-networksecuritygroupflowevent'

    tableaccount = 'Put Your Table Account Name Here'
    tableaccesskey = 'Put Your Table Access Key Here'
    tablename = 'Put Your Table Name Here'

    eventhubadress = "Put Your EventHub Address Here, Format Like amqps://"
    eventhubuser = "Put Your EventHub Identity Here"
    evnethubkey = "Put Your EventHub Access Key Here"

    EventData = event.get_json()
    imresult = json.dumps(EventData)
    logging.info('Python EventGrid trigger processed an event: %s', imresult)
    LogBlockLength = EventData['contentLength']
    BlobNameStrOffset = EventData['url'].rfind("insights-logs-networksecuritygroupflowevent/") + len("insights-logs-networksecuritygroupflowevent/")
    BlobName = EventData['url'][BlobNameStrOffset:]
    BlobEntityName = EventData['url'].replace('/', '-')

    table_service = TableService(tableaccount, tableaccesskey)

    try:
        LogBlockEntity = table_service.get_entity(tablename, BlobEntityName, '001')
        PreviousBlobLength = LogBlockEntity.ContentLength
        LogBlockStartOffset = PreviousBlobLength - 1
        LogBlockEndOffset = LogBlockLength -3
        LogString = downloadblobblock(blobaccount, blobaccesskey, blobcontainername, BlobName, LogBlockStartOffset, LogBlockEndOffset)
        try:
            ingestlogentry(LogString, eventhubadress, eventhubuser, evnethubkey)
        except Exception:
            pass
        UpdatedLogBlockEntity = Entity()
        UpdatedLogBlockEntity.PartitionKey = BlobEntityName
        UpdatedLogBlockEntity.RowKey = '001'
        UpdatedLogBlockEntity.ContentLength = LogBlockLength
        table_service.update_entity(tablename, UpdatedLogBlockEntity)
    except Exception:
        UpdatedLogBlockEntity = Entity()
        UpdatedLogBlockEntity.PartitionKey = BlobEntityName
        UpdatedLogBlockEntity.RowKey = '001'
        UpdatedLogBlockEntity.ContentLength = LogBlockLength
        table_service.insert_or_replace_entity(tablename, UpdatedLogBlockEntity)
        LogBlockStartOffset = 12
        LogBlockEndOffset = LogBlockLength -3
        LogString = downloadblobblock(blobaccount, blobaccesskey, blobcontainername, BlobName, LogBlockStartOffset, LogBlockEndOffset)
        try:
            ingestlogentry(LogString, eventhubadress, eventhubuser, evnethubkey)
        except Exception:
            pass
```
上述涉及服务的配置方法这里不做一一赘述，关键的 Azure Function 服务的配置部署可以通过 Visual Studio Code 来实现，可以参阅如下链接：https://code.visualstudio.com/docs/python/tutorial-azure-functions 。 下一篇我会为大家介绍后续流式日志的采集以及在 Data Explorer 中的查询示例，敬请期待。
