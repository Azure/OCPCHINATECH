"""
Python support for Azure automation is now public preview!

Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk

This tutorial runbook demonstrate how to authenticate against Azure using the Azure automation service principal and then lists the resource groups present in the specified subscription.
"""
import json
import requests
import datetime
import hashlib
import hmac
import base64

import azure.mgmt.resource
import azure.mgmt.compute
import automationassets
from msrestazure.azure_cloud import AZURE_CHINA_CLOUD

# For Authentication Credentials
def get_automation_runas_credential(runas_connection, resource_url, authority_url ):
    """ Returns credentials to authenticate against Azure resoruce manager """
    from OpenSSL import crypto
    from msrestazure import azure_active_directory
    import adal

    # Get the Azure Automation RunAs service principal certificate
    cert = automationassets.get_automation_certificate("AzureRunAsCertificate")
    pks12_cert = crypto.load_pkcs12(cert)
    pem_pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pks12_cert.get_privatekey())

    # Get run as connection information for the Azure Automation service principal
    application_id = runas_connection["ApplicationId"]
    thumbprint = runas_connection["CertificateThumbprint"]
    tenant_id = runas_connection["TenantId"]

    # Authenticate with service principal certificate
    authority_full_url = (authority_url + '/' + tenant_id)
    context = adal.AuthenticationContext(authority_full_url)
    return azure_active_directory.AdalAuthentication(
        lambda: context.acquire_token_with_client_certificate(
            resource_url,
            application_id,
            pem_pkey,
            thumbprint)
    )

# Authenticate to Azure using the Azure Automation RunAs service principal
runas_connection = automationassets.get_automation_connection("AzureRunAsConnection")
resource_url = AZURE_CHINA_CLOUD.endpoints.active_directory_resource_id
authority_url = AZURE_CHINA_CLOUD.endpoints.active_directory
resourceManager_url = AZURE_CHINA_CLOUD.endpoints.resource_manager
azure_credential = get_automation_runas_credential(runas_connection, resource_url, authority_url)

# Intialize the resource management client with the RunAs credential and subscription
resource_client = azure.mgmt.resource.ResourceManagementClient(
    azure_credential,
    str(runas_connection["SubscriptionId"]),
    base_url=resourceManager_url)

# Intialize the compute management client for Virtual Machines
compute_client = azure.mgmt.compute.ComputeManagementClient(
    azure_credential,
    str(runas_connection['SubscriptionId']),
    base_url=resourceManager_url)

all_vms = compute_client.virtual_machines.list_all()
vmPowerStates = []

# Retrival All VM Status
for vm in all_vms:
    vmID = vm.id
    vmRG = vmID.split("/")[4]
    vmInstanceView = compute_client.virtual_machines.get(vmRG, vm.name,  expand='instanceView')
    vmExtendGraph = {}
    vmExtendGraph['vm_name'] = vm.name
    vmExtendGraph['vm_rg'] = vmRG
    vmExtendGraph['vm_state'] = vmInstanceView.instance_view.statuses[1].display_status
    vmExtendGraph['graph_tag'] = 'extend_graph_vm_state'
    vmPowerStates.append(vmExtendGraph)

# Log Analytics Creds
logAnalyticsCreds = automationassets.get_automation_credential("logAnalyticsCreds")
workspaceId = logAnalyticsCreds['username']
key = logAnalyticsCreds['password']

# Send Datas to Log Analytics
log_type = 'vmExtendGraph'
body = json.dumps(vmPowerStates)

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

post_data(workspaceId, key, body, log_type)