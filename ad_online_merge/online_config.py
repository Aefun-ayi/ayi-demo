import url_cfg
import requests
import Get_Umid

class OnlineCfg():
    def __init__(self, appid, cha, pid):
        self.ip = url_cfg.ip
        self.login_cfg = url_cfg.login
        self.v2_cfg = url_cfg.v2
        self.v3fk_cfg = url_cfg.v3fk
        self.audit_cfg = url_cfg.audit
        self.custom_cfg = url_cfg.custom
        self.first_cfg = url_cfg.first
        self.dmo_cfg = url_cfg.dmo
        self.jh_cfg = url_cfg.jh
        self.blackCfg = url_cfg.blackcfg
        self.appid = appid
        self.pid = pid
        self.cha = cha

    def login(self):
        url = f'{self.ip}{self.login_cfg}'
        head = {'value': 'eyJ1bmFtZSI6InBhbmhkIiwicHdkIjoicGFuaGQwMzE5In0',
                'indexCode': 'bG9naW4='}
        response = requests.post(url, head)
        tokenzhi = response.json().get('token')
        return tokenzhi

    def v2(self):
        v2url = f'{self.ip}{self.v2_cfg}'
        head2 = {'token': f'{self.login()}',
                 'start': '0',
                 'limit': '100',
                 'appid': f'{self.appid}',
                 'cha': f'{self.cha}',
                 'prjid': '',
                 'buy_id': '',
                 'buy_act': '',
                 'status': '1',
                 'indexCode': 'VjJMb2NrQ29uZmlnX0ZvTW92ZQ%3D%3D'}

        response1 = requests.post(v2url, head2)
        return response1.json()['data']

    def v3fk(self):
        v3_url = f'{self.ip}{self.v3fk_cfg}'
        v3_head = {'token': f'{self.login()}',
                   'appidList': f'{self.appid}',
                   'chaList': '',
                   'prjid': f'',
                   'status': '',
                   'start': '1',
                   'limit': '100',
                   'indexCode': 'cHJvTmV3Umlza01hbmFnZW1lbnRDb25maWc%3D'}
        v3_res = requests.post(v3_url, v3_head)
        V3_collect = v3_res.json()['data']['list']
        if V3_collect != []:
            for d_res in V3_collect:
                if 'prjid' in dict(d_res).keys() and self.pid in dict(d_res)['prjid'] and self.pid != '':
                    return d_res
            for d_res in V3_collect:
                if 'cha' in dict(d_res).keys() and self.cha in dict(d_res)['cha']:
                    return d_res
        # return v3_res.json()['data']

    def audit(self):
        audit_url = f'{self.ip}{self.audit_cfg}'
        audithead = {'token': f'{self.login()}',
                     'appid': f"{self.appid}",
                     'cha_id': '',
                     'prjid': f'{self.pid}',
                     'note': '',
                     'limit': '100',
                     'start': '0',
                     'indexCode': 'bW9iaWxlU3ViQ2hhbm5lbENvbmZpZ19Gb01vdmU%3D'}
        audit_response = requests.post(audit_url, audithead)
        return audit_response.json()['data']

    def custom(self):
        custom_url = f'{self.ip}{self.custom_cfg}'
        custom_head = {'start': '0',
                       'limit': '100',
                       'appid': f'{self.appid}',
                       'cha': '',
                       'prjid': f'{self.pid}',
                       'status': '',
                       'params': '',
                       'token': f'{self.login()}',
                       'indexCode': 'Q3VzdG9tUGFyYW1Db25maWdfRm9Nb3Zl'}
        custom_res = requests.post(custom_url, custom_head)
        return custom_res.json()['data']

    def first(self):
        first_url = f'{self.ip}{self.first_cfg}'
        first_head = {'token': f'{self.login()}',
                      'appid': f'{self.appid}',
                      'cha': '',
                      'prjid': f'{self.pid}',
                      'status': '',
                      'pageNum': '1',
                      'pageSize': '100',
                      'indexCode': 'cHJvTGVhZGluZ1BhcmFtZXRlckNvbmZpZw%3D%3D'}
        first_response = requests.post(first_url, first_head)
        return first_response.json()['data']

    def dmo(self):
        dmo_url = f'{self.ip}{self.dmo_cfg}'
        dmo_head = {'appid': f'{self.appid}',
                    'cha': f'{self.cha}',
                    'prjid': f'{self.pid}',
                    'limit': "100",
                    'start': "0",
                    'token': f'{self.login()}'}
        dmo_res = requests.post(dmo_url, dmo_head)

        dmo_collect = dmo_res.json()['data']
        if dmo_collect != []:
            for d_res in dmo_collect:
                if 'prjid' in dict(d_res).keys() and self.pid in dict(d_res)['prjid'] and self.pid != '':
                    return d_res
            for d_res in dmo_collect:
                if 'cha' in dict(d_res).keys() and self.cha in dict(d_res)['cha']:
                    return d_res


    def jh(self):
        jh_url = f'{self.ip}{self.jh_cfg}'
        jh_head = {'appid': f'{self.appid}',
                   'cha': f'{self.cha}',
                   'prjid': f'{self.pid}',
                   'limit': "100",
                   'start': "0",
                   'token': f'{self.login()}',
                   'indexCode': 'QmxhY2tsaXN0RGV2aWNlRmlsdGVyaW5nXzJGb01vdmU='}

        jh_res = requests.post(jh_url, jh_head)
        res_collect = jh_res.json()['data']
        # print(res_collect)
        if res_collect != []:
            for res in res_collect:
                if 'prjid' in dict(res).keys() and self.pid in dict(res)['prjid'] and self.pid != '':
                    return res
            for res in res_collect:
                if 'cha' in dict(res).keys() and self.cha in dict(res)['cha']:
                    return res


#
# if __name__ == '__main__':
#     a = OnlineCfg()
#     a.Black_Cfg()
#     print(a.Black_Cfg())

