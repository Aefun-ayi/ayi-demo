import datetime
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget
import untitled


class MainWindow(QWidget, untitled.Ui_Form):

    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tst)

    def tst(self):
        a = self.textEdit.toPlainText()
        info_list = a.split('\n')
        del info_list[0]
        del info_list[-1]
        print(info_list)
        # 筛选出包含“头”字的元素
        filtered_elements = [element for element in info_list if '头-' in element]

        # 根据筛选出的元素进行分割
        result_lists = []
        current_list = []

        for element in info_list:
            if element in filtered_elements:
                # 如果元素在筛选出的列表中，创建新的列表
                if current_list:
                    result_lists.append(current_list)
                current_list = [element]
            else:
                current_list.append(element)

        # 添加最后一个列表
        result_lists.append(current_list)

        now = datetime.datetime.now()
        date = now.strftime('%m')
        pro_date = now.strftime('%m%d-%H-%M')
        isExists = os.path.exists(fr'D:\keep\公用-储存安装包\{date}_moon')
        if not isExists:
            os.mkdir(fr'D:\keep\公用-储存安装包\{date}_moon')
            # self.ParentDirectory.emit(fr'D:\keep\公用-储存安装包\{date}_moon' + ' 创建成功')
            print(fr'D:\keep\公用-储存安装包\{date}_moon' + ' 创建成功')
        else:
            pass

        # 打印分割后的子列表
        for sublist in result_lists:
            directory_name = sublist[0]
            # 创建目录
            os.makedirs(fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{directory_name}', exist_ok=True)
            # 文件路径，使用子列表的第二个元素作为文件名
            file_path = os.path.join(fr'D:\keep\公用-储存安装包\{date}_moon\{pro_date}{directory_name}',
                                         f"{sublist[1]}.txt")
            # 写入文件内容，使用子列表的第三到最后一个元素
            with open(file_path, 'w') as file:
                file.write('\n'.join(sublist[2:]))
            # self.ProductDirectory.emit(f'{pro_date}{directory_name}创建成功，需求：{sublist[2:]}成功写入')
            print(f'{pro_date}{directory_name}创建成功，需求：{sublist[2:]}成功写入')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
