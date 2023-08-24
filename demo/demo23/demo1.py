# for i in range(5):
#     # print(i)
#     a = f'测试主题-第{i+1}条数据'
#     print(a)


import subprocess
import signal
import time

process = subprocess.Popen(['adb', 'shell', 'screenrecord', '/sdcard/screen1.mp4'])
time.sleep(3)
process.send_signal(signal.SIGTERM)