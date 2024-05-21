from ncclient import manager
import logging
import xmltodict
from lxml.etree import fromstring

#logging.basicConfig(level=logging.DEBUG)

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "lastorangerestoreball8876",
    "hostkey_verify": False,
    "device_params": {"name":"csr"}
}


with manager.connect(**router) as m:
    subs = ["/mdt-oper:mdt-oper-data/mdt-subscriptions","/memory-ios-xe-oper:memory-statistics/memory-statistic"]
    for sub in subs:
        rpc = f"""
            <establish-subscription
            xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications"
            xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
            <stream>yp:yang-push</stream>
            <yp:xpath-filter>{sub}</yp:xpath-filter>
            <yp:period>1000</yp:period>
            </establish-subscription>
        """
        response = m.dispatch(fromstring(rpc))
        python_response = xmltodict.parse(response.xml)
        #print (python_response)

        while True:
            sub_data = m.take_notification()
            python_sub_data = xmltodict.parse(sub_data.notification_xml)
            print(python_sub_data)
            print("------------------------------------------------------------Next subscription")
            if sub != subs[1]: #Cycles through the for loop.
                break
            
            # print(
            #     f"Sub ID: {python_sub_data['notification']['push-update']['subscription-id']}")
            
            # print(
            #     f"Name: {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['name']}")

            # print(
            #     f"Total RAM: {python_sub_data['notification']['push-update']['datastore-contents-xml']['memory-statistics']['memory-statistic'][0]['total-memory']}")
