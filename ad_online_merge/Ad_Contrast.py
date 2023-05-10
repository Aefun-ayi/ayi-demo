import base64
import requests
from PyQt5.QtWidgets import QMessageBox

class Ad_Than_Cfg():
    def __init__(self, appid, pid, chan, pro):
        self.appid = appid
        self.pid = pid
        self.chan = chan
        self.pro = pro

    def ad_contrast_select(self):
        sids = ['all', '1066A_A', '1066B_B', '1066C_C']  # 把目前在用的4个分组放在列表
        res = requests.get('http://192.168.7.30:8008/ad')
        if self.pro not in res.json():
            pro_msg_box = QMessageBox(QMessageBox.Critical, '错误', '输入的key有误')
            pro_msg_box.exec_()
        all_ad_name = res.json()[f'{self.pro}']
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
            ad_name = connect['adPositions']
            actual_adname = []  # 空列表 用于接收实际配置的广告位
            short_ad_name = []  # 空列表 用于接收缺少的广告位
            match_ad_name = []  # 空列表 用于接收匹配的广告位
            tmr_ad_name = []  # 空列表 用于接收冗余的广告位
            for i in range(len(ad_name)):
                actual_adname.append(ad_name[i]['name'])
            for ii in range(len(all_ad_name)):
                if all_ad_name[ii] in actual_adname:
                    match_ad_name.append(all_ad_name[ii])
                if all_ad_name[ii] not in actual_adname:
                    short_ad_name.append(all_ad_name[ii])
            for iii in range(len(actual_adname)):
                if actual_adname[iii] not in all_ad_name:
                    tmr_ad_name.append(actual_adname[iii])
            return match_ad_name, short_ad_name, tmr_ad_name



# if __name__ == '__main__':
#     a = Ad_Than_Cfg('39255','39255011','csj','中台_计步_V1.0.4_兜底')
#     a.ad_select()
#     print(a.ad_select())