from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfDriver(**my_device)
conn.open()

rpc_filter = '''
<get>
<filter xmlns:t="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper"
        type="xpath"
        select="/ospf-oper-data/ospf-state/ospf-instance[af='address-family-ipv4' and router-id=184549129]" />
</get>
'''

#ospf_xpath = '/ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id=184549129]'

response = conn.rpc(rpc_filter)

#response = conn.get_config(source="running")
print(response.result)