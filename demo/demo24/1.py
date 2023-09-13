import datetime

current_time = datetime.datetime.now()
time_str = current_time.strftime('%H')
fen = current_time.strftime('%M')
miao = current_time.strftime('%S')
print("当前时间：", time_str)
print("当前时间：", fen)
print("当前时间：", miao)