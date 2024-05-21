from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "auth_username": "developer",
    "auth_password": "lastorangerestoreball8876",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfDriver(**my_device)
conn.open()

ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
    <ospf-state>
        <ospf-instance>
            <af>address-family-ipv4</af>
            <router-id>168432688</router-id>
                <ospf-area>
                    <area-id>0</area-id>
                        <ospf-interface>
                            <name>GigabitEthernet3</name>
                            <passive> </passive> 
                        </ospf-interface>
                </ospf-area>     
        </ospf-instance>
    </ospf-state>    
</ospf-oper-data>
"""

response = conn.get(
    filter_=ospf_filter, filter_type='subtree'
)

#response = conn.get_config(source="running")
print(response.result)
                                                                           