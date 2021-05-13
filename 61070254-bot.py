import json
import urllib.parse
import requests

url = "https://10.0.15.117/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/name/Loopback61070254"
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
}
username = "admin"
password = "cisco"

result = requests.get(url, auth=(username, password), headers=headers, verify=False)
print(result)

response_json = result.json()
print(response_json[""][4]["oper-status"])
print(json.dumps(response_json, indent=4))

accesstoken = "ZDFiOWQ2OTItN2I4OS00MGI4LTlhYzYtMjFkN2JkNGI2NjhmZmUwYzVhM2QtMzU0_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f"
headers = {
 'Authorization': 'Bearer {}'.format(accesstoken),
 'Content-Type': 'application/json'
}

def ls_room():
    url_list_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_list_room, headers=headers).json()
    print("list of rooms:")
    for i in json_data["items"]:
        print("-", i["title"])
ls_room()

check = input("what room? ")
def room():
    url_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_room, headers=headers).json()
    for i in json_data["items"]:
        if i["title"] == check:
            return i["id"]

def messages():
    url_message = "https://webexapis.com/v1/messages"
    params = {"roomId": room(), "max":1}
    json_data = requests.get(url_message, headers=headers, params=params).json()
    return json_data["items"][0]["text"]

def post_message():
    url = "https://webexapis.com/v1/messages"
    message = "test test"
    params = {"roomId": room(), "markdown": message}
    requests.post(url, headers=headers, json=params)
    # print(res.json())

while True:
    if messages()=="61070254":
        post_message()
        print(messages())
    else:
        print(messages())