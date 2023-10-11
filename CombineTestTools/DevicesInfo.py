import os
import subprocess
import requests


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
    for device in check_adb_devices():
        result = subprocess.run(['adb', '-s', device, 'shell', 'getprop', 'ro.product.brand'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        result1 = subprocess.run(['adb', '-s', device, 'shell', 'getprop', 'ro.product.model'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        model = result.stdout.decode('utf-8').strip()
        model1 = result1.stdout.decode('utf-8').strip()
        url = 'http://192.168.7.188:8101/model_name'
        data = {'model': model1}
        res = requests.post(url, data)
        if res.json()['phone_name'] == '无model信息':
            models.append(f"{model} {model1}/{device}")
        else:
            models.append(f"{model} {res.json()['phone_name']}/{device}")
    return models


#
if __name__ == '__main__':
    # check_adb_devices()
    get_connected_device_models()
    print(get_connected_device_models())
    # print(check_adb_devices())
