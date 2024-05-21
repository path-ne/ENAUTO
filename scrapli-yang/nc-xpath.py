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

ospf_xpath = '/ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id=184549129]'

response = conn.get(
    filter_=ospf_xpath, filter_type='xpath'
)

#response = conn.get_config(source="running")
print(response.result)

#Cisco config:
#conf t
#router ospf 999
#network 192.168.99.0 0.0.0.255 area 0
#!
#int gig 3
#ip address 192.168.99.1 255.255.255.0
