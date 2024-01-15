# -*- coding: utf-8 -*-



import requests

def upload_jks_file(file_path, upload_url, key_name, key_password):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        data = {"key_name": key_name,
                 "key_password": key_password}
        response = requests.post(upload_url, files=files, data=data)
        if response.status_code == 200:
            print(response.json()['hash'])
            return response.json()['hash']
        else:
            print(response.json())
            return '文件上传失败'

# 调用上传函数
file_path = "D:\laying-file\discussed15484.jks"    # 文件路径
upload_url = 'http://192.168.7.188:8111/upload'
keyname = 'discussed15484'  # 别名
keypassword = 'discussed46548'  # 密码
upload_jks_file(file_path, upload_url, key_name=keyname, key_password=keypassword)

