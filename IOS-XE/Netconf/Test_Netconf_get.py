from ncclient import manager
import xmltodict

#********************************************
# Debug connection:

#import logging

#logging.basicConfig(level=logging.DEBUG) 
#********************************************

my_device = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "hostkey_verify": False,
    # When using self generated keys by the device which can't be verfied.
    "port": 830
}

#netconf_filter = open("filter-ietf-interfaces.xml").read()

with manager.connect(**my_device) as m:
    netconf_response = m.get(filter=('xpath' , "/interfaces/interface[name='GigabitEthernet1']"))


print(netconf_response)

#python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]

#print(python_response)

#op = python_response["interface-state"]["interface"]
#config = python_response["interfaces"]["interface"]

#print(f"Name: {config['name']['#text']}")
#print(f"Packets In: {op['statistics']['in-unicast-pkts']}")
