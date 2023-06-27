import os
import subprocess

def check_adb_devices():
    '''
    检查adb 设备，并返回设备sn list

    :return: 设备sn list
    '''
    adb_list = []
    ret = os.popen('adb devices').readlines()
    # print('ret={}'.format(ret))
    if len(ret) == 1:
        # print('未识别到adb 设备...')
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
        result = subprocess.run(['adb', '-s', device, 'shell', 'getprop', 'ro.product.brand'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result1 = subprocess.run(['adb', '-s', device, 'shell', 'getprop', 'ro.product.model'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        model = result.stdout.decode('utf-8').strip()
        model1 = result1.stdout.decode('utf-8').strip()
        models.append(f"{model} {model1}/{device}")
    print(models)
    return models



if __name__ == '__main__':
    check_adb_devices()
    get_connected_device_models()

