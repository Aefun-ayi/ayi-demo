import random
import time
from datetime import datetime, timedelta
import requests
def generate_random_timestamp(existing_timestamps):
    while True:
        # 生成随机的年份
        year = random.randint(2023, 2023)
        # 生成随机的月份
        month = random.randint(7, 7)
        # 根据月份生成随机的日期
        day = random.randint(17, 17)
        # 生成随机的小时
        hour = random.randint(10, 23)
        # 构建时间元组
        timestamp = (year, month, day, hour, 0, 0, 0, 0, 0)
        # 转换为时间戳
        timestamp = int(time.mktime(timestamp))

        if timestamp not in existing_timestamps:
            existing_timestamps.add(timestamp)
            return timestamp

# 生成随机中文字符
def generate_random_chinese(length):
    # 随机选择Unicode编码范围（简体中文字符）
    start = 0x4E00  # 简体中文字符起始编码
    end = 0x9FFF  # 简体中文字符结束编码
    chars = []
    for _ in range(length):
        char = chr(random.randint(start, end))
        chars.append(char)
    return ''.join(chars)


timestamps = set()
timestamp_list = []
for _ in range(5):  # 生成10组开始时间和结束时间
    start_timestamp = generate_random_timestamp(timestamps)
    end_timestamp = start_timestamp + 3600
    random_chinese_list = generate_random_chinese(5)
    timestamp_list.append(f"{random_chinese_list}/{start_timestamp}/{end_timestamp}")
    timestamps.add(start_timestamp)
    print(f"theme: {random_chinese_list}, startTime: {datetime.fromtimestamp(start_timestamp)}, endTime: {datetime.fromtimestamp(end_timestamp)}")
print(timestamp_list)
# 输出时间戳列表
for timestamp in timestamp_list:
    parts = timestamp.split("/")
    theme = parts[0]
    startTime = parts[1]
    endTime = parts[2]

    print(timestamp)
    url = 'https://gateway.test.maxhub.vip/trigger/api/auth/staff/admin/meeting'
    header = {
    "Authorization":"Bearer 6010a360-b63e-43d9-8144-ae9b8c4d7198",
    # "Content-Type":"application/json",
    # "x-auth-userid":"579cbc25-b831-411f-a201-35f9f13d3d42",
    "x-company-id":"85aad105-c7b9-4131-8e3b-a8debdad9cc8",
    "x-member-id":"1631611361655652354"
    }
    data_info = {
    "organizerId":"1631611361655652354",
    "theme":f"{theme}",
    "startTime":startTime,
    "endTime":endTime,
    "roomId":"a700bcab-1d55-426f-9905-fc506e4ed7eb"
    }
    res = requests.post(url=url, headers=header, data=data_info)
    print(res.json())