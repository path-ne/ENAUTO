import requests
import json

base_url = "https://10.10.20.90:8443/"
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

create_temp_url = "dataservice/template/device/feature"

payload = {
  "templateName": "vEdge_Device_Template",
  "templateDescription": "Demo device template",
  "deviceType": "vedge-100",
  "configType": "template",
  "factoryDefault": False,
  "policyId": "",
  "featureTemplateUidRange": [],
  "generalTemplates": [
    {
      "templateId": "3b30e089-2e26-44f1-b5b2-ac44f3f4279e",
      "templateType": "aaa"
    },
    {
      "templateId": "0419c4f6-eb61-4048-a3fe-78ea7f7248b0",
      "templateType": "bfd-vedge"
    },
    {
      "templateId": "7d7396a2-4715-44d8-8f6e-ddf0ca06be44",
      "templateType": "system-vedge",
    },
    {
      "templateId": "171e9bd4-7a7b-460d-b692-83f0d5ce0124",
      "templateType": "vpn-vedge",
      "subTemplates": [
        {
          "templateId": "a632ee5f-f489-46ec-8761-1b493d5a6a40",
          "templateType": "vpn-vedge-interface"
        }
      ]
    },
  ]
}

response = requests.post(
    url=f"{base_url}{create_temp_url}", headers=headers, data=json.dumps(payload), verify=False)

print(response)
print(response.text)
# print(json.dumps(response, indent=2))