import os

folder_path = r"D:\keep\文本存储\outFloder"  # 文件夹路径
file_names = os.listdir(folder_path)  # 获取文件夹下所有文件名
project = []
for file_name in file_names:
    info_list = file_name.split('_')
    pid = info_list[0]
    appid = info_list[0][:5]
    chan = info_list[3]
    project.append(f"{appid}{chan}{pid}")
for i in project:
    appidd = i[:5]
    chanchan = i[5:8]
    pidd = i[8:]
    print(appidd, chanchan, pidd)
print(project)
