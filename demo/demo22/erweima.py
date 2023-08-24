# from PIL import Image
# from pyzbar.pyzbar import decode
#
# img = decode(Image.open(r"D:\laying-file\Snipaste_2023-06-30_11-56-41.png"))
# print(img[0].data.decode('ascii'))

#
# import cv2
#
# qrcode_filename = r"hello.jpg"
# qrcode_image = cv2.imread(qrcode_filename)
# qrCodeDetector = cv2.QRCodeDetector()
# data, bbox, straight_qrcode = qrCodeDetector.detectAndDecode(qrcode_image)
#
# print(data)
import pyzbar.pyzbar as pyzbar
from PIL import Image

# 图片路径
image = "hello.jpg"

img = Image.open(image)

# 解码 image 中的 datamatrix 条形码
barcodes = pyzbar.decode(img)

barcodeData = ""
for barcode in barcodes:
    barcodeData += barcode.data.decode("utf-8")

print(barcodeData)
