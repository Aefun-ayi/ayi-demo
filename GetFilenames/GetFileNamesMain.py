import os
import openpyxl
import pandas as pd
import datetime

def generate_folder_hierarchy_table(folder_path):
    if len(folder_path) == 0:
        print('请输入正确路径')
    else:
        data = pd.DataFrame()
        for root, dirs, files in os.walk(folder_path):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                path_list = dir_path.split(os.path.sep)
                print(path_list)
                row = {}
                for i in range(len(path_list)):
                    row[f'{i + 1}级目录'] = path_list[i]
                data = data.append(row, ignore_index=True)
        return data


while True:
    folder_path = input('请输入路径或拖入文件夹：')
    df = generate_folder_hierarchy_table(folder_path)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    rtime = datetime.datetime.now().strftime('%Y年%m月%d日%H时%M分%S秒')  # 时间戳
    file_name = f'{desktop_path}\\\\\\\\{rtime}_目录表格.xlsx'
    with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        df.groupby(df.columns.tolist()).size().reset_index().to_excel(writer, sheet_name='Sheet2', index=False)
    wb = openpyxl.load_workbook(file_name)
    del wb['Sheet2']
    wb.save(file_name)
    print(f'数据已保存在文件 {file_name} 的 Sheet1 和 Sheet2 工作表中。')