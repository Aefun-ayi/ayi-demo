import os
import sys
import requests
from PyQt5.QtGui import QTextOption, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore
import CombineTestToolsFrame
from qt_material import apply_stylesheet
import qtawesome as qta
from EventHandler import QEventHandler
from queue import Queue
from DevicesInfo import get_connected_device_models
from CreateImgDir import ImgDriName
from WorkerAuto import Worker_Auto
from WorkerAshing import WorkerAshingMain
from WorkerTestToolsInstall import WorkerTestToolsInstallMain
from WorkerCheckProcess import WorkerCheckProcessMain
from WorkerStopApp import WorkerStopAppMain
from WorkerStartApp import WorkerStartAppMain
from WorkerUninstallApp import WorkerUninstallAppMain
from WorkerClearApp import WorkerClearAppMain
from WorkerDebugApp import WorkerDebugAppMain
from WorkerUnDebugApp import WorkerUnDebugAppMain
from WorkerAdSelect import WorkerAdSelect
from WorkerOnlineInfo import WorkerOnline
from WorkerAdContrast import WorkerAdContrast
from WorkerScreenOne import WorkerScreenhostOne
from WorkerScreenhostTwo import WorkerScreenhostTwo
from WorkerScreenhostThree import WorkerScreenhostThree
from WorkerScreenhostFour import WorkerScreenhostFour
from WorkerScreenhostFive import WorkerScreenhostFive
from WorkerLookLock import WorkerLookLock
from WorkerLookUnlock import WorkerLookUnlock
from WorkerLookUnLockAd import WorkerLookUnlockAd
from WorkerLookHome import WorkerLookHome
from WorkerLookHomeAd import WorkerLookHomeAd
from WorkerLookCharge import WorkerLookCharge
from WorkerLookChargeAd import WorkerLookChargeAd
from WorkerLookWifi import WorkerLookWifi
from WorkerLookWifiAd import WorkerLookWifiAd
from WorkerLookTimer import WorkerLookTimer
from WorkerLookTimerAd import WorkerLookTimerAd
from WorkerAshingLookLock import WorkerAshingLookLock
from WorkerAshingLookUnlock import WorkerAshingLookUnlock
from WorkerAshingLookUnlockAd import WorkerAshingLookUnlockAd
from WorkerAshingLookHome import WorkerAshingLookHome
from WorkerAshingLookHomeAd import WorkerAshingLookHomeAd
from WorkerAshingLookCharge import WorkerAshingLookCharge
from WorkerAshingLookChargeAd import WorkerAshingLookChargeAd
from WorkerAshingLookWifi import WorkerAshingLookWifi
from WorkerAshingLookWifiAd import WorkerAshingLookWifiAd
from WorkerAshingLookTimer import WorkerAshingLookTimer
from WorkerAshingLookTimerAd import WorkerAshingLookTimerAd
from WorkerCreateDirfile import WorkerCreateDirfile
from WorkerOnlineConfigOneself import WorkerOnlineConfigOneselfMain
import ApiConfig
import DownloadWindow



