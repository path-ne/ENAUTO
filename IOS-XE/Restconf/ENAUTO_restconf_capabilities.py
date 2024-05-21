import requests
import json
import pprint

router = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "port": "443",
    "username": "admin",
    "password": "C1sco12345"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

headers = {
    "Accept" : "application/yang-data+json",
    "Content-Type" : "application/yang-data+json"
}

response = requests.get(url=url, headers=headers, verify=False, auth=(router["username"], router["password"]))

if response.status_code == 200:
    response_dict = response.json()
    #pprint.pprint(response_dict)
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(capability)