import requests
import base64


class AuditRequest():
    def __init__(self, pid, cha, brand, ver, uid):
        self.pid = pid
        self.cha = cha
        self.brand = brand
        self.ver = ver
        self.uid = uid

    def Phead(self):
        txt = f'cha={self.cha},p_id={self.pid},ver={self.ver},brand={self.brand},uid={self.uid}'
        s = txt.encode("utf-8")  # 对接口需要传值的参数进行转义
        code = base64.b64encode(s).decode("utf-8")
        return code

    def Audit_request_test(self):
        url = "https://sunny-test.careduka.com/sunny-api/app/version"
        payload = {}
        headers = {
            'Phead': self.Phead(),
            'Ex-Head': 'aV9jb2RlPTE2NDI0Mzk2MTYwNDY4MjU0NzI=',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()


    def Audit_request_release(self):
        url = "https://sunny.careduka.com/sunny-api/app/version"
        payload = {}
        headers = {
            'Phead': self.Phead(),
            'Ex-Head': 'aV9jb2RlPTE2NDI0Mzk2MTYwNDY4MjU0NzI=',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

#
# if __name__ == "__main__":
#     a = AuditRequest(pid=38726, ver=1000, cha='csj', uid=10001, brand='OCEAN_ENGINE')
#     print(a.Audit_request())
