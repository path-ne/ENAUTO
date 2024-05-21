from netmiko import ConnectHandler

router = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "port": "22",
    "username": "admin",
    "password": "C1sco12345",
    "device_type": "cisco_ios"
}

configs = ['int loopback203', 'ip address 172.16.103.1 255.255.255.0', 'description Netmiko set', 'no shut']

try:
    c = ConnectHandler(**router)
    c.enable()
    #send = c.send_config_set(configs)
    send = c.send_config_from_file('/mnt/c/Users/Desktop/Desktop/LABs/ENAUTO/Git/Code/Networking/IOS/Netmiko/commands.txt')
    response = c.send_command("show ip int brief", use_textfsm=True)
    c.disconnect()
except Exception as ex:
    print(ex)
else:
    print(send)
    print(response)
