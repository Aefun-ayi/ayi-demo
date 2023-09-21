import re

ren = {
    '中台_计步_V1.0.4_兜底': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_计步_V1.0.4_HW': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_计步_V1.0.4_OP': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_计步_V1.0.4_VI': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_计步_V1.0.4_HW_【合规调整+D】': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'GATE_计步_V1.0.0': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'GATE_计步_V1.0.7.3_datax': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_计步_V1.0.4_VI【弹出优化】': ['splash', 'game_awaken', 'newfriend_video', 'newfriend_msg', '5yuan_video', '5yuan_msg', '3mao_msg' ,'8888_first_video', '8888_second_video', '8888_third_video', 'load_msg', 'double_mfzs', 'extra_mfzs' ,'tx_video', 'wmtx_video', 'switch_plaque', 'auto_video', 'txym_msg', 'djhb_video', 'lqbx_video' ,'lqhb_video' ,'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],

    'GATE_清理、wifi、省电_V1.0.0': ['splash', 'game_awaken', 'recommend_msg', 'clean_landing', 'level_win', 'scan_plaque'
                               ,'htend_plaque', 'dsshome_msg', 'adjust_video', 'jkzs_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'GATE_wifi_【穿山甲平台广告合规化】': ['scratch_video', 'make_video', 'bottom_msg', 'switch_plaque'],
    '中台_清理、wifi、省电_V2.0.2_兜底': ['splash', 'game_awaken', 'recommend_msg', 'clean_landing', 'level_win', 'scan_plaque'
                                ,'htend_plaque', 'dsshome_msg', 'adjust_video', 'jkzs_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_清理、wifi、省电_V2.0.2_HW': ['splash', 'game_awaken', 'recommend_msg', 'clean_landing', 'level_win', 'scan_plaque'
                                ,'htend_plaque', 'dsshome_msg', 'adjust_video', 'jkzs_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_清理、wifi、省电_V2.0.2_OP': ['splash', 'game_awaken', 'recommend_msg', 'clean_landing', 'level_win', 'scan_plaque'
                                ,'htend_plaque', 'dsshome_msg', 'adjust_video', 'jkzs_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_清理、wifi、省电_V2.0.2_VI': ['splash', 'game_awaken', 'recommend_msg', 'clean_landing', 'level_win', 'scan_plaque'
                                ,'htend_plaque', 'dsshome_msg', 'adjust_video', 'jkzs_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_清理、wifi、省电_V2.0.2_【合规调整】HW': ['splash', 'game_awaken', 'recommend_msg', 'clean_landing', 'level_win', 'scan_plaque' ,'htend_plaque', 'dsshome_msg', 'adjust_video', 'jkzs_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],

    'GATE_大字报_V1.0.0': ['splash', 'game_awaken', 'adjust_video', 'exit_msg', 'leave_splash', 'zxtc_msg', 'jkzs_plaque'
                        ,'weather_msg', 'news_landing', 'my_msg', 'lqbx_video', 'lqhb_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_大字报_V1.0.3_兜底': ['splash', 'game_awaken', 'adjust_video', 'exit_msg', 'leave_splash', 'zxtc_msg', 'jkzs_plaque'
                         ,'weather_msg', 'news_landing', 'my_msg', 'lqbx_video', 'lqhb_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_大字报_V1.0.3_HW': ['splash', 'game_awaken', 'adjust_video', 'exit_msg', 'leave_splash', 'zxtc_msg', 'jkzs_plaque'
                         ,'weather_msg', 'news_landing', 'my_msg', 'lqbx_video', 'lqhb_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_大字报_V1.0.3_OP': ['splash', 'game_awaken', 'adjust_video', 'exit_msg', 'leave_splash', 'zxtc_msg', 'jkzs_plaque'
                         ,'weather_msg', 'news_landing', 'my_msg', 'lqbx_video', 'lqhb_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_大字报_V1.0.3_VI': ['splash', 'game_awaken', 'adjust_video', 'exit_msg', 'leave_splash', 'zxtc_msg', 'jkzs_plaque'
                         ,'weather_msg', 'news_landing', 'my_msg', 'lqbx_video', 'lqhb_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_大字报_V1.0.3_VI【弹出优化】': ['splash', 'game_awaken', 'adjust_video', 'exit_msg', 'leave_splash', 'zxtc_msg', 'jkzs_plaque' ,'weather_msg', 'news_landing', 'my_msg', 'lqbx_video', 'lqhb_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],

    'GATE_充电_V1.0.0': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'GATE_充电_【测试】V1.0.1': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'GATE_充电_【测试】V1.0.2': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'GATE_充电_【穿山甲平台广告合规化】': ['powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque'],
    '中台_充电_V1.0.4_兜底': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_充电_V1.0.4_HW': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_充电_V1.0.4_OP': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_充电_V1.0.4_VI': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_充电_V1.0.4_VI【弹出优化】': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_充电_V1.0.4_OP【1466插件版1.0.12】': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_充电_V1.0.4_【1466】HW': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_充电_V1.0.0_【1466】HW-电池好卫士': ['splash', 'game_awaken', 'powersaving_video', 'speedup_video', 'care_msg', 'set_video', 'switch_plaque', 'news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],

    'GATE_天气_V1.0.0': ['splash', 'game_awaken', 'news_msg', 'more_video', 'check_video', 'jkzs_plaque', 'news_landing'
                       ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_天气_V1.1.8_兜底': ['splash', 'game_awaken', 'news_msg', 'more_video', 'check_video', 'jkzs_plaque', 'news_landing'
                        ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_天气_V1.1.8_HW': ['splash', 'game_awaken', 'news_msg', 'more_video', 'check_video', 'jkzs_plaque', 'news_landing'
                        ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_天气_V1.1.8_OP': ['splash', 'game_awaken', 'news_msg', 'more_video', 'check_video', 'jkzs_plaque', 'news_landing'
                        ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_天气_V1.1.8_VI': ['splash', 'game_awaken', 'news_msg', 'more_video', 'check_video', 'jkzs_plaque', 'news_landing'
                        ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_天气_V1.1.8_VI【弹出优化】': ['splash', 'game_awaken', 'news_msg', 'more_video', 'check_video', 'jkzs_plaque', 'news_landing' ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    '中台_天气_V1.1.8【1466插件版1.0.12】': ['splash', 'game_awaken', 'news_msg', 'more_video', 'check_video', 'jkzs_plaque', 'news_landing' ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],

    'shelf_通用_v1.0.0【HW定制化】': ['news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'shelf_通用_v1.0.0【HW定制化+带D+1463】': ['news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'shelf_通用_v1.0.0【HW定制化+带D+1466+合规调整】': ['news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'shelf_通用_v1.0.0【HW定制化+小D】': ['news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],
    'shelf_通用_v1.0.0【兜底包】': ['news_landing', 'game_clean', 'game_video', 'game_ad', 'olanding_msg'],

    'GATE_计步_V1.0.7.3': ['splash' ,'2_plaque', 'game_awaken' ,'first_msg', 'new_first_mix', 'first_bp_plaque', 'new_more_mix', 'tx_button' ,'txbp_plaque', 'result_msg' ,'sign_video' ,'add_video'
                         ,'wx_video' ,'2_tx_mix' ,'limit_msg' ,'succ_msg' ,'2_queue_mix' ,'2_bp_plaque'
                         ,'shared_ad_video' ,'shared_ad_msg' ,'lottery_plaque', 'news_landing' ,'adjust_video', 'game_clean', 'game_video', 'game_ad', 'olanding_msg']
}

# print(ren['中台_计步_V1.0.4_兜底'])

for name in ren:
    # print(f'{name}:{ren[name]}')
    a = re.sub("'", '',str(ren[name])[1:-1])
    # print(a)
    b = a.replace(" ", '')
    # print(b)
    print(f'{name}')
    # print(len(ren))
    # print(type(b))
    # c = b.replace("]", '')