class MainWindow(QWidget, CombineTestToolsFrame.Ui_Form):

    def __init__(self, parent=None):
        # 通过调用父类构造函数并设置UI来初始化主窗口
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        starticon = qta.icon('mdi.restart', color='green')  #启动按钮icon
        refreshicon = qta.icon('ri.restart-line', color='green')  #刷新icon
        createicon = qta.icon('msc.new-folder', color='green')  #新增icon
        installicon = qta.icon('ei.download-alt', color='green')  #安装icon
        checkicon = qta.icon('mdi6.progress-check', color='green')  #查看进程icon
        stopicon = qta.icon('fa.hand-stop-o', color='green')  #强停icon
        uninstallicon = qta.icon('ei.remove', color='green')   #卸载icon
        debugicon = qta.icon('mdi6.key-plus', color='green')   #开debug icon
        undebugicon = qta.icon('mdi6.key-remove', color='green')  #关debug icon
        screenicon = qta.icon('mdi.cellphone-screenshot', color='green')
        selectIcon = qta.icon('ei.search', color='green')  #查询按钮icon
        clearIcon = qta.icon('fa5s.quidditch', color='green')  # 清理按钮icon
        # 查询页面icon设置
        self.SelectOnline.setIcon(selectIcon)
        self.SelectAd.setIcon(selectIcon)
        self.VerifyAd.setIcon(selectIcon)
        self.VerifyAd.setIconSize(QtCore.QSize(35, 35))
        self.ClearOnlineText.setIcon(clearIcon)
        self.ClearAdText.setIcon(clearIcon)
        self.ClearVerifyAdText.setIcon(clearIcon)
        self.ClearVerifyAdText.setIconSize(QtCore.QSize(35, 35))
        self.OneselfSelect.setIcon(selectIcon)
        self.OneselfClear.setIcon(clearIcon)

        # 创建目录页面icon设置
        self.CreateDir.setIcon(createicon)
        self.CreateDir.setIconSize(QtCore.QSize(35, 35))
        self.CreateClear.setIcon(clearIcon)
        self.CreateClear.setIconSize(QtCore.QSize(35, 35))

        # 刷新设备icon设置
        self.DevicesRefresh.setIcon(refreshicon)
        self.DevicesRefresh.setIconSize(QtCore.QSize(30, 30))

        # 截图-五图页面icon设置
        self.ImgMkdirName.setIcon(createicon)
        self.ImgMkdirName.setIconSize(QtCore.QSize(30, 30))
        self.ScreenOne.setIcon(screenicon)
        self.ScreenOne.setIconSize(QtCore.QSize(30, 30))
        self.ScreenTwo.setIcon(screenicon)
        self.ScreenTwo.setIconSize(QtCore.QSize(30, 30))
        self.ScreenThree.setIcon(screenicon)
        self.ScreenThree.setIconSize(QtCore.QSize(30, 30))
        self.ScreenFour.setIcon(screenicon)
        self.ScreenFour.setIconSize(QtCore.QSize(30, 30))
        self.ScreenFive.setIcon(screenicon)
        self.ScreenFive.setIconSize(QtCore.QSize(30, 30))

        # 测试-工具页面icon设置
        self.ClearPathText.setIcon(clearIcon)
        self.InstallApp.setIcon(installicon)
        self.StartApp.setIcon(starticon)
        self.StartApp.setIconSize(QtCore.QSize(30, 30))
        self.CheckProcess.setIcon(checkicon)
        self.CheckProcess.setIconSize(QtCore.QSize(30, 30))
        self.StopApp.setIcon(stopicon)
        self.StopApp.setIconSize(QtCore.QSize(30, 30))
        self.UninstallApp.setIcon(uninstallicon)
        self.ClearApp.setIcon(clearIcon)
        self.DebugApp.setIcon(debugicon)
        self.DebugApp.setIconSize(QtCore.QSize(30, 30))
        self.UndebugApp.setIcon(undebugicon)
        self.UndebugApp.setIconSize(QtCore.QSize(30, 30))
        self.ClearProcessText.setIcon(clearIcon)

        # 外广自动化强停一次页面icon设置
        self.AutoStart.setIcon(starticon)
        self.AutoStart.setIconSize(QtCore.QSize(30, 30))
        self.AutoClearPathText.setIcon(clearIcon)
        self.AutoLockLook.setIcon(selectIcon)
        self.AutoUnlockLook.setIcon(selectIcon)
        self.AutoChargeLook.setIcon(selectIcon)
        self.AutoWifiLook.setIcon(selectIcon)
        self.AutoTimerLook.setIcon(selectIcon)
        self.AutoHomeLook.setIcon(selectIcon)
        self.AutoAdUnlockLook.setIcon(selectIcon)
        self.AutoAdChargeLook.setIcon(selectIcon)
        self.AutoAdHomeLook.setIcon(selectIcon)
        self.AutoAdWifiLook.setIcon(selectIcon)
        self.AutoAdTimerLook.setIcon(selectIcon)

        # 外广自动化强停置灰页面icon设置
        self.AshingStart.setIcon(starticon)
        self.AshingStart.setIconSize(QtCore.QSize(30, 30))
        self.AshingClearPathText.setIcon(clearIcon)
        self.AshingLockLook.setIcon(selectIcon)
        self.AshingUnlockLook.setIcon(selectIcon)
        self.AshingChargeLook.setIcon(selectIcon)
        self.AshingWifiLook.setIcon(selectIcon)
        self.AshingTimerLook.setIcon(selectIcon)
        self.AshingHomeLook.setIcon(selectIcon)
        self.AshingAdUnlockLook.setIcon(selectIcon)
        self.AshingAdChargeLook.setIcon(selectIcon)
        self.AshingAdHomeLook.setIcon(selectIcon)
        self.AshingAdWifiLook.setIcon(selectIcon)
        self.AshingAdTimerLook.setIcon(selectIcon)

        # 设置提示文字，并把输入框解放出来可接收文件
        OnlineApkDir = self.LineApkdirPath.installEventFilter(QEventHandler(self.LineApkdirPath))
        self.LineApkdirPath.setPlaceholderText("请拖入出包文件夹生成路径或复制文件夹路径，注意路径中不可带中文！！！")
        TestApkPath = self.TestToolsPathText.installEventFilter(QEventHandler(self.TestToolsPathText))
        self.TestToolsPathText.setPlaceholderText("拖入apk生成路径或复制apk路径后开始操作")
        Autopath = self.AutoPathText.installEventFilter(QEventHandler(self.AutoPathText))
        self.AutoPathText.setPlaceholderText("拖入apk生成路径或复制apk路径后开始操作")
        Ashpath = self.AshingPathText.installEventFilter(QEventHandler(self.AshingPathText))
        self.AshingPathText.setPlaceholderText("拖入apk生成路径或复制apk路径后开始操作")

        # 设定文字居中显示
        self.option = QTextOption()
        self.option.setAlignment(Qt.AlignCenter)

        # 查询在现配置的线程连接
        self.OnlineQueue = Queue()
        self.OnlineThread = WorkerOnline(self.OnlineQueue)
        self.OnlineThread.Pass.connect(self.UpdateSucCfg)
        self.OnlineThread.Lose.connect(self.UpdateFailCfg)
        self.SelectOnline.clicked.connect(self.OnlineSelectClick)
        self.ClearOnlineText.clicked.connect(self.OnlineCleanClick)

        # 查询广告配置的点击连接以及线程连接
        self.SelectAdQueue = Queue()
        self.SelectAdThread = WorkerAdSelect(self.SelectAdQueue)
        self.SelectAdThread.AllGroup.connect(self.SelectAd_All_Group)
        self.SelectAdThread.AGroup.connect(self.SelectAd_A_Group)
        self.SelectAdThread.BGroup.connect(self.SelectAd_B_Group)
        self.SelectAdThread.CGroup.connect(self.SelectAd_C_Group)
        self.SelectAdThread.SplashName.connect(self.SelectAdSplashName)
        self.SelectAdThread.MsgName.connect(self.SelectAdMsgName)
        self.SelectAdThread.VideoName.connect(self.SelectAdVideoName)
        self.SelectAdThread.PlaqueName.connect(self.SelectAdPlaqueName)
        self.SelectAdThread.SplashSources.connect(self.SelectAdSplashSources)
        self.SelectAdThread.MsgSources.connect(self.SelectAdMsgSources)
        self.SelectAdThread.VideoSources.connect(self.SelectAdVideoSources)
        self.SelectAdThread.PlaqueSources.connect(self.SelectAdPlaqueSources)
        self.SelectAd.clicked.connect(self.AdSelectClick)
        self.ClearAdText.clicked.connect(self.AdClearClick)

        # 确认广告配置的点击连接
        self.AdContrastQueue = Queue()
        self.AdContrastThread = WorkerAdContrast(self.AdContrastQueue)
        self.AdContrastThread.Match.connect(self.AdContrastMatch)
        self.AdContrastThread.Tmr.connect(self.AdContrastTmr)
        self.AdContrastThread.Lack.connect(self.AdContrastLack)
        self.VerifyAd.clicked.connect(self.AdNameContrast)
        self.ClearVerifyAdText.clicked.connect(self.AdNameClear)

        # 查询在线配置--单独的点击连接
        self.OneSelfOnlineCfgQueue = Queue()
        self.OneSelfOnlineCfgThread = WorkerOnlineConfigOneselfMain(self.OneSelfOnlineCfgQueue)
        self.OneSelfOnlineCfgThread.OnlineCfgLog.connect(self.OneSelfOnlineConfigLogUpdate)
        self.OneselfSelect.clicked.connect(self.OneSelfOnlineConfigSelect)
        self.OneselfClear.clicked.connect(self.OneSelfOnlineConfigClear)

        # 选择设备的刷新按钮点击连接
        self.DevicesRefresh.clicked.connect(self.DeviceRefresh)

        # 截图五图页面的点击连接
        self.ImgMkdirName.clicked.connect(self.CreateImgDriClick)

        self.ScreenOneQueue = Queue()
        self.ScreenOneThread = WorkerScreenhostOne(self.ScreenOneQueue)
        self.ScreenOne.clicked.connect(self.ScreenhostOne)
        self.ScreenOneThread.ImgPath.connect(self.ScreenImgShowOne)
        self.ScreenOneThread.CreateDirTips.connect(self.ScreenImgDriTipsOne)
        self.ScreenOneThread.DirNameNone.connect(self.ScreenImdDriNoneOne)
        self.ScreenOneThread.PhoneConnectError.connect(self.ScreenImgPhoneErrorOne)

        self.ScreenTwoQueue = Queue()
        self.ScreenTwoThread = WorkerScreenhostTwo(self.ScreenTwoQueue)
        self.ScreenTwo.clicked.connect(self.ScreenhostTwo)
        self.ScreenTwoThread.ImgPath.connect(self.ScreenImgShowTwo)
        self.ScreenTwoThread.CreateDirTips.connect(self.ScreenImgDriTipsTwo)
        self.ScreenTwoThread.DirNameNone.connect(self.ScreenImdDriNoneTwo)
        self.ScreenTwoThread.PhoneConnectError.connect(self.ScreenImgPhoneErrorTwo)

        self.ScreenThreeQueue = Queue()
        self.ScreenThreeThread = WorkerScreenhostThree(self.ScreenThreeQueue)
        self.ScreenThree.clicked.connect(self.ScreenhostThree)
        self.ScreenThreeThread.ImgPath.connect(self.ScreenImgShowThree)
        self.ScreenThreeThread.CreateDirTips.connect(self.ScreenImgDriTipsThree)
        self.ScreenThreeThread.DirNameNone.connect(self.ScreenImdDriNoneThree)
        self.ScreenThreeThread.PhoneConnectError.connect(self.ScreenImgPhoneErrorThree)

        self.ScreenFourQueue = Queue()
        self.ScreenFourThread = WorkerScreenhostFour(self.ScreenFourQueue)
        self.ScreenFour.clicked.connect(self.ScreenhostFour)
        self.ScreenFourThread.ImgPath.connect(self.ScreenImgShowFour)
        self.ScreenFourThread.CreateDirTips.connect(self.ScreenImgDriTipsFour)
        self.ScreenFourThread.DirNameNone.connect(self.ScreenImdDriNoneFour)
        self.ScreenFourThread.PhoneConnectError.connect(self.ScreenImgPhoneErrorFour)

        self.ScreenFiveQueue = Queue()
        self.ScreenFiveThread = WorkerScreenhostFive(self.ScreenFiveQueue)
        self.ScreenFive.clicked.connect(self.ScreenhostFive)
        self.ScreenFiveThread.ImgPath.connect(self.ScreenImgShowFive)
        self.ScreenFiveThread.CreateDirTips.connect(self.ScreenImgDriTipsFive)
        self.ScreenFiveThread.DirNameNone.connect(self.ScreenImdDriNoneFive)
        self.ScreenFiveThread.PhoneConnectError.connect(self.ScreenImgPhoneErrorFive)

        # 测试-工具页面的点击连接
        self.InstallQueue = Queue()
        self.InstallThread = WorkerTestToolsInstallMain(self.InstallQueue)
        self.InstallApp.clicked.connect(self.InstallAppMain)
        self.InstallThread.InstallInfo.connect(self.DemoInstall)
        self.InstallThread.PutFile.connect(self.DomeDebugInfo)
        self.CheckProcessQueue = Queue()
        self.CheckProcessThread = WorkerCheckProcessMain(self.CheckProcessQueue)
        self.CheckProcess.clicked.connect(self.CheckProcessMain)
        self.CheckProcessThread.ProcessInfo.connect(self.CheckProcessUpdate)
        self.ClearProcessText.clicked.connect(self.CheckProcessClear)
        self.StartAppQueue = Queue()
        self.StartAppThread = WorkerStartAppMain(self.StartAppQueue)
        self.StartApp.clicked.connect(self.StartAppMain)
        self.StopAppQueue = Queue()
        self.StopAppThread = WorkerStopAppMain(self.StopAppQueue)
        self.StopApp.clicked.connect(self.StopAppMain)
        self.UninstallAppQueue = Queue()
        self.UninstallAppThread = WorkerUninstallAppMain(self.UninstallAppQueue)
        self.UninstallApp.clicked.connect(self.UninstallAppMain)
        self.ClearAppQueue = Queue()
        self.ClearAppThread = WorkerClearAppMain(self.ClearAppQueue)
        self.ClearApp.clicked.connect(self.ClearAppMain)
        self.DebugAppQueue = Queue()
        self.DebugAppThread = WorkerDebugAppMain(self.DebugAppQueue)
        self.DebugApp.clicked.connect(self.DebugAppMain)
        self.DebugAppThread.DebugInfo.connect(self.DebugInfoMsgBox)
        self.UnDebugAppQueue = Queue()
        self.UnDebugAppThread = WorkerUnDebugAppMain(self.UnDebugAppQueue)
        self.UndebugApp.clicked.connect(self.UndebugAppMain)
        self.UnDebugAppThread.DebugInfo.connect(self.UnDebugInfoMsgBox)

        # 外广自动化-强停一次页面的线程连接
        self.AutoQueue = Queue()
        self.AutoThread = Worker_Auto(self.AutoQueue)
        self.AutoStart.clicked.connect(self.AutoDriver)
        self.AutoThread.log.connect(self.UpdateAutoCfg)
        self.AutoThread.lock_img_path.connect(self.LockUpdate)
        self.AutoThread.unlock_img_path.connect(self.UnlockUpdate)
        self.AutoThread.unlock_ad_path.connect(self.UnlockAdUpdate)
        self.AutoThread.charge_img_path.connect(self.ChargeUpdate)
        self.AutoThread.charge_ad_path.connect(self.ChargeAdUpdate)
        self.AutoThread.wifi_img_path.connect(self.WifiUpdate)
        self.AutoThread.wifi_ad_path.connect(self.WifiAdUpdate)
        self.AutoThread.home_img_path.connect(self.HomeUpdate)
        self.AutoThread.home_ad_path.connect(self.HomeAdUpdate)
        self.AutoThread.timing_img_path.connect(self.TimerUpdate)
        self.AutoThread.timing_ad_path.connect(self.TimerAdUpdate)
        self.AutoClearPathText.clicked.connect(self.ClearAutoPathText)
        # 外广-自动化（强停置灰）页面的线程连接
        self.AshingQueue = Queue()
        self.AshingThread = WorkerAshingMain(self.AshingQueue)
        self.AshingStart.clicked.connect(self.AshingDriver)
        self.AshingThread.log.connect(self.UpdateAshingCfg)
        self.AshingThread.lock_img_path.connect(self.AshingLockUpdate)
        self.AshingThread.unlock_img_path.connect(self.AshingUnlockUpdate)
        self.AshingThread.unlock_ad_path.connect(self.AshingUnlockAdUpdate)
        self.AshingThread.charge_img_path.connect(self.AshingChargeUpdate)
        self.AshingThread.charge_ad_path.connect(self.AshingChargeAdUpdate)
        self.AshingThread.wifi_img_path.connect(self.AshingWifiUpdate)
        self.AshingThread.wifi_ad_path.connect(self.AshingWifiAdUpdate)
        self.AshingThread.home_img_path.connect(self.AshingHomeUpdate)
        self.AshingThread.home_ad_path.connect(self.AshingHomeAdUpdate)
        self.AshingThread.timing_img_path.connect(self.AshingTimerUpdate)
        self.AshingThread.timing_ad_path.connect(self.AshingTimerAdUpdate)
        self.AshingClearPathText.clicked.connect(self.ClearAshingPathText)
        # 强停一次页面层级的查看原图按钮的线程
        self.LookLockQueue = Queue()
        self.LookLockThread = WorkerLookLock(self.LookLockQueue)
        self.LookUnlockQueue = Queue()
        self.LookUnlockThread = WorkerLookUnlock(self.LookUnlockQueue)
        self.LookUnlockAdQueue = Queue()
        self.LookUnlockAdThread = WorkerLookUnlockAd(self.LookUnlockAdQueue)
        self.LookChargeQueue = Queue()
        self.LookChargeThread = WorkerLookCharge(self.LookChargeQueue)
        self.LookChargeAdQueue = Queue()
        self.LookChargeAdThread = WorkerLookChargeAd(self.LookChargeAdQueue)
        self.LookWifiQueue = Queue()
        self.LookWifiThread = WorkerLookWifi(self.LookWifiQueue)
        self.LookWifiAdQueue = Queue()
        self.LookWifiAdThread = WorkerLookWifiAd(self.LookWifiAdQueue)
        self.LookHomeQueue = Queue()
        self.LookHomeThread = WorkerLookHome(self.LookHomeQueue)
        self.LookHomeAdQueue = Queue()
        self.LookHomeAdThread = WorkerLookHomeAd(self.LookHomeAdQueue)
        self.LookTimerQueue = Queue()
        self.LookTimerThread = WorkerLookTimer(self.LookTimerQueue)
        self.LookTimerAdQueue = Queue()
        self.LookTimerAdThread = WorkerLookTimerAd(self.LookTimerAdQueue)
        # 强停置灰页面层级的查看原图按钮的线程
        self.AshingLookLockQueue = Queue()
        self.AshingLookLockThread = WorkerAshingLookLock(self.AshingLookLockQueue)
        self.AshingLookUnlockQueue = Queue()
        self.AshingLookUnlockThread = WorkerAshingLookUnlock(self.AshingLookUnlockQueue)
        self.AshingLookUnlockAdQueue = Queue()
        self.AshingLookUnlockAdThread = WorkerAshingLookUnlockAd(self.AshingLookUnlockAdQueue)
        self.AshingLookChargeQueue = Queue()
        self.AshingLookChargeThread = WorkerAshingLookCharge(self.AshingLookChargeQueue)
        self.AshingLookChargeAdQueue = Queue()
        self.AshingLookChargeAdThread = WorkerAshingLookChargeAd(self.AshingLookChargeAdQueue)
        self.AshingLookWifiQueue = Queue()
        self.AshingLookWifiThread = WorkerAshingLookWifi(self.AshingLookWifiQueue)
        self.AshingLookWifiAdQueue = Queue()
        self.AshingLookWifiAdThread = WorkerAshingLookWifiAd(self.AshingLookWifiAdQueue)
        self.AshingLookHomeQueue = Queue()
        self.AshingLookHomeThread = WorkerAshingLookHome(self.AshingLookHomeQueue)
        self.AshingLookHomeAdQueue = Queue()
        self.AshingLookHomeAdThread = WorkerAshingLookHomeAd(self.AshingLookHomeAdQueue)
        self.AshingLookTimerQueue = Queue()
        self.AshingLookTimerThread = WorkerAshingLookTimer(self.AshingLookTimerQueue)
        self.AshingLookTimerAdQueue = Queue()
        self.AshingLookTimerAdThread = WorkerAshingLookTimerAd(self.AshingLookTimerAdQueue)
        # 查看原图按钮的线程连接
        self.AutoLockLook.clicked.connect(self.AutoLockLookMain)
        self.AutoUnlockLook.clicked.connect(self.AutoUnlockLookMain)
        self.AutoChargeLook.clicked.connect(self.AutoChargeLookMain)
        self.AutoWifiLook.clicked.connect(self.AutoWifiLookMain)
        self.AutoTimerLook.clicked.connect(self.AutoTimerLookMain)
        self.AutoHomeLook.clicked.connect(self.AutoHomeLookMain)
        self.AutoAdUnlockLook.clicked.connect(self.AutoAdUnlockLookMain)
        self.AutoAdChargeLook.clicked.connect(self.AutoAdChargeLookMain)
        self.AutoAdHomeLook.clicked.connect(self.AutoAdHomeLookMain)
        self.AutoAdWifiLook.clicked.connect(self.AutoAdWifiLookMain)
        self.AutoAdTimerLook.clicked.connect(self.AutoAdTimerLookMain)
        self.AshingLockLook.clicked.connect(self.AshingLockLookMain)
        self.AshingUnlockLook.clicked.connect(self.AshingUnlockLookMain)
        self.AshingChargeLook.clicked.connect(self.AshingChargeLookMain)
        self.AshingWifiLook.clicked.connect(self.AshingWifiLookMain)
        self.AshingTimerLook.clicked.connect(self.AshingTimerLookMain)
        self.AshingHomeLook.clicked.connect(self.AshingHomeLookMain)
        self.AshingAdUnlockLook.clicked.connect(self.AshingAdUnlockLookMain)
        self.AshingAdChargeLook.clicked.connect(self.AshingAdChargeLookMain)
        self.AshingAdHomeLook.clicked.connect(self.AshingAdHomeLookMain)
        self.AshingAdWifiLook.clicked.connect(self.AshingAdWifiLookMain)
        self.AshingAdTimerLook.clicked.connect(self.AshingAdTimerLookMain)
        # 创建目录的线程连接
        self.CreateDirQueue = Queue()
        self.CreateDirThread = WorkerCreateDirfile(self.CreateDirQueue)
        self.CreateDir.clicked.connect(self.CreateDirMain)
        self.CreateDirThread.ProductDirectory.connect(self.CreateDirProductDirTips)
        self.CreateDirThread.ParentDirectory.connect(self.CreateDirParentDirTips)
        self.CreateClear.clicked.connect(self.CreateClearDirText)
        # 启动时检查版本号 不符合则拉起接口下载新版
        self.CurrentVersion = '1.3'  # 当前版本号
        self.session = requests.Session()
        self.CheckVersion()
        # 启动时自动刷新一次设备信息填充至DevicesList
        self.DeviceRefresh()


    def CheckVersion(self):
        try:
            version_api = self.session.get(f'{ApiConfig.centos()}/version')
            remote_version = version_api.json()
            print(remote_version)
            if self.CurrentVersion != remote_version['version']:
                QMessageBox.warning(self, "提示", f"发现新版本{remote_version}，开始更新")
                self.chile_Win = DownloadWindow.MainWindow()
                self.chile_Win.show()
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # 定义桌面路径 获取任意使用的当前电脑的桌面路径
                exe = fr'{desktop_path}\测试工具箱V1.4.exe'  # 文件存放地址
                QMessageBox.warning(self, "提示", f"更新完成，存放路径{exe}，已放置桌面，请关闭旧版本，启动新版本开始使用")
                delay = 2000  # 延时2秒关闭窗口
                timer = QTimer()
                timer.start(delay)  # 启动定时器
                app.exec_()
        except:
            pass



    def OnlineSelectClick(self):
        path = self.LineApkdirPath.text()
        self.OnlineQueue.put(path)
        #点击按钮时启动工作线程
        self.OnlineThread.start()

    def UpdateSucCfg(self, text):
        self.SucConfig.append(text)
        self.SucConfig.document().setDefaultTextOption(self.option)

    def UpdateFailCfg(self, text):
        self.FailConfig.append(text)
        self.FailConfig.document().setDefaultTextOption(self.option)

    def OnlineCleanClick(self):
        self.SucConfig.clear()
        self.FailConfig.clear()

    def AdSelectClick(self):
        try:
            pid = self.SelectPrid.text()
            chan = self.SelectChan.text()
            # 输入项目id为空则弹窗提示
            if pid == '':
                pid_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入项目id')
                pid_msg_box.exec_()
            # 输入渠道标识为空则弹窗提示
            if chan == '':
                chan_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入渠道')
                chan_msg_box.exec_()
            else:
                appinfo = f"{pid}&{chan}"
                self.SelectAdQueue.put(appinfo)
                self.SelectAdThread.start()
        except Exception as e:
            tips = QMessageBox(QMessageBox.Critical, '错误', f'程序错误:{e}')
            tips.exec_()

    def SelectAd_All_Group(self, text):
        self.AllGroupText.append(text)
        self.AllGroupText.document().setDefaultTextOption(self.option)

    def SelectAd_A_Group(self, text):
        self.AGroupText.append(text)
        self.BGroupText.document().setDefaultTextOption(self.option)

    def SelectAd_B_Group(self, text):
        self.BGroupText.append(text)
        self.BGroupText.document().setDefaultTextOption(self.option)

    def SelectAd_C_Group(self, text):
        self.CGroupText.append(text)
        self.CGroupText.document().setDefaultTextOption(self.option)

    def SelectAdSplashName(self, text):
        self.SplashCfgText.append(text)
        self.SplashCfgText.document().setDefaultTextOption(self.option)

    def SelectAdMsgName(self, text):
        self.MsgCfgText.append(text)
        self.MsgCfgText.document().setDefaultTextOption(self.option)

    def SelectAdVideoName(self, text):
        self.VideoCfgText.append(text)
        self.VideoCfgText.document().setDefaultTextOption(self.option)

    def SelectAdPlaqueName(self, text):
        self.PlaqueCfgText.append(text)
        self.PlaqueCfgText.document().setDefaultTextOption(self.option)

    def SelectAdSplashSources(self, text):
        self.SplashSourceText.append(text)
        self.SplashSourceText.document().setDefaultTextOption(self.option)

    def SelectAdMsgSources(self, text):
        self.MsgSourceText.append(text)
        self.MsgSourceText.document().setDefaultTextOption(self.option)

    def SelectAdVideoSources(self, text):
        self.VideoSourceText.append(text)
        self.VideoSourceText.document().setDefaultTextOption(self.option)

    def SelectAdPlaqueSources(self, text):
        self.PlaqueSourceText.append(text)
        self.PlaqueSourceText.document().setDefaultTextOption(self.option)

    def AdClearClick(self):
        self.AllGroupText.clear()
        self.AGroupText.clear()
        self.BGroupText.clear()
        self.CGroupText.clear()
        self.SplashCfgText.clear()
        self.MsgCfgText.clear()
        self.PlaqueCfgText.clear()
        self.VideoCfgText.clear()
        self.SplashSourceText.clear()
        self.MsgSourceText.clear()
        self.PlaqueSourceText.clear()
        self.VideoSourceText.clear()

    def AdNameContrast(self):
        try:
            pid = self.VerifyPrid.text()
            chan = self.VerifyChan.text()
            pro = self.PackageInfo.text()
            # 输入项目id为空则弹窗提示
            if pid == '':
                pid_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入项目id')
                pid_msg_box.exec_()
            # 输入渠道标识为空则弹窗提示
            if chan == '':
                chan_msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入渠道')
                chan_msg_box.exec_()
            if pro == '':
                pro_msg_box = QMessageBox(QMessageBox.Critical, '错误', 'key不可为空')
                pro_msg_box.exec_()
            else:
                appinfo = f'{pid}&{chan}&{pro}'
                self.AdContrastQueue.put(appinfo)
                self.AdContrastThread.start()
        except Exception as e:
            tips = QMessageBox(QMessageBox.Critical, '错误', f'程序错误:{e}')
            tips.exec_()

    def AdContrastMatch(self, text):
        self.MatchText.append(text)
        self.MatchText.document().setDefaultTextOption(self.option)

    def AdContrastTmr(self, text):
        self.TmrText.append(text)
        self.TmrText.document().setDefaultTextOption(self.option)

    def AdContrastLack(self, text):
        self.LackText.append(text)
        self.LackText.document().setDefaultTextOption(self.option)

    def AdNameClear(self):
        self.MatchText.clear()
        self.LackText.clear()
        self.TmrText.clear()

    def OneSelfOnlineConfigLogUpdate(self, text):
        self.OneselfOnlineCfg.append(text)

    def OneSelfOnlineConfigSelect(self):
        pid = self.OneselfPid.text()
        chan = self.Oneselfchan.text()
        appinfo = f'{pid}&{chan}'
        self.OneSelfOnlineCfgQueue.put(appinfo)
        self.OneSelfOnlineCfgThread.start()


    def OneSelfOnlineConfigClear(self):
        self.OneselfOnlineCfg.clear()


    def DeviceRefresh(self):
        try:
            self.DevicesList.clear()
            for i in get_connected_device_models():
                self.DevicesList.addItem(f'{i}')
        except Exception as e:
            # print(e)
            # pass
            print(e)
            msg_box = QMessageBox(QMessageBox.Critical, '错误', str(e))
            msg_box.exec_()

    def devices_info(self):
        devices_id = self.DevicesList.currentText()
        id = devices_id.split("/")[-1]
        return id

    def CreateImgDriClick(self):
        ImgDriName(self.ImgDriName.text())

    def ScreenhostOne(self):
        path = self.ImgDriName.text()
        deviceid = self.devices_info()
        screeninfo = f"{path}&{deviceid}"
        self.ScreenOneQueue.put(screeninfo)
        self.ScreenOneThread.start()

    def ScreenImgShowOne(self, text):
        showImage = QPixmap(text).scaled(self.ImgOne.width(), self.ImgOne.height())
        # 展示图片，达到预览效果
        self.ImgOne.setPixmap(showImage)

    def ScreenImgDriTipsOne(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImdDriNoneOne(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImgPhoneErrorOne(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenhostTwo(self):
        path = self.ImgDriName.text()
        deviceid = self.devices_info()
        screeninfo = f"{path}&{deviceid}"
        self.ScreenTwoQueue.put(screeninfo)
        self.ScreenTwoThread.start()

    def ScreenImgShowTwo(self, text):
        showImage = QPixmap(text).scaled(self.ImgTwo.width(), self.ImgTwo.height())
        # 展示图片，达到预览效果
        self.ImgTwo.setPixmap(showImage)

    def ScreenImgDriTipsTwo(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImdDriNoneTwo(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImgPhoneErrorTwo(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenhostThree(self):
        path = self.ImgDriName.text()
        deviceid = self.devices_info()
        screeninfo = f"{path}&{deviceid}"
        self.ScreenThreeQueue.put(screeninfo)
        self.ScreenThreeThread.start()

    def ScreenImgShowThree(self, text):
        showImage = QPixmap(text).scaled(self.ImgThree.width(), self.ImgThree.height())
        # 展示图片，达到预览效果
        self.ImgThree.setPixmap(showImage)

    def ScreenImgDriTipsThree(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImdDriNoneThree(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImgPhoneErrorThree(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenhostFour(self):
        path = self.ImgDriName.text()
        deviceid = self.devices_info()
        screeninfo = f"{path}&{deviceid}"
        self.ScreenFourQueue.put(screeninfo)
        self.ScreenFourThread.start()

    def ScreenImgShowFour(self, text):
        showImage = QPixmap(text).scaled(self.ImgFour.width(), self.ImgFour.height())
        # 展示图片，达到预览效果
        self.ImgFour.setPixmap(showImage)

    def ScreenImgDriTipsFour(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImdDriNoneFour(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImgPhoneErrorFour(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenhostFive(self):
        path = self.ImgDriName.text()
        deviceid = self.devices_info()
        screeninfo = f"{path}&{deviceid}"
        self.ScreenFiveQueue.put(screeninfo)
        self.ScreenFiveThread.start()

    def ScreenImgShowFive(self, text):
        showImage = QPixmap(text).scaled(self.ImgFive.width(), self.ImgFive.height())
        # 展示图片，达到预览效果
        self.ImgFive.setPixmap(showImage)

    def ScreenImgDriTipsFive(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImdDriNoneFive(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def ScreenImgPhoneErrorFive(self, text):
        msg_box = QMessageBox(QMessageBox.Critical, '错误', text)
        msg_box.exec_()

    def InstallAppMain(self):
        path = self.TestToolsPathText.text()
        demo = self.DemoApp.currentText()
        devices_info = self.devices_info()
        TestInfo = f"{path}&{demo}&{devices_info}"
        self.InstallQueue.put(TestInfo)
        self.InstallThread.start()

    def DemoInstall(self, text):
        msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{text}')
        msg_box.exec_()

    def DomeDebugInfo(self, text):
        msg_box = QMessageBox(QMessageBox.Information, '安装信息', f'{text}')
        msg_box.exec_()

    def StartAppMain(self):
        path = self.TestToolsPathText.text()
        devices_info = self.devices_info()
        startinfo = f"{path}&{devices_info}"
        self.StartAppQueue.put(startinfo)
        self.StartAppThread.start()

    def CheckProcessMain(self):
        path = self.TestToolsPathText.text()
        devices_info = self.devices_info()
        checkinfo = f"{path}&{devices_info}"
        self.CheckProcessQueue.put(checkinfo)
        self.CheckProcessThread.start()

    def CheckProcessUpdate(self, text):
        self.ProcessText.append(text)

    def CheckProcessClear(self):
        self.ProcessText.clear()

    def StopAppMain(self):
        path = self.TestToolsPathText.text()
        devices_info = self.devices_info()
        stopinfo = f"{path}&{devices_info}"
        self.StopAppQueue.put(stopinfo)
        self.StopAppThread.start()

    def UninstallAppMain(self):
        path = self.TestToolsPathText.text()
        devices_info = self.devices_info()
        uninstallinfo = f"{path}&{devices_info}"
        self.UninstallAppQueue.put(uninstallinfo)
        self.UninstallAppThread.start()

    def ClearAppMain(self):
        path = self.TestToolsPathText.text()
        devices_info = self.devices_info()
        clearinfo = f"{path}&{devices_info}"
        self.ClearAppQueue.put(clearinfo)
        self.ClearAppThread.start()

    def DebugAppMain(self):
        path = self.TestToolsPathText.text()
        devices_info = self.devices_info()
        debuginfo = f"{path}&{devices_info}"
        self.DebugAppQueue.put(debuginfo)
        self.DebugAppThread.start()

    def DebugInfoMsgBox(self, text):
        msg_box = QMessageBox(QMessageBox.Information, 'debug开关', f'{text}')
        msg_box.exec_()

    def UndebugAppMain(self):
        path = self.TestToolsPathText.text()
        devices_info = self.devices_info()
        undebuginfo = f"{path}&{devices_info}"
        self.DebugAppQueue.put(undebuginfo)
        self.DebugAppThread.start()

    def UnDebugInfoMsgBox(self, text):
        msg_box = QMessageBox(QMessageBox.Information, 'debug开关', f'{text}')
        msg_box.exec_()

    def AutoDriver(self):
        auto_path = self.AutoPathText.text()
        auto_driverid = self.devices_info()
        autolist = f"{auto_path}&{auto_driverid}"
        self.AutoQueue.put(autolist)
        self.AutoThread.start()

    def UpdateAutoCfg(self, text):
        self.AutoInfo.append(text)

    def LockUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoLockImg.width(), self.AutoLockImg.height())
        # 展示图片，达到预览效果
        self.AutoLockImg.setPixmap(showImage)
        self.AutoLockPath.setText(text)

    def UnlockUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoUnlockImg.width(), self.AutoUnlockImg.height())
        # 展示图片，达到预览效果
        self.AutoUnlockImg.setPixmap(showImage)
        self.AutoUnlockPath.setText(text)

    def UnlockAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoAdUnlockImg.width(), self.AutoAdUnlockImg.height())
        # 展示图片，达到预览效果
        self.AutoAdUnlockImg.setPixmap(showImage)
        self.AutoAdUnlockPath.setText(text)

    def ChargeUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoChargeImg.width(), self.AutoChargeImg.height())
        # 展示图片，达到预览效果
        self.AutoChargeImg.setPixmap(showImage)
        self.AutoChargePath.setText(text)

    def ChargeAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoAdChargeImg.width(), self.AutoAdChargeImg.height())
        # 展示图片，达到预览效果
        self.AutoAdChargeImg.setPixmap(showImage)
        self.AutoAdChargePath.setText(text)

    def WifiUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoWifiImg.width(), self.AutoWifiImg.height())
        # 展示图片，达到预览效果
        self.AutoWifiImg.setPixmap(showImage)
        self.AutoWifiPath.setText(text)

    def WifiAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoAdWifiImg.width(), self.AutoAdWifiImg.height())
        # 展示图片，达到预览效果
        self.AutoAdWifiImg.setPixmap(showImage)
        self.AutoAdWifiPath.setText(text)

    def HomeUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoHomeImg.width(), self.AutoHomeImg.height())
        # 展示图片，达到预览效果
        self.AutoHomeImg.setPixmap(showImage)
        self.AutoHomePath.setText(text)

    def HomeAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoAdHomeImg.width(), self.AutoAdHomeImg.height())
        # 展示图片，达到预览效果
        self.AutoAdHomeImg.setPixmap(showImage)
        self.AutoAdHomePath.setText(text)

    def TimerUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoTimerImg.width(), self.AutoTimerImg.height())
        # 展示图片，达到预览效果
        self.AutoTimerImg.setPixmap(showImage)
        self.AutoTimerPath.setText(text)

    def TimerAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AutoAdTimerImg.width(), self.AutoAdTimerImg.height())
        # 展示图片，达到预览效果
        self.AutoAdTimerImg.setPixmap(showImage)
        self.AutoAdTimerPath.setText(text)

    def AutoLockLookMain(self):
        path = self.AutoLockPath.toPlainText()
        self.LookLockQueue.put(path)
        self.LookLockThread.start()

    def AutoUnlockLookMain(self):
        path = self.AutoUnlockPath.toPlainText()
        self.LookUnlockQueue.put(path)
        self.LookUnlockThread.start()

    def AutoChargeLookMain(self):
        path = self.AutoChargePath.toPlainText()
        self.LookChargeQueue.put(path)
        self.LookChargeThread.start()

    def AutoWifiLookMain(self):
        path = self.AutoWifiPath.toPlainText()
        self.LookWifiQueue.put(path)
        self.LookWifiThread.start()

    def AutoTimerLookMain(self):
        path = self.AutoTimerPath.toPlainText()
        self.LookTimerQueue.put(path)
        self.LookTimerThread.start()

    def AutoHomeLookMain(self):
        path = self.AutoHomePath.toPlainText()
        self.LookHomeQueue.put(path)
        self.LookHomeThread.start()

    def AutoAdUnlockLookMain(self):
        path = self.AutoAdUnlockPath.toPlainText()
        self.LookUnlockAdQueue.put(path)
        self.LookUnlockAdThread.start()

    def AutoAdChargeLookMain(self):
        path = self.AutoAdChargePath.toPlainText()
        self.LookChargeAdQueue.put(path)
        self.LookChargeAdThread.start()

    def AutoAdHomeLookMain(self):
        path = self.AutoAdHomePath.toPlainText()
        self.LookHomeAdQueue.put(path)
        self.LookHomeAdThread.start()

    def AutoAdWifiLookMain(self):
        path = self.AutoAdWifiPath.toPlainText()
        self.LookWifiAdQueue.put(path)
        self.LookWifiAdThread.start()

    def AutoAdTimerLookMain(self):
        path = self.AutoAdTimerPath.toPlainText()
        self.LookTimerAdQueue.put(path)
        self.LookTimerAdThread.start()

    def ClearAutoPathText(self):
        self.AutoPathText.clear()

    def AshingDriver(self):
        Ashing_path = self.AshingPathText.text()
        Ashing_driverid = self.devices_info()
        Ashinglist = f"{Ashing_path}&{Ashing_driverid}"
        self.AutoQueue.put(Ashinglist)
        self.AutoThread.start()

    def UpdateAshingCfg(self, text):
        self.AshingInfo.append(text)

    def AshingLockUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingLockImg.width(), self.AshingLockImg.height())
        # 展示图片，达到预览效果
        self.AshingLockImg.setPixmap(showImage)
        self.AshingLockPath.setText(text)

    def AshingUnlockUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingUnlockImg.width(), self.AshingUnlockImg.height())
        # 展示图片，达到预览效果
        self.AshingUnlockImg.setPixmap(showImage)
        self.AshingUnlockPath.setText(text)

    def AshingUnlockAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingAdUnlockImg.width(), self.AshingAdUnlockImg.height())
        # 展示图片，达到预览效果
        self.AshingAdUnlockImg.setPixmap(showImage)
        self.AshingAdUnlockPath.setText(text)

    def AshingChargeUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingChargeImg.width(), self.AshingChargeImg.height())
        # 展示图片，达到预览效果
        self.AshingChargeImg.setPixmap(showImage)
        self.AshingChargePath.setText(text)

    def AshingChargeAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingAdChargeImg.width(), self.AshingAdChargeImg.height())
        # 展示图片，达到预览效果
        self.AshingAdChargeImg.setPixmap(showImage)
        self.AshingAdChargePath.setText(text)

    def AshingWifiUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingWifiImg.width(), self.AshingWifiImg.height())
        # 展示图片，达到预览效果
        self.AshingWifiImg.setPixmap(showImage)
        self.AshingWifiPath.setText(text)

    def AshingWifiAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingAdWifiImg.width(), self.AshingAdWifiImg.height())
        # 展示图片，达到预览效果
        self.AshingAdWifiImg.setPixmap(showImage)
        self.AshingAdWifiPath.setText(text)

    def AshingHomeUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingHomeImg.width(), self.AshingHomeImg.height())
        # 展示图片，达到预览效果
        self.AshingHomeImg.setPixmap(showImage)
        self.AshingHomePath.setText(text)

    def AshingHomeAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingAdHomeImg.width(), self.AshingAdHomeImg.height())
        # 展示图片，达到预览效果
        self.AshingAdHomeImg.setPixmap(showImage)
        self.AshingAdHomePath.setText(text)

    def AshingTimerUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingTimerImg.width(), self.AshingTimerImg.height())
        # 展示图片，达到预览效果
        self.AshingTimerImg.setPixmap(showImage)
        self.AshingTimerPath.setText(text)

    def AshingTimerAdUpdate(self,text):
        showImage = QPixmap(text).scaled(self.AshingAdTimerImg.width(), self.AshingAdTimerImg.height())
        # 展示图片，达到预览效果
        self.AshingAdTimerImg.setPixmap(showImage)
        self.AshingAdTimerPath.setText(text)

    def AshingLockLookMain(self):
        path = self.AshingLockPath.toPlainText()
        self.AshingLookLockQueue.put(path)
        self.AshingLookLockThread.start()

    def AshingUnlockLookMain(self):
        path = self.AshingUnlockPath.toPlainText()
        self.AshingLookUnlockQueue.put(path)
        self.AshingLookUnlockThread.start()

    def AshingChargeLookMain(self):
        path = self.AshingChargePath.toPlainText()
        self.AshingLookChargeQueue.put(path)
        self.AshingLookChargeThread.start()

    def AshingWifiLookMain(self):
        path = self.AshingWifiPath.toPlainText()
        self.AshingLookWifiQueue.put(path)
        self.AshingLookWifiThread.start()

    def AshingTimerLookMain(self):
        path = self.AshingTimerPath.toPlainText()
        self.AshingLookTimerQueue.put(path)
        self.AshingLookTimerThread.start()

    def AshingHomeLookMain(self):
        path = self.AshingHomePath.toPlainText()
        self.AshingLookHomeQueue.put(path)
        self.AshingLookHomeThread.start()

    def AshingAdUnlockLookMain(self):
        path = self.AshingAdUnlockPath.toPlainText()
        self.AshingLookUnlockAdQueue.put(path)
        self.AshingLookUnlockAdThread.start()

    def AshingAdChargeLookMain(self):
        path = self.AshingAdChargePath.toPlainText()
        self.AshingLookChargeAdQueue.put(path)
        self.AshingLookChargeAdThread.start()

    def AshingAdHomeLookMain(self):
        path = self.AshingAdHomePath.toPlainText()
        self.AshingLookHomeAdQueue.put(path)
        self.AshingLookHomeAdThread.start()

    def AshingAdWifiLookMain(self):
        path = self.AshingAdWifiPath.toPlainText()
        self.AshingLookWifiAdQueue.put(path)
        self.AshingLookWifiAdThread.start()

    def AshingAdTimerLookMain(self):
        path = self.AshingAdTimerPath.toPlainText()
        self.AshingLookTimerAdQueue.put(path)
        self.AshingLookTimerAdThread.start()

    def ClearAshingPathText(self):
        self.AshingPathText.clear()

    def CreateDirMain(self):
        path = self.CreateDirText.toPlainText()
        self.CreateDirQueue.put(path)
        self.CreateDirThread.start()

    def CreateDirProductDirTips(self, text):
        mmm_box = QMessageBox(QMessageBox.Information, '提示', text)
        mmm_box.exec_()

    def CreateDirParentDirTips(self, text):
        mmm_box = QMessageBox(QMessageBox.Information, '提示', text)
        mmm_box.exec_()

    def CreateClearDirText(self):
        self.CreateDirText.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
