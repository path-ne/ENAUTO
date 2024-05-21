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
    "Content-Type": "application/json"
}

# Inventory section. 
device_endpoint = "intent/api/v1/network-device"

device_response = requests.get(
    url=f"{base_url}{device_endpoint}", headers=headers, verify=False).json()
print(json.dumps(device_response, indent=2))