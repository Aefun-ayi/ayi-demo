import base64
import json
import requests
import re
import changgui_ad_name


chan = 'csj'
pid = '38727027'


sids = ['all', '1066A_A', '1066B_B', '1066C_C']

appid = pid[:5]
for i in sids:

    txt = '{"buy_id":"default",' \
          '"imei":"658992ce-34ad-45f6-965c-ecec952a4294",' \
          f'"pid":"{pid}",' \
          f'"sid":"{i}",' \
          '"lsn":"85202900",' \
          f'"appid":"{appid}",' \
          '"isNewUser":"1",' \
          '"brand":"HUAWEI",' \
          '"os_version":"ele-al00 10.1.0.162(c00e160r2p11)",' \
          '"debug":"1",' \
          '"oaid":"658992ce-34ad-45f6-965c-ecec952a4294",' \
          f'"cha_id":"{chan}",' \
          '"buy_act":"default",' \
          '"os":"EmotionUI_12.0.0"}'

    s = txt.encode("utf-8")

    code = base64.b64encode(s).decode("utf-8")

    url = f'https://cfg.vigame.cn/v14/extend?value={code}'
    http_get = requests.get(url)
    connect = http_get.json()
    group = connect['sid']
    ad_strategys = connect['strategys']
    ad_name = connect['adPositions']
    # print(connect)
    # print(connect['adPositions'])
    adad = []
    if 'all' in group:
        for i in range(len(ad_name)):
            all_ad_name = ad_name[i]['name']
            adad.append(all_ad_name)
            for i in range(len(adad,changgui_ad_name.run_ad_name)):
                if adad == changgui_ad_name.run_ad_name:
                    print('匹配')
                else:
                    print('不匹配')
            # print(type(all_ad_name))
            # for iii in range(len(all_ad_name)):
            #     test_ad_name = all_ad_name[iii]
            #     print(test_ad_name)
            # print(all_ad_name['name'])
        # for ii in range(len(changgui_ad_name.run_ad_name)):
            # run1_ad_name = changgui_ad_name.run_ad_name[ii]

        # for ii in range(len(changgui_ad_name.run_ad_name)):
        #     run1_ad_name = changgui_ad_name.run_ad_name[ii]
        #     for iii in range(len(adad)):
        #         if adad[iii] == run1_ad_name:
        #             print('匹配' + run1_ad_name)
        #         else:
        #             print('不匹配' + adad[iii])
            # print(type(run1_ad_name))
        # if all_ad_name in run1_ad_name:
        #     print(changgui_ad_name)
            # print(run1_ad_name)
        # if run1_ad_name in all_ad_name['name']:
            # print('对得上的广告位' + run1_ad_name)
        # if test_ad_name in run1_ad_name:
        #     print('多余的广告位' + test_ad_name)
        # else:
        #     print('对不上的广告位' + test_ad_name)
                # else:
                #     print(changgui_ad_name.run_ad_name[ii])
                # if run1_ad_name not in ad_name['name']:
                #     print(changgui_ad_name.run_ad_name[ii])
        # print(ad_name)
        # print(group)