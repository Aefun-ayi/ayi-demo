import base64
import requests

class AdSourcesCfg():
    def __init__(self, appid, pid, chan):
        self.appid = appid
        self.pid = pid
        self.chan = chan

    def ad_sids_select(self):
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
            list_strate = connect["strategys"]
            msg_sid = []
            video_sid = []
            plaque_sid = []
            splash_sid = []
            for i in range(len(list_strate)):
                all_source = list_strate[i]
                for ii in range(len(all_source['sids'])):
                    if '_msg' in all_source['sids'][ii]:
                        msg_source = all_source['sids'][ii]
                        msg_sid.append(msg_source)
                    if '_video' in all_source['sids'][ii]:
                        video_source = all_source['sids'][ii]
                        video_sid.append(video_source)
                    if '_plaque' in all_source['sids'][ii]:
                        plaque_source = all_source['sids'][ii]
                        plaque_sid.append(plaque_source)
                    if '_splash' in all_source['sids'][ii]:
                        splash_source = all_source['sids'][ii]
                        splash_sid.append(splash_source)
            return splash_sid, msg_sid, plaque_sid, video_sid

# if __name__ == '__main__':
#     a = Ad_Sids_Cfg('39255','39255011','csj')
#     a.ad_select()
#     print(a.ad_select())
