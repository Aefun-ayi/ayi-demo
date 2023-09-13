from PyQt5.QtCore import QThread, pyqtSignal, QMutex
import uiautomator2 as u2
import os
import datetime


class WorkerScreenhostOne(QThread):
    PhoneConnectError = pyqtSignal(str)
    DirNameNone = pyqtSignal(str)
    ImgPath = pyqtSignal(str)
    CreateDirTips = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        scrInfo = self.queue.get()
        dir_name = scrInfo.split("&")[0]
        device_id = scrInfo.split("&")[1]
        try:
            # 加入try 避免出现连接失败时产生的闪退问题
            d = u2.connect(device_id)
        except RuntimeError as run:
            self.PhoneConnectError.emit(run)
        # 判断输入为空处理
        if dir_name == '':
            self.DirNameNone.emit("请输入创建五图文件夹的目录名")
        else:
            if '\n' in dir_name:
                dir_remove_line = dir_name.replace("\n", '')
                # 把里面的空格替换成下划线，为了满足创建文件夹的名称限制
                dir_path = dir_remove_line.replace('	', '_')
                isExists = os.path.exists(fr'D:\keep\五图截图\{dir_path}')
                # 进入判断是否存在这个文件夹
                if isExists:
                    # 时间戳
                    filetime = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日',)
                    # 截图路径
                    path = d.screenshot(fr"D:\keep\五图截图\{dir_path}\{filetime}五图-1.png")
                    self.ImgPath.emit(path)
                else:
                    self.CreateDirTips.emit(fr'D:\keep\五图截图\{dir_path}' + ' 目录不存在，请先创建对应目录')
