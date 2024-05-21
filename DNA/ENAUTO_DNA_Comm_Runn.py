import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint  = "system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password), verify=False).json() #Converts 

token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Content-Type": "application\json"
}

device_url = "intent/api/v1/network-device?family=Switches and Hubs&series=Cisco Catalyst 9000 Series Virtual Switches"

dev_response = requests.get(
    url=f"{base_url}{device_url}", headers=headers, verify=False).json()

print(json.dumps(dev_response, indent=2))
#print(f"{dev_response['response'][0]['id']}")

device_Ids = []
for device in dev_response['response']:
    device_id = device['id']
    device_Ids.append(device_id)

payload = {
    "commands": [
        "show version",
        "show inventory"
    ],
    "deviceUuids" : device_Ids
}

command_endpoint = "intent/api/v1/network-device-poller/cli/read-request"

cli_response = requests.post(
    url=f"{base_url}{command_endpoint}", headers=headers, data=json.dumps(payload), verify=False)

print(cli_response.text)

