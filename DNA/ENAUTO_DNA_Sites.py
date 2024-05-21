import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint  = "system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password), verify=False).json() #Converts response to a python dictionary.

token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Content-Type": "application\json"
}

# Site section. 
sites_endpoint = "intent/api/v1/site"

# site_response = requests.get(
#     url=f"{base_url}{sites_endpoint}", headers=headers, verify=False).json()
# print(json.dumps(site_response, indent=2))

# Topology Section

topology_endpoint = "intent/api/v1/topology/site-topology"

top_response = requests.get(
    url=f"{base_url}{topology_endpoint}", headers=headers, verify=False).json()
#print(json.dumps(top_response, indent=2))

for site in top_response['response']['sites']:
    print(site['name'], '->', site['groupNameHierarchy'])
#print (top_response)