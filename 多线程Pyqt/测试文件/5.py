import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64


url = "TQCvXCMpbhXWAQfz%2BNjH3MYgTlCwMSLNpeZ86oxlweaR5aMHAm0juTG10n6bUWQLzOrRHRSrFefIReD253DYYuDIEJ1zUvIzvX1sxQfOMo4hm1Eynx%2BEISccg1m4YJrwjssFIOJ0aoPF5NzTqgY23%2BRX9wWL73mRK9WnIXuLE1rKNZPtAJRchYl8%2BOBi6LSRb4A0kNIY6%2BGP%2BxUzoJN9M0%2B0Dqdv2qiwqd9BoevJqgnWWBs52%2B0nI5BPKjJirmDpY6oJaDsIljlqZTRgDnjgxPvTO9TrzzsjX5iMrmSfK3fmraGaEcAtIeKsXQH9x6Rr"
decoded_url = requests.utils.unquote(url)
decoded_str = base64.b64decode(decoded_url)
print(decoded_url)
block_size = 128
padder = padding.PKCS7(block_size).padder()
padded_data = padder.update(decoded_url) + padder.finalize()
key = b"dwnxthekey902902"  # 密钥，长度为32
iv = b"dwnxthekey902902"  # 初始向量，长度为16
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
decrypted_str = decryptor.update(decoded_str) + decryptor.finalize()

print(decrypted_str.decode('utf-8', errors='replace'))  # 输出解密后的字符串
print(type(decrypted_str.decode()))