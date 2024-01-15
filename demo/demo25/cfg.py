# coding:utf-8

import pymysql
from ex import aaa
# 定义一个函数，用来创建连接数据库
def mysql_db():
    con = pymysql.connect(
        host='192.168.7.188',
        port=3306,
        database='aefun_databese',
        charset='utf8mb4',
        user='root',
        password='admin'
    )
    # try:
    with con.cursor() as cursor:
            # 一、查询
            # sql = "select * from device_info;"
            sql = "select * from test where appid = 12345;"
            # sql ="insert into phone_info(id, phone_mobile, phone_name)value(1,'123456','vivo Y80');"
            # res = aaa()
            # print(res)
            # res = [{"packinfo": "中台_计步_V1.0.4_兜底", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_HW", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_OP", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_VI", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_HW_【合规调整+D】", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_计步_V1.0.0", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_计步_V1.0.7.3_datax", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_VI【弹出优化】", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_清理、wifi、省电_V1.0.0", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_wifi_【穿山甲平台广告合规化】", "adinfo": "scratch_video,make_video,bottom_msg,switch_plaque"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_兜底", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_HW", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_OP", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_VI", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_【合规调整】HW", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_大字报_V1.0.0", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_兜底", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_HW", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_OP", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_VI", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_VI【弹出优化】", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_V1.0.0", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_【测试】V1.0.1", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_【测试】V1.0.2", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_【穿山甲平台广告合规化】", "adinfo": "powersaving_video,speedup_video,care_msg,set_video,switch_plaque"}, {"packinfo": "中台_充电_V1.0.4_兜底", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_HW", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_OP", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_VI", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_VI【弹出优化】", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_OP【1466插件版1.0.12】", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_【1466】HW", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.0_【1466】HW-电池好卫士", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_天气_V1.0.0", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_兜底", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_HW", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_OP", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_VI", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_VI【弹出优化】", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8【1466插件版1.0.12】", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化+带D+1463】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化+带D+1466+合规调整】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化+小D】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【兜底包】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_计步_V1.0.7.3", "adinfo": "splash,2_plaque,game_awaken,first_msg,new_first_mix,first_bp_plaque,new_more_mix,tx_button,txbp_plaque,result_msg,sign_video,add_video,wx_video,2_tx_mix,limit_msg,succ_msg,2_queue_mix,2_bp_plaque,shared_ad_video,shared_ad_msg,lottery_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}]

            # for i in res:
                # print(i)
                # phonemobile = i['model']
                # phonename = i['phonename']
                # sql =f"insert into device_info(phone_mobile, phone_name)value('{phonemobile}','{phonename}');"

            # 执行SQL语句
            # 执行后的结果都保存在cursor中
            cursor.execute(sql)

            # 1-从cursor中获取全部数据用fetchall
            datas = cursor.fetchall()
            # print(type(datas))
            for i in datas[0]:
                if i == datas[0][0]:
                    continue
                elif len(i) == 0:
                    continue
                print(i)
            print("获取的数据：\n",datas)

            # 2-从cursor中获取一条数据用fetchall
            # data = cursor.fetchone()
            # print("获取的数据：\n",data)

            # 3-想要从cursor中获取几条数据用fetchmany
            # datas = cursor.fetchmany(3)
            # print("获取的数据：\.n", datas)
            # 执行玩SQL语句要提交
            con.commit()
            print("提交成功")

    # except Exception as e:
    #     con.rollback()
    #     print("数据库异常：\n", e)
    # finally:
    #     # 不管成功还是失败，都要关闭数据库连接
    #     con.close()


if __name__ == '__main__':
    mysql_db()