import requests
import json
#import logging

#logging.basicConfig(level=logging.DEBUG)

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint  = "system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password), verify=False).json() #Converts response to JSON.

token = auth_response['Token']
# print(token)

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

events_endpoint = "intent/api/v1/events?tags=ASSURANCE"
#events_url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/events?tags=ASSURANCE'

events_response = requests.get(url=f"{base_url}{events_endpoint}", headers=headers, verify=False).json()

print(json.dumps(events_response, indent=2))
# print(events_response)
# print(events_response.text)


events_list = ["NETWORK-DEVICES-2-153", "NETWORK-DEVICES-3-154"]

payload = [
    {
        "name": "CBT Nuggets subs AP",
        "subscriptionEndpoints": [
            {
                "subscriptionDetails": {
                    "connectorType": "REST",
                    "name": "My Azure Python Function App",
                    "description": "ingest payload into CosmosDB",
                    "method": "POST",
                    "url": "https://knoxsfunction.azurewebsites.net/dnaApp"
                }
            }
        ],
        "filter": {
            "eventsIds": events_list
        }
    }
]

sub_endpoint = "intent/api/v1/event/subscription"

event_sub_response = requests.post(
    url=f"{base_url}{sub_endpoint}", headers=headers, data=json.dumps(payload), verify=False)

print(event_sub_response.status_code)
print(event_sub_response.text)