"""
Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""
import sys
import csv
import json
import urllib2

url = sys.argv[1]

cost_file = urllib2.urlopen(url)
costFile = csv.reader(cost_file)

def isTitleLine(row):
    if not row : return False
    for item in row:
        if 'SubscriptionGuid' in item:
            return True
    return False

import requests
import datetime
import hashlib
import hmac
import base64

# Update the customer ID to your Log Analytics workspace ID
customer_id = '$yourLogAnalyticsID'
# For the shared key, use either the primary or the secondary Connected Sources client authentication key
shared_key = "yourLogAnalyticsKey"

# The log type is the name of the event that is being submitted
log_type = 'TestCost'

#####################
######Functions######
#####################

# Build the API signature
def build_signature(customer_id, shared_key, date, content_length, method, content_type, resource):
    x_headers = 'x-ms-date:' + date
    string_to_hash = method + "\n" + str(content_length) + "\n" + content_type + "\n" + x_headers + "\n" + resource
    bytes_to_hash = bytes(string_to_hash).encode('utf-8')
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest())
    authorization = "SharedKey {}:{}".format(customer_id,encoded_hash)
    return authorization

# Build and send a request to the POST API
def post_data(customer_id, shared_key, body, log_type):
    method = 'POST'
    content_type = 'application/json'
    resource = '/api/logs'
    rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    content_length = len(body)
    signature = build_signature(customer_id, shared_key, rfc1123date, content_length, method, content_type, resource)
    #uri = 'https://' + customer_id + '.ods.opinsights.azure.com' + resource + '?api-version=2016-04-01'
    uri = 'https://' + customer_id + '.ods.opinsights.azure.cn' + resource + '?api-version=2016-04-01'

    headers = {
        'content-type': content_type,
        'Authorization': signature,
        'Log-Type': log_type,
        'x-ms-date': rfc1123date
    }

    response = requests.post(uri,data=body, headers=headers)
    if (response.status_code >= 200 and response.status_code <= 299):
        print 'Accepted'
    else:
        print "Response code: {}".format(response.status_code)

with open('tempOut.csv', 'wb') as outFile:
    writer = csv.writer(outFile)
    convertToEng = False
    for row in costFile:
        if len(row) <= 5:
            continue
        if not convertToEng and isTitleLine(row):
            convertToEng = True
            titleRow = ['AccountOwnerId', 'Account Name', 'ServiceAdministratorId', 'SubscriptionId', 'SubscriptionGuid', 'Subscription Name', 'Date', 'Month', 'Day', 'Year', 'Product', 'Meter ID', 'Meter Category', 'Meter Sub-Category', 'Meter Region', 'Meter Name', 'Consumed Quantity', 'ResourceRate', 'ExtendedCost', 'Resource Location', 'Consumed Service', 'Instance ID', 'ServiceInfo1', 'ServiceInfo2', 'AdditionalInfo', 'Tags', 'Store Service Identifier', 'Department Name', 'Cost Center', 'Unit of Measure', 'Resource Group', '']
            writer.writerow(titleRow)
        else:
            writer.writerow(row)

with open('tempOut.csv', 'rb') as costs:
    costDetails = csv.DictReader(costs)
    data = []
    count = 0
    body = ""

    import time

    ts = time.time()

    for row in costDetails:
        row['CostTableUpdated'] = ts
        data.append(row)
        count += 1
        if count >= 5000:
            body = json.dumps(data)
            post_data(customer_id, shared_key, body, log_type)
            data = []
            body = ""
            count = 0

    if count > 0:
        body = json.dumps(data)
        post_data(customer_id, shared_key, body, log_type)







