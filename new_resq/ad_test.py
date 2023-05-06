import requests
import re

class AD_Test():

    def ad_id(self):
        space_id = ['没有token情况下请求的配置如下：']
        url = 'https://ttt.yangguangzhujia.com/commercial/space/adSelect'
        head = {
            "Content-Type": "application/json"
        }
        data = {
            "appId": "39136",
            "type": "1"
        }
        res = requests.post(url, headers=head, json=data)
        ad_info = res.json()['data']
        for i in range(len(ad_info)):
            space_id.append(ad_info[i]['value'])
        print(space_id)
        return space_id

    def spacead(self):
        url = 'http://192.168.7.30:8009/ttt_spaceid'
        res = requests.get(url)
        ad_info = res.json()['田园走路']
        print(ad_info)
        return ad_info

    def remove_punctuation_and_replace(self, s):
        remove_douhao = re.sub(r',', '\n', str(s)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
        remove_danyinhao = remove_douhao.replace("'", '')
        remove_xiegang = remove_danyinhao.replace('/', '\n')
        remove_juhao = remove_xiegang.replace('。', '\n')
        return remove_juhao.replace(' ', '')


    def space(self):
        splash_name = []
        splash_source = []
        video_name = []
        video_source = []
        plaque_name = []
        plaque_source = []
        msg_name = []
        msg_source = []

        url = 'https://ttt.careduka.com/space-slot/getSlotList'
        head = {
            "Content-Type": "application/json"
        }
        for i in self.spacead():
            data = {
                    "is_new":"2",   #是否新老 这个参数比较重要 用于切用户人群
                    "app_id":"39136",  # 需替换对应产品id
                    "space_id":f"{i}"  # 这个可以查询获取对应的space id   只能当做假设使用 假设本地代码写入的spaceid正确所请求出的广告信息
            }
            res = requests.post(url, headers=head, json=data)
            cfg = res.json()
            print(cfg)
            try:
                if cfg['message'] == '该广告位id不存在':
                    print(f'缺少正确的space id: {i}，请联系变现确认')
                else:
                    slot = res.json()['data']['rit_group']
                    for i in range(len(slot)):
                        bidding = slot[i]['rit']['binding']
                        if slot[i]['ad_type'] == 1:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                splash_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}。")
                                splash_source.append(f'代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}。')
                            waterfall = slot[i]['rit']['price']
                            for iii in range(len(waterfall)):
                                waterfall_source = waterfall[iii]['rit_name']
                                waterfall_id = waterfall[iii]['rit_id']
                                splash_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}。")
                                splash_source.append(f"代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}。")
                        if slot[i]['ad_type'] == 2:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                video_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}。")
                                video_source.append(f"代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}。")
                            waterfall = slot[i]['rit']['price']
                            for iii in range(len(waterfall)):
                                waterfall_source = waterfall[iii]['rit_name']
                                waterfall_id = waterfall[iii]['rit_id']
                                video_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}。")
                                video_source.append(f"代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}。")
                        if slot[i]['ad_type'] == 3:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                msg_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}。")
                                msg_source.append(f"代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}。")
                            waterfall = slot[i]['rit']['price']
                            for iii in range(len(waterfall)):
                                waterfall_source = waterfall[iii]['rit_name']
                                waterfall_id = waterfall[iii]['rit_id']
                                msg_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}/")
                                msg_source.append(f"代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}。")
                        if slot[i]['ad_type'] == 4:
                            for ii in range(len(bidding)):
                                bidding_source = bidding[ii]['rit_name']
                                bidding_id = bidding[ii]['rit_id']
                                plaque_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}。")
                                plaque_source.append(f"代码位名称：bidding-{bidding_source}/代码位id：{bidding_id}。")
                            waterfall = slot[i]['rit']['price']
                            for iii in range(len(waterfall)):
                                waterfall_source = waterfall[iii]['rit_name']
                                waterfall_id = waterfall[iii]['rit_id']
                                plaque_name.append(f"广告位名称：{res.json()['data']['space_id_name']}/space_id：{res.json()['data']['space_id']}/")
                                plaque_source.append(f"代码位名称：waterfall-{waterfall_source}/代码位id：{waterfall_id}。")
            except TypeError as t:
                print(f'异常报错：{t}')
        splash_name_info = self.remove_punctuation_and_replace(splash_name)
        print(splash_name_info)
        video_name_info = self.remove_punctuation_and_replace(video_name)
        print(video_name_info)
        msg_name_info = self.remove_punctuation_and_replace(msg_name)
        print(msg_name_info)
        plaque_name_info = self.remove_punctuation_and_replace(plaque_name)
        print(plaque_name_info)

        splash_source_info = self.remove_punctuation_and_replace(splash_source)
        print(splash_source_info)
        video_source_info = self.remove_punctuation_and_replace(video_source)
        print(video_source_info)
        plaque_source_info = self.remove_punctuation_and_replace(plaque_source)
        print(plaque_source_info)
        msg_source_info = self.remove_punctuation_and_replace(msg_source)
        print(msg_source_info)



# 代码测试



if __name__ == '__main__':
    a = AD_Test()
    a.ad_id()
    a.space()
    a.spacead()
