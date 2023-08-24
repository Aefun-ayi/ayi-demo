import base64


def Phead(pid, cha, brand, ver, uid):
# pid = 39856
# cha = 'csj'
# brand = 'OCEAN_ENGINE'
# ver = 1000
# uid = 10001

    txt = f'cha={cha},p_id={pid},ver={ver},brand={brand},uid={uid}'

    s = txt.encode("utf-8")  # 对接口需要传值的参数进行转义
    code = base64.b64encode(s).decode("utf-8")

    return code