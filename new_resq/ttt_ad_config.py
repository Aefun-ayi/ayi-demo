import requests
import Remove
from PyQt5.QtWidgets import QMessageBox

def ttt_ad(new_or_old, appid, out_pack):
    splash_name = []
    splash_source = []
    video_name = []
    video_source = []
    plaque_name = []
    plaque_source = []
    msg_name = []
    msg_source = []
    try:
        if out_pack == '':
            msg_box = QMessageBox(QMessageBox.Critical, '错误', f"请求有误：出包备注不能为空")
            msg_box.exec_()
        else:
            url = 'http://192.168.7.30:8009/ttt_spaceid'
            res = requests.get(url)
            ad_info = res.json()[f'{out_pack}']
            url = 'https://ttt.careduka.com/space-slot/getSlotList'
            head = {
                "Content-Type": "application/json"
            }
            for i in ad_info:
                data = {
                    "is_new": f"{new_or_old}",  # 是否新老 这个参数比较重要 用于切用户人群
                    "app_id": f"{appid}",  # 需替换对应产品id
                    "space_id": f"{i}"  # 这个可以查询获取对应的space id   只能当做假设使用 假设本地代码写入的spaceid正确所请求出的广告信息
                }
                res = requests.post(url, headers=head, json=data)
                cfg = res.json()
                # print(cfg)

                if cfg['message'] != '成功':
                    msg_box = QMessageBox(QMessageBox.Critical, '错误', f'缺少正确的space id: {i}，请联系变现确认')
                    msg_box.exec_()
                    # print(f'缺少正确的space id: {i}，请联系变现确认')
                else:
                    slot = res.json()['data']['rit_group']
                    # print(cfg)
                    slot1 = res.json()['data']['space_id']
                    for iiii in range(len(slot)):
                        if slot[iiii]['ad_type'] == 1:
                            splash_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{slot1}/")
                        if slot[iiii]['ad_type'] == 2:
                            video_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{slot1}/")
                        if slot[iiii]['ad_type'] == 3:
                            msg_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{slot1}/")
                        if slot[iiii]['ad_type'] == 4:
                            plaque_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{slot1}/")

                    for i in range(len(slot)):
                        bidding = slot[i]['rit']['binding']
                        if slot[i]['ad_type'] == 1:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                splash_source.append(
                                    f"space_id：{res.json()['data']['space_id']}/代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}/")
                            waterfall = slot[i]['rit']['price']
                            if len(waterfall) > 0:
                                for iii in range(len(waterfall)):
                                    waterfall_source = waterfall[iii]['rit_name']
                                    waterfall_id = waterfall[iii]['rit_id']
                                    splash_source.append(
                                        f"space_id：{res.json()['data']['space_id']}/代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}/")
                        if slot[i]['ad_type'] == 2:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                video_source.append(
                                    f"space_id：{res.json()['data']['space_id']}/代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}/")
                            waterfall = slot[i]['rit']['price']
                            if len(waterfall) > 0:
                                for iii in range(len(waterfall)):
                                    waterfall_source = waterfall[iii]['rit_name']
                                    waterfall_id = waterfall[iii]['rit_id']
                                    video_source.append(
                                        f"space_id：{res.json()['data']['space_id']}/代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}/")
                        if slot[i]['ad_type'] == 3:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                msg_source.append(
                                    f"space_id：{res.json()['data']['space_id']}/代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}/")
                            waterfall = slot[i]['rit']['price']
                            if len(waterfall) > 0:
                                for iii in range(len(waterfall)):
                                    waterfall_source = waterfall[iii]['rit_name']
                                    waterfall_id = waterfall[iii]['rit_id']
                                    msg_source.append(
                                        f"space_id：{res.json()['data']['space_id']}/代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}/")
                        if slot[i]['ad_type'] == 4:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                plaque_source.append(
                                    f"space_id：{res.json()['data']['space_id']}/代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}/")
                            waterfall = slot[i]['rit']['price']
                            if len(waterfall) > 0:
                                for iii in range(len(waterfall)):
                                    waterfall_source = waterfall[iii]['rit_name']
                                    waterfall_id = waterfall[iii]['rit_id']
                                    plaque_source.append(
                                        f"space_id：{res.json()['data']['space_id']}/代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}/")


                return splash_name, splash_source, video_name, video_source, msg_name, msg_source, plaque_name, plaque_source
    except:
        msg_box = QMessageBox(QMessageBox.Critical, '错误', f"请求有误：检查产品id、出包备注是否填写正确")
        msg_box.exec_()

