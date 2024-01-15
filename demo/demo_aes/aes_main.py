from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 定义PKCS7填充和反填充函数
def pkcs7_padding(data):
    return pad(data, AES.block_size, style='pkcs7')

def pkcs7_unpadding(data):
    return unpad(data, AES.block_size, style='pkcs7')

# 定义AES加密函数
def aes_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pkcs7_padding(plaintext.encode('utf-8')))
    return base64.b64encode(ciphertext)

# 定义AES解密函数
def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext))
    return pkcs7_unpadding(plaintext).decode('utf-8')

# 示例用法
if __name__ == "__main__":
    # 128位的密钥，这里是16字节
    key = b'1234561234561234'

    # 16字节的随机IV
    iv = b'1234561234561234'

    # 待加密的数据
    plaintext = 'Hello, AES with Padding!'

    # 加密
    encrypted_data = aes_encrypt(plaintext, key, iv)
    print("加密后的数据:", encrypted_data.decode('utf-8'))

    # 解密
    decrypted_data = aes_decrypt(encrypted_data, key, iv)
    print("解密后的数据:", decrypted_data)
