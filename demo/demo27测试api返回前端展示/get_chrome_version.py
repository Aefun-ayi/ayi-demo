import os
import platform
import re
import subprocess
import requests
import urllib
import zipfile
def get_chrome_version():
    """
    获取本地浏览器版本信息
    :return:
    """
    system = platform.system()
    # 不同的系统，注册表命令不一致
    if system == "Linux":
        command = "google-chrome --version"
    elif system == "Windows":
        command = 'reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome" /v DisplayVersion'
    elif system == "Darwin":  # macOS
        command = 'mdls -name kMDItemVersion -raw /Applications/Google\ Chrome.app'
    else:
        print("无法识别此电脑系统")

    # 通过注册表来获取谷歌浏览器版本
    try:
        version_info = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL).decode("utf-8")
        version = re.search(r"(\d+\.\d+\.\d+\.\d+)", version_info)
        if version:
            # print("Google Chrome 版本:", version.group(1))
            return version.group(1)
    except (subprocess.CalledProcessError, AttributeError):

        return '获取Google Chrome 版本 失败！！！'

# print(get_chrome_version())

def three():
    ver = str(get_chrome_version())
    li = ver.split('.')
    new_ver = f'{li[0]}.{li[1]}.{li[2]}'
    return new_ver

def two():
    ver = str(get_chrome_version())
    li = ver.split('.')
    new_ver = f'{li[0]}.{li[1]}'
    return new_ver

def one():
    ver = str(get_chrome_version())
    li = ver.split('.')
    new_ver = f'{li[0]}'
    return new_ver
#
# print(three())
# print(two())
# print(one())