import os


def Path_List(path):
    file_list = os.listdir(path)
    for file_name in file_list:
        file = file_name.split('_')
        pid = file[0]
        appid = pid[:5]
        chan = file[3]
        return appid, pid, chan
