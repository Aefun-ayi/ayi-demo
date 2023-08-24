# import qrcode
#
# # 二维码内容
# data = "hello world!"
#
# qr = qrcode.QRCode(
#     version=4,  # 整数（1-40）
#     error_correction=qrcode.constants.ERROR_CORRECT_L,  # 二维码的纠错范围
#     box_size=100,  # 每个点（方块）中的像素个数
#     border=4  # 二维码距图像外围边框距离，默认为4，而且相关规定最小为4
# )
#
# # 将数据添加到此QR码。
# qr.add_data(data)
# # 将数据编译为QR Code数组。
# qr.make(fit=True)
#
# # 生成二维码
# img = qr.make_image()
# # 直接显示二维码
# img.show()
# # 保存二维码为文件
# img.save("hello.jpg")



import requests

a = requests.get('ftp://192.168.7.111/testae.txt')
print(a.text)