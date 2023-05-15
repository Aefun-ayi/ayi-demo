from PyQt5.QtCore import QThread, pyqtSignal, QMutex
import path_list
from apk_object import apk
from Pattern_Test import Pattern_API
import re



class Worker(QThread):
    sig1 = pyqtSignal(str)
    sig2 = pyqtSignal(str)

    def __init__(self, queue):
        # 通过调用父类构造函数并设置初始计数值来初始化工作线程
        super().__init__()
        self.queue = queue

    def run(self):
        path = self.queue.get()
        os_p = path_list.system()
        for i in list(os_p.get_dirs_ptha(fr"{path}")):
            a = apk(i)
            a.set_AppInof(i)
            t = Pattern_API(a)
            update_lose = str(t.testms()[0])
            update_pass = str(t.testms()[1])
            remove_douhao_lose = re.sub(r',', '\n', update_lose[1:-1])
            remove_danyinhao_lose = remove_douhao_lose.replace("'", '')
            keep_otc_lose = remove_danyinhao_lose.replace('"', '')
            remove_douhao_pass = re.sub(r',', '\n', update_pass[1:-1])
            remove_danyinhao_pass = remove_douhao_pass.replace("'", '')
            keep_otc_pass = remove_danyinhao_pass.replace('"', '')
            self.sig1.emit(f'项目id：{a.pid} \n渠道：{a.cha} \n{keep_otc_pass}\n----------------------------------\n')
            self.sig2.emit(f'项目id：{a.pid} \n渠道：{a.cha} \n{keep_otc_lose}\n----------------------------------\n')