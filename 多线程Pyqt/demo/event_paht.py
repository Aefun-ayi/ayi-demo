from PyQt5 import QtCore


class QEventHandler(QtCore.QObject):
    def eventFilter(self, obj, event):
        """
        目前已经实现将拖到控件上文件的路径设置为控件的显示文本；
        """
        if event.type() == QtCore.QEvent.DragEnter:
            event.accept()
        if event.type() == QtCore.QEvent.Drop:
            md = event.mimeData()
            if md.hasUrls():
            	# 此处md.urls()的返回值为拖入文件的file路径列表，支持多文件同时拖入；默认读取第一个文件的路径进行处理
                url = md.urls()[0]
                obj.setText(url.toLocalFile())
                # print(str(url.toLocalFile()))
                # print(type(url))
                return True
        return super().eventFilter(obj, event)