import requests
import json
import pprint

router = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "port": "443",
    "username": "admin",
    "password": "C1sco12345"
}

headers = {
    "Accept" : "application/yang-data+json",
    "Content-Type" : "application/yang-data+json"
}

# url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-routing:routing"

# response = requests.get(url=url, headers=headers, verify=False, auth=(router["username"], router["password"])).json()

# print(json.dumps(response, indent=5))

# url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

# response = requests.get(url=url, headers=headers, verify=False, auth=(router["username"], router["password"])).json()

# print(json.dumps(response, indent=2))


url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"

response = requests.get(url=url, headers=headers, verify=False, auth=(router["username"], router["password"])).json()

print(json.dumps(response, indent=2))