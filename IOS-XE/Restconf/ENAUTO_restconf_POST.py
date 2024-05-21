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

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback150",
        "description": "RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.100.1",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {}
    }
}

response = requests.post(url=url, headers=headers, verify=False, data=json.dumps(payload), auth=(router["username"], router["password"]))

print(response)

if response.status_code == 201:
    print(response)
    print(response.text)