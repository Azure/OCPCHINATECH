# -*- coding: utf-8 -*-
import os, requests, uuid, json

key_var_name = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
subscription_key = 'key'

endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
endpoint = 'endpoint'

path = '/translate?api-version=3.0'
params = '&to=de&to=en'
constructed_url = endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
    'text': '你好，这是文本翻译试验环节'
}]

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': ')))