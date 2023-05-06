import re

def remove_punctuation_and_replace(s):
    remove_douhao = re.sub(r',', '\n', str(s)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
    remove_danyinhao = remove_douhao.replace("'", '')
    remove_xiegang = remove_danyinhao.replace('/', '\n')
    source_info = remove_xiegang.replace(' ', '')
    return source_info