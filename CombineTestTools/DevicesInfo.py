import os
import subprocess
from MySQLConnect import MysqlConnection

def check_adb_devices():
    adb_list = []
    ret = os.popen('adb devices').readlines()
    if len(ret) == 1:
        return adb_list
    else:
        for n in ret:
            if '\tdevice\n' in n:
                adb = str(n).strip().split('\tdevice')[0].strip()
                adb_list.append(str(adb))
        return adb_list

def get_connected_device_models():
    # 获取设备model
    models = []
    db = MysqlConnection()
    for device in check_adb_devices():
        result = subprocess.run(['adb', '-s', device, 'shell', 'getprop', 'ro.product.brand'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        result1 = subprocess.run(['adb', '-s', device, 'shell', 'getprop', 'ro.product.model'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        model = result.stdout.decode('utf-8').strip()
        model1 = result1.stdout.decode('utf-8').strip()
        phone_name = db.select(f'select phone_name from Device_Info where phone_mobile = "{model1}"')
        if len(phone_name) == 0:
            models.append(f"{model} {model1}/{device}")
        else:
            models.append(f"{model} {phone_name[0][0]}/{device}")
    db.exit()
    return models


#
# if __name__ == '__main__':
#     check_adb_devices()
#     get_connected_device_models()
#     print(get_connected_device_models())
    # print(check_adb_devices())
