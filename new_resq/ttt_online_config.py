import requests
from PyQt5.QtWidgets import QMessageBox


def ttt_test(appid,cha,apk_version,track_channel):


    ttt_info = ['-----------------测试环境-----------------']
    try:
        audit_url = ' https://ttt.yangguangzhujia.com/activity/get/state'
        audit_head = {"Content-Type": "application/json", }
        audit_data = {"app_id": f"{appid}", "cha": f"{cha}", "version": "1.0.1", "apk_version": f"{apk_version}"}
        audit_res = requests.post(audit_url, headers=audit_head, json=audit_data)
        if audit_res.json()['message'] != '成功':
            msg_box = QMessageBox(QMessageBox.Critical, '错误', f"请求有误：{audit_res.json()['message']}")
            msg_box.exec_()
        else:
            if 'audit_state' not in audit_res.json()['data']:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', f"查不到审核配置，检查产品id，渠道，版本号是否正确")
                msg_box.exec_()
            else:
                audit_state = audit_res.json()['data']['audit_state']  # 0关闭审核  1开启审核
                if audit_state == 0:
                    ttt_info.append('审核开关：关闭')
                    switch_url = 'https://ttt.yangguangzhujia.com/activity/get/switch'
                    switch_head = {"Content-Type": "application/json", }
                    switch_data = {"app_id": f"{appid}", "cha": f"{cha}", "apk_version": f"{apk_version}","track_channel": f"{track_channel}"}
                    switch_res = requests.post(switch_url, headers=switch_head, json=switch_data)
                    if switch_res.json()['message'] != '成功':
                        msg_box = QMessageBox(QMessageBox.Critical, '错误', f"请求有误：{switch_res.json()['message']}")
                        msg_box.exec_()
                    else:
                        bh = switch_res.json()['data']['app_alive_module']  # 保活模块
                        if bh == 1:
                            ttt_info.append('保活模块开关：打开')
                            Dmo_url = 'https://ttt.yangguangzhujia.com/activity/d-model'
                            dmo_head = {"Content-Type": "application/json"}
                            dmo_data = {"app_id": f"{appid}", "cha": f"{cha}", "apk_version": f"{apk_version}"}
                            dmo_res = requests.post(Dmo_url, headers=dmo_head, json=dmo_data)
                            d_model = dmo_res.json()['data']
                            if 'd_model' not in d_model:
                                msg_box = QMessageBox(QMessageBox.Critical, '错误', f"查不到D模配置，检查产品id，渠道，版本号是否正确或测试服是否有配置")
                                msg_box.exec_()
                            else:
                                if d_model['d_model'] == '1':
                                    ttt_info.append('D模开关：打开')
                                    ttt_info.append(f"D模激活延迟时间：{d_model['d_time']}秒")
                                if d_model['d_model'] == '0':
                                    ttt_info.append('D模开关：关闭')
                        if bh == 0:
                            ttt_info.append('保活模块开关：关闭')
                        outside = switch_res.json()['data']['outside_activity']  # 站外营销模块
                        if outside == 1:
                            ttt_info.append('站外营销模块开关：打开')
                            outside_url = 'https://ttt.yangguangzhujia.com/activity/get/config/market'
                            outside_head = {"Content-Type": "application/json", }
                            outside_data = {"app_id": f"{appid}", "cha": f"{cha}", "apk_version": f"{apk_version}"}
                            outside_res = requests.post(outside_url, headers=outside_head, json=outside_data)
                            market = outside_res.json()['data']['detail']
                            nqdt = market['nqDt']
                            ttt_info.append(f'自然量延时：{str(nqdt)}秒')
                            lock_dig = market['market_param']['lock']['lock_on']  # 锁屏弹窗开关
                            if lock_dig == 1:
                                ttt_info.append('锁屏弹窗开关：打开')
                                lock_delay = market['market_param']['lock']['lock_first_time']  # 锁屏弹窗的首次延时
                                ttt_info.append(f'锁屏弹窗首次延时：{str(lock_delay)}秒')
                            if lock_dig == 0:
                                ttt_info.append('锁屏弹窗开关：关闭')

                            unlock_dig = market['market_param']['unlock']['unlock_on']  # 解锁后弹窗开关
                            if unlock_dig == 1:
                                ttt_info.append('解锁后弹窗开关：打开')
                                unlock_qiangtan = market['market_param']['unlock']['unlock_super_on']  # 解锁后弹窗强停开关
                                if unlock_qiangtan == 1:
                                    ttt_info.append('解锁后弹窗广告强弹开关：打开')
                                if unlock_qiangtan == 0:
                                    ttt_info.append('解锁后弹窗广告强弹开关：关闭')
                                unlock_delay = market['market_param']['unlock']['unlock_first_time']  # 解锁后弹窗首次延时
                                ttt_info.append(f'解锁后弹窗首次延时：{str(unlock_delay)}秒')
                                unlock_rate_type = market['market_param']['unlock']['unlock_rate']['rate_type']  # 解锁后弹窗频次类型  1为时间间隔  2为次数间隔
                                if unlock_rate_type == 1:
                                    ttt_info.append('解锁后弹窗频次类型：时间间隔')
                                    unlock_rate_value = market['market_param']['unlock']['unlock_rate']['rate_value']  # 解锁后弹窗时间间隔-数值，数值单位/秒
                                    ttt_info.append(f'解锁后弹窗时间间隔：{str(unlock_rate_value)}秒')
                                if unlock_rate_type == 2:
                                    ttt_info.append('解锁后弹窗频次类型：次数间隔')
                                    unlock_rate_first_order = market['market_param']['unlock']['unlock_rate']['first_order']  # 解锁后弹窗频次次数间隔（首次在第几次触发）
                                    ttt_info.append(f'解锁后弹窗频次-次数间隔：首次在第{str(unlock_rate_first_order)}次触发')
                                    unlock_rate_interval_num = market['market_param']['unlock']['unlock_rate']['interval_num']  # 解锁后弹窗频次次数间隔-间隔次数
                                    ttt_info.append(f'解锁后弹窗频次-次数间隔：后续间隔次数{str(unlock_rate_interval_num)}次')
                            if unlock_dig == 0:
                                ttt_info.append('解锁后弹窗开关：关闭')

                            home_dig = market['market_param']['home']['home_on']  # home弹窗开关
                            if home_dig == 1:
                                ttt_info.append('home键弹窗开关：打开')
                                home_qiangtan = market['market_param']['home']['home_super_on']  # home弹窗广告强弹开关
                                if home_qiangtan == 1:
                                    ttt_info.append('home键弹窗广告强弹开关：打开')
                                if home_qiangtan == 0:
                                    ttt_info.append('home键弹窗广告强弹开关：关闭')
                                home_delay = market['market_param']['home']['home_first_time']  # home弹窗首次延时
                                ttt_info.append(f'home键弹窗首次延时：{str(home_delay)}秒')
                                home_rate_type = market['market_param']['home']['home_interval']['rate_type']  # home弹窗频次类型 1为时间间隔  2为次数间隔
                                if home_rate_type == 1:
                                    ttt_info.append('home键弹窗频次类型：时间间隔')
                                    home_rate_value = market['market_param']['home']['home_interval']['rate_value']  # home弹窗时间间隔-数值，数值单位/秒
                                    ttt_info.append(f'home键弹窗时间间隔：{home_rate_value}秒')
                                if home_rate_type == 2:
                                    ttt_info.append('home键弹窗频次类型：次数间隔')
                                    home_rate_first_order = market['market_param']['home']['home_interval']['first_order']  # home弹窗频次次数间隔（首次在第几次触发）
                                    ttt_info.append(f'home键弹窗频次-次数间隔：首次在第{str(home_rate_first_order)}次触发')
                                    home_rate_interval_num = market['market_param']['home']['home_interval']['interval_num']  # home弹窗频次次数间隔-间隔次数
                                    ttt_info.append(f'home键弹窗频次-次数间隔：后续间隔次数{str(home_rate_interval_num)}次')
                            if home_dig == 0:
                                ttt_info.append('home键弹窗开关：关闭')

                            electric = market['market_param']['electric']['electric_on']  # 电量弹窗开关
                            if electric == 1:
                                ttt_info.append('电量弹窗开关：打开')
                                electric_super_on = market['market_param']['electric']['electric_super_on']  # 电量弹窗广告强弹开关
                                if electric_super_on == 1:
                                    ttt_info.append('电量弹窗广告强弹开关：打开')
                                if electric_super_on == 0:
                                    ttt_info.append('电量弹窗广告强弹开关：关闭')
                                pop_method = market['market_param']['electric']['pop_method']  # 电量弹窗弹出方式 1马上弹出 2下次触发home时弹窗
                                if pop_method == 1:
                                    ttt_info.append('电量弹窗弹出方式：马上弹出')
                                if pop_method == 2:
                                    ttt_info.append('电量弹窗弹出方式：下次触发home时弹出')
                                pop_interval = market['market_param']['electric']['pop_interval']  # 电量弹窗的继续弹出间隔 单位秒
                                ttt_info.append(f'电量弹窗继续弹出间隔{str(pop_interval)}秒')
                            if electric == 0:
                                ttt_info.append('电量弹窗开关：关闭')

                            charge_on = market['market_param']['charge']['charge_on']  # 充电弹窗开关
                            if charge_on == 1:
                                ttt_info.append('充电弹窗开关：打开')
                                charge_super_on = market['market_param']['charge']['charge_super_on']  # 充电弹窗广告强弹开关
                                if charge_super_on == 1:
                                    ttt_info.append('充电弹窗广告强弹开关：打开')
                                if charge_super_on == 0:
                                    ttt_info.append('充电弹窗广告强弹开关：关闭')
                            if charge_on == 0:
                                ttt_info.append('充电弹窗开关：关闭')

                            timer_on = market['market_param']['timer']['timer_on']  # 定时弹窗开关
                            if timer_on == 1:
                                ttt_info.append('定时弹窗开关：打开')
                                timer_super_on = market['market_param']['timer']['timer_super_on']  # 定时弹窗广告强弹开关
                                if timer_super_on == 1:
                                    ttt_info.append('定时弹窗广告强弹开关：打开')
                                if timer_super_on == 0:
                                    ttt_info.append('定时弹窗广告强弹开关：关闭')
                                timer_first_time = market['market_param']['timer']['timer_first_time']  # 定时弹窗首次触发时间
                                ttt_info.append(f'定时弹窗首次触发时间：{str(timer_first_time)}秒')
                                timer_interval = market['market_param']['timer']['timer_interval']  # 定时弹窗频次 单位秒
                                ttt_info.append(f'定时弹窗频次：{str(timer_interval)}秒')
                            if timer_on == 0:
                                ttt_info.append('定时弹窗开关：关闭')
                        if outside == 0:
                            ttt_info.append('站外营销模块开关：关闭')

                    ad_module = switch_res.json()['data']['ad_module']  # 广告模块  0关闭 1开启
                    if ad_module == 1:
                        ttt_info.append('广告模块开关：打开')
                    if ad_module == 0:
                        ttt_info.append('广告模块开关：关闭')
                if audit_state == 1:
                    ttt_info.append('审核开关：打开')
                    state_ad_model = audit_res.json()['data']['ad_model']
                    if state_ad_model == 0:
                        ttt_info.append('广告模块开关：关闭')
                    if state_ad_model == 1:
                        ttt_info.append('广告模块开关：打开')



    except ValueError as v:
        msg_box = QMessageBox(QMessageBox.Critical, '错误', f'异常信息：key有误{v}，请检查是否appid，渠道，版本号是否有误')
        msg_box.exec_()
        # print(f'异常信息：key有误{v}，请检查是否appid，渠道，版本号是否有误')
    return ttt_info