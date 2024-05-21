import requests
import json

base_url = "https://10.10.20.90/"
auth_endpoint = "j_security_check"

login_body = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

#sesh = requests.session()
login_response = requests.post(
    url=f"{base_url}{auth_endpoint}", data=login_body, verify=False)

cookies = login_response.headers['set-cookie']
#print(cookies)
jsessionid = cookies.split(";")[0]
#print(jsessionid)

if not login_response.ok or login_response.text:
    print("login failed")
    import sys
    sys.exit(1)
else:
    print("login succeeded")

token_headers = {
    "Cookie": jsessionid
}

token_url = "dataservice/client/token"

token_response = requests.get(
    url=f"{base_url}{token_url}", headers=token_headers, verify=False)

token = token_response.text

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Cookie": jsessionid,
    "X-XSRF-TOKEN": token
}

cert_endpoint = "dataservice/certificate/vsmart/list"

# response = requests.get(
#     url=f"{base_url}{cert_endpoint}", headers=headers, verify=False).json()

# print(json.dumps(response, indent=2))

root_endpoint = "dataservice/certificate/rootcertificate"

response = requests.get(
     url=f"{base_url}{root_endpoint}", headers=headers, verify=False).json()

print(json.dumps(response, indent=2))