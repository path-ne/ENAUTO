import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint  = "system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password), verify=False).json() #Converts 

token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Content-Type": "application/json"
}

cred_cli_endpoint = "intent/api/v1/global-credential?credentialSubType=CLI"

cli_response = requests.get(url=f"{base_url}{cred_cli_endpoint}", headers=headers, verify=False).json()['response'][0]
print(cli_response)
cli_cred = cli_response['id']


cred_snmp_endpoint = "intent/api/v1/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY"

snmp_response = requests.get(url=f"{base_url}{cred_snmp_endpoint}", headers=headers, verify=False).json()['response']
print(snmp_response)
#snmp_cred = snmp_response['id']

payload = {
    "name" : "Discovery",
    "discoveryType" : "Range",
    "ipAddressList" : "10.10.20.30-10.10.20.254",
    "timeout" : 1,
    "protocolOrder" : "ssh,telnet",
    "preferredMgmtIpMethod" : "None",
    "globalCredentialList" : [cli_cred]
}

discovery_endpoint = "intent/api/v1/discovery"

disc_response = requests.post(
    url=f"{base_url}{discovery_endpoint}", headers=headers, data=json.dumps(payload), verify=False)
print(disc_response)
print(disc_response.text)