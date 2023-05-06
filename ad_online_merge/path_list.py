import os



class system(object):
    def get_filename(self, prj_path):
        lists = os.listdir(prj_path)  # 列出目录的下所有文件和文件夹保存到lists
        lists.sort(key=lambda fn: os.path.getmtime(prj_path + "\\" + fn))  # 按时间排序
        file_new = os.path.join(prj_path, lists[-1])  # 获取最新的文件保存到file_new
        return file_new


    def get_file_app_info(self, prj_path):
        lists = os.listdir(prj_path)  # 列出目录的下所有文件和文件夹保存到lists
        print(lists)
        lists.sort(key=lambda fn: os.path.getmtime(prj_path + "\\" + fn))  # 按时间排序
        pid = lists[-1].split("_")[0]
        cha = lists[-1].split("_")[3]
        appid = pid[:-3]
        return appid, cha, pid


    def getCurrentPath(self, keyword='.'):
        """
        获取当前路径
        :keyword:./代表当前所在的目录，../ 代表上一层目录，../../ 代表上上一层目录， / 代表根目录
        :return: 路径
        """
        path = self.os.path.abspath(f'{keyword}')
        return path


    def makedirs(self, path):
        """
        创建多个文件目录
        :path:.文件路径
        :return: 文件路径
        """
        try:
            self.os.makedirs(path)
            return path
        except FileExistsError as e:
            print(type(e), e)


    def create_folder_HMS(self, path):
        """
        在指定目录下根据当前时分秒创建一个文件目录
        :param path: 文件绝对路径
        :return: 返回已经创建完成文件夹的绝对路径
        """
        try:
            folderName = fr'{path}\{self.time_HM}'
            self.os.makedirs(folderName)
            return folderName
        except FileExistsError as e:
            print(e)


    def create_folder_YMD(self, path):
        """
        在指定目录下根据当前年月日创建一个文件目录
        :param path: 绝对路径
        :return: 返回已经创建完成文件夹的绝对路径
        """
        try:
            folderName = fr'{path}\{self.time_YMD}'
            self.os.makedirs(folderName)
            return folderName
        except FileExistsError as e:
            print(e)


    def create_fulltime_folder(self, path):
        """
        在指定目录下根据当前年月日/时分秒创建一个文件目录
        :param path: 绝对路径
        :return: 返回已经创建完成文件夹的绝对路径
        """
        try:
            self.create_folder_YMD(path)
        except FileExistsError as e:
            # 可以忽略的报错
            print(e)
        finally:
            fullTimePath = self.create_folder_HMS(fr'{path}\{self.time_YMD}')
            return fullTimePath

        #   得到一个路径下所有的[文件夹名称]


    def get_dirs_name(self, filepath):
        """
        得到一个路径下所有的[文件夹名称]
        :param filepath:绝对路径
        :return:
        """
        for root, dirs, files in os.walk(filepath):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录
            # print(files) #当前路径下所有非目录子文件
            return dirs


    def get_files_name(self, filepath):
        """
        得到一个路径下所有的[文件夹名称]
        :param filepath:绝对路径
        :return:
        """
        for root, dirs, files in os.walk(filepath):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录
            # print(files) #当前路径下所有非目录子文件
            return files
        #   得到一个路径下所有的[文件夹名称]


    def get_dirs_ptha(self, filepath):
        """
        得到一个路径下所有的[文件夹名称]
        :param filepath:绝对路径
        :return:
        """
        pathlist = []
        for root, dirs, files in os.walk(filepath):
            for i in files:
                path = fr'{filepath}\{i}'
                pathlist.append(path)
        return pathlist

    def get_files_num(self, filepath):
        apk_count = 0
        for root, dirs, files in os.walk(filepath):  # 遍历统计
            for each in files:
                if each.endswith('apk'):
                    apk_count += 1  # 统计文件夹下apk文件个数
        return apk_count
