from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import requests
import re

# 定义PKCS7填充和反填充函数
def pkcs7_padding(data):
    return pad(data, AES.block_size, style='pkcs7')

def pkcs7_unpadding(data):
    return unpad(data, AES.block_size, style='pkcs7')

# 定义AES解密函数
def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return pkcs7_unpadding(plaintext)

# 测试代码
if __name__ == '__main__':
    while True:
        try:
            url2 = input('输入接口地址：')
            if 'value=' in url2:
                p1 = "value=.+"
                a = re.findall(p1, url2)
                b = str(a)[8:-2]
                decoded_url = requests.utils.unquote(b)
                # 加密后的数据
                ciphertext = base64.b64decode(decoded_url)
                # 密钥
                key = b'dwnxthekey902902'
                # 偏移量
                iv = b'dwnxthekey902902'
                # 解密数据
                plaintext = aes_decrypt(ciphertext, key, iv)
                # 输出结果
                print(plaintext.decode())
            if 'data' in url2:
                p2 = '"data":".+?"'
                a1 = re.findall(p2, url2)
                b1 = str(a1)[10:-3]
                # 加密后的数据
                ciphertext1 = base64.b64decode(b1)
                # 密钥
                key1 = b'dwnxthekey902902'
                # 偏移量
                iv1 = b'dwnxthekey902902'
                # 解密数据
                plaintext1 = aes_decrypt(ciphertext1, key1, iv1)
                # 输出结果
                print(plaintext1.decode())
            else:
                ciphertext2 = base64.b64decode(url2)
                # 密钥
                key2 = b'dwnxthekey902902'
                # 偏移量
                iv2 = b'dwnxthekey902902'
                # 解密数据
                plaintext2 = aes_decrypt(ciphertext2, key2, iv2)
                # 输出结果
                print(plaintext2.decode())
        except ValueError as v:
            print(f'异常信息：{v}')


