import datetime
import urllib.parse
import requests

rtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 定义待编码的字符串
# s = "2023-06-25 17:18:44"
# 编码字符串为URL编码格式
encoded_s = urllib.parse.quote(rtime)
url = f'https://gateway.test.maxhub.vip/trigger/api/auth/staff/admin/room/statistic-data?currentDate={encoded_s}'
data = {"Authorization": "Bearer fa777dc8-3fa4-4b2c-8a37-b9e6a6a871d1",
        "x-auth-userid": "579cbc25-b831-411f-a201-35f9f13d3d42",
        "x-company-id": "85aad105-c7b9-4131-8e3b-a8debdad9cc8",
        "x-member-id": "1631611361655652354"}
req = requests.get(url, headers=data)

print(req.json())