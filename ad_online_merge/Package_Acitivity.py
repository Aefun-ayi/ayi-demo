import subprocess

def get_package_name(apk_path):
    """
    获取apk包名
    :param apk_path: apk文件路径
    :return: 包名
    """
    cmd = ["aapt", "dump", "badging", apk_path]
    output = subprocess.check_output(cmd, universal_newlines=True)

    package_start = output.find("package: name='") + len("package: name='")
    package_end = output.find("'", package_start)
    package_name = output[package_start:package_end]

    return package_name


def get_activity_name(apk_path):
    """
    获取apk启动Activity名
    :param apk_path: apk文件路径
    :return: 启动Activity名
    """
    cmd = ["aapt", "dump", "badging", apk_path]
    output = subprocess.check_output(cmd, universal_newlines=True)

    activity_start = output.find("launchable-activity: name='") + len("launchable-activity: name='")
    activity_end = output.find("'", activity_start)
    activity_name = output[activity_start:activity_end]

    return activity_name

def get_apk_app_name(apk_path):
    command = ["aapt", "dump", "badging", apk_path]
    output = subprocess.check_output(command).decode("utf-8")
    start = output.find("application-label:") + 19
    end = output.find("'", start)
    app_name = output[start:end]
    return app_name