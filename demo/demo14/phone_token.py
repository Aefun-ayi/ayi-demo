import requests
import urllib.parse


login_url = 'https://edc.vigame.cn:6115/all/login'
login_data = {"value": "eyJ1bmFtZSI6InBhbmppYW53ZWkiLCJ1c2VyX2lkIjoicGFuamlhbndlaSIsIndiYXBwaWQiOjE2ODQzOTg5MDQ5NTMsInB3IjoicGFuamlhbndlaSIsInB3ZCI6InBhbmppYW53ZWkiLCJuZXdMb2ciOnRydWUsInN5c19tYXJrIjoic2VydmljZSJ9",
              "indexCode": "QmxhY2tsaXN0RGV2aWNlRmlsdGVyaW5nXzJGb01vdmU="}
login_headers = {"Content-Type": "application/x-www-form-urlencoded"}

encoded_data = urllib.parse.urlencode(login_data)
login = requests.post(url=login_url, headers=login_headers, data=encoded_data)

print(login.json().get('token'))


black_list_url = 'https://edc.vigame.cn:6115/mobile/blackConfig/list'
black_list_data = {"start":"0",
                   "limit":"100",
                   "type":"white",
                   "key":"A5AE8F21-C00F-AA32-3211-A290BFC43A18",
                   "token":f"{login.json().get('token')}",
                   "indexCode":"QmxhY2tsaXN0RGV2aWNlRmlsdGVyaW5nXzJGb01vdmU="}
black_list_headers = {"Content-Type": "application/x-www-form-urlencoded"}
black_encoded_data = urllib.parse.urlencode(black_list_data)
black = requests.post(url=black_list_url, headers=black_list_headers, data=black_encoded_data)

print(black.json())