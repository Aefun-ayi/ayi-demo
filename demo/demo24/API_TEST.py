import requests
import base64


pid = 39856
cha = 'csj'
brand = 'OCEAN_ENGINE'
ver = 1000
uid = 10001

txt = f'cha={cha},p_id={pid},ver={ver},brand={brand},uid={uid}'
s = txt.encode("utf-8")  # 对接口需要传值的参数进行转义
code = base64.b64encode(s).decode("utf-8")

url = "https://sunny-test.careduka.com/sunny-api/app/version"
payload = {}
headers = {
   'Phead': code,
   'Ex-Head': 'aV9jb2RlPTE2NDI0Mzk2MTYwNDY4MjU0NzI=',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.json())