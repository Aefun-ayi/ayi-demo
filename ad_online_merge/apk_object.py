import re
import subprocess
from path_list import system



class apk(object):
    def __init__(self, APpath):
        # self.log = Logging().log(level='INFO')
        # self.get = GetInfo()
        self.os_p = system()
        self.set_AppInof(APpath)
        self.apk_name = self.get_appPackagename(APpath)
        # 路径问题
        # self.apk_name_list = self.get_Packagename_list(r'/test_apk')
        # self.AppInof = self.get_AppInof_dict(r'/test_apk')
        # self.cha_id =
        # self.appid =
        #  得到一个路径下可读的包信息，包名作为主键，返回一个字典{包名：文件名}

    def set_AppInof(self, APpath):
        file_name = APpath.split('\\')[-1]
        apkinfo_list = file_name.split('_')
        try:
            # 处理appid
            appid = list(apkinfo_list[0])[0:5]
            self.appid = ''.join(appid)
            self.pid = apkinfo_list[0]
            self.apk_name_file = apkinfo_list[1]
            self.version = apkinfo_list[2]
            self.cha = apkinfo_list[3]
            self.Out_time = apkinfo_list[4]
        except Exception as e:
            print('不合法的apk文件名称')
            # self.log.error(f'不合法的apk文件名称:{e}')


    # def get_AppInof_dict(self, path):
    #     """
    #     :param path: 传入包的路径
    #     :return: 返回一个字典{项目id：[文件名]}
    #     """
    #     sqlit_file_name = []
    #     appinfo_dict = {}
    #     Packagename_list = self.get_Packagename_list(path)
    #     file_name_list = self.get.get_files_name(path, type='full_path')
    #     file_name_list = list(file_name_list)
    #     indexv = 0
    #     for file_name in file_name_list:
    #         sqlit_file_name.append(file_name.split('_'))
    #         new_sqlit_file_name = sqlit_file_name[indexv]
    #         new_sqlit_file_name.append(file_name)
    #         # print('>?>>',new_sqlit_file_name)
    #         indexv += 1
    #
    #     for index in range(len(Packagename_list)):
    #         # 包名是主键
    #         # appinfo_dict[Packagename_list[index]] = sqlit_file_name[index]
    #         appinfo_dict[sqlit_file_name[index][0]] = sqlit_file_name[index]
    #     # print('>?>>',appinfo_dict)
    #     return appinfo_dict


    def get_Packagename_list(self, path):
        appPackageNames = []
        file_name_list = self.get.get_files_name(path)
        for file_name in file_name_list:
            appPackageName = self.get_appPackagename(file_name)
            appPackageNames.append(appPackageName)
        return appPackageNames

        # 获取包名
    def get_appPackagename(self, APpath):
        """
        :param path: 包的绝对路径，反编译包得到包的包名
        :return:
        """
        cmd = "aapt dump badging %s" % APpath
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        appPackage = match.group(1)
        # 还可以返回本版号
        versionName = match.group(3)
        return appPackage
# ap = r'E:\AutomatedOffice\test_apk\39132007_com.android.hctslkg.twctsaio_1.0.0_xmttzn_20220923.apk'
# os_p = system()
# for i in list(os_p.get_dirs_ptha(r'F:\tools\createApk\outFloder')):
#     a = apk(i)
#     a.set_AppInof(i)
#     print(a.cha_id)
#     print(a.pid)
#     print(a.appid)

