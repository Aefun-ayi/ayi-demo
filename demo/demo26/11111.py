import requests

url = 'http://192.168.80.128:8100/ad_names'

data = {'pid': '38726001',
        'chan': 'csj'}

res = requests.post(url, data)

print(res.json())
