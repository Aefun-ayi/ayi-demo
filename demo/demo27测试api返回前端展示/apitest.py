# -*- coding: utf-8 -*-

import requests

url = f'https://edc.vigame.cn:6115/all/login'
head = {'value': 'eyJ1bmFtZSI6InBhbmhkIiwicHdkIjoicGFuaGQwMzE5In0',
                'indexCode': 'bG9naW4='}
response = requests.post(url, head)
tokenzhi = response.json().get('token')
print(tokenzhi)