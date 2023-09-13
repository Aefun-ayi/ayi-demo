import re

def Remove(s):
    remove_Comma = re.sub(r',', '\n',str(s)[1:-1])  # 去除逗号 一并删除以及替换成换行符
    remove_Rsquo = remove_Comma.replace("'", '')  # 去除单引号
    keep_otc_msg = remove_Rsquo.replace(' ', '')  # 去除空格
    return keep_otc_msg

