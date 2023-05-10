import re

def remove_punctuation_and_replace(s):
    remove_douhao_msg = re.sub(r',', '\n',str(s)[1:-1])  # 去除不必要的标点符号 一并删除以及替换成换行符
    remove_danyinhao_msg = remove_douhao_msg.replace("'", '')
    keep_otc_msg = remove_danyinhao_msg.replace(' ', '')
    return keep_otc_msg

