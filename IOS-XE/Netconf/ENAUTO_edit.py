from ncclient import manager
from router_info import router

config_template = open("/mnt/c/Users/Desktop/Desktop/LABs/ENAUTO/Git/Code/Networking/IOS-XE/ios_config.xml").read()

print(config_template)

netconf_config = config_template.format(
    interface_name="GigabitEthernet3", interface_desc="test description")

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.edit_config(netconf_config, target="running")

print(response)