
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
    print(url)
    http_get = requests.get(url)
    connect = http_get.json()
    group = connect['sid']
    ad_strategys = connect['strategys']
    ad_name = connect['adPositions']
    run = []
    run_out = changgui_ad_name.run_ad_name+changgui_ad_name.out_ad
    lose = []
    pipei = []
    queshao = []
    if 'all' in group:
        for i in range(len(ad_name)):
            all_ad_name = ad_name[i]['name']
            run.append(all_ad_name)

        for ii in run:
            if ii in run_out:
                pipei.append(ii)
            else:
                lose.append(ii)
        for iii in run_out:
            if iii not in run:
                queshao.append(iii)
        print(pipei,'匹配成功的广告位')
        print(lose, '冗余的广告位')

        if len(queshao) == 0:
            print('无缺少的广告位')
        else:
            print(queshao,'缺少的广告位')


        # for ii in adad:
        #     if ii in changgui_ad_name.run_ad_name:
        #         pipei.append(ii)
        #         # print(ii,'匹配的广告位')
        #
        #     if ii not in changgui_ad_name.run_ad_name:
        #         lose.append(ii)
        # for iii in adad:
        # # for iii in adad:
        #     if iii in changgui_ad_name.out_ad:
        #         pipei.append(iii)
        #     # if iii not in changgui_ad_name.out_ad:
        #     #     aaaa.append(iii)
        #     if iii not in changgui_ad_name.out_ad:
        #
        #         lose.remove(iii)
        # print(pipei, '匹配的广告位')
        # print(lose, '冗余的广告位')
                # print(ii, '冗余的广告位')
            # else:
            #     print(ii, '缺少的广告位')
            # if ii in changgui_ad_name.out_ad:
            #     print(ii, '匹配的外广广告位')
            # if ii not in changgui_ad_name.out_ad:
            #     print(ii , '缺少的外广广告位')
            # else:
            #     print(ii, '冗余的外广广告位')


        # print(str(set(adad)&set(changgui_ad_name.run_ad_name)&set(changgui_ad_name.out_ad)))
        # print(str(set(adad)^set(changgui_ad_name.run_ad_name)^set(changgui_ad_name.out_ad)))