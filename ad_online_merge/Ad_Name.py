import base64
import requests

class Ad_Name_Cfg():
    def __init__(self, appid, pid, chan):
        self.appid = appid
        self.pid = pid
        self.chan = chan
    def ad_name_select(self):
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
            list_strate = connect["strategys"]  # 获取分组内的策略信息
            ad_name = connect["adPositions"]  # 获取分组内策略里面的广告位信息
            msg_config = []
            video_config = []
            plaque_config = []
            splash_config = []
            # 利用分组内的策略名和广告位所配置的策略名对比 一致后输出正确有效的广告位
            for iii in range(len(list_strate)):
                for index in range(len(ad_name)):
                    if list_strate[iii]['name'] in ad_name[index]['strategys']:
                        if 'msg' in ad_name[index]['strategys']:
                            msg_config.append(ad_name[index]['name'])
                        if 'video' in ad_name[index]['strategys']:
                            video_config.append(ad_name[index]['name'])
                        if 'plaque' in ad_name[index]['strategys']:
                            plaque_config.append(ad_name[index]['name'])
                        if 'splash' in ad_name[index]['strategys']:
                            splash_config.append(ad_name[index]['name'])
            return splash_config,msg_config,plaque_config,video_config

# if __name__ == '__main__':
#     a = Ad_Name_Cfg('39255','39255011','csj')
#     a.ad_select()
#     print(a.ad_select())