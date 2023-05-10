from online_config import OnlineCfg


class Pattern_API():
    def __init__(self, apk_object):
        # self.API.v2() = OnlineCfg().v2()
        # self.API.v3fk() = OnlineCfg().v3fk()
        # self.API.audit() = OnlineCfg().audit()
        # self.API.custom() = OnlineCfg().custom()
        # self.API.first() = OnlineCfg().first()
        # self.API.dmo() = OnlineCfg().dmo()
        self.API = OnlineCfg(apk_object.appid, apk_object.cha, apk_object.pid)

    def exception_handling(self, func):
        try:
            func()
        except Exception as e:
            return None

    def testms(self):
        passlist = ['通过']
        loselist = ['失败']

        if self.API.jh()['status']:
            if self.API.jh()['status'] == '1':
                passlist.append("V2锁屏开关：打开")
                if self.API.jh()['lockSwitch'] == '1':
                    passlist.append("锁屏新闻开关：打开")
                elif self.API.jh()['lockSwitch'] == '0':
                    loselist.append("锁屏新闻开关：关闭")
                else:
                    loselist.append("找不到锁屏新闻配置")

                if self.API.jh()['unLockSwitch'] == '1':
                    passlist.append("解锁后弹窗开关：打开")
                    passlist.append(f"解锁后弹窗频次：{self.API.jh()['unLockInterval']}")
                elif self.API.jh()['unLockSwitch'] == '0':
                    loselist.append("解锁后弹窗开关：关闭")
                else:
                    loselist.append("找不到解锁后弹窗配置")

                if self.API.jh()['homeSwitch'] == '1':
                    passlist.append("home键弹窗开关：打开")
                    passlist.append(f"home键弹窗频次：{self.API.jh()['homeInterval']}")
                elif self.API.jh()['homeSwitch'] == '0':
                    loselist.append("home键弹窗开关：关闭")
                else:
                    loselist.append("找不到home键弹窗配置")

                if self.API.jh()['dianLiangSwitch'] == '1':
                    passlist.append("电量场景开关：打开")
                elif self.API.jh()['dianLiangSwitch'] == '0':
                    loselist.append("电量场景开关：关闭")
                else:
                    loselist.append("找不到电量场景配置")

                if self.API.jh()['chongdianSwitch'] == '1':
                    passlist.append("充电场景开关：打开")
                elif self.API.jh()['chongdianSwitch'] == '0':
                    loselist.append("充电场景开关：关闭")
                else:
                    loselist.append("找不到充电场景配置")

                if self.API.jh()['taSw'] == '1':
                    passlist.append("定时弹窗场景开关：打开")
                    passlist.append(f"定时弹窗频次：{self.API.jh()['taIt']}")
                elif self.API.jh()['taSw'] == '0':
                    loselist.append("定时弹窗场景开关：关闭")
                else:
                    loselist.append("找不到定时弹窗配置")
            if self.API.jh()['nqDt'] == '0':
                passlist.append(f"自然量延时{self.API.jh()['nqDt']}秒")
            else:
                loselist.append(f"自然量延时{self.API.jh()['nqDt']}秒")
            if self.API.jh()['city'] == '4403' and self.API.jh()['cityStatus'] == '1':
                loselist.append("V2锁屏在线配置已屏蔽深圳")
            else:
                passlist.append("V2锁屏在线配置未屏蔽深圳")

        elif self.API.jh()['status'] == '0':
            loselist.append("V2锁屏开关：关闭")

        elif not self.API.jh()['status']:
            loselist.append('v2锁屏配置为空')

        if len(self.API.audit()) < 1:
            passlist.append(f"分渠道全部配置v20配置为空：{self.API.audit()}，默认关闭")
        else:
            if self.API.audit()[0]['app_audit'] == 0:
                passlist.append("审核关闭")
            else:
                loselist.append("审核打开")

        if len(self.API.first()['list']) < 1:
            passlist.append(f"合规化配置为空：{self.API.first()['list']}，默认关闭")
        else:
            if self.API.first()['list'][0]['audit'] == '0':
                passlist.append("合规化关闭")
            else:
                loselist.append("合规化打开")

        if len(self.API.v3fk()['list']) < 1:
            loselist.append(f"v3风控配置为空：{self.API.v3fk()['list']}，默认打开")
        else:
            if self.API.v3fk()['list'][0]['enable'] == '0':
                passlist.append("v3风控关闭")
            else:
                loselist.append("v3风控打开")

        if len(self.API.custom()) < 1:
            loselist.append(f"vpush风控配置为空：{self.API.custom()}，未配自定义参数，默认打开")
        else:
            if '"vivo_push_safe_check": "0"' in self.API.custom()[0]['params']:
                passlist.append("vpush风控关闭")
            else:
                loselist.append("vpush风控打开")
        try:
            if 'd_status' in self.API.jh():
                if self.API.jh()['d_status'] == '1':
                    passlist.append("D模式配置开关：打开")
                    passlist.append(f"D模式上报比例：{self.API.jh()['d_rate']}")
                    passlist.append(f"D模式延时时间：{self.API.jh()['d_atTime']}")
                elif self.API.jh()['d_status'] == '0':
                    loselist.append("D模式配置开关：关闭")
                else:
                    loselist.append("D模式配置为空")
            else:
                loselist.append("D模式配置为空")
        except:
            loselist.append('D模参数有误，请手动检查')

        return loselist,passlist


#
# if __name__ == '__main__':
#     a = Pattern_API()
#     a.testms()
#     print(a.testms()[0])
#     print(a.testms()[1])
