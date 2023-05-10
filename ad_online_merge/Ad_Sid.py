import base64
import requests

class Ad_Group_Cfg():
    def __init__(self, appid, pid, chan):
        self.appid = appid
        self.pid = pid
        self.chan = chan

    def ad_sid_select(self):
        sids = ['all', '1066A_A', '1066B_B', '1066C_C']  # 把目前在用的4个分组放在列表

        for i in sids:  # 对列表进行循环，列表内每一个分组的值进行输出
            txt = '{"buy_id":"default",' \
                  '"imei":"658992ce-34ad-45f6-965c-ecec952a4294",' \
                  f'"pid":"{self.pid}",' \
                  f'"sid":"{i}",' \
                  '"lsn":"85202900",' \
                  f'"appid":"{self.appid}",' \
                  '"isNewUser":"1",' \
                  '"brand":"HUAWEI",' \
                  '"os_version":"ele-al00 10.1.0.162(c00e160r2p11)",' \
                  '"debug":"1",' \
                  '"oaid":"658992ce-34ad-45f6-965c-ecec952a4294",' \
                  f'"cha_id":"{self.chan}",' \
                  '"buy_act":"default",' \
                  '"os":"EmotionUI_12.0.0"}'
            s = txt.encode("utf-8")  # 对接口需要传值的参数进行转义
            code = base64.b64encode(s).decode("utf-8")
            url = f'https://cfg.vigame.cn/v14/extend?value={code}'
            http_get = requests.get(url)
            connect = http_get.json()
            ad_group = connect['sid']
            stra_name = connect['strategys']
            a_group = []
            b_group = []
            c_group = []
            all_group = []
            # 加上分组判断 按照分组输出对应的分组内的策略信息
            if "1066C_C" in ad_group:
                for i in range(len(stra_name)):
                    c_strate = stra_name[i]['strategy']
                    c_group.append(c_strate)
            if "1066B_B" in ad_group:
                for i in range(len(stra_name)):
                    b_strate = stra_name[i]['strategy']
                    b_group.append(b_strate)
            if "1066A_A" in ad_group:
                for i in range(len(stra_name)):
                    a_strate = stra_name[i]['strategy']
                    a_group.append(a_strate)
            if "all" in ad_group:
                for i in range(len(stra_name)):
                    all_strate = stra_name[i]['strategy']
                    all_group.append(all_strate)
            return all_group, a_group, b_group, c_group


# if __name__ == '__main__':
#     a = Ad_Group_Cfg('39255','39255011','csj')
#     a.ad_select()
#     print(a.ad_select())
