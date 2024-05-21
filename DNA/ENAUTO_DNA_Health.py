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
    "Content-Type": "application\json"
}

# Health Section. 
health_endpoint = "intent/api/v1/client-health"

query_string = {"timestamp" : ""}

response = requests.get(
    url=f"{base_url}{health_endpoint}", headers=headers, verify=False, params=query_string).json()

#print(json.dumps(response, indent=2))

print(
    f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")

scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f" {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == 'WIRELESS':
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f" {score_value['scoreCategory']['value']}: {score_value['clientCount']}")