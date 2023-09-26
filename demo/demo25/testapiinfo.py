import base64

from urllib import parse
import requests


#
# andId=54dd84f4b91ee00b
# &appid=39779&cha=viyy
# &imei=6a4042303920b05c5a422e9333711e4a1ad88fdae3527ec7572291005ee0ea5d
# &lsn=226043268
# &oaid=6a4042303920b05c5a422e9333711e4a1ad88fdae3527ec7572291005ee0ea5d\
# &platform=android\
#           &prjid=39779004\
#                  &timestamp=1695697131193\
#                             &sign=ae0d28c98bbf808f8dd078e6afe88412\
#                                   &\isDebug=1
prjid='39879002'
cha='viyy'
appid='39879'

andId='54dd84f4b91ee00b'
imei='6a4042303920b05c5a422e9333711e4a1ad88fdae3527ec7572291005ee0ea5d'
lsn='226043268'
oaid='6a4042303920b05c5a422e9333711e4a1ad88fdae3527ec7572291005ee0ea5d'
platform='android'
timestamp='1695697131200'
sign='575c0cd50f5e323e4b421ce07ecbf9b5'
isDebug = 1

txt = f"prjid={prjid}&cha={cha}&appid={appid}&andId={andId}&imei={imei}&lsn={lsn}&oaid={oaid}&platform={platform}&timestamp={timestamp}&sign={sign}&isDebug={isDebug}"
s = txt.encode("utf-8")  # 对接口需要传值的参数进行转义
code = base64.b64encode(s).decode("utf-8")
# print(code)
decoded_url = parse.quote(code)
print(decoded_url)

a = f"https://s.hzsnwlkj.com/dsrCtr/v2?value={decoded_url}"

head = {"x-dsa-trace-id": "169569713147ac9a1abbd938da80e5b182b37d13de",
        "Connection":"keep-alive"
        }
http_get = requests.get(url=a, headers=head)
connect = http_get.json()
print(connect)
