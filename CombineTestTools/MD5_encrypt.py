import hashlib


def md5_encrypt(input_string):
    # 创建 MD5 对象
    md5_hash = hashlib.md5()

    # 更新对象以处理输入字符串
    md5_hash.update(input_string.encode('utf-8'))

    # 获取加密后的结果
    encrypted_string = md5_hash.hexdigest()

    return encrypted_string