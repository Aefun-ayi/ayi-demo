import subprocess

def GetPackageName(apk_path):
    """
    获取apk包名
    :param apk_path: apk文件路径
    :return: 包名
    """
    cmd = ["aapt", "dump", "badging", apk_path]
    output = subprocess.check_output(cmd, universal_newlines=True, encoding="utf-8")
    package_start = output.find("package: name='") + len("package: name='")
    package_end = output.find("'", package_start)
    package_name = output[package_start:package_end]

    return package_name


def GetActivityName(apk_path):
    """
    获取apk启动Activity名
    :param apk_path: apk文件路径
    :return: 启动Activity名
    """
    cmd = ["aapt", "dump", "badging", apk_path]
    output = subprocess.check_output(cmd, universal_newlines=True, encoding="utf-8")

    activity_start = output.find("launchable-activity: name='") + len("launchable-activity: name='")
    activity_end = output.find("'", activity_start)
    activity_name = output[activity_start:activity_end]

    return activity_name

def GetApkName(apk_path):
    """
    获取apk的名称
    :param apk_path: apk文件路径
    :return: 名称
    """
    command = ["aapt", "dump", "badging", apk_path]
    output = subprocess.check_output(command).decode("utf-8")
    start = output.find("application-label:") + 19
    end = output.find("'", start)
    app_name = output[start:end]
    return app_name