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

# admin_endpoint = "dataservice/admin/user"

# payload = {
#     "group": ["netadmin"],
#     "description": "Test User",
#     "userName": "test_user",
#     "password": "Password!23"
# }

# response = requests.post(
#     url=f"{base_url}{admin_endpoint}", headers=headers, data=json.dumps(payload), verify=False)

# print(response)
# print(response.text)

pw_endpoint = "dataservice/admin/user/password/test_user"

payload = {
    "userName": "test_user",
    "password": "pass"
}

response = requests.put(
     url=f"{base_url}{pw_endpoint}", headers=headers, data=json.dumps(payload), verify=False)

print(response)
print(response.text)