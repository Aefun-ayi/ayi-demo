import openpyxl
import json
def aaa():
    # 打开 Excel 文件
    wb = openpyxl.load_workbook(r"C:\Users\Administrator\Desktop\adinfotable.xlsx")

    # 获取工作表中的数据
    sheet = wb.active
    rows = sheet.rows

    # 定义一个空列表
    data = []

    # 遍历每一行数据，并将其转换为字典对象
    for row in rows:
        # 获取每一行数据
        values = [cell.value for cell in row]
        # a = values[0].split(",")
        # 将每一行数据转换为字典对象
        # list(res[0][0].split(","))
        # print(a)
        data.append({
            "model": values[0],
            "phonename": values[1]
            # "gender": values[2]
        })

    # 将数据转换为 json 对象并输出
    # json_data = json.dumps(data, ensure_ascii=False)
    # print(json_data)
    return data

a = aaa()
print(a)