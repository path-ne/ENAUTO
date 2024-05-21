from ncclient import manager

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


with manager.connect(**my_device, device_params={'name':'iosxe'}) as m:
    for capability in m.server_capabilities:
        print('*' * 100)
        print(' ')
        print(capability)

