# coding:utf-8

import pymysql

# 定义一个函数，用来创建连接数据库
def mysql_db():
    con = pymysql.connect(
        host='192.168.7.43',
        port=2023,
        database='my_database',
        charset='utf8',
        user='root',
        password='123456'
    )
    try:
        with con.cursor() as cursor:
            # 一、查询
            # sql = "select * from phone_info;"
            # sql ="insert into phone_info(id, phone_mobile, phone_name)value(1,'123456','vivo Y80');"
            res = [
    {
        "model": "YAL-AL00",
        "phonename": "HuaweiHONOR 20"
    },
    {
        "model": "YAL-TL00",
        "phonename": "HuaweiHONOR 20"
    },
    {
        "model": "MAR-LX1R",
        "phonename": "HuaweiHONOR 20 LITE"
    },
    {
        "model": "YAL-AL10",
        "phonename": "HuaweiHONOR 20 PRO"
    },
    {
        "model": "MAR-LX1H",
        "phonename": "HuaweiHONOR 20S"
    },
    {
        "model": "Che2-L12",
        "phonename": "HuaweiHONOR 4X"
    },
    {
        "model": "KSA-LX2",
        "phonename": "HuaweiHONOR 8S"
    },
    {
        "model": "KSA-LX3",
        "phonename": "HuaweiHONOR 8S"
    },
    {
        "model": "KSA-LX9",
        "phonename": "HuaweiHONOR 8S"
    },
    {
        "model": "PCT-TL10",
        "phonename": "HuaweiHONOR V20"
    },
    {
        "model": "PCT-AL10",
        "phonename": "HuaweiHONOR View20"
    },
    {
        "model": "PCT-L29",
        "phonename": "HuaweiHONOR View20"
    },
    {
        "model": "SLA-L03",
        "phonename": "HuaweiHUAWEI G Elite Plus"
    },
    {
        "model": "BLL-L21",
        "phonename": "HuaweiHUAWEI GR5 2017"
    },
    {
        "model": "BLL-L22",
        "phonename": "HuaweiHUAWEI GR5 2017"
    },
    {
        "model": "HUAWEI BLL-L21",
        "phonename": "HuaweiHUAWEI GR5 2017"
    },
    {
        "model": "HUAWEI BLL-L22",
        "phonename": "HuaweiHUAWEI GR5 2017"
    },
    {
        "model": "LYA-L0C",
        "phonename": "HuaweiHUAWEI Mate 20 Pro"
    },
    {
        "model": "EVR-AN00",
        "phonename": "HuaweiHUAWEI Mate 20 X (5G)"
    },
    {
        "model": "BLL-L23",
        "phonename": "HuaweiHUAWEI Mate 9 lite"
    },
    {
        "model": "HUAWEI BLL-L23",
        "phonename": "HuaweiHUAWEI Mate 9 lite"
    },
    {
        "model": "701HW",
        "phonename": "HuaweiHUAWEI MediaPad M3 Lite"
    },
    {
        "model": "702HW",
        "phonename": "HuaweiHUAWEI MediaPad M3 Lite"
    },
    {
        "model": "CPN-L09",
        "phonename": "HuaweiHUAWEI MediaPad M3 Lite"
    },
    {
        "model": "CPN-W09",
        "phonename": "HuaweiHUAWEI MediaPad M3 Lite"
    },
    {
        "model": "HDN-L09",
        "phonename": "HuaweiHUAWEI MediaPad M3 Lite 10 wp"
    },
    {
        "model": "HDN-W09",
        "phonename": "HuaweiHUAWEI MediaPad M3 Lite 10 wp"
    },
    {
        "model": "CMR-W19",
        "phonename": "HuaweiHUAWEI MediaPad M5 Pro"
    },
    {
        "model": "BAH2-L09",
        "phonename": "HuaweiHUAWEI MediaPad M5 lite"
    },
    {
        "model": "BAH2-W19",
        "phonename": "HuaweiHUAWEI MediaPad M5 lite"
    },
    {
        "model": "JDN2-L09",
        "phonename": "HuaweiHUAWEI MediaPad M5 lite"
    },
    {
        "model": "AGS-L03",
        "phonename": "HuaweiHUAWEI MediaPad T3 10"
    },
    {
        "model": "AGS-L09",
        "phonename": "HuaweiHUAWEI MediaPad T3 10"
    },
    {
        "model": "AGS-W09",
        "phonename": "HuaweiHUAWEI MediaPad T3 10"
    },
    {
        "model": "BG2-U03",
        "phonename": "HuaweiHUAWEI MediaPad T3 7"
    },
    {
        "model": "AGS2-W09",
        "phonename": "HuaweiHUAWEI MediaPad T5"
    },
    {
        "model": "FIG-LA1",
        "phonename": "HuaweiHUAWEI P smart"
    },
    {
        "model": "FIG-LX2",
        "phonename": "HuaweiHUAWEI P smart"
    },
    {
        "model": "FIG-LX3",
        "phonename": "HuaweiHUAWEI P smart"
    },
    {
        "model": "POT-LX1",
        "phonename": "HuaweiHUAWEI P smart 2019"
    },
    {
        "model": "POT-LX1AF",
        "phonename": "HuaweiHUAWEI P smart 2019"
    },
    {
        "model": "POT-LX1A",
        "phonename": "HuaweiHUAWEI P smart 2020"
    },
    {
        "model": "POT-LX1T",
        "phonename": "HuaweiHUAWEI P smart+ 2019"
    },
    {
        "model": "ANE-LX2J",
        "phonename": "HuaweiHUAWEI P20 Lite"
    },
    {
        "model": "HWV32",
        "phonename": "HuaweiHUAWEI P20 Lite"
    },
    {
        "model": "ELE-L04",
        "phonename": "HuaweiHUAWEI P30"
    },
    {
        "model": "ELE-L14",
        "phonename": "HuaweiHUAWEI P30"
    },
    {
        "model": "ELE-L39",
        "phonename": "HuaweiHUAWEI P30"
    },
    {
        "model": "ELE-L49",
        "phonename": "HuaweiHUAWEI P30"
    },
    {
        "model": "ELE-TL00",
        "phonename": "HuaweiHUAWEI P30"
    },
    {
        "model": "HWV33",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX1A",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX1Am",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX1B",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX1M",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX1Mm",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX2",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX2B",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX2m",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX3A",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX3Am",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "MAR-LX3Bm",
        "phonename": "HuaweiHUAWEI P30 lite"
    },
    {
        "model": "SLA-L02",
        "phonename": "HuaweiHUAWEI P9 lite mini"
    },
    {
        "model": "SLA-L22",
        "phonename": "HuaweiHUAWEI P9 lite mini"
    },
    {
        "model": "SLA-L23",
        "phonename": "HuaweiHUAWEI P9 lite mini"
    },
    {
        "model": "ARS-L22",
        "phonename": "HuaweiHUAWEI Y MAX"
    },
    {
        "model": "CRO-L02",
        "phonename": "HuaweiHUAWEI Y3 2017"
    },
    {
        "model": "CRO-L22",
        "phonename": "HuaweiHUAWEI Y3 2017"
    },
    {
        "model": "HUAWEI CRO-L02",
        "phonename": "HuaweiHUAWEI Y3 2017"
    },
    {
        "model": "HUAWEI CRO-L22",
        "phonename": "HuaweiHUAWEI Y3 2017"
    },
    {
        "model": "CAG-L02",
        "phonename": "HuaweiHUAWEI Y3 2018"
    },
    {
        "model": "CAG-L22",
        "phonename": "HuaweiHUAWEI Y3 2018"
    },
    {
        "model": "DRA-L01",
        "phonename": "HuaweiHUAWEI Y5 2018"
    },
    {
        "model": "DRA-L21",
        "phonename": "HuaweiHUAWEI Y5 2018"
    },
    {
        "model": "DRA-LX3",
        "phonename": "HuaweiHUAWEI Y5 2018"
    },
    {
        "model": "AMN-LX1",
        "phonename": "HuaweiHUAWEI Y5 2019"
    },
    {
        "model": "AMN-LX2",
        "phonename": "HuaweiHUAWEI Y5 2019"
    },
    {
        "model": "AMN-LX3",
        "phonename": "HuaweiHUAWEI Y5 2019"
    },
    {
        "model": "AMN-LX9",
        "phonename": "HuaweiHUAWEI Y5 2019"
    },
    {
        "model": "CRO-L03",
        "phonename": "HuaweiHUAWEI Y5 lite 2017"
    },
    {
        "model": "CRO-L23",
        "phonename": "HuaweiHUAWEI Y5 lite 2017"
    },
    {
        "model": "HUAWEI CRO-L03",
        "phonename": "HuaweiHUAWEI Y5 lite 2017"
    },
    {
        "model": "HUAWEI CRO-L23",
        "phonename": "HuaweiHUAWEI Y5 lite 2017"
    },
    {
        "model": "CAG-L03",
        "phonename": "HuaweiHUAWEI Y5 lite 2018"
    },
    {
        "model": "CAG-L23",
        "phonename": "HuaweiHUAWEI Y5 lite 2018"
    },
    {
        "model": "MYA-L11",
        "phonename": "HuaweiHUAWEI Y6 2017"
    },
    {
        "model": "ATU-L11",
        "phonename": "HuaweiHUAWEI Y6 2018"
    },
    {
        "model": "ATU-L21",
        "phonename": "HuaweiHUAWEI Y6 2018"
    },
    {
        "model": "ATU-L22",
        "phonename": "HuaweiHUAWEI Y6 2018"
    },
    {
        "model": "ATU-LX3",
        "phonename": "HuaweiHUAWEI Y6 2018"
    },
    {
        "model": "MRD-LX1",
        "phonename": "HuaweiHUAWEI Y6 2019"
    },
    {
        "model": "MRD-LX1F",
        "phonename": "HuaweiHUAWEI Y6 2019"
    },
    {
        "model": "MRD-LX1N",
        "phonename": "HuaweiHUAWEI Y6 2019"
    },
    {
        "model": "MRD-LX3",
        "phonename": "HuaweiHUAWEI Y6 2019"
    },
    {
        "model": "ATU-L31",
        "phonename": "HuaweiHUAWEI Y6 Prime 2018"
    },
    {
        "model": "ATU-L42",
        "phonename": "HuaweiHUAWEI Y6 Prime 2018"
    },
    {
        "model": "MRD-LX2",
        "phonename": "HuaweiHUAWEI Y6 Pro 2019"
    },
    {
        "model": "HUAWEI CAM-L53",
        "phonename": "HuaweiHUAWEI Y6II"
    },
    {
        "model": "LDN-L01",
        "phonename": "HuaweiHUAWEI Y7 2018"
    },
    {
        "model": "LDN-LX3",
        "phonename": "HuaweiHUAWEI Y7 2018"
    },
    {
        "model": "FLA-LX1",
        "phonename": "HuaweiHUAWEI Y9 2018"
    },
    {
        "model": "FLA-LX2",
        "phonename": "HuaweiHUAWEI Y9 2018"
    },
    {
        "model": "FLA-LX3",
        "phonename": "HuaweiHUAWEI Y9 2018"
    },
    {
        "model": "JKM-LX1",
        "phonename": "HuaweiHUAWEI Y9 2019"
    },
    {
        "model": "JKM-LX2",
        "phonename": "HuaweiHUAWEI Y9 2019"
    },
    {
        "model": "JKM-LX3",
        "phonename": "HuaweiHUAWEI Y9 2019"
    },
    {
        "model": "BAC-L21",
        "phonename": "HuaweiHUAWEI nova 2 Plus"
    },
    {
        "model": "BAC-L22",
        "phonename": "HuaweiHUAWEI nova 2 Plus"
    },
    {
        "model": "704HW",
        "phonename": "HuaweiHUAWEI nova lite 2"
    },
    {
        "model": "608HW",
        "phonename": "HuaweiHUAWEI nova lite for Y!mobile"
    },
    {
        "model": "KOB-L09",
        "phonename": "HuaweiHUWEI MediaPad T3"
    },
    {
        "model": "KOB-W09",
        "phonename": "HuaweiHUWEI MediaPad T3"
    },
    {
        "model": "HW-03E",
        "phonename": "HuaweiHW-03E"
    },
    {
        "model": "HWT31",
        "phonename": "HuaweiHWT31"
    },
    {
        "model": "Hol-T00",
        "phonename": "HuaweiHol-T00"
    },
    {
        "model": "Hol-U10",
        "phonename": "HuaweiHol-U10"
    },
    {
        "model": "Hol-U19",
        "phonename": "HuaweiHol-U19"
    },
    {
        "model": "COL-AL00",
        "phonename": "HuaweiHonor 10"
    },
    {
        "model": "COL-AL10",
        "phonename": "HuaweiHonor 10"
    },
    {
        "model": "COL-L29",
        "phonename": "HuaweiHonor 10"
    },
    {
        "model": "COL-TL10",
        "phonename": "HuaweiHonor 10"
    },
    {
        "model": "HRY-AL00a",
        "phonename": "HuaweiHonor 10 Lite"
    },
    {
        "model": "HRY-AL00Ta",
        "phonename": "HuaweiHonor 20i"
    },
    {
        "model": "SCL-CL00",
        "phonename": "HuaweiHonor 4A"
    },
    {
        "model": "SCL-TL00",
        "phonename": "HuaweiHonor 4A"
    },
    {
        "model": "SCL-TL00H",
        "phonename": "HuaweiHonor 4A"
    },
    {
        "model": "HUAWEI LYO-L21",
        "phonename": "HuaweiHonor 5A"
    },
    {
        "model": "LYO-L21",
        "phonename": "HuaweiHonor 5A"
    },
    {
        "model": "NEM-L21",
        "phonename": "HuaweiHonor 5C"
    },
    {
        "model": "NEM-L22",
        "phonename": "HuaweiHonor 5C"
    },
    {
        "model": "NEM-L51",
        "phonename": "HuaweiHonor 5C"
    },
    {
        "model": "KIW-L21",
        "phonename": "HuaweiHonor 5X"
    },
    {
        "model": "KIW-TL00H",
        "phonename": "HuaweiHonor 5X"
    },
    {
        "model": "DLI-L22",
        "phonename": "HuaweiHonor 6A"
    },
    {
        "model": "DLI-TL20",
        "phonename": "HuaweiHonor 6A"
    },
    {
        "model": "BLN-L24",
        "phonename": "HuaweiHonor 6X"
    },
    {
        "model": "PLK-AL10",
        "phonename": "HuaweiHonor 7"
    },
    {
        "model": "PLK-CL00",
        "phonename": "HuaweiHonor 7"
    },
    {
        "model": "PLK-L01",
        "phonename": "HuaweiHonor 7"
    },
    {
        "model": "PLK-TL00",
        "phonename": "HuaweiHonor 7"
    },
    {
        "model": "PLK-TL01H",
        "phonename": "HuaweiHonor 7"
    },
    {
        "model": "PLK-UL00",
        "phonename": "HuaweiHonor 7"
    },
    {
        "model": "AUM-AL00",
        "phonename": "HuaweiHonor 7A"
    },
    {
        "model": "AUM-AL20",
        "phonename": "HuaweiHonor 7A"
    },
    {
        "model": "AUM-L29",
        "phonename": "HuaweiHonor 7A"
    },
    {
        "model": "AUM-L33",
        "phonename": "HuaweiHonor 7A"
    },
    {
        "model": "AUM-TL00",
        "phonename": "HuaweiHonor 7A"
    },
    {
        "model": "AUM-TL20",
        "phonename": "HuaweiHonor 7A"
    },
    {
        "model": "AUM-L41",
        "phonename": "HuaweiHonor 7C"
    },
    {
        "model": "LND-AL30",
        "phonename": "HuaweiHonor 7C"
    },
    {
        "model": "LND-AL40",
        "phonename": "HuaweiHonor 7C"
    },
    {
        "model": "LND-L29",
        "phonename": "HuaweiHonor 7C"
    },
    {
        "model": "LND-TL30",
        "phonename": "HuaweiHonor 7C"
    },
    {
        "model": "LND-TL40",
        "phonename": "HuaweiHonor 7C"
    },
    {
        "model": "DRA-LX5",
        "phonename": "HuaweiHonor 7S"
    },
    {
        "model": "DUA-LX3",
        "phonename": "HuaweiHonor 7S"
    },
    {
        "model": "BND-L21",
        "phonename": "HuaweiHonor 7X"
    },
    {
        "model": "BND-L24",
        "phonename": "HuaweiHonor 7X"
    },
    {
        "model": "BND-L31",
        "phonename": "HuaweiHonor 7X"
    },
    {
        "model": "ATH-AL00",
        "phonename": "HuaweiHonor 7i"
    },
    {
        "model": "ATH-CL00",
        "phonename": "HuaweiHonor 7i"
    },
    {
        "model": "FRD-AL10",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "FRD-DL00",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "FRD-L04",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "FRD-L09",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "FRD-L14",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "FRD-L19",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "FRD-L24",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "FRD-TL00",
        "phonename": "HuaweiHonor 8"
    },
    {
        "model": "DUK-L09",
        "phonename": "HuaweiHonor 8 Pro"
    },
    {
        "model": "VEN-L22",
        "phonename": "HuaweiHonor 8 Smart"
    },
    {
        "model": "JAT-L29",
        "phonename": "HuaweiHonor 8A"
    },
    {
        "model": "JAT-L41",
        "phonename": "HuaweiHonor 8A"
    },
    {
        "model": "JAT-LX1",
        "phonename": "HuaweiHonor 8A"
    },
    {
        "model": "JAT-LX3",
        "phonename": "HuaweiHonor 8A"
    },
    {
        "model": "JSN-L21",
        "phonename": "HuaweiHonor 8X"
    },
    {
        "model": "JSN-L22",
        "phonename": "HuaweiHonor 8X"
    },
    {
        "model": "JSN-L23",
        "phonename": "HuaweiHonor 8X"
    },
    {
        "model": "ARE-L22HN",
        "phonename": "HuaweiHonor 8X Max"
    },
    {
        "model": "JSN-L42",
        "phonename": "HuaweiHonor 8x"
    },
    {
        "model": "STF-AL00",
        "phonename": "HuaweiHonor 9"
    },
    {
        "model": "STF-AL10",
        "phonename": "HuaweiHonor 9"
    },
    {
        "model": "STF-L09",
        "phonename": "HuaweiHonor 9"
    },
    {
        "model": "STF-L09S",
        "phonename": "HuaweiHonor 9"
    },
    {
        "model": "STF-TL10",
        "phonename": "HuaweiHonor 9"
    },
    {
        "model": "LLD-L21",
        "phonename": "HuaweiHonor 9 Lite"
    },
    {
        "model": "LLD-L31",
        "phonename": "HuaweiHonor 9 Lite"
    },
    {
        "model": "M321",
        "phonename": "HuaweiHonor Box"
    },
    {
        "model": "HiTV-M1",
        "phonename": "HuaweiHonor Box Pro"
    },
    {
        "model": "M311",
        "phonename": "HuaweiHonor Box voice"
    },
    {
        "model": "HUAWEI NTS-AL00",
        "phonename": "HuaweiHonor Magic"
    },
    {
        "model": "NTS-AL00",
        "phonename": "HuaweiHonor Magic"
    },
    {
        "model": "TNY-AL00",
        "phonename": "HuaweiHonor Magic 2"
    },
    {
        "model": "TNY-TL00",
        "phonename": "HuaweiHonor Magic 2"
    },
    {
        "model": "RVL-AL09",
        "phonename": "HuaweiHonor Note10"
    },
    {
        "model": "COR-AL00",
        "phonename": "HuaweiHonor Play"
    },
    {
        "model": "COR-AL10",
        "phonename": "HuaweiHonor Play"
    },
    {
        "model": "COR-L29",
        "phonename": "HuaweiHonor Play"
    },
    {
        "model": "COR-TL10",
        "phonename": "HuaweiHonor Play"
    },
    {
        "model": "BKL-AL00",
        "phonename": "HuaweiHonor V10"
    },
    {
        "model": "BKL-AL20",
        "phonename": "HuaweiHonor V10"
    },
    {
        "model": "BKL-TL10",
        "phonename": "HuaweiHonor V10"
    },
    {
        "model": "KNT-AL10",
        "phonename": "HuaweiHonor V8"
    },
    {
        "model": "KNT-AL20",
        "phonename": "HuaweiHonor V8"
    },
    {
        "model": "KNT-TL10",
        "phonename": "HuaweiHonor V8"
    },
    {
        "model": "KNT-UL10",
        "phonename": "HuaweiHonor V8"
    },
    {
        "model": "DUK-AL20",
        "phonename": "HuaweiHonor V9"
    },
    {
        "model": "DUK-TL30",
        "phonename": "HuaweiHonor V9"
    },
    {
        "model": "BKL-L04",
        "phonename": "HuaweiHonor View 10"
    },
    {
        "model": "BKL-L09",
        "phonename": "HuaweiHonor View 10"
    },
    {
        "model": "H30-T10",
        "phonename": "HuaweiHonor3"
    },
    {
        "model": "H30-U10",
        "phonename": "HuaweiHonor3"
    },
    {
        "model": "HUAWEI HN3-U00",
        "phonename": "HuaweiHonor3"
    },
    {
        "model": "HUAWEI HN3-U01",
        "phonename": "HuaweiHonor3"
    },
    {
        "model": "H1711",
        "phonename": "HuaweiHuawei Ascend XT2™"
    },
    {
        "model": "H1711z",
        "phonename": "HuaweiHuawei Elate™"
    },
    {
        "model": "EVR-TL00",
        "phonename": "HuaweiHuawei Mate 20 X"
    },
    {
        "model": "EVR-N29",
        "phonename": "HuaweiHuawei Mate 20 X (5G)"
    },
    {
        "model": "AGS2-L03",
        "phonename": "HuaweiHuawei MediaPad T5"
    },
    {
        "model": "AGS2-L09",
        "phonename": "HuaweiHuawei MediaPad T5"
    },
    {
        "model": "AGS2-W19",
        "phonename": "HuaweiHuawei MediaPad T5"
    },
    {
        "model": "PIC-LX9",
        "phonename": "HuaweiHuawei Nova 2"
    },
    {
        "model": "EVR-AL00",
        "phonename": "HuaweiHuwei Mate 20 X"
    },
    {
        "model": "Comet",
        "phonename": "HuaweiIDEOS"
    },
    {
        "model": "Ideos",
        "phonename": "HuaweiIDEOS"
    },
    {
        "model": "Ice-Twist",
        "phonename": "HuaweiIce-Twist"
    },
    {
        "model": "Huawei U8800-51",
        "phonename": "HuaweiIdeos X5"
    },
    {
        "model": "IDEOS X5",
        "phonename": "HuaweiIdeos X5"
    },
    {
        "model": "U8800",
        "phonename": "HuaweiIdeos X5"
    },
    {
        "model": "U8800-51",
        "phonename": "HuaweiIdeos X5"
    },
    {
        "model": "H1622",
        "phonename": "HuaweiKiwi-2"
    },
    {
        "model": "HUAWEI M2-A01L",
        "phonename": "HuaweiLISZT"
    },
    {
        "model": "HUAWEI M2-A01W",
        "phonename": "HuaweiLISZT"
    },
    {
        "model": "HUAWEI M2-801L",
        "phonename": "HuaweiM2"
    },
    {
        "model": "HUAWEI M2-801W",
        "phonename": "HuaweiM2"
    },
    {
        "model": "HUAWEI M2-802L",
        "phonename": "HuaweiM2"
    },
    {
        "model": "HUAWEI M2-803L",
        "phonename": "HuaweiM2"
    },
    {
        "model": "M220",
        "phonename": "HuaweiM220"
    },
    {
        "model": "M220c",
        "phonename": "HuaweiM220"
    },
    {
        "model": "dTV01",
        "phonename": "HuaweiM220"
    },
    {
        "model": "M310",
        "phonename": "HuaweiM310"
    },
    {
        "model": "M620",
        "phonename": "HuaweiM620"
    },
    {
        "model": "TB01",
        "phonename": "HuaweiM620"
    },
    {
        "model": "HUAWEI-M835",
        "phonename": "HuaweiM835"
    },
    {
        "model": "M860",
        "phonename": "HuaweiM860"
    },
    {
        "model": "M865",
        "phonename": "HuaweiM865"
    },
    {
        "model": "USCCADR3305",
        "phonename": "HuaweiM865"
    },
    {
        "model": "HUAWEI M868",
        "phonename": "HuaweiM868"
    },
    {
        "model": "RNE-AL00",
        "phonename": "HuaweiMAIMANG 6"
    },
    {
        "model": "SNE-AL00",
        "phonename": "HuaweiMAIMANG 7"
    },
    {
        "model": "MS4C",
        "phonename": "HuaweiMS4C"
    },
    {
        "model": "HUAWEI MT1-U06",
        "phonename": "HuaweiMT1"
    },
    {
        "model": "HUAWEI MT2-L01",
        "phonename": "HuaweiMT2-L01"
    },
    {
        "model": "HUAWEI MT2-L02",
        "phonename": "HuaweiMT2-L02"
    },
    {
        "model": "HUAWEI MT2-L05",
        "phonename": "HuaweiMT2-L05"
    },
    {
        "model": "HUAWEI MT1-T00",
        "phonename": "HuaweiMate"
    },
    {
        "model": "ALP-AL00",
        "phonename": "HuaweiMate 10"
    },
    {
        "model": "ALP-L09",
        "phonename": "HuaweiMate 10"
    },
    {
        "model": "ALP-L29",
        "phonename": "HuaweiMate 10"
    },
    {
        "model": "ALP-TL00",
        "phonename": "HuaweiMate 10"
    },
    {
        "model": "BLA-AL00",
        "phonename": "HuaweiMate 10 Pro"
    },
    {
        "model": "BLA-L09",
        "phonename": "HuaweiMate 10 Pro"
    },
    {
        "model": "BLA-L29",
        "phonename": "HuaweiMate 10 Pro"
    },
    {
        "model": "BLA-TL00",
        "phonename": "HuaweiMate 10 Pro"
    },
    {
        "model": "RNE-L01",
        "phonename": "HuaweiMate 10 lite"
    },
    {
        "model": "RNE-L03",
        "phonename": "HuaweiMate 10 lite"
    },
    {
        "model": "RNE-L21",
        "phonename": "HuaweiMate 10 lite"
    },
    {
        "model": "RNE-L23",
        "phonename": "HuaweiMate 10 lite"
    },
    {
        "model": "HMA-TL00",
        "phonename": "HuaweiMate 20"
    },
    {
        "model": "LYA-AL00",
        "phonename": "HuaweiMate 20 Pro"
    },
    {
        "model": "LYA-AL10",
        "phonename": "HuaweiMate 20 Pro"
    },
    {
        "model": "LYA-TL00",
        "phonename": "HuaweiMate 20 Pro"
    },
    {
        "model": "LYA-AL00P",
        "phonename": "HuaweiMate 20 RS"
    },
    {
        "model": "SNE-LX1",
        "phonename": "HuaweiMate 20 lite"
    },
    {
        "model": "SNE-LX2",
        "phonename": "HuaweiMate 20 lite"
    },
    {
        "model": "SNE-LX3",
        "phonename": "HuaweiMate 20 lite"
    },
    {
        "model": "HUAWEI MT7-CL00",
        "phonename": "HuaweiMate 7"
    },
    {
        "model": "HUAWEI MT7-J1",
        "phonename": "HuaweiMate 7"
    },
    {
        "model": "HUAWEI MT7-L09",
        "phonename": "HuaweiMate 7"
    },
    {
        "model": "HUAWEI MT7-TL00",
        "phonename": "HuaweiMate 7"
    },
    {
        "model": "HUAWEI MT7-TL10",
        "phonename": "HuaweiMate 7"
    },
    {
        "model": "HUAWEI MT7-UL00",
        "phonename": "HuaweiMate 7"
    },
    {
        "model": "HUAWEI NXT-AL10",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "HUAWEI NXT-CL00",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "HUAWEI NXT-DL00",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "HUAWEI NXT-L09",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "HUAWEI NXT-L29",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "HUAWEI NXT-TL00",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "HUAWEI NXT-TL00B",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "NXT-AL10",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "NXT-CL00",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "NXT-DL00",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "NXT-L09",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "NXT-L29",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "NXT-TL00",
        "phonename": "HuaweiMate 8"
    },
    {
        "model": "MHA-AL00",
        "phonename": "HuaweiMate 9"
    },
    {
        "model": "MHA-L09",
        "phonename": "HuaweiMate 9"
    },
    {
        "model": "MHA-TL00",
        "phonename": "HuaweiMate 9"
    },
    {
        "model": "LON-AL00",
        "phonename": "HuaweiMate 9 Pro"
    },
    {
        "model": "HUAWEI CRR-CL00",
        "phonename": "HuaweiMate S"
    },
    {
        "model": "HUAWEI CRR-CL20",
        "phonename": "HuaweiMate S"
    },
    {
        "model": "HUAWEI CRR-L09",
        "phonename": "HuaweiMate S"
    },
    {
        "model": "HUAWEI CRR-TL00",
        "phonename": "HuaweiMate S"
    },
    {
        "model": "HUAWEI CRR-UL00",
        "phonename": "HuaweiMate S"
    },
    {
        "model": "HUAWEI CRR-UL20",
        "phonename": "HuaweiMate S"
    },
    {
        "model": "HUAWEI MT2-C00",
        "phonename": "HuaweiMate2"
    },
    {
        "model": "HUAWEI MediaPad T1 7.0 3G",
        "phonename": "HuaweiMediaPad"
    },
    {
        "model": "T1 7.0",
        "phonename": "HuaweiMediaPad"
    },
    {
        "model": "T1-701u",
        "phonename": "HuaweiMediaPad"
    },
    {
        "model": "T1-701ua",
        "phonename": "HuaweiMediaPad"
    },
    {
        "model": "T1-701us",
        "phonename": "HuaweiMediaPad"
    },
    {
        "model": "T1-701w",
        "phonename": "HuaweiMediaPad"
    },
    {
        "model": "dtab 01",
        "phonename": "HuaweiMediaPad 10 Link"
    },
    {
        "model": "402HW",
        "phonename": "HuaweiMediaPad 10 Link+"
    },
    {
        "model": "MediaPad 10 Link+",
        "phonename": "HuaweiMediaPad 10 Link+"
    },
    {
        "model": "S10-232L",
        "phonename": "HuaweiMediaPad 10 Link+"
    },
    {
        "model": "SpeedTAB",
        "phonename": "HuaweiMediaPad 10 Link+"
    },
    {
        "model": "MediaPad 7 Lite",
        "phonename": "HuaweiMediaPad 7 Lite"
    },
    {
        "model": "Telpad QS",
        "phonename": "HuaweiMediaPad 7 Lite Quad"
    },
    {
        "model": "Telpad Quad S",
        "phonename": "HuaweiMediaPad 7 Lite Quad"
    },
    {
        "model": "S7-721u",
        "phonename": "HuaweiMediaPad 7 Youth2"
    },
    {
        "model": "403HW",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "CNPC Security Pad S1",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "HUAWEI MediaPad M1 8.0",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "MediaPad M1 8.0",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "MediaPad M1 8.0 (LTE)",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "MediaPad M1 8.0 (WIFI)",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "S8-303L",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "S8-303LT",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "S8-306L",
        "phonename": "HuaweiMediaPad M1 8.0"
    },
    {
        "model": "BAH-L09",
        "phonename": "HuaweiMediaPad M3 Lite 10"
    },
    {
        "model": "605HW",
        "phonename": "HuaweiMediaPad T2 10.0 Pro"
    },
    {
        "model": "606HW",
        "phonename": "HuaweiMediaPad T2 10.0 Pro"
    },
    {
        "model": "FDR-A05L",
        "phonename": "HuaweiMediaPad T2 10.0 Pro"
    },
    {
        "model": "FDR-A01L",
        "phonename": "HuaweiMediaPad T2 10.0 pro"
    },
    {
        "model": "BGO-DL09",
        "phonename": "HuaweiMediaPad T2 7.0"
    },
    {
        "model": "BGO-L03",
        "phonename": "HuaweiMediaPad T2 7.0"
    },
    {
        "model": "JDN-L01",
        "phonename": "HuaweiMediaPad T2 8.0 Pro"
    },
    {
        "model": "BG2-U01",
        "phonename": "HuaweiMediaPad T3 7"
    },
    {
        "model": "BG2-W09",
        "phonename": "HuaweiMediaPad T3 7"
    },
    {
        "model": "7D-501u",
        "phonename": "HuaweiMediaPad X1 7.0"
    },
    {
        "model": "MediaPad X1",
        "phonename": "HuaweiMediaPad X1 7.0"
    },
    {
        "model": "MediaPad X1 7.0",
        "phonename": "HuaweiMediaPad X1 7.0"
    },
    {
        "model": "X1 7.0",
        "phonename": "HuaweiMediaPad X1 7.0"
    },
    {
        "model": "M380-10",
        "phonename": "HuaweiMediaQ M380"
    },
    {
        "model": "Nexus 6P",
        "phonename": "HuaweiNexus 6P"
    },
    {
        "model": "INE-LX2r",
        "phonename": "HuaweiNova 3i"
    },
    {
        "model": "VTR-AL00",
        "phonename": "HuaweiP10"
    },
    {
        "model": "VTR-TL00",
        "phonename": "HuaweiP10"
    },
    {
        "model": "VKY-AL00",
        "phonename": "HuaweiP10 Plus"
    },
    {
        "model": "VKY-TL00",
        "phonename": "HuaweiP10 Plus"
    },
    {
        "model": "WAS-L03T",
        "phonename": "HuaweiP10 lite"
    },
    {
        "model": "WAS-LX1",
        "phonename": "HuaweiP10 lite"
    },
    {
        "model": "WAS-LX1A",
        "phonename": "HuaweiP10 lite"
    },
    {
        "model": "WAS-LX2",
        "phonename": "HuaweiP10 lite"
    },
    {
        "model": "WAS-LX2J",
        "phonename": "HuaweiP10 lite"
    },
    {
        "model": "WAS-LX3",
        "phonename": "HuaweiP10 lite"
    },
    {
        "model": "HUAWEI P2-6070",
        "phonename": "HuaweiP2"
    },
    {
        "model": "EML-AL00",
        "phonename": "HuaweiP20"
    },
    {
        "model": "EML-TL00",
        "phonename": "HuaweiP20"
    },
    {
        "model": "HW-01K",
        "phonename": "HuaweiP20 Pro"
    },
    {
        "model": "CLT-AL00",
        "phonename": "HuaweiP20 Pro"
    },
    {
        "model": "CLT-AL00l",
        "phonename": "HuaweiP20 Pro"
    },
    {
        "model": "CLT-AL01",
        "phonename": "HuaweiP20 Pro"
    },
    {
        "model": "CLT-L04",
        "phonename": "HuaweiP20 Pro"
    },
    {
        "model": "CLT-TL00",
        "phonename": "HuaweiP20 Pro"
    },
    {
        "model": "CLT-TL01",
        "phonename": "HuaweiP20 Pro"
    },
    {
        "model": "ANE-LX1",
        "phonename": "HuaweiP20 lite"
    },
    {
        "model": "ANE-LX2",
        "phonename": "HuaweiP20 lite"
    },
    {
        "model": "ANE-LX3",
        "phonename": "HuaweiP20 lite"
    },
    {
        "model": "CLT-L09",
        "phonename": "HuaweiP20Pro"
    },
    {
        "model": "CLT-L29",
        "phonename": "HuaweiP20Pro"
    },
    {
        "model": "HW-02L",
        "phonename": "HuaweiP30 Pro"
    },
    {
        "model": "VOG-AL00",
        "phonename": "HuaweiP30 Pro"
    },
    {
        "model": "VOG-AL10",
        "phonename": "HuaweiP30 Pro"
    },
    {
        "model": "VOG-TL00",
        "phonename": "HuaweiP30 Pro"
    },
    {
        "model": "MAR-LX2J",
        "phonename": "HuaweiP30 lite"
    },
    {
        "model": "HUAWEI P6-C00",
        "phonename": "HuaweiP6"
    },
    {
        "model": "HUAWEI P6-T00",
        "phonename": "HuaweiP6"
    },
    {
        "model": "HUAWEI P6-T00V",
        "phonename": "HuaweiP6"
    },
    {
        "model": "HUAWEI Ascend P6",
        "phonename": "HuaweiP6"
    },
    {
        "model": "HUAWEI P6-U06",
        "phonename": "HuaweiP6"
    },
    {
        "model": "HUAWEI P6-U06-orange",
        "phonename": "HuaweiP6"
    },
    {
        "model": "P6 S-L04",
        "phonename": "HuaweiP6S"
    },
    {
        "model": "302HW",
        "phonename": "HuaweiP6S-L04"
    },
    {
        "model": "HUAWEI P6 S-U06",
        "phonename": "HuaweiP6S-U06"
    },
    {
        "model": "HUAWEI P7-L00",
        "phonename": "HuaweiP7"
    },
    {
        "model": "HUAWEI P7-L05",
        "phonename": "HuaweiP7"
    },
    {
        "model": "HUAWEI P7-L07",
        "phonename": "HuaweiP7"
    },
    {
        "model": "HUAWEI P7-L10",
        "phonename": "HuaweiP7"
    },
    {
        "model": "HUAWEI P7-L11",
        "phonename": "HuaweiP7"
    },
    {
        "model": "HUAWEI P7-L12",
        "phonename": "HuaweiP7"
    },
    {
        "model": "HUAWEI P7 mini",
        "phonename": "HuaweiP7 mini"
    },
    {
        "model": "HUAWEI P7-L09",
        "phonename": "HuaweiP7-L09"
    },
    {
        "model": "HUAWEI GRA-CL00",
        "phonename": "HuaweiP8"
    },
    {
        "model": "HUAWEI GRA-CL10",
        "phonename": "HuaweiP8"
    },
    {
        "model": "HUAWEI GRA-L09",
        "phonename": "HuaweiP8"
    },
    {
        "model": "HUAWEI GRA-TL00",
        "phonename": "HuaweiP8"
    },
    {
        "model": "HUAWEI GRA-UL00",
        "phonename": "HuaweiP8"
    },
    {
        "model": "HUAWEI GRA-UL10",
        "phonename": "HuaweiP8"
    },
    {
        "model": "503HW",
        "phonename": "HuaweiP8 Lite"
    },
    {
        "model": "ALE-L02",
        "phonename": "HuaweiP8 Lite"
    },
    {
        "model": "ALE-L21",
        "phonename": "HuaweiP8 Lite"
    },
    {
        "model": "ALE-L23",
        "phonename": "HuaweiP8 Lite"
    },
    {
        "model": "Autana LTE",
        "phonename": "HuaweiP8 Lite"
    },
    {
        "model": "HUAWEI ALE-CL00",
        "phonename": "HuaweiP8 Lite"
    },
    {
        "model": "HUAWEI ALE-L04",
        "phonename": "HuaweiP8 Lite"
    },
    {
        "model": "PRA-LA1",
        "phonename": "HuaweiP8 lite 2017"
    },
    {
        "model": "PRA-LX1",
        "phonename": "HuaweiP8 lite 2017"
    },
    {
        "model": "ALE-TL00",
        "phonename": "HuaweiP8 青春版"
    },
    {
        "model": "ALE-UL00",
        "phonename": "HuaweiP8 青春版"
    },
    {
        "model": "HUAWEI P8max",
        "phonename": "HuaweiP8max"
    },
    {
        "model": "EVA-AL00",
        "phonename": "HuaweiP9"
    },
    {
        "model": "EVA-AL10",
        "phonename": "HuaweiP9"
    },
    {
        "model": "EVA-CL00",
        "phonename": "HuaweiP9"
    },
    {
        "model": "EVA-DL00",
        "phonename": "HuaweiP9"
    },
    {
        "model": "EVA-L19",
        "phonename": "HuaweiP9"
    },
    {
        "model": "EVA-L29",
        "phonename": "HuaweiP9"
    },
    {
        "model": "EVA-TL00",
        "phonename": "HuaweiP9"
    },
    {
        "model": "HUAWEI VNS-L52",
        "phonename": "HuaweiP9 Lite PREMIUM"
    },
    {
        "model": "VIE-AL10",
        "phonename": "HuaweiP9 Plus"
    },
    {
        "model": "VIE-L09",
        "phonename": "HuaweiP9 Plus"
    },
    {
        "model": "HUAWEI VNS-L21",
        "phonename": "HuaweiP9 lite"
    },
    {
        "model": "HUAWEI VNS-L22",
        "phonename": "HuaweiP9 lite"
    },
    {
        "model": "HUAWEI VNS-L23",
        "phonename": "HuaweiP9 lite"
    },
    {
        "model": "HUAWEI VNS-L31",
        "phonename": "HuaweiP9 lite"
    },
    {
        "model": "HUAWEI VNS-L53",
        "phonename": "HuaweiP9 lite"
    },
    {
        "model": "HUAWEI VNS-L62",
        "phonename": "HuaweiP9 lite"
    },
    {
        "model": "DIG-L03",
        "phonename": "HuaweiP9 lite smart"
    },
    {
        "model": "DIG-L23",
        "phonename": "HuaweiP9 lite smart"
    },
    {
        "model": "PE-CL00",
        "phonename": "HuaweiPE-CL00"
    },
    {
        "model": "PE-TL00M",
        "phonename": "HuaweiPE-TL00M"
    },
    {
        "model": "PE-TL10",
        "phonename": "HuaweiPE-TL10"
    },
    {
        "model": "PE-TL20",
        "phonename": "HuaweiPE-TL20"
    },
    {
        "model": "PE-UL00",
        "phonename": "HuaweiPE-UL00"
    },
    {
        "model": "NEO-AL00",
        "phonename": "HuaweiPORSCHE DESIGN HUAWEI Mate RS"
    },
    {
        "model": "Prism II",
        "phonename": "HuaweiPrism II"
    },
    {
        "model": "Q22",
        "phonename": "HuaweiQ22"
    },
    {
        "model": "HUAWEI RIO-CL00",
        "phonename": "HuaweiRIO-CL00"
    },
    {
        "model": "MediaPad 10 FHD",
        "phonename": "HuaweiS10"
    },
    {
        "model": "MediaPad 10 LINK",
        "phonename": "HuaweiS10"
    },
    {
        "model": "MediaPad 7 Youth",
        "phonename": "HuaweiS7"
    },
    {
        "model": "Orinoquia Roraima S7-932u",
        "phonename": "HuaweiS7"
    },
    {
        "model": "MediaPad 7 Lite+",
        "phonename": "HuaweiS7"
    },
    {
        "model": "Telpad Dual S",
        "phonename": "HuaweiS7"
    },
    {
        "model": "HUAWEI SC-CL00",
        "phonename": "HuaweiSC-CL00"
    },
    {
        "model": "HUAWEI SC-UL10",
        "phonename": "HuaweiSC-UL10"
    },
    {
        "model": "H710VL",
        "phonename": "HuaweiSensa LTE"
    },
    {
        "model": "H715BL",
        "phonename": "HuaweiSensa LTE"
    },
    {
        "model": "HUAWEI ATH-UL01",
        "phonename": "HuaweiShotX"
    },
    {
        "model": "HUAWEI ATH-UL06",
        "phonename": "HuaweiShotX"
    },
    {
        "model": "Huawei_8100-9",
        "phonename": "HuaweiT-Mobile Pulse"
    },
    {
        "model": "Tactile internet",
        "phonename": "HuaweiT-Mobile Pulse"
    },
    {
        "model": "U8100",
        "phonename": "HuaweiT-Mobile Pulse"
    },
    {
        "model": "Videocon_V7400",
        "phonename": "HuaweiT-Mobile Pulse"
    },
    {
        "model": "T1-821L",
        "phonename": "HuaweiT1"
    },
    {
        "model": "HUAWEI MediaPad T1 10 4G",
        "phonename": "HuaweiT1 10"
    },
    {
        "model": "T1-A21L",
        "phonename": "HuaweiT1 10"
    },
    {
        "model": "T1-A21W",
        "phonename": "HuaweiT1 10"
    },
    {
        "model": "T1-A22L",
        "phonename": "HuaweiT1 10"
    },
    {
        "model": "T1-A23L",
        "phonename": "HuaweiT1 10"
    },
    {
        "model": "T-101",
        "phonename": "HuaweiT101"
    },
    {
        "model": "T101 PAD",
        "phonename": "HuaweiT101"
    },
    {
        "model": "QH-10",
        "phonename": "HuaweiT102"
    },
    {
        "model": "T102 PAD",
        "phonename": "HuaweiT102"
    },
    {
        "model": "T801 PAD",
        "phonename": "HuaweiT801"
    },
    {
        "model": "MT-803G",
        "phonename": "HuaweiT802"
    },
    {
        "model": "T802 PAD",
        "phonename": "HuaweiT802"
    },
    {
        "model": "HUAWEI T8808D",
        "phonename": "HuaweiT8808D"
    },
    {
        "model": "HUAWEI TAG-AL00",
        "phonename": "HuaweiTANGO"
    },
    {
        "model": "HUAWEI TAG-CL00",
        "phonename": "HuaweiTANGO"
    },
    {
        "model": "HUAWEI TAG-TL00",
        "phonename": "HuaweiTANGO"
    },
    {
        "model": "Vodafone 845",
        "phonename": "HuaweiU8120"
    },
    {
        "model": "Pulse",
        "phonename": "HuaweiU8220"
    },
    {
        "model": "U8220",
        "phonename": "HuaweiU8220"
    },
    {
        "model": "U8220PLUS",
        "phonename": "HuaweiU8220"
    },
    {
        "model": "U8230",
        "phonename": "HuaweiU8230"
    },
    {
        "model": "Huawei-U8652",
        "phonename": "HuaweiU8652"
    },
    {
        "model": "U8652",
        "phonename": "HuaweiU8652"
    },
    {
        "model": "Huawei-U8687",
        "phonename": "HuaweiU8687"
    },
    {
        "model": "U8812D",
        "phonename": "HuaweiU8812D"
    },
    {
        "model": "U8832D",
        "phonename": "HuaweiU8832D"
    },
    {
        "model": "U8836D",
        "phonename": "HuaweiU8836D"
    },
    {
        "model": "HUAWEI-U8850",
        "phonename": "HuaweiU8850"
    },
    {
        "model": "HUAWEI-U9000",
        "phonename": "HuaweiU9000"
    },
    {
        "model": "Y538",
        "phonename": "HuaweiUNION"
    },
    {
        "model": "Huawei 858",
        "phonename": "HuaweiV858"
    },
    {
        "model": "MTC 950",
        "phonename": "HuaweiV858"
    },
    {
        "model": "MTC Mini",
        "phonename": "HuaweiV858"
    },
    {
        "model": "Vodafone 858",
        "phonename": "HuaweiV858"
    },
    {
        "model": "MediaPad 7 Classic",
        "phonename": "HuaweiVogue7"
    },
    {
        "model": "MediaPad 7 Lite II",
        "phonename": "HuaweiVogue7"
    },
    {
        "model": "MediaPad 7 Vogue",
        "phonename": "HuaweiVogue7"
    },
    {
        "model": "HUAWEI WATCH",
        "phonename": "HuaweiWATCH"
    },
    {
        "model": "HUAWEI-WATCH",
        "phonename": "HuaweiWATCH"
    },
    {
        "model": "LEO-BX9",
        "phonename": "HuaweiWatch 2"
    },
    {
        "model": "LEO-DLXX",
        "phonename": "HuaweiWatch 2"
    },
    {
        "model": "GEM-701L",
        "phonename": "HuaweiX2"
    },
    {
        "model": "GEM-702L",
        "phonename": "HuaweiX2"
    },
    {
        "model": "GEM-703L",
        "phonename": "HuaweiX2"
    },
    {
        "model": "GEM-703LT",
        "phonename": "HuaweiX2"
    },
    {
        "model": "Orinoquia Auyantepui Y210",
        "phonename": "HuaweiY210"
    },
    {
        "model": "Y220-U00",
        "phonename": "HuaweiY220"
    },
    {
        "model": "Y220-U05",
        "phonename": "HuaweiY220"
    },
    {
        "model": "Y220-U17",
        "phonename": "HuaweiY220"
    },
    {
        "model": "HUAWEI Y220-T10",
        "phonename": "HuaweiY220-T10"
    },
    {
        "model": "Y220-U10",
        "phonename": "HuaweiY220-U10"
    },
    {
        "model": "HUAWEI Y 220T",
        "phonename": "HuaweiY220T"
    },
    {
        "model": "HUAWEI Y221-U03",
        "phonename": "HuaweiY221-U03"
    },
    {
        "model": "ORINOQUIA Auyantepui+Y221-U03",
        "phonename": "HuaweiY221-U03"
    },
    {
        "model": "HUAWEI Y221-U12",
        "phonename": "HuaweiY221-U12"
    },
    {
        "model": "HUAWEI Y221-U22",
        "phonename": "HuaweiY221-U22"
    },
    {
        "model": "HUAWEI Y221-U33",
        "phonename": "HuaweiY221-U33"
    },
    {
        "model": "HUAWEI Y221-U43",
        "phonename": "HuaweiY221-U43"
    },
    {
        "model": "HUAWEI Y221-U53",
        "phonename": "HuaweiY221-U53"
    },
    {
        "model": "HUAWEI Ascend Y300",
        "phonename": "HuaweiY300"
    },
    {
        "model": "HUAWEI Y300-0100",
        "phonename": "HuaweiY300"
    },
    {
        "model": "HUAWEI Y300-0151",
        "phonename": "HuaweiY300"
    },
    {
        "model": "Pelephone-Y300-",
        "phonename": "HuaweiY300"
    },
    {
        "model": "HUAWEI Y300-0000",
        "phonename": "HuaweiY300-0000"
    },
    {
        "model": "Huawei Y301A1",
        "phonename": "HuaweiY301A1"
    },
    {
        "model": "Huawei Y301A2",
        "phonename": "HuaweiY301A2"
    },
    {
        "model": "HUAWEI Y310-5000",
        "phonename": "HuaweiY310-5000"
    },
    {
        "model": "HUAWEI Y310-T10",
        "phonename": "HuaweiY310-T10"
    },
    {
        "model": "HUAWEI Y320-C00",
        "phonename": "HuaweiY320"
    },
    {
        "model": "HUAWEI Y320-T00",
        "phonename": "HuaweiY320-T00"
    },
    {
        "model": "HUAWEI Y320-U01",
        "phonename": "HuaweiY320-U01"
    },
    {
        "model": "Y320-U01",
        "phonename": "HuaweiY320-U01"
    },
    {
        "model": "HUAWEI Y320-U10",
        "phonename": "HuaweiY320-U10"
    },
    {
        "model": "HUAWEI Y320-U151",
        "phonename": "HuaweiY320-U151"
    },
    {
        "model": "HUAWEI Y320-U30",
        "phonename": "HuaweiY320-U30"
    },
    {
        "model": "HUAWEI Y320-U351",
        "phonename": "HuaweiY320-U351"
    },
    {
        "model": "HUAWEI Y321-U051",
        "phonename": "HuaweiY321"
    },
    {
        "model": "HUAWEI Y321-C00",
        "phonename": "HuaweiY321"
    },
    {
        "model": "HUAWEI Y325-T00",
        "phonename": "HuaweiY325-T00"
    },
    {
        "model": "Bucare Y330-U05",
        "phonename": "HuaweiY330"
    },
    {
        "model": "HUAWEI Y330-U05",
        "phonename": "HuaweiY330"
    },
    {
        "model": "HUAWEI Y330-U21",
        "phonename": "HuaweiY330"
    },
    {
        "model": "HUAWEI Y330-C00",
        "phonename": "HuaweiY330-C00"
    },
    {
        "model": "HUAWEI Y330-U01",
        "phonename": "HuaweiY330-U01"
    },
    {
        "model": "Luno",
        "phonename": "HuaweiY330-U01"
    },
    {
        "model": "HUAWEI Y330-U07",
        "phonename": "HuaweiY330-U07"
    },
    {
        "model": "HUAWEI Y330-U08",
        "phonename": "HuaweiY330-U08"
    },
    {
        "model": "HUAWEI Y330-U11",
        "phonename": "HuaweiY330-U11"
    },
    {
        "model": "V8510",
        "phonename": "HuaweiY330-U11"
    },
    {
        "model": "HUAWEI Y330-U15",
        "phonename": "HuaweiY330-U15"
    },
    {
        "model": "HUAWEI Y330-U17",
        "phonename": "HuaweiY330-U17"
    },
    {
        "model": "HUAWEI Y336-A1",
        "phonename": "HuaweiY336-A1"
    },
    {
        "model": "HUAWEI Y336-U02",
        "phonename": "HuaweiY336-U02"
    },
    {
        "model": "HUAWEI Y336-U12",
        "phonename": "HuaweiY336-U12"
    },
    {
        "model": "Y340-U081",
        "phonename": "HuaweiY340-U081"
    },
    {
        "model": "HUAWEI Y360-U03",
        "phonename": "HuaweiY360-U03"
    },
    {
        "model": "HUAWEI Y360-U103",
        "phonename": "HuaweiY360-U103"
    },
    {
        "model": "HUAWEI Y360-U12",
        "phonename": "HuaweiY360-U12"
    },
    {
        "model": "HUAWEI Y360-U23",
        "phonename": "HuaweiY360-U23"
    },
    {
        "model": "HUAWEI Y360-U31",
        "phonename": "HuaweiY360-U31"
    },
    {
        "model": "HUAWEI Y360-U42",
        "phonename": "HuaweiY360-U42"
    },
    {
        "model": "HUAWEI Y360-U61",
        "phonename": "HuaweiY360-U61"
    },
    {
        "model": "HUAWEI Y360-U72",
        "phonename": "HuaweiY360-U72"
    },
    {
        "model": "HUAWEI Y360-U82",
        "phonename": "HuaweiY360-U82"
    },
    {
        "model": "Delta Y360-U93",
        "phonename": "HuaweiY360-U93"
    },
    {
        "model": "HUAWEI Y360-U93",
        "phonename": "HuaweiY360-U93"
    },
    {
        "model": "HUAWEI LUA-L01",
        "phonename": "HuaweiY3II"
    },
    {
        "model": "HUAWEI LUA-L02",
        "phonename": "HuaweiY3II"
    },
    {
        "model": "HUAWEI LUA-L21",
        "phonename": "HuaweiY3II"
    },
    {
        "model": "HUAWEI LUA-U02",
        "phonename": "HuaweiY3II"
    },
    {
        "model": "HUAWEI LUA-U22",
        "phonename": "HuaweiY3II"
    },
    {
        "model": "CRO-U00",
        "phonename": "HuaweiY3III"
    },
    {
        "model": "CRO-U23",
        "phonename": "HuaweiY3III"
    },
    {
        "model": "HUAWEI CRO-U00",
        "phonename": "HuaweiY3III"
    },
    {
        "model": "HUAWEI CRO-U23",
        "phonename": "HuaweiY3III"
    },
    {
        "model": "HUAWEI Y560-L02",
        "phonename": "HuaweiY5"
    },
    {
        "model": "HUAWEI Y560-L23",
        "phonename": "HuaweiY5"
    },
    {
        "model": "HUAWEI Y560-U03",
        "phonename": "HuaweiY5"
    },
    {
        "model": "MYA-AL00",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "MYA-L02",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "MYA-L03",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "MYA-L13",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "MYA-L22",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "MYA-L23",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "MYA-TL00",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "MYA-U29",
        "phonename": "HuaweiY5 2017"
    },
    {
        "model": "HUAWEI Y500-T00",
        "phonename": "HuaweiY500-T00"
    },
    {
        "model": "HUAWEI Y511-T00",
        "phonename": "HuaweiY511-T00"
    },
    {
        "model": "Y511-T00",
        "phonename": "HuaweiY511-T00"
    },
    {
        "model": "Y511-U00",
        "phonename": "HuaweiY511-U00"
    },
    {
        "model": "HUAWEI Y511-U10",
        "phonename": "HuaweiY511-U10"
    },
    {
        "model": "HUAWEI Y511-U251",
        "phonename": "HuaweiY511-U251"
    },
    {
        "model": "HUAWEI Y511-U30",
        "phonename": "HuaweiY511-U30"
    },
    {
        "model": "VIETTEL V8506",
        "phonename": "HuaweiY511-U30"
    },
    {
        "model": "HUAWEI Y516-T00",
        "phonename": "HuaweiY516-"
    },
    {
        "model": "HUAWEI Y518-T00",
        "phonename": "HuaweiY518-T00"
    },
    {
        "model": "HUAWEI Y520-U03",
        "phonename": "HuaweiY520-U03"
    },
    {
        "model": "HUAWEI Y520-U12",
        "phonename": "HuaweiY520-U12"
    },
    {
        "model": "HUAWEI Y520-U22",
        "phonename": "HuaweiY520-U22"
    },
    {
        "model": "HUAWEI Y520-U33",
        "phonename": "HuaweiY520-U33"
    },
    {
        "model": "HUAWEI Y523-L076",
        "phonename": "HuaweiY523-L076"
    },
    {
        "model": "HUAWEI Y523-L176",
        "phonename": "HuaweiY523-L176"
    },
    {
        "model": "HUAWEI Y530-U00",
        "phonename": "HuaweiY530"
    },
    {
        "model": "HUAWEI Y530",
        "phonename": "HuaweiY530-U051"
    },
    {
        "model": "HUAWEI Y530-U051",
        "phonename": "HuaweiY530-U051"
    },
    {
        "model": "HUAWEI Y535-C00",
        "phonename": "HuaweiY535"
    },
    {
        "model": "HUAWEI Y535D-C00",
        "phonename": "HuaweiY535D-C00"
    },
    {
        "model": "HUAWEI Y536A1",
        "phonename": "HuaweiY536-A1"
    },
    {
        "model": "HUAWEI Y540-U01",
        "phonename": "HuaweiY540-U01"
    },
    {
        "model": "HUAWEI Y541-U02",
        "phonename": "HuaweiY541-U02"
    },
    {
        "model": "Y541-U02",
        "phonename": "HuaweiY541-U02"
    },
    {
        "model": "Y545-U05",
        "phonename": "HuaweiY545-U05"
    },
    {
        "model": "HUAWEI Y550-L01",
        "phonename": "HuaweiY550-L01"
    },
    {
        "model": "HUAWEI Y550-L02",
        "phonename": "HuaweiY550-L02"
    },
    {
        "model": "Y550-L02",
        "phonename": "HuaweiY550-L02"
    },
    {
        "model": "HUAWEI Y550",
        "phonename": "HuaweiY550-L03"
    },
    {
        "model": "HUAWEI Y550-L03",
        "phonename": "HuaweiY550-L03"
    },
    {
        "model": "Personal Huawei Y550",
        "phonename": "HuaweiY550-L03"
    },
    {
        "model": "Y550-L03",
        "phonename": "HuaweiY550-L03"
    },
    {
        "model": "HUAWEI Y560-CL00",
        "phonename": "HuaweiY560-CL00"
    },
    {
        "model": "HUAWEI Y560-L01",
        "phonename": "HuaweiY560-L01"
    },
    {
        "model": "HUAWEI Y560-L03",
        "phonename": "HuaweiY560-L03"
    },
    {
        "model": "HUAWEI Y560-U02",
        "phonename": "HuaweiY560-U02"
    },
    {
        "model": "HUAWEI Y560-U12",
        "phonename": "HuaweiY560-U12"
    },
    {
        "model": "HUAWEI Y560-U23",
        "phonename": "HuaweiY560-U23"
    },
    {
        "model": "CUN-L22",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-L01",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-L02",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-L03",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-L21",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-L22",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-L23",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-L33",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI CUN-U29",
        "phonename": "HuaweiY5II"
    },
    {
        "model": "HUAWEI SCC-U21",
        "phonename": "HuaweiY6"
    },
    {
        "model": "SCC-U21",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HUAWEI SCL-L01",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HUAWEI SCL-L02",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HUAWEI SCL-L03",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HUAWEI SCL-L04",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HUAWEI SCL-L21",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HW-SCL-L32",
        "phonename": "HuaweiY6"
    },
    {
        "model": "SCL-L01",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HUAWEI SCL-U23",
        "phonename": "HuaweiY6"
    },
    {
        "model": "HUAWEI SCL-U31",
        "phonename": "HuaweiY6"
    },
    {
        "model": "SCL-U23",
        "phonename": "HuaweiY6"
    },
    {
        "model": "MYA-L41",
        "phonename": "HuaweiY6 2017"
    },
    {
        "model": "HUAWEI LYO-L02",
        "phonename": "HuaweiY6 Elite"
    },
    {
        "model": "HUAWEI TIT-AL00",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "HUAWEI TIT-CL10",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "HUAWEI TIT-L01",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "HUAWEI TIT-TL00",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "TIT-AL00",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "TIT-L01",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "HUAWEI TIT-CL00",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "HUAWEI TIT-U02",
        "phonename": "HuaweiY6 Pro"
    },
    {
        "model": "HUAWEI LYO-L01",
        "phonename": "HuaweiY6 Ⅱ Compact"
    },
    {
        "model": "HUAWEI Y600-U00",
        "phonename": "HuaweiY600"
    },
    {
        "model": "HUAWEI Y600-U151",
        "phonename": "HuaweiY600"
    },
    {
        "model": "HUAWEI Y600-U20",
        "phonename": "HuaweiY600"
    },
    {
        "model": "HUAWEI Y600-U351",
        "phonename": "HuaweiY600-U351"
    },
    {
        "model": "HUAWEI Y600-U40",
        "phonename": "HuaweiY600-U40"
    },
    {
        "model": "HUAWEI Y600D-C00",
        "phonename": "HuaweiY600D-C00"
    },
    {
        "model": "HUAWEI Y610-U00",
        "phonename": "HuaweiY610"
    },
    {
        "model": "HUAWEI Y618-T00",
        "phonename": "HuaweiY618"
    },
    {
        "model": "Kavak Y625-U03",
        "phonename": "HuaweiY625-U03"
    },
    {
        "model": "HUAWEI Y625-U13",
        "phonename": "HuaweiY625-U13"
    },
    {
        "model": "HUAWEI Y625-U21",
        "phonename": "HuaweiY625-U21"
    },
    {
        "model": "HUAWEI Y625-U32",
        "phonename": "HuaweiY625-U32"
    },
    {
        "model": "HUAWEI Y625-U43",
        "phonename": "HuaweiY625-U43"
    },
    {
        "model": "HUAWEI Y625-U51",
        "phonename": "HuaweiY625-U51"
    },
    {
        "model": "HUAWEI Y635-CL00",
        "phonename": "HuaweiY635-CL00"
    },
    {
        "model": "Y635-L01",
        "phonename": "HuaweiY635-L01"
    },
    {
        "model": "HUAWEI Y635-L02",
        "phonename": "HuaweiY635-L02"
    },
    {
        "model": "Y635-L02",
        "phonename": "HuaweiY635-L02"
    },
    {
        "model": "HUAWEI Y635-L03",
        "phonename": "HuaweiY635-L03"
    },
    {
        "model": "Y635-L03",
        "phonename": "HuaweiY635-L03"
    },
    {
        "model": "Y635-L21",
        "phonename": "HuaweiY635-L21"
    },
    {
        "model": "HUAWEI Y635-TL00",
        "phonename": "HuaweiY635-TL00"
    },
    {
        "model": "Y635-TL00",
        "phonename": "HuaweiY635-TL00"
    },
    {
        "model": "CAM-L03",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "CAM-L21",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "CAM-L23",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "CAM-U22",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "HUAWEI CAM-L03",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "HUAWEI CAM-L21",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "HUAWEI CAM-L23",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "HUAWEI CAM-U22",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "CAM-L32",
        "phonename": "HuaweiY6II"
    },
    {
        "model": "HUAWEI LYO-L03",
        "phonename": "HuaweiY6ⅡCompact"
    },
    {
        "model": "TRT-L21A",
        "phonename": "HuaweiY7"
    },
    {
        "model": "TRT-L53",
        "phonename": "HuaweiY7"
    },
    {
        "model": "TRT-LX1",
        "phonename": "HuaweiY7"
    },
    {
        "model": "TRT-LX2",
        "phonename": "HuaweiY7"
    },
    {
        "model": "TRT-LX3",
        "phonename": "HuaweiY7"
    },
    {
        "model": "DUB-LX1",
        "phonename": "HuaweiY7 Prime 2019"
    },
    {
        "model": "STK-L22",
        "phonename": "HuaweiY9 Prime 2019"
    },
    {
        "model": "STK-LX3",
        "phonename": "HuaweiY9 Prime 2019"
    },
    {
        "model": "Orinoquia Gran Roraima S7-702u",
        "phonename": "HuaweiYouth"
    },
    {
        "model": "H1623",
        "phonename": "Huaweiascend-5w"
    },
    {
        "model": "d-01G",
        "phonename": "Huaweid-01G"
    },
    {
        "model": "d-01H",
        "phonename": "Huaweid-01H"
    },
    {
        "model": "d-02H",
        "phonename": "Huaweid-02H"
    },
    {
        "model": "eH811",
        "phonename": "HuaweieH811"
    },
    {
        "model": "HRY-LX1",
        "phonename": "Huaweihonor 10 Lite"
    },
    {
        "model": "HRY-LX1MEB",
        "phonename": "Huaweihonor 10 Lite"
    },
    {
        "model": "HRY-LX2",
        "phonename": "Huaweihonor 10 Lite"
    },
    {
        "model": "HRY-AL00",
        "phonename": "Huaweihonor 10 Lite"
    },
    {
        "model": "KIW-L22",
        "phonename": "Huaweihonor 5X"
    },
    {
        "model": "KIW-L23",
        "phonename": "Huaweihonor 5X"
    },
    {
        "model": "KIW-L24",
        "phonename": "Huaweihonor 5X"
    },
    {
        "model": "DLI-L42",
        "phonename": "Huaweihonor 6A Pro"
    },
    {
        "model": "DIG-L21HN",
        "phonename": "Huaweihonor 6C"
    },
    {
        "model": "JMM-L22",
        "phonename": "Huaweihonor 6C Pro"
    },
    {
        "model": "BLN-L21",
        "phonename": "Huaweihonor 6x"
    },
    {
        "model": "BLN-L22",
        "phonename": "Huaweihonor 6x"
    },
    {
        "model": "BKK-L21",
        "phonename": "Huaweihonor 8C"
    },
    {
        "model": "BKK-L22",
        "phonename": "Huaweihonor 8C"
    },
    {
        "model": "BKK-LX2",
        "phonename": "Huaweihonor 8C"
    },
    {
        "model": "HWV31",
        "phonename": "Huaweihuawei nova 2"
    },
    {
        "model": "204HW",
        "phonename": "Huaweihw204HW"
    },
    {
        "model": "HUAWEI M881",
        "phonename": "Huaweim881"
    },
    {
        "model": "HUAWEI CAN-AL10",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAN-L01",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAN-L02",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAN-L03",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAN-L11",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAN-L12",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAN-L13",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAZ-AL00",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAZ-AL10",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAZ-TL10",
        "phonename": "Huaweinova"
    },
    {
        "model": "HUAWEI CAZ-TL20",
        "phonename": "Huaweinova"
    },
    {
        "model": "PIC-AL00",
        "phonename": "Huaweinova 2"
    },
    {
        "model": "PIC-TL00",
        "phonename": "Huaweinova 2"
    },
    {
        "model": "BAC-AL00",
        "phonename": "Huaweinova 2 Plus"
    },
    {
        "model": "BAC-L01",
        "phonename": "Huaweinova 2 Plus"
    },
    {
        "model": "BAC-L03",
        "phonename": "Huaweinova 2 Plus"
    },
    {
        "model": "BAC-L23",
        "phonename": "Huaweinova 2 Plus"
    },
    {
        "model": "BAC-TL00",
        "phonename": "Huaweinova 2 Plus"
    },
    {
        "model": "RNE-L02",
        "phonename": "Huaweinova 2i"
    },
    {
        "model": "HWI-AL00",
        "phonename": "Huaweinova 2s"
    },
    {
        "model": "HWI-TL00",
        "phonename": "Huaweinova 2s"
    },
    {
        "model": "PAR-AL00",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "PAR-L21",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "PAR-L29",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "PAR-LX1",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "PAR-LX1M",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "PAR-LX9",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "PAR-TL00",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "PAR-TL20",
        "phonename": "Huaweinova 3"
    },
    {
        "model": "ANE-AL00",
        "phonename": "Huaweinova 3e"
    },
    {
        "model": "ANE-TL00",
        "phonename": "Huaweinova 3e"
    },
    {
        "model": "INE-AL00",
        "phonename": "Huaweinova 3i"
    },
    {
        "model": "INE-LX1r",
        "phonename": "Huaweinova 3i"
    },
    {
        "model": "INE-TL00",
        "phonename": "Huaweinova 3i"
    },
    {
        "model": "VCE-AL00",
        "phonename": "Huaweinova 4"
    },
    {
        "model": "VCE-TL00",
        "phonename": "Huaweinova 4"
    },
    {
        "model": "MAR-AL00",
        "phonename": "Huaweinova 4e"
    },
    {
        "model": "MAR-TL00",
        "phonename": "Huaweinova 4e"
    },
    {
        "model": "PRA-LX2",
        "phonename": "Huaweinova lite"
    },
    {
        "model": "PRA-LX3",
        "phonename": "Huaweinova lite"
    },
    {
        "model": "HUAWEI MLA-L01",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "HUAWEI MLA-L02",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "HUAWEI MLA-L03",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "HUAWEI MLA-L11",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "HUAWEI MLA-L12",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "HUAWEI MLA-L13",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "MLA-L01",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "MLA-L02",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "MLA-L03",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "MLA-L11",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "MLA-L12",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "MLA-L13",
        "phonename": "Huaweinova plus"
    },
    {
        "model": "WAS-AL00",
        "phonename": "Huaweinova 青春版本"
    },
    {
        "model": "WAS-TL10",
        "phonename": "Huaweinova 青春版本"
    },
    {
        "model": "MediaPad T1 8.0",
        "phonename": "Huaweit1_8p0"
    },
    {
        "model": "S8-701u",
        "phonename": "Huaweit1_8p0"
    },
    {
        "model": "S8-701w",
        "phonename": "Huaweit1_8p0"
    },
    {
        "model": "HUAWEI MediaPad T1 8.0 4G",
        "phonename": "Huaweit1_8p0lte"
    },
    {
        "model": "Honor T1 8.0",
        "phonename": "Huaweit1_8p0lte"
    },
    {
        "model": "MediaPad T1 8.0 Pro",
        "phonename": "Huaweit1_8p0lte"
    },
    {
        "model": "S8-821w",
        "phonename": "Huaweit1_8p0lte"
    },
    {
        "model": "T1-821w",
        "phonename": "Huaweit1_8p0lte"
    },
    {
        "model": "HUAWEI VNS-DL00",
        "phonename": "Huawei华为G9青春版"
    },
    {
        "model": "HUAWEI VNS-TL00",
        "phonename": "Huawei华为G9青春版"
    },
    {
        "model": "BZW-AL00",
        "phonename": "Huawei华为平板 C5"
    },
    {
        "model": "MON-AL19B",
        "phonename": "Huawei华为平板 C5"
    },
    {
        "model": "MON-W19",
        "phonename": "Huawei华为平板 C5"
    },
    {
        "model": "BAH2-AL00",
        "phonename": "Huawei华为平板 M5 青春版"
    },
    {
        "model": "JDN2-AL00",
        "phonename": "Huawei华为平板M5青春版"
    },
    {
        "model": "BZK-L00",
        "phonename": "Huawei华为平板T3 8行业专享版"
    },
    {
        "model": "PLE-701L",
        "phonename": "Huawei华为揽阅M2青春版7.0"
    },
    {
        "model": "DRA-AL00",
        "phonename": "Huawei华为畅享 8e 青春"
    },
    {
        "model": "DRA-TL00",
        "phonename": "Huawei华为畅享 8e 青春"
    },
    {
        "model": "POT-AL00a",
        "phonename": "Huawei华为畅享 9S"
    },
    {
        "model": "POT-TL00a",
        "phonename": "Huawei华为畅享 9S"
    },
    {
        "model": "MRD-AL00",
        "phonename": "Huawei华为畅享 9e"
    },
    {
        "model": "MRD-TL00",
        "phonename": "Huawei华为畅享 9e"
    },
    {
        "model": "ARS-AL00",
        "phonename": "Huawei华为畅享 MAX"
    },
    {
        "model": "ARS-TL00",
        "phonename": "Huawei华为畅享 MAX"
    },
    {
        "model": "STK-TL00",
        "phonename": "Huawei华为畅享10 Plus"
    },
    {
        "model": "NCE-AL00",
        "phonename": "Huawei华为畅享6"
    },
    {
        "model": "NCE-AL10",
        "phonename": "Huawei华为畅享6"
    },
    {
        "model": "NCE-TL10",
        "phonename": "Huawei华为畅享6"
    },
    {
        "model": "DIG-AL00",
        "phonename": "Huawei华为畅享6S"
    },
    {
        "model": "DIG-TL10",
        "phonename": "Huawei华为畅享6S"
    },
    {
        "model": "SLA-AL00",
        "phonename": "Huawei华为畅享7"
    },
    {
        "model": "SLA-TL10",
        "phonename": "Huawei华为畅享7"
    },
    {
        "model": "FIG-AL00",
        "phonename": "Huawei华为畅享7S"
    },
    {
        "model": "FIG-TL00",
        "phonename": "Huawei华为畅享7S"
    },
    {
        "model": "FIG-TL10",
        "phonename": "Huawei华为畅享7S"
    },
    {
        "model": "LDN-AL00",
        "phonename": "Huawei华为畅享8"
    },
    {
        "model": "LDN-AL10",
        "phonename": "Huawei华为畅享8"
    },
    {
        "model": "LDN-AL20",
        "phonename": "Huawei华为畅享8"
    },
    {
        "model": "LDN-TL00",
        "phonename": "Huawei华为畅享8"
    },
    {
        "model": "LDN-TL10",
        "phonename": "Huawei华为畅享8"
    },
    {
        "model": "LDN-TL20",
        "phonename": "Huawei华为畅享8"
    },
    {
        "model": "FLA-AL00",
        "phonename": "Huawei华为畅享8 Plus"
    },
    {
        "model": "FLA-AL10",
        "phonename": "Huawei华为畅享8 Plus"
    },
    {
        "model": "FLA-AL20",
        "phonename": "Huawei华为畅享8 Plus"
    },
    {
        "model": "FLA-TL00",
        "phonename": "Huawei华为畅享8 Plus"
    },
    {
        "model": "FLA-TL10",
        "phonename": "Huawei华为畅享8 Plus"
    },
    {
        "model": "ATU-AL10",
        "phonename": "Huawei华为畅享8e"
    },
    {
        "model": "ATU-TL10",
        "phonename": "Huawei华为畅享8e"
    },
    {
        "model": "DUB-AL00a",
        "phonename": "Huawei华为畅享9"
    },
    {
        "model": "DUB-TL00",
        "phonename": "Huawei华为畅享9"
    },
    {
        "model": "DUB-TL00a",
        "phonename": "Huawei华为畅享9"
    },
    {
        "model": "JKM-AL00",
        "phonename": "Huawei华为畅享9 Plus"
    },
    {
        "model": "JKM-TL00",
        "phonename": "Huawei华为畅享9 Plus"
    },
    {
        "model": "JKM-AL00b",
        "phonename": "Huawei华为畅享9 Plus"
    },
    {
        "model": "JSN-AL00",
        "phonename": "Huawei荣耀 8X"
    },
    {
        "model": "JSN-TL00",
        "phonename": "Huawei荣耀 8X"
    },
    {
        "model": "JMM-AL00",
        "phonename": "Huawei荣耀 V9 play"
    },
    {
        "model": "JMM-AL10",
        "phonename": "Huawei荣耀 V9 play"
    },
    {
        "model": "JMM-TL00",
        "phonename": "Huawei荣耀 V9 play"
    },
    {
        "model": "JMM-TL10",
        "phonename": "Huawei荣耀 V9 play"
    },
    {
        "model": "HRY-TL00",
        "phonename": "Huawei荣耀10青春版"
    },
    {
        "model": "HRY-AL00T",
        "phonename": "Huawei荣耀20i"
    },
    {
        "model": "HRY-TL00T",
        "phonename": "Huawei荣耀20i"
    },
    {
        "model": "SCL-AL00",
        "phonename": "Huawei荣耀4A"
    },
    {
        "model": "KIW-AL10",
        "phonename": "Huawei荣耀5X"
    },
    {
        "model": "KIW-AL20",
        "phonename": "Huawei荣耀5X"
    },
    {
        "model": "KIW-CL00",
        "phonename": "Huawei荣耀5X"
    },
    {
        "model": "KIW-TL00",
        "phonename": "Huawei荣耀5X"
    },
    {
        "model": "KIW-UL00",
        "phonename": "Huawei荣耀5X"
    },
    {
        "model": "ARE-AL00",
        "phonename": "Huawei荣耀8X Max"
    },
    {
        "model": "ARE-TL00",
        "phonename": "Huawei荣耀8X Max"
    },
    {
        "model": "ARE-AL10",
        "phonename": "Huawei荣耀8X Max"
    },
    {
        "model": "PRA-AL00",
        "phonename": "Huawei荣耀8青春版"
    },
    {
        "model": "PRA-AL00X",
        "phonename": "Huawei荣耀8青春版"
    },
    {
        "model": "PRA-TL10",
        "phonename": "Huawei荣耀8青春版"
    },
    {
        "model": "LLD-AL20",
        "phonename": "Huawei荣耀9i"
    },
    {
        "model": "LLD-AL30",
        "phonename": "Huawei荣耀9i"
    },
    {
        "model": "LLD-AL00",
        "phonename": "Huawei荣耀9青春版"
    },
    {
        "model": "LLD-AL10",
        "phonename": "Huawei荣耀9青春版"
    },
    {
        "model": "LLD-TL10",
        "phonename": "Huawei荣耀9青春版"
    },
    {
        "model": "EDI-AL10",
        "phonename": "Huawei荣耀Note8"
    },
    {
        "model": "EDI-DL00",
        "phonename": "Huawei荣耀Note8"
    },
    {
        "model": "HDL-AL09",
        "phonename": "Huawei荣耀Waterplay 8英寸"
    },
    {
        "model": "HDL-W09",
        "phonename": "Huawei荣耀Waterplay 8英寸"
    },
    {
        "model": "AGS2-AL00HN",
        "phonename": "Huawei荣耀平板5"
    },
    {
        "model": "AGS2-W09HN",
        "phonename": "Huawei荣耀平板5"
    },
    {
        "model": "JDN2-AL00HN",
        "phonename": "Huawei荣耀平板5"
    },
    {
        "model": "JDN2-W09HN",
        "phonename": "Huawei荣耀平板5"
    },
    {
        "model": "TRT-AL00",
        "phonename": "Huawei荣耀畅享7 Plus"
    },
    {
        "model": "TRT-AL00A",
        "phonename": "Huawei荣耀畅享7 Plus"
    },
    {
        "model": "TRT-TL10",
        "phonename": "Huawei荣耀畅享7 Plus"
    },
    {
        "model": "TRT-TL10A",
        "phonename": "Huawei荣耀畅享7 Plus"
    },
    {
        "model": "BLN-AL10",
        "phonename": "Huawei荣耀畅玩 6X"
    },
    {
        "model": "BLN-AL20",
        "phonename": "Huawei荣耀畅玩 6X"
    },
    {
        "model": "BLN-AL30",
        "phonename": "Huawei荣耀畅玩 6X"
    },
    {
        "model": "BLN-AL40",
        "phonename": "Huawei荣耀畅玩 6X"
    },
    {
        "model": "BLN-TL00",
        "phonename": "Huawei荣耀畅玩 6X"
    },
    {
        "model": "BLN-TL10",
        "phonename": "Huawei荣耀畅玩 6X"
    },
    {
        "model": "CHM-TL00",
        "phonename": "Huawei荣耀畅玩4C"
    },
    {
        "model": "CHM-TL00H",
        "phonename": "Huawei荣耀畅玩4C"
    },
    {
        "model": "CHM-UL00",
        "phonename": "Huawei荣耀畅玩4C"
    },
    {
        "model": "CHE-TL00",
        "phonename": "Huawei荣耀畅玩4X"
    },
    {
        "model": "CHE-TL00H",
        "phonename": "Huawei荣耀畅玩4X"
    },
    {
        "model": "CAM-CL00",
        "phonename": "Huawei荣耀畅玩5A"
    },
    {
        "model": "CAM-TL00",
        "phonename": "Huawei荣耀畅玩5A"
    },
    {
        "model": "CAM-TL00H",
        "phonename": "Huawei荣耀畅玩5A"
    },
    {
        "model": "CAM-UL00",
        "phonename": "Huawei荣耀畅玩5A"
    },
    {
        "model": "CAM-AL00",
        "phonename": "Huawei荣耀畅玩5A"
    },
    {
        "model": "NEM-AL10",
        "phonename": "Huawei荣耀畅玩5C"
    },
    {
        "model": "NEM-TL00",
        "phonename": "Huawei荣耀畅玩5C"
    },
    {
        "model": "NEM-TL00H",
        "phonename": "Huawei荣耀畅玩5C"
    },
    {
        "model": "NEM-UL10",
        "phonename": "Huawei荣耀畅玩5C"
    },
    {
        "model": "MYA-AL10",
        "phonename": "Huawei荣耀畅玩6"
    },
    {
        "model": "MYA-TL10",
        "phonename": "Huawei荣耀畅玩6"
    },
    {
        "model": "DLI-AL10",
        "phonename": "Huawei荣耀畅玩6A"
    },
    {
        "model": "DUA-AL00",
        "phonename": "Huawei荣耀畅玩7"
    },
    {
        "model": "DUA-TL00",
        "phonename": "Huawei荣耀畅玩7"
    },
    {
        "model": "BND-AL00",
        "phonename": "Huawei荣耀畅玩7X"
    },
    {
        "model": "BND-TL10",
        "phonename": "Huawei荣耀畅玩7X"
    },
    {
        "model": "KSA-AL00",
        "phonename": "Huawei荣耀畅玩8"
    },
    {
        "model": "KSA-TL00",
        "phonename": "Huawei荣耀畅玩8"
    },
    {
        "model": "JAT-AL00",
        "phonename": "Huawei荣耀畅玩8A"
    },
    {
        "model": "JAT-TL00",
        "phonename": "Huawei荣耀畅玩8A"
    },
    {
        "model": "BKK-AL00",
        "phonename": "Huawei荣耀畅玩8C"
    },
    {
        "model": "BKK-AL10",
        "phonename": "Huawei荣耀畅玩8C"
    },
    {
        "model": "BKK-TL00",
        "phonename": "Huawei荣耀畅玩8C"
    },
    {
        "model": "BZA-W00",
        "phonename": "Huawei荣耀畅玩平板2 9.6"
    },
    {
        "model": "POT-AL00",
        "phonename": "Huawei麦芒 8"
    },
    {
        "model": "POT-AL10",
        "phonename": "Huawei麦芒 8"
    },
    {
        "model": "HUAWEI RIO-AL00",
        "phonename": "Huawei麦芒4"
    },
    {
        "model": "HUAWEI MLA-AL00",
        "phonename": "Huawei麦芒5"
    },
    {
        "model": "HUAWEI MLA-AL10",
        "phonename": "Huawei麦芒5"
    },
    {
        "model": "MLA-AL00",
        "phonename": "Huawei麦芒5"
    },
    {
        "model": "MLA-AL10",
        "phonename": "Huawei麦芒5"
    },
    {
        "model": "V2202",
        "phonename": "VivoV25"
    },
    {
        "model": "V2228",
        "phonename": "VivoV25"
    },
    {
        "model": "V2158",
        "phonename": "VivoV25 Pro"
    },
    {
        "model": "V2201",
        "phonename": "VivoV25e"
    },
    {
        "model": "V2209",
        "phonename": "VivoV25e"
    },
    {
        "model": "V2242",
        "phonename": "VivoV25e"
    },
    {
        "model": "V2231",
        "phonename": "VivoV27"
    },
    {
        "model": "V2246",
        "phonename": "VivoV27"
    },
    {
        "model": "V2230",
        "phonename": "VivoV27 Pro"
    },
    {
        "model": "V2237",
        "phonename": "VivoV27e"
    },
    {
        "model": "V2250",
        "phonename": "VivoV29"
    },
    {
        "model": "vivo V3",
        "phonename": "VivoV3"
    },
    {
        "model": "vivo V3Lite",
        "phonename": "VivoV3Lite"
    },
    {
        "model": "vivo PD1524B",
        "phonename": "VivoV3M A"
    },
    {
        "model": "vivo V3Max",
        "phonename": "VivoV3Max"
    },
    {
        "model": "vivo V3Max+ A",
        "phonename": "VivoV3Max + A"
    },
    {
        "model": "vivo PD1523A",
        "phonename": "VivoV3Max A"
    },
    {
        "model": "vivo V5Plus",
        "phonename": "VivoV5Plus"
    },
    {
        "model": "vivo 1851",
        "phonename": "VivoV9 Pro"
    },
    {
        "model": "vivo X5",
        "phonename": "VivoX5"
    },
    {
        "model": "vivo 2004",
        "phonename": "VivoX50"
    },
    {
        "model": "vivo 2006",
        "phonename": "VivoX50 Pro"
    },
    {
        "model": "vivo X5M",
        "phonename": "VivoX5M"
    },
    {
        "model": "vivo X5Max",
        "phonename": "VivoX5Max"
    },
    {
        "model": "vivo X5Max S",
        "phonename": "VivoX5Max S"
    },
    {
        "model": "vivo X5MaxV",
        "phonename": "VivoX5MaxV"
    },
    {
        "model": "vivo X5Pro",
        "phonename": "VivoX5Pro"
    },
    {
        "model": "vivo X5Pro D",
        "phonename": "VivoX5Pro D"
    },
    {
        "model": "vivo X5Pro V",
        "phonename": "VivoX5Pro V"
    },
    {
        "model": "vivo PD1415A",
        "phonename": "VivoX6A"
    },
    {
        "model": "vivo X6D",
        "phonename": "VivoX6D"
    },
    {
        "model": "vivo PD1515A",
        "phonename": "VivoX6Plus A"
    },
    {
        "model": "vivo PD1501D",
        "phonename": "VivoX6Plus D"
    },
    {
        "model": "vivo X6S A",
        "phonename": "VivoX6S A"
    },
    {
        "model": "vivo PD1515BA",
        "phonename": "VivoX6SPlusA"
    },
    {
        "model": "vivo X7",
        "phonename": "VivoX7"
    },
    {
        "model": "vivo X7Plus",
        "phonename": "VivoX7Plus"
    },
    {
        "model": "V2144",
        "phonename": "VivoX80"
    },
    {
        "model": "V2208",
        "phonename": "VivoX80 Lite  5G"
    },
    {
        "model": "V2145",
        "phonename": "VivoX80 Pro"
    },
    {
        "model": "vivo X9",
        "phonename": "VivoX9"
    },
    {
        "model": "V2218",
        "phonename": "VivoX90"
    },
    {
        "model": "V2219",
        "phonename": "VivoX90 Pro"
    },
    {
        "model": "vivo X9i",
        "phonename": "VivoX9i"
    },
    {
        "model": "vivo PD1522A",
        "phonename": "VivoXplay5A"
    },
    {
        "model": "vivo Xplay5A",
        "phonename": "VivoXplay5A"
    },
    {
        "model": "vivo Xplay6",
        "phonename": "VivoXplay6"
    },
    {
        "model": "V2166",
        "phonename": "VivoY01A"
    },
    {
        "model": "V2217",
        "phonename": "VivoY02"
    },
    {
        "model": "V2234_PK",
        "phonename": "VivoY02"
    },
    {
        "model": "V2236",
        "phonename": "VivoY02"
    },
    {
        "model": "V2234",
        "phonename": "VivoY02A"
    },
    {
        "model": "V2203",
        "phonename": "VivoY02s"
    },
    {
        "model": "V2221",
        "phonename": "VivoY02s"
    },
    {
        "model": "V2229",
        "phonename": "VivoY02s"
    },
    {
        "model": "V2252",
        "phonename": "VivoY02t"
    },
    {
        "model": "V2254",
        "phonename": "VivoY02t"
    },
    {
        "model": "V2239",
        "phonename": "VivoY100"
    },
    {
        "model": "V2222",
        "phonename": "VivoY100A"
    },
    {
        "model": "vivo Y15",
        "phonename": "VivoY15"
    },
    {
        "model": "V2212",
        "phonename": "VivoY15C"
    },
    {
        "model": "vivo Y15S",
        "phonename": "VivoY15S"
    },
    {
        "model": "V2204",
        "phonename": "VivoY16"
    },
    {
        "model": "V2214",
        "phonename": "VivoY16"
    },
    {
        "model": "V2305",
        "phonename": "VivoY16"
    },
    {
        "model": "V2310",
        "phonename": "VivoY17s"
    },
    {
        "model": "vivo Y21",
        "phonename": "VivoY21"
    },
    {
        "model": "V2149",
        "phonename": "VivoY21A"
    },
    {
        "model": "vivo Y21L",
        "phonename": "VivoY21L"
    },
    {
        "model": "V2206",
        "phonename": "VivoY22s"
    },
    {
        "model": "V2249",
        "phonename": "VivoY27"
    },
    {
        "model": "vivo Y27",
        "phonename": "VivoY27"
    },
    {
        "model": "V2302",
        "phonename": "VivoY27 5G"
    },
    {
        "model": "V2160",
        "phonename": "VivoY30 5G"
    },
    {
        "model": "vivo Y31",
        "phonename": "VivoY31"
    },
    {
        "model": "vivo Y31L",
        "phonename": "VivoY31L"
    },
    {
        "model": "vivo 1707",
        "phonename": "VivoY31i"
    },
    {
        "model": "vivo Y31i",
        "phonename": "VivoY31i"
    },
    {
        "model": "vivo Y33",
        "phonename": "VivoY33"
    },
    {
        "model": "V2236A",
        "phonename": "VivoY33t"
    },
    {
        "model": "vivo Y35",
        "phonename": "VivoY35"
    },
    {
        "model": "V2205",
        "phonename": "VivoY35"
    },
    {
        "model": "vivo Y35A",
        "phonename": "VivoY35A"
    },
    {
        "model": "V2279A",
        "phonename": "VivoY35m+"
    },
    {
        "model": "V2247",
        "phonename": "VivoY36"
    },
    {
        "model": "V2324",
        "phonename": "VivoY36"
    },
    {
        "model": "V2248",
        "phonename": "VivoY36 5G"
    },
    {
        "model": "vivo Y51",
        "phonename": "VivoY51"
    },
    {
        "model": "vivo Y51A",
        "phonename": "VivoY51A"
    },
    {
        "model": "vivo 1606",
        "phonename": "VivoY53"
    },
    {
        "model": "vivo PD1628",
        "phonename": "VivoY53L"
    },
    {
        "model": "V2230A",
        "phonename": "VivoY53t"
    },
    {
        "model": "vivo 1603",
        "phonename": "VivoY55"
    },
    {
        "model": "vivo Y55",
        "phonename": "VivoY55A"
    },
    {
        "model": "vivo 1610",
        "phonename": "VivoY55s"
    },
    {
        "model": "V2164A",
        "phonename": "VivoY55s"
    },
    {
        "model": "V2225",
        "phonename": "VivoY56 5G"
    },
    {
        "model": "V2311",
        "phonename": "VivoY56 5G"
    },
    {
        "model": "vivo Y66",
        "phonename": "VivoY66"
    },
    {
        "model": "vivo Y67",
        "phonename": "VivoY67"
    },
    {
        "model": "vivo 1801",
        "phonename": "VivoY71"
    },
    {
        "model": "V2278A",
        "phonename": "VivoY78"
    },
    {
        "model": "V2244",
        "phonename": "VivoY78 5G"
    },
    {
        "model": "V2271A",
        "phonename": "VivoY78+"
    },
    {
        "model": "vivo PD1708",
        "phonename": "VivoY79A"
    },
    {
        "model": "vivo Y79A",
        "phonename": "VivoY79A"
    },
    {
        "model": "vivo Y937",
        "phonename": "VivoY937"
    },
    {
        "model": "V1818BA",
        "phonename": "VivoY93标准版 64G"
    },
    {
        "model": "V1818CA",
        "phonename": "VivoY93标准版 64G"
    },
    {
        "model": "vivo Z1",
        "phonename": "VivoZ1"
    },
    {
        "model": "vivo 1951",
        "phonename": "VivoZ1 Pro"
    },
    {
        "model": "V2217A",
        "phonename": "VivoiQOO 10"
    },
    {
        "model": "V2218A",
        "phonename": "VivoiQOO 10 Pro"
    },
    {
        "model": "I2212",
        "phonename": "VivoiQOO 11"
    },
    {
        "model": "V2243A",
        "phonename": "VivoiQOO 11"
    },
    {
        "model": "V2254A",
        "phonename": "VivoiQOO 11 Pro"
    },
    {
        "model": "V2304A",
        "phonename": "VivoiQOO 11S"
    },
    {
        "model": "I2022",
        "phonename": "VivoiQOO 9 Pro"
    },
    {
        "model": "I2019",
        "phonename": "VivoiQOO 9 SE"
    },
    {
        "model": "I2201",
        "phonename": "VivoiQOO 9T"
    },
    {
        "model": "V2154A",
        "phonename": "VivoiQOO Neo5S"
    },
    {
        "model": "V2196A",
        "phonename": "VivoiQOO Neo6"
    },
    {
        "model": "V2199A",
        "phonename": "VivoiQOO Neo6 SE"
    },
    {
        "model": "I2214",
        "phonename": "VivoiQOO Neo7"
    },
    {
        "model": "V2231A",
        "phonename": "VivoiQOO Neo7"
    },
    {
        "model": "I2217",
        "phonename": "VivoiQOO Neo7 Pro"
    },
    {
        "model": "V2238A",
        "phonename": "VivoiQOO Neo7 SE"
    },
    {
        "model": "V2232A",
        "phonename": "VivoiQOO Neo7 竞速版"
    },
    {
        "model": "V2301A",
        "phonename": "VivoiQOO Neo8"
    },
    {
        "model": "V2302A",
        "phonename": "VivoiQOO Neo8 Pro"
    },
    {
        "model": "iPA2375",
        "phonename": "VivoiQOO Pad"
    },
    {
        "model": "I2018",
        "phonename": "VivoiQOO Z5"
    },
    {
        "model": "V2188A",
        "phonename": "VivoiQOO Z5 6000mAh"
    },
    {
        "model": "I2203",
        "phonename": "VivoiQOO Z6"
    },
    {
        "model": "I2206",
        "phonename": "VivoiQOO Z6"
    },
    {
        "model": "I2208",
        "phonename": "VivoiQOO Z6 Lite 5G"
    },
    {
        "model": "I2126",
        "phonename": "VivoiQOO Z6 Pro"
    },
    {
        "model": "V2164KA",
        "phonename": "VivoiQOO Z6x"
    },
    {
        "model": "V2270A",
        "phonename": "VivoiQOO Z7"
    },
    {
        "model": "I2207",
        "phonename": "VivoiQOO Z7 5G"
    },
    {
        "model": "I2213",
        "phonename": "VivoiQOO Z7 5G"
    },
    {
        "model": "I2301",
        "phonename": "VivoiQOO Z7 Pro 5G"
    },
    {
        "model": "V2230EA",
        "phonename": "VivoiQOO Z7i"
    },
    {
        "model": "I2223",
        "phonename": "VivoiQOO Z7s 5G"
    },
    {
        "model": "V2272A",
        "phonename": "VivoiQOO Z7x (m)"
    },
    {
        "model": "I2216",
        "phonename": "VivoiQOO Z7x 5G"
    },
    {
        "model": "V2312A",
        "phonename": "VivoiQOO Z8x"
    },
    {
        "model": "vivo X21i A",
        "phonename": "Vivovivo  X21i  A"
    },
    {
        "model": "vivo Y75s",
        "phonename": "Vivovivo  Y75s"
    },
    {
        "model": "vivo Y85A",
        "phonename": "Vivovivo  Y85A"
    },
    {
        "model": "vivo 1611",
        "phonename": "Vivovivo 1611"
    },
    {
        "model": "vivo 1714",
        "phonename": "Vivovivo 1714"
    },
    {
        "model": "vivo 1716",
        "phonename": "Vivovivo 1716"
    },
    {
        "model": "vivo 1718",
        "phonename": "Vivovivo 1718"
    },
    {
        "model": "vivo 1720",
        "phonename": "Vivovivo 1720"
    },
    {
        "model": "vivo 1721",
        "phonename": "Vivovivo 1721"
    },
    {
        "model": "vivo 1723",
        "phonename": "Vivovivo 1723"
    },
    {
        "model": "vivo 1724",
        "phonename": "Vivovivo 1724"
    },
    {
        "model": "vivo 1725",
        "phonename": "Vivovivo 1725"
    },
    {
        "model": "vivo 1726",
        "phonename": "Vivovivo 1726"
    },
    {
        "model": "vivo 1727",
        "phonename": "Vivovivo 1727"
    },
    {
        "model": "vivo 1802",
        "phonename": "Vivovivo 1802"
    },
    {
        "model": "vivo 1803",
        "phonename": "Vivovivo 1803"
    },
    {
        "model": "vivo 1804",
        "phonename": "Vivovivo 1804"
    },
    {
        "model": "vivo 1805",
        "phonename": "Vivovivo 1805"
    },
    {
        "model": "vivo 1806",
        "phonename": "Vivovivo 1806"
    },
    {
        "model": "vivo 1807",
        "phonename": "Vivovivo 1807"
    },
    {
        "model": "vivo 1808",
        "phonename": "Vivovivo 1808"
    },
    {
        "model": "vivo 1811",
        "phonename": "Vivovivo 1811"
    },
    {
        "model": "vivo 1812",
        "phonename": "Vivovivo 1812"
    },
    {
        "model": "vivo 1813",
        "phonename": "Vivovivo 1813"
    },
    {
        "model": "vivo 1814",
        "phonename": "Vivovivo 1814"
    },
    {
        "model": "vivo 1815",
        "phonename": "Vivovivo 1815"
    },
    {
        "model": "vivo 1816",
        "phonename": "Vivovivo 1816"
    },
    {
        "model": "vivo 1817",
        "phonename": "Vivovivo 1817"
    },
    {
        "model": "vivo 1818",
        "phonename": "Vivovivo 1818"
    },
    {
        "model": "V1832A",
        "phonename": "Vivovivo 1818"
    },
    {
        "model": "vivo 1819",
        "phonename": "Vivovivo 1819"
    },
    {
        "model": "vivo 1820",
        "phonename": "Vivovivo 1820"
    },
    {
        "model": "vivo 1901",
        "phonename": "Vivovivo 1901"
    },
    {
        "model": "vivo 1904",
        "phonename": "Vivovivo 1904"
    },
    {
        "model": "vivo 1906",
        "phonename": "Vivovivo 1906"
    },
    {
        "model": "vivo 2007",
        "phonename": "Vivovivo 1906"
    },
    {
        "model": "vivo 1907",
        "phonename": "Vivovivo 1907"
    },
    {
        "model": "vivo 1909",
        "phonename": "Vivovivo 1909"
    },
    {
        "model": "vivo 1910",
        "phonename": "Vivovivo 1910"
    },
    {
        "model": "vivo 1912",
        "phonename": "Vivovivo 1912"
    },
    {
        "model": "vivo 1913",
        "phonename": "Vivovivo 1913"
    },
    {
        "model": "vivo 1914",
        "phonename": "Vivovivo 1914"
    },
    {
        "model": "vivo 1915",
        "phonename": "Vivovivo 1915"
    },
    {
        "model": "vivo 1916",
        "phonename": "Vivovivo 1916"
    },
    {
        "model": "vivo 1917",
        "phonename": "Vivovivo 1917"
    },
    {
        "model": "vivo 1919",
        "phonename": "Vivovivo 1919"
    },
    {
        "model": "vivo 1920",
        "phonename": "Vivovivo 1920"
    },
    {
        "model": "vivo 1921",
        "phonename": "Vivovivo 1921"
    },
    {
        "model": "vivo 1929",
        "phonename": "Vivovivo 1929"
    },
    {
        "model": "vivo 1933",
        "phonename": "Vivovivo 1933"
    },
    {
        "model": "vivo 1935",
        "phonename": "Vivovivo 1935"
    },
    {
        "model": "vivo 1937",
        "phonename": "Vivovivo 1937"
    },
    {
        "model": "vivo 1938",
        "phonename": "Vivovivo 1938"
    },
    {
        "model": "vivo 1940",
        "phonename": "Vivovivo 1940"
    },
    {
        "model": "vivo 2005",
        "phonename": "Vivovivo 2005"
    },
    {
        "model": "vivo 1902",
        "phonename": "Vivovivo 2010"
    },
    {
        "model": "vivo 2010",
        "phonename": "Vivovivo 2010"
    },
    {
        "model": "vivo 2015",
        "phonename": "Vivovivo 2015"
    },
    {
        "model": "vivo 2015_21",
        "phonename": "Vivovivo 2015_21"
    },
    {
        "model": "vivo 2018",
        "phonename": "Vivovivo 2018"
    },
    {
        "model": "vivo 2019",
        "phonename": "Vivovivo 2019"
    },
    {
        "model": "vivo NEX A",
        "phonename": "Vivovivo NEX A"
    },
    {
        "model": "vivo NEX S",
        "phonename": "Vivovivo NEX S"
    },
    {
        "model": "PA2353",
        "phonename": "Vivovivo Pad Air"
    },
    {
        "model": "PA2373",
        "phonename": "Vivovivo Pad2"
    },
    {
        "model": "V1831A",
        "phonename": "Vivovivo S1"
    },
    {
        "model": "V2207A",
        "phonename": "Vivovivo S15 Pro"
    },
    {
        "model": "V2244A",
        "phonename": "Vivovivo S16"
    },
    {
        "model": "V2245A",
        "phonename": "Vivovivo S16 Pro"
    },
    {
        "model": "V2239A",
        "phonename": "Vivovivo S16e"
    },
    {
        "model": "V2285A",
        "phonename": "Vivovivo S17e"
    },
    {
        "model": "V2199GA",
        "phonename": "Vivovivo T2"
    },
    {
        "model": "V2256A",
        "phonename": "Vivovivo X Flip"
    },
    {
        "model": "V2178A",
        "phonename": "Vivovivo X Fold"
    },
    {
        "model": "V2229A",
        "phonename": "Vivovivo X Fold+"
    },
    {
        "model": "V2266A",
        "phonename": "Vivovivo X Fold2"
    },
    {
        "model": "V2170A",
        "phonename": "Vivovivo X Note"
    },
    {
        "model": "vivo PD1709",
        "phonename": "Vivovivo X20"
    },
    {
        "model": "vivo X20A",
        "phonename": "Vivovivo X20"
    },
    {
        "model": "vivo PD1710",
        "phonename": "Vivovivo X20Plus"
    },
    {
        "model": "vivo X20Plus A",
        "phonename": "Vivovivo X20Plus"
    },
    {
        "model": "vivo PD1721",
        "phonename": "Vivovivo X20Plus UD"
    },
    {
        "model": "vivo X20Plus UD",
        "phonename": "Vivovivo X20Plus UD"
    },
    {
        "model": "vivo X21A",
        "phonename": "Vivovivo X21A"
    },
    {
        "model": "vivo X21UD A",
        "phonename": "Vivovivo X21UD A"
    },
    {
        "model": "V2114",
        "phonename": "Vivovivo X70 Pro+"
    },
    {
        "model": "V2183A",
        "phonename": "Vivovivo X80"
    },
    {
        "model": "V2185A",
        "phonename": "Vivovivo X80 Pro"
    },
    {
        "model": "V2186A",
        "phonename": "Vivovivo X80 Pro 天玑9000版"
    },
    {
        "model": "V2241A",
        "phonename": "Vivovivo X90"
    },
    {
        "model": "V2242A",
        "phonename": "Vivovivo X90 Pro"
    },
    {
        "model": "V2227A",
        "phonename": "Vivovivo X90 Pro+"
    },
    {
        "model": "V2241HA",
        "phonename": "Vivovivo X90s"
    },
    {
        "model": "vivo X9Plus",
        "phonename": "Vivovivo X9Plus"
    },
    {
        "model": "vivo PD1616B",
        "phonename": "Vivovivo X9s"
    },
    {
        "model": "vivo X9s",
        "phonename": "Vivovivo X9s"
    },
    {
        "model": "vivo PD1635",
        "phonename": "Vivovivo X9s Plus"
    },
    {
        "model": "vivo X9s Plus",
        "phonename": "Vivovivo X9s Plus"
    },
    {
        "model": "vivo Y11",
        "phonename": "Vivovivo Y11"
    },
    {
        "model": "V2207",
        "phonename": "Vivovivo Y22"
    },
    {
        "model": "V2238",
        "phonename": "Vivovivo Y22"
    },
    {
        "model": "vivo Y22",
        "phonename": "Vivovivo Y22"
    },
    {
        "model": "vivo Y28",
        "phonename": "Vivovivo Y28"
    },
    {
        "model": "vivo 1719",
        "phonename": "Vivovivo Y65"
    },
    {
        "model": "vivo Y66i A",
        "phonename": "Vivovivo Y66i A"
    },
    {
        "model": "vivo Y69A",
        "phonename": "Vivovivo Y69A"
    },
    {
        "model": "vivo Y71A",
        "phonename": "Vivovivo Y71A"
    },
    {
        "model": "vivo Y75A",
        "phonename": "Vivovivo Y75A"
    },
    {
        "model": "V2069BA",
        "phonename": "Vivovivo Y75s"
    },
    {
        "model": "V2219A",
        "phonename": "Vivovivo Y77"
    },
    {
        "model": "vivo Y83A",
        "phonename": "Vivovivo Y83A"
    },
    {
        "model": "vivo Y89",
        "phonename": "Vivovivo Z1i"
    },
    {
        "model": "vivo Z1i",
        "phonename": "Vivovivo Z1i"
    },
    {
        "model": "vivo Z3x",
        "phonename": "Vivovivo Z3x"
    },
    {
        "model": "vivo Y37",
        "phonename": "VivoV1Max"
    },
    {
        "model": "V2283A",
        "phonename": "VivoS17"
    },
    {
        "model": "V2284A",
        "phonename": "VivoS17 Pro"
    },
    {
        "model": "V2153",
        "phonename": "VivoT1"
    },
    {
        "model": "V2154",
        "phonename": "VivoT1"
    },
    {
        "model": "V2168",
        "phonename": "VivoT1"
    },
    {
        "model": "V2150",
        "phonename": "VivoT1 5G"
    },
    {
        "model": "V2151",
        "phonename": "VivoT1 Pro 5G"
    },
    {
        "model": "V2143",
        "phonename": "VivoT1x"
    },
    {
        "model": "V2320",
        "phonename": "VivoT2"
    },
    {
        "model": "V2240",
        "phonename": "VivoT2 5G"
    },
    {
        "model": "V2253",
        "phonename": "VivoT2x 5G"
    },
    {
        "model": "V2312",
        "phonename": "VivoT2x 5G"
    },
    {
        "model": "V2180GA",
        "phonename": "VivoU5x"
    },
    {
        "model": "vivo V1",
        "phonename": "VivoV1"
    },
    {
        "model": "R8107",
        "phonename": "OppoR5"
    },
    {
        "model": "R8109",
        "phonename": "OppoR5"
    },
    {
        "model": "R6006",
        "phonename": "OppoR6006"
    },
    {
        "model": "R6007",
        "phonename": "OppoR6007"
    },
    {
        "model": "OPPO R7",
        "phonename": "OppoR7"
    },
    {
        "model": "R7",
        "phonename": "OppoR7"
    },
    {
        "model": "R7Plus",
        "phonename": "OppoR7 Plus"
    },
    {
        "model": "R7Plusm",
        "phonename": "OppoR7 Plusm"
    },
    {
        "model": "R7005",
        "phonename": "OppoR7005"
    },
    {
        "model": "R7007",
        "phonename": "OppoR7007"
    },
    {
        "model": "R7plusf",
        "phonename": "OppoR7Plusf"
    },
    {
        "model": "R7Plust",
        "phonename": "OppoR7Plust"
    },
    {
        "model": "R7c",
        "phonename": "OppoR7c"
    },
    {
        "model": "R7f",
        "phonename": "OppoR7f"
    },
    {
        "model": "R7g",
        "phonename": "OppoR7g"
    },
    {
        "model": "R7kc",
        "phonename": "OppoR7kc"
    },
    {
        "model": "R7kf",
        "phonename": "OppoR7kf"
    },
    {
        "model": "R7kt",
        "phonename": "OppoR7kt"
    },
    {
        "model": "OPPO R7s",
        "phonename": "OppoR7s"
    },
    {
        "model": "R7s",
        "phonename": "OppoR7s"
    },
    {
        "model": "OPPO R7sPlus",
        "phonename": "OppoR7s Plus"
    },
    {
        "model": "R7sf",
        "phonename": "OppoR7sfg"
    },
    {
        "model": "R7sm",
        "phonename": "OppoR7sm"
    },
    {
        "model": "R7st",
        "phonename": "OppoR7st"
    },
    {
        "model": "R7t",
        "phonename": "OppoR7t"
    },
    {
        "model": "R8000",
        "phonename": "OppoR8000"
    },
    {
        "model": "R8001",
        "phonename": "OppoR8001"
    },
    {
        "model": "R8006",
        "phonename": "OppoR8006"
    },
    {
        "model": "R8007",
        "phonename": "OppoR8007"
    },
    {
        "model": "R809T",
        "phonename": "OppoR809T"
    },
    {
        "model": "R8106",
        "phonename": "OppoR8106"
    },
    {
        "model": "R815",
        "phonename": "OppoR815"
    },
    {
        "model": "R815T",
        "phonename": "OppoR815T"
    },
    {
        "model": "R815W",
        "phonename": "OppoR815W"
    },
    {
        "model": "R819",
        "phonename": "OppoR819"
    },
    {
        "model": "R819T",
        "phonename": "OppoR819T"
    },
    {
        "model": "R820",
        "phonename": "OppoR820"
    },
    {
        "model": "R8200",
        "phonename": "OppoR8200"
    },
    {
        "model": "R8201",
        "phonename": "OppoR8201"
    },
    {
        "model": "R8205",
        "phonename": "OppoR8205"
    },
    {
        "model": "R8206",
        "phonename": "OppoR8206"
    },
    {
        "model": "R8207",
        "phonename": "OppoR8207"
    },
    {
        "model": "R821",
        "phonename": "OppoR821"
    },
    {
        "model": "R821T",
        "phonename": "OppoR821T"
    },
    {
        "model": "R823T",
        "phonename": "OppoR823T"
    },
    {
        "model": "R827",
        "phonename": "OppoR827"
    },
    {
        "model": "R827T",
        "phonename": "OppoR827T"
    },
    {
        "model": "R829",
        "phonename": "OppoR829"
    },
    {
        "model": "R829T",
        "phonename": "OppoR829T"
    },
    {
        "model": "R830",
        "phonename": "OppoR830"
    },
    {
        "model": "R830S",
        "phonename": "OppoR830S"
    },
    {
        "model": "R831",
        "phonename": "OppoR831"
    },
    {
        "model": "R831K",
        "phonename": "OppoR831K"
    },
    {
        "model": "R831L",
        "phonename": "OppoR831L"
    },
    {
        "model": "R831S",
        "phonename": "OppoR831S"
    },
    {
        "model": "R831T",
        "phonename": "OppoR831T"
    },
    {
        "model": "R833T",
        "phonename": "OppoR833T"
    },
    {
        "model": "R850",
        "phonename": "OppoR850"
    },
    {
        "model": "OPPO R9",
        "phonename": "OppoR9"
    },
    {
        "model": "OPPO R9 Plus A",
        "phonename": "OppoR9 Plus A"
    },
    {
        "model": "OPPO R9 Plusm A",
        "phonename": "OppoR9PlusmA"
    },
    {
        "model": "OPPO R9 Plust A",
        "phonename": "OppoR9PlustA"
    },
    {
        "model": "OPPO R9 Plustm A",
        "phonename": "OppoR9PlustmA"
    },
    {
        "model": "OPPO R9k",
        "phonename": "OppoR9k"
    },
    {
        "model": "OPPO R9km",
        "phonename": "OppoR9km"
    },
    {
        "model": "OPPO R9m",
        "phonename": "OppoR9m"
    },
    {
        "model": "CPH1607",
        "phonename": "OppoR9s"
    },
    {
        "model": "CPH1607fw",
        "phonename": "OppoR9s"
    },
    {
        "model": "OPPO R9s",
        "phonename": "OppoR9s"
    },
    {
        "model": "CPH1611",
        "phonename": "OppoR9s Plus"
    },
    {
        "model": "OPPO R9s Plus",
        "phonename": "OppoR9s Plus"
    },
    {
        "model": "OPPO R9s Plust",
        "phonename": "OppoR9s Plus"
    },
    {
        "model": "OPPO R9sPlus",
        "phonename": "OppoR9s Plus"
    },
    {
        "model": "OPPO R9sk",
        "phonename": "OppoR9sk"
    },
    {
        "model": "OPPO R9skt",
        "phonename": "OppoR9sk"
    },
    {
        "model": "OPPO R9st",
        "phonename": "OppoR9st"
    },
    {
        "model": "OPPO R9t",
        "phonename": "OppoR9t"
    },
    {
        "model": "OPPO R9tm",
        "phonename": "OppoR9tm"
    },
    {
        "model": "CPH1917",
        "phonename": "OppoReno"
    },
    {
        "model": "CPH1919RU",
        "phonename": "OppoReno 10x Zoom"
    },
    {
        "model": "CPH1919",
        "phonename": "OppoReno 10x Zoom"
    },
    {
        "model": "CPH1921",
        "phonename": "OppoReno 10x room"
    },
    {
        "model": "PCCM00",
        "phonename": "OppoReno 10倍变焦版"
    },
    {
        "model": "PCCT00",
        "phonename": "OppoReno 10倍变焦版"
    },
    {
        "model": "PCKM00",
        "phonename": "OppoReno 2 中国版"
    },
    {
        "model": "CPH2065",
        "phonename": "OppoReno 4Z 5G"
    },
    {
        "model": "CPH1983",
        "phonename": "OppoReno A"
    },
    {
        "model": "PCLM10",
        "phonename": "OppoReno Ace"
    },
    {
        "model": "PDHM00",
        "phonename": "OppoReno Ace2"
    },
    {
        "model": "PCDM10",
        "phonename": "OppoReno Z 中国版"
    },
    {
        "model": "PCDT10",
        "phonename": "OppoReno Z 中国版"
    },
    {
        "model": "PCAT00",
        "phonename": "OppoReno 标准版"
    },
    {
        "model": "CPH2531",
        "phonename": "OppoReno10 5G"
    },
    {
        "model": "A302OP",
        "phonename": "OppoReno10 Pro 5G"
    },
    {
        "model": "CPH2525",
        "phonename": "OppoReno10 Pro 5G"
    },
    {
        "model": "CPH2541",
        "phonename": "OppoReno10 Pro 5G"
    },
    {
        "model": "CPH2521",
        "phonename": "OppoReno10 Pro+ 5G"
    },
    {
        "model": "CPH1945",
        "phonename": "OppoReno2 Z"
    },
    {
        "model": "CPH1951",
        "phonename": "OppoReno2 Z"
    },
    {
        "model": "PCKM80",
        "phonename": "OppoReno2 Z 中国版"
    },
    {
        "model": "CPH2043",
        "phonename": "OppoReno3"
    },
    {
        "model": "A001OP",
        "phonename": "OppoReno3 5G"
    },
    {
        "model": "PDCM00",
        "phonename": "OppoReno3 5G 中国版"
    },
    {
        "model": "A002OP",
        "phonename": "OppoReno3 A"
    },
    {
        "model": "CPH2013",
        "phonename": "OppoReno3 A"
    },
    {
        "model": "CPH2035",
        "phonename": "OppoReno3 Pro"
    },
    {
        "model": "CPH2036",
        "phonename": "OppoReno3 Pro"
    },
    {
        "model": "CPH2037",
        "phonename": "OppoReno3 Pro"
    },
    {
        "model": "PCRM00",
        "phonename": "OppoReno3 Pro 5G中国版"
    },
    {
        "model": "PCLM50",
        "phonename": "OppoReno3 元气版 5G"
    },
    {
        "model": "CPH2091",
        "phonename": "OppoReno4 5G"
    },
    {
        "model": "CPH2209",
        "phonename": "OppoReno4 F"
    },
    {
        "model": "CPH2125",
        "phonename": "OppoReno4 Lite"
    },
    {
        "model": "PDNT00",
        "phonename": "OppoReno4 Pro"
    },
    {
        "model": "CPH2089",
        "phonename": "OppoReno4 Pro 5G"
    },
    {
        "model": "PDNM00",
        "phonename": "OppoReno4 Pro 中国版"
    },
    {
        "model": "PDPM00",
        "phonename": "OppoReno4 中国版"
    },
    {
        "model": "PDPT00",
        "phonename": "OppoReno4 中国版"
    },
    {
        "model": "A103OP",
        "phonename": "OppoReno5 A (eSIM)"
    },
    {
        "model": "CPH2217",
        "phonename": "OppoReno5 F"
    },
    {
        "model": "CPH2205",
        "phonename": "OppoReno5 Lite"
    },
    {
        "model": "CPH2505",
        "phonename": "OppoReno8 T 5G"
    },
    {
        "model": "A301OP",
        "phonename": "OppoReno9 A"
    },
    {
        "model": "CPH2523",
        "phonename": "OppoReno9 A"
    },
    {
        "model": "U3",
        "phonename": "OppoU3"
    },
    {
        "model": "U707",
        "phonename": "OppoU707"
    },
    {
        "model": "U707T",
        "phonename": "OppoU707T"
    },
    {
        "model": "U708",
        "phonename": "OppoU708"
    },
    {
        "model": "U705W",
        "phonename": "OppoUlike2"
    },
    {
        "model": "U705T",
        "phonename": "OppoUlike2"
    },
    {
        "model": "X9000",
        "phonename": "OppoX9000"
    },
    {
        "model": "X9006",
        "phonename": "OppoX9006"
    },
    {
        "model": "X9007",
        "phonename": "OppoX9007"
    },
    {
        "model": "X9009",
        "phonename": "OppoX9009"
    },
    {
        "model": "X9009fw",
        "phonename": "OppoX9009fw"
    },
    {
        "model": "X9070",
        "phonename": "OppoX9070"
    },
    {
        "model": "X9076",
        "phonename": "OppoX9076"
    },
    {
        "model": "X9077",
        "phonename": "OppoX9077"
    },
    {
        "model": "X9079",
        "phonename": "OppoX9079"
    },
    {
        "model": "CPH1859",
        "phonename": "Opporealme 1"
    },
    {
        "model": "CPH1861",
        "phonename": "Opporealme 1"
    },
    {
        "model": "RMX1805",
        "phonename": "Opporealme 2"
    },
    {
        "model": "RMX1809",
        "phonename": "Opporealme 2"
    },
    {
        "model": "RMX1803",
        "phonename": "Opporealme 2 Pro"
    },
    {
        "model": "RMX1807",
        "phonename": "Opporealme 2 Pro"
    },
    {
        "model": "RMX1821",
        "phonename": "Opporealme 3"
    },
    {
        "model": "RMX1822",
        "phonename": "Opporealme 3"
    },
    {
        "model": "RMX1825",
        "phonename": "Opporealme 3"
    },
    {
        "model": "RMX1853",
        "phonename": "Opporealme 3Pro"
    },
    {
        "model": "RMX1827",
        "phonename": "Opporealme 3i"
    },
    {
        "model": "RMX1911",
        "phonename": "Opporealme 5"
    },
    {
        "model": "RMX1811",
        "phonename": "Opporealme C1"
    },
    {
        "model": "RMX1941",
        "phonename": "Opporealme C2"
    },
    {
        "model": "RMX1942",
        "phonename": "Opporealme C2"
    },
    {
        "model": "RMX1943",
        "phonename": "Opporealme C2"
    },
    {
        "model": "RMX1945",
        "phonename": "Opporealme C2"
    },
    {
        "model": "RMX1831",
        "phonename": "Opporealme U1"
    },
    {
        "model": "RMX1833",
        "phonename": "Opporealme U1"
    },
    {
        "model": "RMX1901",
        "phonename": "Opporealme X"
    },
    {
        "model": "RMX1851",
        "phonename": "Opporealme X Lite"
    },
    {
        "model": "RMX2051",
        "phonename": "Opporealme X50 5G"
    },
    {
        "model": "OPPO R11",
        "phonename": "OppoR11"
    },
    {
        "model": "OPPO R11t",
        "phonename": "OppoR11"
    },
    {
        "model": "OPPO R11 Plus",
        "phonename": "OppoR11 Plus"
    },
    {
        "model": "OPPO R11 Plusk",
        "phonename": "OppoR11 Plusk"
    },
    {
        "model": "OPPO R11 Pluskt",
        "phonename": "OppoR11 Pluskt"
    },
    {
        "model": "OPPO R11 Plust",
        "phonename": "OppoR11 Plust"
    },
    {
        "model": "OPPO R11s",
        "phonename": "OppoR11s"
    },
    {
        "model": "OPPO R11s Plus",
        "phonename": "OppoR11sPlus"
    },
    {
        "model": "OPPO R11s Plust",
        "phonename": "OppoR11sPlust"
    },
    {
        "model": "OPPO R11st",
        "phonename": "OppoR11st"
    },
    {
        "model": "CPH1835",
        "phonename": "OppoR15"
    },
    {
        "model": "CPH1831",
        "phonename": "OppoR15 Pro"
    },
    {
        "model": "CPH1833",
        "phonename": "OppoR15 Pro"
    },
    {
        "model": "PACM00",
        "phonename": "OppoR15 中国版"
    },
    {
        "model": "PAAT00",
        "phonename": "OppoR15 梦境版"
    },
    {
        "model": "PBCM10",
        "phonename": "OppoR15x"
    },
    {
        "model": "PBCT10",
        "phonename": "OppoR15x"
    },
    {
        "model": "PBEM00",
        "phonename": "OppoR17"
    },
    {
        "model": "PBET00",
        "phonename": "OppoR17"
    },
    {
        "model": "PBDM00",
        "phonename": "OppoR17 Pro"
    },
    {
        "model": "PBDT00",
        "phonename": "OppoR17 Pro"
    },
    {
        "model": "CPH2137",
        "phonename": "OppoOPPO A33"
    },
    {
        "model": "PECM30",
        "phonename": "OppoOPPO A53 5G"
    },
    {
        "model": "CPH2321",
        "phonename": "OppoOPPO A53s 5G"
    },
    {
        "model": "PEZM00",
        "phonename": "OppoOPPO A54"
    },
    {
        "model": "CPH2197",
        "phonename": "OppoOPPO A74 5G"
    },
    {
        "model": "CPH2341",
        "phonename": "OppoOPPO F21 Pro 5G"
    },
    {
        "model": "OPD2101",
        "phonename": "OppoOPPO Pad"
    },
    {
        "model": "OPD2201",
        "phonename": "OppoOPPO Pad 2"
    },
    {
        "model": "OPD2202",
        "phonename": "OppoOPPO Pad 2"
    },
    {
        "model": "OPD2102",
        "phonename": "OppoOPPO Pad Air"
    },
    {
        "model": "PHW110",
        "phonename": "OppoOPPO Reno10 5G"
    },
    {
        "model": "PHU110",
        "phonename": "OppoOPPO Reno10 Pro+ 5G"
    },
    {
        "model": "A101OP",
        "phonename": "OppoOPPO Reno5 A"
    },
    {
        "model": "CPH2199",
        "phonename": "OppoOPPO Reno5 A"
    },
    {
        "model": "CPH2237",
        "phonename": "OppoOPPO Reno6 Z 5G"
    },
    {
        "model": "CPH2371",
        "phonename": "OppoOPPO Reno7 5G/Find X5 Lite"
    },
    {
        "model": "A201OP",
        "phonename": "OppoOPPO Reno7 A"
    },
    {
        "model": "CPH2353",
        "phonename": "OppoOPPO Reno7 A"
    },
    {
        "model": "OPG04",
        "phonename": "OppoOPPO Reno7 A"
    },
    {
        "model": "CPH2343",
        "phonename": "OppoOPPO Reno7 Z 5G/F21 Pro 5G/Reno8 Lite 5G"
    },
    {
        "model": "CPH2359",
        "phonename": "OppoOPPO Reno8 5G"
    },
    {
        "model": "CPH2357",
        "phonename": "OppoOPPO Reno8 Pro 5G"
    },
    {
        "model": "PGX110",
        "phonename": "OppoOPPO Reno9 Pro 5G"
    },
    {
        "model": "OPPO Watch",
        "phonename": "OppoOPPO Watch"
    },
    {
        "model": "CPH1913",
        "phonename": "OppoF11"
    },
    {
        "model": "CPH1915",
        "phonename": "OppoF11"
    },
    {
        "model": "CPH1969",
        "phonename": "OppoF11 Pro"
    },
    {
        "model": "CPH1987",
        "phonename": "OppoF11 Pro"
    },
    {
        "model": "CPH2119",
        "phonename": "OppoF17 Pro"
    },
    {
        "model": "CPH2285",
        "phonename": "OppoF19 Pro"
    },
    {
        "model": "F1fw",
        "phonename": "OppoF1fw"
    },
    {
        "model": "F1f",
        "phonename": "OppoF1w"
    },
    {
        "model": "F1w",
        "phonename": "OppoF1w"
    },
    {
        "model": "CPH1819",
        "phonename": "OppoF7"
    },
    {
        "model": "CPH1821",
        "phonename": "OppoF7"
    },
    {
        "model": "CPH1823",
        "phonename": "OppoF9"
    },
    {
        "model": "CPH1825",
        "phonename": "OppoF9"
    },
    {
        "model": "CPH1881",
        "phonename": "OppoF9"
    },
    {
        "model": "PEUM00",
        "phonename": "OppoFind N"
    },
    {
        "model": "CPH2437",
        "phonename": "OppoFind N2 Flip"
    },
    {
        "model": "PGT110",
        "phonename": "OppoFind N2 Flip 中国版"
    },
    {
        "model": "CPH1871",
        "phonename": "OppoFind X"
    },
    {
        "model": "CPH1875",
        "phonename": "OppoFind X"
    },
    {
        "model": "PAFM00",
        "phonename": "OppoFind X"
    },
    {
        "model": "PAFT00",
        "phonename": "OppoFind X"
    },
    {
        "model": "PAHM00",
        "phonename": "OppoFind X 兰博基尼"
    },
    {
        "model": "CPH2023",
        "phonename": "OppoFind X2"
    },
    {
        "model": "CPH2005",
        "phonename": "OppoFind X2 Lite"
    },
    {
        "model": "CPH2009",
        "phonename": "OppoFind X2 Neo/Reno3 Pro"
    },
    {
        "model": "CPH2025",
        "phonename": "OppoFind X2 Pro"
    },
    {
        "model": "OPG01",
        "phonename": "OppoFind X2 Pro"
    },
    {
        "model": "PDEM30",
        "phonename": "OppoFind X2 Pro 中国版"
    },
    {
        "model": "PDEM10",
        "phonename": "OppoFind X2 中国版"
    },
    {
        "model": "PDET10",
        "phonename": "OppoFind X2 中国版"
    },
    {
        "model": "CPH2173",
        "phonename": "OppoFind X3 Pro"
    },
    {
        "model": "OPG03",
        "phonename": "OppoFind X3 Pro"
    },
    {
        "model": "CPH2307",
        "phonename": "OppoFind X5"
    },
    {
        "model": "CPH2305",
        "phonename": "OppoFind X5 Pro"
    },
    {
        "model": "PGFM10",
        "phonename": "OppoFind X6"
    },
    {
        "model": "PGEM10",
        "phonename": "OppoFind X6 Pro"
    },
    {
        "model": "X909",
        "phonename": "OppoFind5"
    },
    {
        "model": "X909T",
        "phonename": "OppoFind5"
    },
    {
        "model": "PBCM30",
        "phonename": "OppoK1"
    },
    {
        "model": "PCGM00",
        "phonename": "OppoK3"
    },
    {
        "model": "PCGT00",
        "phonename": "OppoK3"
    },
    {
        "model": "CPH1955",
        "phonename": "OppoK3"
    },
    {
        "model": "PCNM00",
        "phonename": "OppoK5"
    },
    {
        "model": "N1",
        "phonename": "OppoN1"
    },
    {
        "model": "N5111",
        "phonename": "OppoN1 mimi"
    },
    {
        "model": "N5116",
        "phonename": "OppoN1 mimi"
    },
    {
        "model": "N1T",
        "phonename": "OppoN1T"
    },
    {
        "model": "N1W",
        "phonename": "OppoN1W"
    },
    {
        "model": "N5206",
        "phonename": "OppoN3"
    },
    {
        "model": "N5207",
        "phonename": "OppoN3"
    },
    {
        "model": "N5209",
        "phonename": "OppoN3"
    },
    {
        "model": "N5110",
        "phonename": "OppoN5110"
    },
    {
        "model": "N5117",
        "phonename": "OppoN5117"
    },
    {
        "model": "PHQ110",
        "phonename": "OppoA1 Pro 5G"
    },
    {
        "model": "A11",
        "phonename": "OppoA11"
    },
    {
        "model": "PCHM10",
        "phonename": "OppoA11 中国版"
    },
    {
        "model": "PCHT10",
        "phonename": "OppoA11 中国版"
    },
    {
        "model": "A11f",
        "phonename": "OppoA11f"
    },
    {
        "model": "A11t",
        "phonename": "OppoA11t"
    },
    {
        "model": "A11w",
        "phonename": "OppoA11w"
    },
    {
        "model": "PCHM30",
        "phonename": "OppoA11x 中国版"
    },
    {
        "model": "PCHT30",
        "phonename": "OppoA11x 中国版"
    },
    {
        "model": "A31t",
        "phonename": "OppoA13t"
    },
    {
        "model": "A1601",
        "phonename": "OppoA1601"
    },
    {
        "model": "A1601fw",
        "phonename": "OppoA1601fw"
    },
    {
        "model": "A1603",
        "phonename": "OppoA1603"
    },
    {
        "model": "CPH2477",
        "phonename": "OppoA17"
    },
    {
        "model": "CPH2471",
        "phonename": "OppoA17k"
    },
    {
        "model": "CPH1923",
        "phonename": "OppoA1k"
    },
    {
        "model": "CPH1837",
        "phonename": "OppoA3"
    },
    {
        "model": "A31",
        "phonename": "OppoA31"
    },
    {
        "model": "A31c",
        "phonename": "OppoA31c"
    },
    {
        "model": "A31u",
        "phonename": "OppoA31u"
    },
    {
        "model": "PDVM00",
        "phonename": "OppoA32 中国版"
    },
    {
        "model": "A33",
        "phonename": "OppoA33"
    },
    {
        "model": "A33f",
        "phonename": "OppoA33f"
    },
    {
        "model": "A33fw",
        "phonename": "OppoA33f"
    },
    {
        "model": "OPPO A33m",
        "phonename": "OppoA33m"
    },
    {
        "model": "A33t",
        "phonename": "OppoA33t"
    },
    {
        "model": "A33w",
        "phonename": "OppoA33w"
    },
    {
        "model": "OPPO A35",
        "phonename": "OppoA35"
    },
    {
        "model": "OPPO A37",
        "phonename": "OppoA37"
    },
    {
        "model": "A37f",
        "phonename": "OppoA37f"
    },
    {
        "model": "A37fw",
        "phonename": "OppoA37fw"
    },
    {
        "model": "OPPO A37m",
        "phonename": "OppoA37m"
    },
    {
        "model": "OPPO A37t",
        "phonename": "OppoA37t"
    },
    {
        "model": "OPPO A37tm",
        "phonename": "OppoA37tm"
    },
    {
        "model": "OPPO A39",
        "phonename": "OppoA39"
    },
    {
        "model": "OPPO A39m",
        "phonename": "OppoA39m"
    },
    {
        "model": "OPPO A39t",
        "phonename": "OppoA39t"
    },
    {
        "model": "OPPO A39tm",
        "phonename": "OppoA39tm"
    },
    {
        "model": "CPH1803",
        "phonename": "OppoA3s"
    },
    {
        "model": "CPH1853",
        "phonename": "OppoA3s"
    },
    {
        "model": "PADT00",
        "phonename": "OppoA3中国版"
    },
    {
        "model": "CPH1809",
        "phonename": "OppoA5"
    },
    {
        "model": "PBAM00",
        "phonename": "OppoA5"
    },
    {
        "model": "PBBT30",
        "phonename": "OppoA5"
    },
    {
        "model": "CPH1931",
        "phonename": "OppoA5 2020"
    },
    {
        "model": "CPH1933",
        "phonename": "OppoA5 2020"
    },
    {
        "model": "CPH1943",
        "phonename": "OppoA5 2020"
    },
    {
        "model": "A51",
        "phonename": "OppoA51"
    },
    {
        "model": "Lava A51",
        "phonename": "OppoA51"
    },
    {
        "model": "A51f",
        "phonename": "OppoA51f"
    },
    {
        "model": "A51kc",
        "phonename": "OppoA51kc"
    },
    {
        "model": "A51w",
        "phonename": "OppoA51w"
    },
    {
        "model": "CPH2069",
        "phonename": "OppoA52"
    },
    {
        "model": "PDAM10",
        "phonename": "OppoA52 中国版"
    },
    {
        "model": "OPPO A53",
        "phonename": "OppoA53"
    },
    {
        "model": "CPH2127",
        "phonename": "OppoA53"
    },
    {
        "model": "CPH2131",
        "phonename": "OppoA53"
    },
    {
        "model": "CPH2133",
        "phonename": "OppoA53"
    },
    {
        "model": "CPH2139",
        "phonename": "OppoA53"
    },
    {
        "model": "PECM20",
        "phonename": "OppoA53 5G"
    },
    {
        "model": "A53f",
        "phonename": "OppoA53f"
    },
    {
        "model": "A53fw",
        "phonename": "OppoA53fw"
    },
    {
        "model": "OPPO A53m",
        "phonename": "OppoA53m"
    },
    {
        "model": "CPH2135",
        "phonename": "OppoA53s"
    },
    {
        "model": "A53w",
        "phonename": "OppoA53w"
    },
    {
        "model": "CPH2303",
        "phonename": "OppoA54 5G"
    },
    {
        "model": "PEMM00",
        "phonename": "OppoA55 5G"
    },
    {
        "model": "PEMT00",
        "phonename": "OppoA55 5G"
    },
    {
        "model": "PEMT20",
        "phonename": "OppoA55 5G"
    },
    {
        "model": "A102OP",
        "phonename": "OppoA55s 5G"
    },
    {
        "model": "OPPO A57",
        "phonename": "OppoA57"
    },
    {
        "model": "CPH2387",
        "phonename": "OppoA57"
    },
    {
        "model": "CPH2407",
        "phonename": "OppoA57"
    },
    {
        "model": "CPH2385",
        "phonename": "OppoA57s/A77"
    },
    {
        "model": "CPH2577",
        "phonename": "OppoA58"
    },
    {
        "model": "OPPO A59",
        "phonename": "OppoA59"
    },
    {
        "model": "OPPO A59s",
        "phonename": "OppoA59"
    },
    {
        "model": "OPPO A59st",
        "phonename": "OppoA59st"
    },
    {
        "model": "OPPO A59t",
        "phonename": "OppoA59t"
    },
    {
        "model": "OPPO A59tm",
        "phonename": "OppoA59tm"
    },
    {
        "model": "CPH1905",
        "phonename": "OppoA7"
    },
    {
        "model": "PBFM00",
        "phonename": "OppoA7"
    },
    {
        "model": "PBFT00",
        "phonename": "OppoA7"
    },
    {
        "model": "CPH2067",
        "phonename": "OppoA72"
    },
    {
        "model": "OPPO A73",
        "phonename": "OppoA73"
    },
    {
        "model": "OPPO A73t",
        "phonename": "OppoA73t"
    },
    {
        "model": "OPPO A77",
        "phonename": "OppoA77"
    },
    {
        "model": "OPPO A77t",
        "phonename": "OppoA77"
    },
    {
        "model": "CPH2339",
        "phonename": "OppoA77 5G"
    },
    {
        "model": "CPH2483",
        "phonename": "OppoA78 5G"
    },
    {
        "model": "CPH2495",
        "phonename": "OppoA78 5G"
    },
    {
        "model": "OPPO A79",
        "phonename": "OppoA79"
    },
    {
        "model": "OPPO A79k",
        "phonename": "OppoA79k"
    },
    {
        "model": "OPPO A79kt",
        "phonename": "OppoA79kt"
    },
    {
        "model": "OPPO A79t",
        "phonename": "OppoA79t"
    },
    {
        "model": "OPPO A83",
        "phonename": "OppoA83"
    },
    {
        "model": "OPPO A83t",
        "phonename": "OppoA83t"
    },
    {
        "model": "CPH1941",
        "phonename": "OppoA9 2020"
    },
    {
        "model": "PCAT10",
        "phonename": "OppoA9 中国版"
    },
    {
        "model": "PCPM00",
        "phonename": "OppoA91"
    },
    {
        "model": "CPH2059",
        "phonename": "OppoA92"
    },
    {
        "model": "CPH2121",
        "phonename": "OppoA93"
    },
    {
        "model": "CPH2123",
        "phonename": "OppoA93"
    },
    {
        "model": "CPH2203",
        "phonename": "OppoA94"
    },
    {
        "model": "PFUM10",
        "phonename": "OppoA96 5G"
    },
    {
        "model": "CPH2529",
        "phonename": "OppoA98 5G"
    },
    {
        "model": "PCEM00",
        "phonename": "OppoA9x"
    },
    {
        "model": "PCET00",
        "phonename": "OppoA9x"
    },
    {
        "model": "CPH1920",
        "phonename": "OppoAX5s"
    },
    {
        "model": "POCOPHONE F1",
        "phonename": "XiaomiPOCO F1"
    },
    {
        "model": "2207117BPG",
        "phonename": "XiaomiPOCO M5s"
    },
    {
        "model": "2013023",
        "phonename": "XiaomiRedmi"
    },
    {
        "model": "Redmi Note 6 Pro",
        "phonename": "XiaomiRedmi  Note  6  Pro"
    },
    {
        "model": "Redmi Note 7 Pro",
        "phonename": "XiaomiRedmi  Note  7 Pro"
    },
    {
        "model": "Redmi 3",
        "phonename": "XiaomiRedmi 3"
    },
    {
        "model": "ido",
        "phonename": "XiaomiRedmi 3"
    },
    {
        "model": "Redmi 3S",
        "phonename": "XiaomiRedmi 3S"
    },
    {
        "model": "Redmi 4",
        "phonename": "XiaomiRedmi 4 Pro"
    },
    {
        "model": "Redmi 4A",
        "phonename": "XiaomiRedmi 4A"
    },
    {
        "model": "Redmi 4X",
        "phonename": "XiaomiRedmi 4X"
    },
    {
        "model": "santoni",
        "phonename": "XiaomiRedmi 4X"
    },
    {
        "model": "Redmi 5",
        "phonename": "XiaomiRedmi 5"
    },
    {
        "model": "Redmi 5 Plus",
        "phonename": "XiaomiRedmi 5 Plus"
    },
    {
        "model": "Redmi 5A",
        "phonename": "XiaomiRedmi 5A"
    },
    {
        "model": "Redmi 6",
        "phonename": "XiaomiRedmi 6"
    },
    {
        "model": "Redmi 6A",
        "phonename": "XiaomiRedmi 6A"
    },
    {
        "model": "Redmi 6 Pro",
        "phonename": "XiaomiRedmi 6Pro"
    },
    {
        "model": "ONC",
        "phonename": "XiaomiRedmi 7"
    },
    {
        "model": "Redmi 7",
        "phonename": "XiaomiRedmi 7"
    },
    {
        "model": "Redmi 7A",
        "phonename": "XiaomiRedmi 7A"
    },
    {
        "model": "Redmi 8",
        "phonename": "XiaomiRedmi 8"
    },
    {
        "model": "Redmi Go",
        "phonename": "XiaomiRedmi Go"
    },
    {
        "model": "Redmi K30 Pro Zoom Edition",
        "phonename": "XiaomiRedmi K30 Pro Zoom Edition"
    },
    {
        "model": "Redmi Note 3",
        "phonename": "XiaomiRedmi Note 3"
    },
    {
        "model": "Redmi Note 4X",
        "phonename": "XiaomiRedmi Note 4"
    },
    {
        "model": "Redmi Note 4",
        "phonename": "XiaomiRedmi Note 4"
    },
    {
        "model": "Redmi Note 5",
        "phonename": "XiaomiRedmi Note 5"
    },
    {
        "model": "Redmi Note 5 Pro",
        "phonename": "XiaomiRedmi Note 5 Pro"
    },
    {
        "model": "Redmi Y1",
        "phonename": "XiaomiRedmi Note 5A"
    },
    {
        "model": "Redmi Note 5A",
        "phonename": "XiaomiRedmi Note 5A"
    },
    {
        "model": "Redmi Note 8",
        "phonename": "XiaomiRedmi Note 8"
    },
    {
        "model": "Redmi Pro",
        "phonename": "XiaomiRedmi Pro"
    },
    {
        "model": "Redmi S2",
        "phonename": "XiaomiRedmi S2"
    },
    {
        "model": "MIBOX3",
        "phonename": "XiaomiTELEBEE"
    },
    {
        "model": "2109119DG",
        "phonename": "XiaomiXiaomi 11 Lite 5G NE"
    },
    {
        "model": "2109119DI",
        "phonename": "XiaomiXiaomi 11 Lite NE"
    },
    {
        "model": "21081111RG",
        "phonename": "XiaomiXiaomi 11T"
    },
    {
        "model": "2107113SG",
        "phonename": "XiaomiXiaomi 11T Pro"
    },
    {
        "model": "2107113SI",
        "phonename": "XiaomiXiaomi 11T Pro"
    },
    {
        "model": "2107113SR",
        "phonename": "XiaomiXiaomi 11T Pro"
    },
    {
        "model": "21091116I",
        "phonename": "XiaomiXiaomi 11i"
    },
    {
        "model": "21091116UI",
        "phonename": "XiaomiXiaomi 11i HyperCharge"
    },
    {
        "model": "2201123C",
        "phonename": "XiaomiXiaomi 12"
    },
    {
        "model": "2201123G",
        "phonename": "XiaomiXiaomi 12"
    },
    {
        "model": "2203129G",
        "phonename": "XiaomiXiaomi 12 Lite"
    },
    {
        "model": "2201122C",
        "phonename": "XiaomiXiaomi 12 Pro"
    },
    {
        "model": "2201122G",
        "phonename": "XiaomiXiaomi 12 Pro"
    },
    {
        "model": "2207122MC",
        "phonename": "XiaomiXiaomi 12 Pro Dimensity"
    },
    {
        "model": "2206123SC",
        "phonename": "XiaomiXiaomi 12S"
    },
    {
        "model": "2206122SC",
        "phonename": "XiaomiXiaomi 12S Pro"
    },
    {
        "model": "2203121C",
        "phonename": "XiaomiXiaomi 12S Ultra"
    },
    {
        "model": "22071212AG",
        "phonename": "XiaomiXiaomi 12T"
    },
    {
        "model": "22081212C",
        "phonename": "XiaomiXiaomi 12T Pro"
    },
    {
        "model": "22081212R",
        "phonename": "XiaomiXiaomi 12T Pro"
    },
    {
        "model": "22081212UG",
        "phonename": "XiaomiXiaomi 12T Pro"
    },
    {
        "model": "22200414R",
        "phonename": "XiaomiXiaomi 12T Pro"
    },
    {
        "model": "A201XM",
        "phonename": "XiaomiXiaomi 12T Pro"
    },
    {
        "model": "2112123AC",
        "phonename": "XiaomiXiaomi 12X"
    },
    {
        "model": "2211133C",
        "phonename": "XiaomiXiaomi 13"
    },
    {
        "model": "2211133G",
        "phonename": "XiaomiXiaomi 13"
    },
    {
        "model": "2210129SG",
        "phonename": "XiaomiXiaomi 13 Lite"
    },
    {
        "model": "2210132G",
        "phonename": "XiaomiXiaomi 13 Pro"
    },
    {
        "model": "2304FPN6DC",
        "phonename": "XiaomiXiaomi 13 Ultra"
    },
    {
        "model": "2304FPN6DG",
        "phonename": "XiaomiXiaomi 13 Ultra"
    },
    {
        "model": "2210132C",
        "phonename": "XiaomiXiaomi 13 pro"
    },
    {
        "model": "2109119BC",
        "phonename": "XiaomiXiaomi Civi"
    },
    {
        "model": "M2011J18C",
        "phonename": "XiaomiXiaomi MIX Fold"
    },
    {
        "model": "22061218C",
        "phonename": "XiaomiXiaomi MIX Fold 2"
    },
    {
        "model": "2308CPXD0C",
        "phonename": "XiaomiXiaomi MIX Fold 3"
    },
    {
        "model": "21051182C",
        "phonename": "XiaomiXiaomi Pad 5"
    },
    {
        "model": "21051182G",
        "phonename": "XiaomiXiaomi Pad 5"
    },
    {
        "model": "22081281AC",
        "phonename": "XiaomiXiaomi Pad 5 Pro"
    },
    {
        "model": "M2105K81AC",
        "phonename": "XiaomiXiaomi Pad 5 Pro"
    },
    {
        "model": "M2105K81C",
        "phonename": "XiaomiXiaomi Pad 5 Pro 5G"
    },
    {
        "model": "23043RP34C",
        "phonename": "XiaomiXiaomi Pad 6"
    },
    {
        "model": "23043RP34G",
        "phonename": "XiaomiXiaomi Pad 6"
    },
    {
        "model": "23043RP34I",
        "phonename": "XiaomiXiaomi Pad 6"
    },
    {
        "model": "2307BRPDCC",
        "phonename": "XiaomiXiaomi Pad 6 Max 14"
    },
    {
        "model": "HM 1AC",
        "phonename": "XiaomiHM 1SC"
    },
    {
        "model": "HM 1S",
        "phonename": "XiaomiHM 1SC"
    },
    {
        "model": "HM 1SC",
        "phonename": "XiaomiHM 1SC"
    },
    {
        "model": "HM 1SW",
        "phonename": "XiaomiHM 1SC"
    },
    {
        "model": "2014501",
        "phonename": "XiaomiHM 1SLTETD"
    },
    {
        "model": "2014011",
        "phonename": "XiaomiHM 1STD"
    },
    {
        "model": "2014502",
        "phonename": "XiaomiHM 2A"
    },
    {
        "model": "HM 2A",
        "phonename": "XiaomiHM 2A"
    },
    {
        "model": "2014819",
        "phonename": "XiaomiHM 2LTE-BR"
    },
    {
        "model": "2014813",
        "phonename": "XiaomiHM 2LTE-CMCC"
    },
    {
        "model": "2014812",
        "phonename": "XiaomiHM 2LTE-CT"
    },
    {
        "model": "2014811",
        "phonename": "XiaomiHM 2LTE-CU"
    },
    {
        "model": "2014818",
        "phonename": "XiaomiHM 2LTE-IN"
    },
    {
        "model": "2014817",
        "phonename": "XiaomiHM 2LTE-SA"
    },
    {
        "model": "HM NOTE 1LTE",
        "phonename": "XiaomiHM NOTE 1LTETD"
    },
    {
        "model": "HM NOTE 1LTETD",
        "phonename": "XiaomiHM NOTE 1LTETD"
    },
    {
        "model": "HM NOTE 1LTEW",
        "phonename": "XiaomiHM NOTE 1LTETD"
    },
    {
        "model": "HM NOTE 1S",
        "phonename": "XiaomiHM NOTE 1S CT"
    },
    {
        "model": "gucci",
        "phonename": "XiaomiHM NOTE 1S CT"
    },
    {
        "model": "HM NOTE 1TD",
        "phonename": "XiaomiHM NOTE 1TD"
    },
    {
        "model": "HM NOTE 1W",
        "phonename": "XiaomiHM NOTE 1W"
    },
    {
        "model": "Redmi Note 2",
        "phonename": "XiaomiHM Note 2"
    },
    {
        "model": "2013022",
        "phonename": "XiaomiHong Mi"
    },
    {
        "model": "Redmi K30 Pro 5G Zoom Edition",
        "phonename": "XiaomiK30 PRO"
    },
    {
        "model": "Redmi K30 Pro 5G",
        "phonename": "XiaomiK30 pro"
    },
    {
        "model": "MI 8 Explorer Edition",
        "phonename": "XiaomiMI  8  Explorer  Edition"
    },
    {
        "model": "lotus",
        "phonename": "XiaomiMI  PLAY"
    },
    {
        "model": "MI 2",
        "phonename": "XiaomiMI 2"
    },
    {
        "model": "MI 2S",
        "phonename": "XiaomiMI 2"
    },
    {
        "model": "MI 2A",
        "phonename": "XiaomiMI 2A"
    },
    {
        "model": "MI 3W",
        "phonename": "XiaomiMI 3W"
    },
    {
        "model": "MI 4C",
        "phonename": "XiaomiMI 4LTE"
    },
    {
        "model": "MI 4W",
        "phonename": "XiaomiMI 4LTE"
    },
    {
        "model": "MI 4LTE",
        "phonename": "XiaomiMI 4LTE-CT"
    },
    {
        "model": "MI 4S",
        "phonename": "XiaomiMI 4s"
    },
    {
        "model": "MI 5C",
        "phonename": "XiaomiMI 5C"
    },
    {
        "model": "Meri",
        "phonename": "XiaomiMI 5C"
    },
    {
        "model": "MI 5X",
        "phonename": "XiaomiMI 5X"
    },
    {
        "model": "MI 5s Plus",
        "phonename": "XiaomiMI 5s Plus"
    },
    {
        "model": "MI 6X",
        "phonename": "XiaomiMI 6X"
    },
    {
        "model": "MI 8",
        "phonename": "XiaomiMI 8"
    },
    {
        "model": "MI 8 Lite",
        "phonename": "XiaomiMI 8 Lite"
    },
    {
        "model": "Platina",
        "phonename": "XiaomiMI 8 Lite"
    },
    {
        "model": "MI 8 SE",
        "phonename": "XiaomiMI 8 SE"
    },
    {
        "model": "sirius",
        "phonename": "XiaomiMI 8 SE"
    },
    {
        "model": "MI 8 Pro",
        "phonename": "XiaomiMI 8 UD"
    },
    {
        "model": "MI 8 UD",
        "phonename": "XiaomiMI 8 UD"
    },
    {
        "model": "equuleus",
        "phonename": "XiaomiMI 8 UD"
    },
    {
        "model": "MI 9",
        "phonename": "XiaomiMI 9"
    },
    {
        "model": "Mi 9 SE",
        "phonename": "XiaomiMI 9 SE"
    },
    {
        "model": "MI CC 9",
        "phonename": "XiaomiMI CC 9"
    },
    {
        "model": "Mi 9 Lite",
        "phonename": "XiaomiMI CC 9"
    },
    {
        "model": "Pyxis",
        "phonename": "XiaomiMI CC 9"
    },
    {
        "model": "MI CC 9e",
        "phonename": "XiaomiMI CC 9e"
    },
    {
        "model": "laurus",
        "phonename": "XiaomiMI CC 9e"
    },
    {
        "model": "MI CC9 Pro",
        "phonename": "XiaomiMI CC9 Pro"
    },
    {
        "model": "Mi Note 10",
        "phonename": "XiaomiMI CC9 Pro"
    },
    {
        "model": "MI MAX",
        "phonename": "XiaomiMI MAX"
    },
    {
        "model": "MI MAX 2",
        "phonename": "XiaomiMI MAX 2"
    },
    {
        "model": "MI MAX 3",
        "phonename": "XiaomiMI MAX 3"
    },
    {
        "model": "MI NOTE LTE",
        "phonename": "XiaomiMI NOTE LTE"
    },
    {
        "model": "MI NOTE Pro",
        "phonename": "XiaomiMI NOTE Pro"
    },
    {
        "model": "Mi Note 3",
        "phonename": "XiaomiMI Note 3"
    },
    {
        "model": "MI PAD",
        "phonename": "XiaomiMI PAD"
    },
    {
        "model": "MI PAD 3",
        "phonename": "XiaomiMI PAD 3"
    },
    {
        "model": "MI PAD 4",
        "phonename": "XiaomiMI PAD 4"
    },
    {
        "model": "MI PLAY",
        "phonename": "XiaomiMI PLAY"
    },
    {
        "model": "MI 6",
        "phonename": "XiaomiMI6"
    },
    {
        "model": "MiBOX_PRO",
        "phonename": "XiaomiMIBOXPRO"
    },
    {
        "model": "MI PAD 2",
        "phonename": "XiaomiMIPAD2"
    },
    {
        "model": "MiTV3S",
        "phonename": "XiaomiMITV3S"
    },
    {
        "model": "MiTV4",
        "phonename": "XiaomiMITV3S-55/60"
    },
    {
        "model": "MIX",
        "phonename": "XiaomiMIX"
    },
    {
        "model": "lithium",
        "phonename": "XiaomiMIX"
    },
    {
        "model": "MIX 2",
        "phonename": "XiaomiMIX 2"
    },
    {
        "model": "Mi MIX 2",
        "phonename": "XiaomiMIX 2"
    },
    {
        "model": "MIX 2S",
        "phonename": "XiaomiMIX 2S"
    },
    {
        "model": "Mi MIX 2S",
        "phonename": "XiaomiMIX 2S"
    },
    {
        "model": "MIX 3",
        "phonename": "XiaomiMIX 3"
    },
    {
        "model": "Mi MIX 3",
        "phonename": "XiaomiMIX 3"
    },
    {
        "model": "2106118C",
        "phonename": "XiaomiMIX 4"
    },
    {
        "model": "Mi 10",
        "phonename": "XiaomiMi 10"
    },
    {
        "model": "Umi",
        "phonename": "XiaomiMi 10"
    },
    {
        "model": "XIG01",
        "phonename": "XiaomiMi 10 Lite 5G"
    },
    {
        "model": "M2002J9E",
        "phonename": "XiaomiMi 10 Lite zoom"
    },
    {
        "model": "Cmi",
        "phonename": "XiaomiMi 10 Pro"
    },
    {
        "model": "Mi 10 Pro",
        "phonename": "XiaomiMi 10 Pro"
    },
    {
        "model": "M2007J1SC",
        "phonename": "XiaomiMi 10 Ultra"
    },
    {
        "model": "M2002J9G",
        "phonename": "XiaomiMi 10 lite 5G"
    },
    {
        "model": "M2002J9S",
        "phonename": "XiaomiMi 10 lite 5G"
    },
    {
        "model": "M2102J2SC",
        "phonename": "XiaomiMi 10S"
    },
    {
        "model": "Thyme",
        "phonename": "XiaomiMi 10S"
    },
    {
        "model": "M2007J3SP",
        "phonename": "XiaomiMi 10T"
    },
    {
        "model": "M2007J3SY",
        "phonename": "XiaomiMi 10T"
    },
    {
        "model": "M2007J17G",
        "phonename": "XiaomiMi 10T Lite"
    },
    {
        "model": "M2007J3SG",
        "phonename": "XiaomiMi 10T Pro"
    },
    {
        "model": "M2007J3SI",
        "phonename": "XiaomiMi 10T pro"
    },
    {
        "model": "M2007J17I",
        "phonename": "XiaomiMi 10i"
    },
    {
        "model": "M2011K2C",
        "phonename": "XiaomiMi 11"
    },
    {
        "model": "M2011K2G",
        "phonename": "XiaomiMi 11"
    },
    {
        "model": "2107119DC",
        "phonename": "XiaomiMi 11 LE"
    },
    {
        "model": "M2101K9AG",
        "phonename": "XiaomiMi 11 Lite"
    },
    {
        "model": "M2101K9AI",
        "phonename": "XiaomiMi 11 Lite"
    },
    {
        "model": "M2101K9C",
        "phonename": "XiaomiMi 11 Lite 5G"
    },
    {
        "model": "M2101K9G",
        "phonename": "XiaomiMi 11 Lite 5G"
    },
    {
        "model": "M2102K1C",
        "phonename": "XiaomiMi 11 Ultra"
    },
    {
        "model": "M2102K1G",
        "phonename": "XiaomiMi 11 Ultra"
    },
    {
        "model": "M2012K11I",
        "phonename": "XiaomiMi 11X Pro"
    },
    {
        "model": "M2012K11G",
        "phonename": "XiaomiMi 11i"
    },
    {
        "model": "MI 3",
        "phonename": "XiaomiMi 3"
    },
    {
        "model": "Mi-4c",
        "phonename": "XiaomiMi 4c"
    },
    {
        "model": "Mi 4i",
        "phonename": "XiaomiMi 4i"
    },
    {
        "model": "MI 5",
        "phonename": "XiaomiMi 5"
    },
    {
        "model": "MI 5s",
        "phonename": "XiaomiMi 5s"
    },
    {
        "model": "Mi 9T",
        "phonename": "XiaomiMi 9T"
    },
    {
        "model": "Mi 9T Pro",
        "phonename": "XiaomiMi 9T Pro"
    },
    {
        "model": "MI A1",
        "phonename": "XiaomiMi A1"
    },
    {
        "model": "Mi A2",
        "phonename": "XiaomiMi A2"
    },
    {
        "model": "Mi A2 Lite",
        "phonename": "XiaomiMi A2 Lite"
    },
    {
        "model": "Mi A3",
        "phonename": "XiaomiMi A3"
    },
    {
        "model": "MiProjA1",
        "phonename": "Xiaomi\"Mi Laser Projector 150\"\"\""
    },
    {
        "model": "MiProjL1",
        "phonename": "XiaomiMi Laser Projector 4K"
    },
    {
        "model": "Mi MIX 3 5G",
        "phonename": "XiaomiMi MIX 3 5G"
    },
    {
        "model": "Mi Note 10 Lite",
        "phonename": "XiaomiMi Note 10 Lite"
    },
    {
        "model": "Mi Note 2",
        "phonename": "XiaomiMi Note2"
    },
    {
        "model": "MiTV-AESP0",
        "phonename": "XiaomiMi TV Stick"
    },
    {
        "model": "MiProjM05",
        "phonename": "XiaomiMi smart projector"
    },
    {
        "model": "Mi9 Pro 5G",
        "phonename": "XiaomiMi9 Pro 5G"
    },
    {
        "model": "MiBOX1S",
        "phonename": "XiaomiMiBOX1S"
    },
    {
        "model": "MiBOX2",
        "phonename": "XiaomiMiBOX2"
    },
    {
        "model": "MiBOX3S",
        "phonename": "XiaomiMiBOX3S"
    },
    {
        "model": "MiBOX_mini",
        "phonename": "XiaomiMiBOX_mini"
    },
    {
        "model": "MIBOX4",
        "phonename": "XiaomiMiBox S"
    },
    {
        "model": "LIO-AN00m",
        "phonename": "HUAWEIMate30EPro5G全网通版"
    },
    {
        "model": "OCE-AN50",
        "phonename": "HUAWEIMate40E5G全网通版"
    },
    {
        "model": "OCE-AL50",
        "phonename": "HUAWEIMate40E4G全网通版"
    },
    {
        "model": "TET-AN50",
        "phonename": "HUAWEIMateX2典藏版5G全网通版"
    },
    {
        "model": "TET-AL00",
        "phonename": "HUAWEIMateX24G全网通版"
    },
    {
        "model": "ANA-AL00",
        "phonename": "HUAWEIP404G全网通版"
    },
    {
        "model": "ABR-AL00",
        "phonename": "HUAWEIP504G全网通版"
    },
    {
        "model": "GLK-LX1U",
        "phonename": "HUAWEInova5i联通定制版"
    },
    {
        "model": "CDL-AN50",
        "phonename": "HUAWEInova7SE5G乐活版全网通版"
    },
    {
        "model": "BRQ-AL00",
        "phonename": "HUAWEInova8Pro4G全网通版"
    },
    {
        "model": "NAM-AL00",
        "phonename": "HUAWEInova94G全网通版"
    },
    {
        "model": "AQM-TL00",
        "phonename": "华为畅享10S移动4G+版"
    },
    {
        "model": "DVC-TN20",
        "phonename": "华为畅享20Pro5G移动定制版"
    },
    {
        "model": "WKG-TN00",
        "phonename": "华为畅享205G移动定制版"
    },
    {
        "model": "PPA-AL20",
        "phonename": "华为畅享20SE全网通版"
    },
    {
        "model": "MLD-AL10",
        "phonename": "华为畅享20e全网通版(HelioP35)"
    },
    {
        "model": "PLE-703L",
        "phonename": "华为揽阅M2青春版7.0英寸全网通版"
    },
    {
        "model": "FDR-A03L",
        "phonename": "华为揽阅M2青春版10.1英寸LTE版"
    },
    {
        "model": "BTV-DL09",
        "phonename": "华为平板M3LTE版"
    },
    {
        "model": "CPN-AL00",
        "phonename": "华为平板M3青春版8.0英寸全网通版"
    },
    {
        "model": "BAH-W09",
        "phonename": "华为平板M3青春版10.1英寸Wi-Fi版"
    },
    {
        "model": "BAH-AL00",
        "phonename": "华为平板M3青春版10.1英寸全网通版"
    },
    {
        "model": "SHT-W09",
        "phonename": "华为平板M58.4英寸Wi-Fi版"
    },
    {
        "model": "SHT-AL09",
        "phonename": "华为平板M58.4英寸全网通版"
    },
    {
        "model": "CMR-W09",
        "phonename": "华为平板M510.8英寸Wi-Fi版"
    },
    {
        "model": "CMR-AL09",
        "phonename": "华为平板M510.8英寸全网通版"
    },
    {
        "model": "CMR-AL19",
        "phonename": "华为平板M5Pro全网通版"
    },
    {
        "model": "BAH2-W09",
        "phonename": "华为平板M5青春版10.1英寸Wi-Fi版"
    },
    {
        "model": "BAH2-AL10",
        "phonename": "华为平板M5青春版10.1英寸全网通版"
    },
    {
        "model": "VRD-W09",
        "phonename": "华为平板M68.4英寸Wi-Fi版"
    },
    {
        "model": "VRD-AL09",
        "phonename": "华为平板M68.4英寸全网通版"
    },
    {
        "model": "VRD-W10",
        "phonename": "华为平板M6高能版8.4英寸Wi-Fi版"
    },
    {
        "model": "VRD-AL10",
        "phonename": "华为平板M6高能版8.4英寸全网通版"
    },
    {
        "model": "SCM-W09",
        "phonename": "华为平板M610.8英寸Wi-Fi版"
    },
    {
        "model": "SCM-AL09",
        "phonename": "华为平板M610.8英寸全网通版"
    },
    {
        "model": "MRX-AL09",
        "phonename": "HUAWEIMatePadPro10.8英寸全网通版(6GB+128GB/8GB+256GB)"
    },
    {
        "model": "MRX-AL19",
        "phonename": "HUAWEIMatePadPro10.8英寸全网通版(8GB+512GB)"
    },
    {
        "model": "MRX-AN19",
        "phonename": "HUAWEIMatePadPro10.8英寸5G全网通版"
    },
    {
        "model": "WGR-AN19",
        "phonename": "HUAWEIMatePadPro12.6英寸全网通版(麒麟9000)"
    },
    {
        "model": "BAH3-AL00",
        "phonename": "HUAWEIMatePad10.4英寸全网通版(麒麟810)"
    },
    {
        "model": "SCMR-W09",
        "phonename": "HUAWEIMatePad10.8英寸Wi-Fi版"
    },
    {
        "model": "DBY-W09",
        "phonename": "HUAWEIMatePad11英寸Wi-Fi版"
    },
    {
        "model": "AGS2-AL00",
        "phonename": "华为畅享平板10.1英寸全网通版"
    },
    {
        "model": "AGS3-W00D",
        "phonename": "华为畅享平板210.1英寸Wi-Fi版(4GB+64GB)"
    },
    {
        "model": "AGS3-W00E",
        "phonename": "华为畅享平板210.1英寸Wi-Fi版(4GB+128GB)"
    },
    {
        "model": "BZK-W00",
        "phonename": "华为平板C3(华为平板T3行业专享版)8英寸Wi-Fi版"
    },
    {
        "model": "BZA-L00",
        "phonename": "华为平板C3(华为平板T3行业专享版)9.6英寸LTE版"
    },
    {
        "model": "MON-AL19",
        "phonename": "华为平板C58英寸全网通版"
    },
    {
        "model": "BZT-W09",
        "phonename": "华为平板C510.1英寸Wi-Fi版"
    },
    {
        "model": "BZT-AL00",
        "phonename": "华为平板C510.1英寸全网通标配版"
    },
    {
        "model": "BZW-AL10",
        "phonename": "华为平板C58英寸2020款全网通版(4GB+64GB)"
    },
    {
        "model": "8681-M02",
        "phonename": "360手机奇酷青春版双网通版"
    },
    {
        "model": "MHA-L29",
        "phonename": "HUAWEIMate9DualSIM"
    },
    {
        "model": "LON-L29",
        "phonename": "PORSCHEDESIGNHUAWEIMate9DualSIM"
    },
    {
        "model": "BLA-A09",
        "phonename": "PORSCHEDESIGNHUAWEIMate10(UnitedStates)"
    },
    {
        "model": "BND-L34",
        "phonename": "HUAWEIMateSE(UnitedStates)"
    },
    {
        "model": "NEO-L29",
        "phonename": "PORSCHEDESIGNHUAWEIMateRSDualSIM"
    },
    {
        "model": "HMA-L09",
        "phonename": "HUAWEIMate20SingleSIM"
    },
    {
        "model": "HMA-L29",
        "phonename": "HUAWEIMate20DualSIM"
    },
    {
        "model": "LYA-L29",
        "phonename": "PORSCHEDESIGNHUAWEIMate20RSDualSIM"
    },
    {
        "model": "EVR-L29",
        "phonename": "HUAWEIMate20XDualSIM"
    },
    {
        "model": "TAS-L29",
        "phonename": "HUAWEIMate30DualSIM"
    },
    {
        "model": "NOH-NX9",
        "phonename": "HUAWEIMate40Pro5GDualSIM"
    },
    {
        "model": "EVA-L09",
        "phonename": "HUAWEIP9SingleSIM"
    },
    {
        "model": "VTR-L09",
        "phonename": "HUAWEIP10SingleSIM"
    },
    {
        "model": "VKY-L09",
        "phonename": "HUAWEIP10PlusSingleSIM"
    },
    {
        "model": "VKY-L29",
        "phonename": "HUAWEIP10PlusDualSIM"
    },
    {
        "model": "EML-L09",
        "phonename": "HUAWEIP20SingleSIM"
    },
    {
        "model": "ELE-L09",
        "phonename": "HUAWEIP30SingleSIM"
    },
    {
        "model": "ELE-L29",
        "phonename": "HUAWEIP30DualSIM"
    },
    {
        "model": "VOG-L09",
        "phonename": "HUAWEIP30ProSingleSIM"
    },
    {
        "model": "VOG-L29",
        "phonename": "HUAWEIP30ProDualSIM"
    },
    {
        "model": "ELS-NX9",
        "phonename": "HUAWEIP40ProDualSIM"
    },
    {
        "model": "JNY-LX1",
        "phonename": "HUAWEInova7iDualSIM"
    },
    {
        "model": "JNY-LX2",
        "phonename": "HUAWEIP40liteSingleSIM"
    },
    {
        "model": "INE-LX1",
        "phonename": "HUAWEIPsmart+"
    },
    {
        "model": "STK-L21",
        "phonename": "HUAWEIY9sSingleSIM"
    },
    {
        "model": "PPA-LX2",
        "phonename": "HUAWEIPsmart2021DualSIM"
    },
    {
        "model": "LDN-LX2",
        "phonename": "HUAWEInova2lite"
    },
    {
        "model": "VCE-L22",
        "phonename": "HUAWEInova4"
    },
    {
        "model": "YAL-L21",
        "phonename": "HUAWEInova5T"
    },
    {
        "model": "YAL-L41",
        "phonename": "HUAWEInova5TPro"
    },
    {
        "model": "DRA-LX9",
        "phonename": "HUAWEIY5pDualSIM"
    },
    {
        "model": "LDN-L21",
        "phonename": "HUAWEIY7Prime2018DualSIM"
    },
    {
        "model": "AQM-LX1",
        "phonename": "HUAWEIY8pDualSIM"
    },
    {
        "model": "M973Q",
        "phonename": "魅族16sPro公开版"
    },
    {
        "model": "XT1965-6",
        "phonename": "motorolag7plus"
    },
    {
        "model": "XT1970-5",
        "phonename": "motorolap50"
    },
    {
        "model": "XT2071-4",
        "phonename": "motorolarazr5G"
    },
    {
        "model": "XT2125-4",
        "phonename": "motorolaedges"
    },
    {
        "model": "XT2143-1",
        "phonename": "motorolaedge轻奢版"
    },
    {
        "model": "XT2153-1",
        "phonename": "motorolaedgespro"
    },
    {
        "model": "XT2137-2",
        "phonename": "motorolag50"
    },
    {
        "model": "TA-1094",
        "phonename": "Nokia9PureView"
    },
    {
        "model": "NX507J",
        "phonename": "nubiaZ7mini全网通版"
    },
    {
        "model": "NX627J",
        "phonename": "nubiaZ20"
    },
    {
        "model": "NX659J",
        "phonename": "红魔5S"
    },
    {
        "model": "NX669J",
        "phonename": "腾讯红魔游戏手机6"
    },
    {
        "model": "NX666J",
        "phonename": "腾讯红魔游戏手机6R"
    },
    {
        "model": "NX651J",
        "phonename": "nubiaPlay"
    },
    {
        "model": "HD1925",
        "phonename": "OnePlus7TPro5GT-Mobile版/OnePlusConceptOne"
    },
    {
        "model": "KB2000",
        "phonename": "OnePlus8T全网通版"
    },
    {
        "model": "LE2100",
        "phonename": "OnePlus9R全网通版"
    },
    {
        "model": "LE2110",
        "phonename": "OnePlus9全网通版"
    },
    {
        "model": "MT2110",
        "phonename": "OnePlus9RT全网通版"
    },
    {
        "model": "BE2029",
        "phonename": "OnePlusNordN10国际版"
    },
    {
        "model": "PEDM00",
        "phonename": "OPPOFindX3全网通版"
    },
    {
        "model": "PEEM00",
        "phonename": "OPPOFindX3Pro全网通版"
    },
    {
        "model": "PEGT00",
        "phonename": "OPPOReno5移动版"
    },
    {
        "model": "PEGT10",
        "phonename": "OPPOReno5K移动版"
    },
    {
        "model": "PDRM00",
        "phonename": "OPPOReno5Pro+全网通版"
    },
    {
        "model": "PEQM00",
        "phonename": "OPPOReno6全网通版"
    },
    {
        "model": "PFCM00",
        "phonename": "OPPOReno7SE全网通版"
    },
    {
        "model": "PBBT00",
        "phonename": "OPPOA7x移动版"
    },
    {
        "model": "PCDM00",
        "phonename": "OPPOA7n全网通版"
    },
    {
        "model": "PCDT00",
        "phonename": "OPPOA7n移动版"
    },
    {
        "model": "PEFM00",
        "phonename": "OPPOA35全网通版"
    },
    {
        "model": "PDAT10",
        "phonename": "OPPOA52移动版"
    },
    {
        "model": "PECT30",
        "phonename": "OPPOA53(2020)移动版"
    },
    {
        "model": "PFVM10",
        "phonename": "OPPOA56全网通版"
    },
    {
        "model": "PDYM10",
        "phonename": "OPPOA72n全网通版"
    },
    {
        "model": "PEHT00",
        "phonename": "OPPOA93移动版"
    },
    {
        "model": "PFGM00",
        "phonename": "OPPOA93s全网通版"
    },
    {
        "model": "PELM00",
        "phonename": "OPPOA95全网通版"
    },
    {
        "model": "PERM00",
        "phonename": "OPPOK7x全网通版"
    },
    {
        "model": "PERM10",
        "phonename": "OPPOK9s全网通版"
    },
    {
        "model": "PEYM00",
        "phonename": "OPPOK9Pro全网通版"
    },
    {
        "model": "CPH2145",
        "phonename": "OPPOReno55G"
    },
    {
        "model": "CPH2159",
        "phonename": "OPPOReno5"
    },
    {
        "model": "CPH2201",
        "phonename": "OPPOReno5Pro"
    },
    {
        "model": "CPH2095",
        "phonename": "OPPOF17"
    },
    {
        "model": "CPH1879",
        "phonename": "OPPOR17"
    },
    {
        "model": "CPH1877",
        "phonename": "OPPOR17Pro"
    },
    {
        "model": "CPH1903",
        "phonename": "OPPOAX7"
    },
    {
        "model": "CPH2161",
        "phonename": "OPPOA735G"
    },
    {
        "model": "CPH2211",
        "phonename": "OPPOA945G"
    },
    {
        "model": "RMX2025",
        "phonename": "真我X505G移动版"
    },
    {
        "model": "RMX2072",
        "phonename": "真我X50Pro玩家版"
    },
    {
        "model": "RMX2052",
        "phonename": "真我X50t5G"
    },
    {
        "model": "RMX2112",
        "phonename": "真我V55G运营商定制版"
    },
    {
        "model": "RMX3122",
        "phonename": "真我V115G运营商定制版"
    },
    {
        "model": "RMX3092",
        "phonename": "真我V155G全网通版"
    },
    {
        "model": "RMX2173",
        "phonename": "真我Q2Pro5G"
    },
    {
        "model": "RMX3142",
        "phonename": "真我Q3Pro狂欢版5G"
    },
    {
        "model": "RMX3042",
        "phonename": "真我Q3i5G"
    },
    {
        "model": "RMX2202",
        "phonename": "真我GT5G"
    },
    {
        "model": "RMX3031",
        "phonename": "真我GTNeo5G"
    },
    {
        "model": "RMX3350",
        "phonename": "真我GTNeo闪速版5G"
    },
    {
        "model": "RMX3361",
        "phonename": "真我GT大师版5G"
    },
    {
        "model": "RMX3370",
        "phonename": "真我GTNeo25G"
    },
    {
        "model": "RMX3357",
        "phonename": "真我GTNeo2T5G"
    },
    {
        "model": "RMX3085",
        "phonename": "realme8"
    },
    {
        "model": "GT-I9507V",
        "phonename": "GalaxyS4联通4G定制版"
    },
    {
        "model": "SM-G7810",
        "phonename": "GalaxyS20FE5G"
    },
    {
        "model": "SM-G9910",
        "phonename": "GalaxyS215G"
    },
    {
        "model": "SM-G9960",
        "phonename": "GalaxyS21+5G"
    },
    {
        "model": "SM-F9260",
        "phonename": "GalaxyZFold35G"
    },
    {
        "model": "SM-F7070",
        "phonename": "GalaxyZFlip5G"
    },
    {
        "model": "SM-F7110",
        "phonename": "GalaxyZFlip35G"
    },
    {
        "model": "V2111A",
        "phonename": "vivoy53s"
    },
    {
        "model": "PEGM00",
        "phonename": "opporeno5"
    },
    {
        "model": "M2012K11C",
        "phonename": "红米k40pro"
    },
    {
        "model": "PCHM00",
        "phonename": "oppok9pro"
    },
    {
        "model": "LIO-L29",
        "phonename": "华为mate30pro"
    },
    {
        "model": "AGS3-AL00",
        "phonename": "华为畅享平板2"
    },
    {
        "model": "conquest-S16",
        "phonename": "征服S16"
    },
    {
        "model": "INE-LX2",
        "phonename": "华为nova3i"
    },
    {
        "model": "MRX-W09",
        "phonename": "华为matepadpro"
    },
    {
        "model": "SM-G991U",
        "phonename": "SamsungGalaxyS21"
    },
    {
        "model": "SM-A207F",
        "phonename": "SamsungGalaxyA20s"
    },
    {
        "model": "21091116AC",
        "phonename": "红米note115G"
    },
    {
        "model": "RMX3115",
        "phonename": "OPPOrealmeX7Pro"
    },
    {
        "model": "M2007J20CG",
        "phonename": "小米POCOX3"
    },
    {
        "model": "M12pro",
        "phonename": "金立M12pro"
    },
    {
        "model": "SM-G981U",
        "phonename": "SamsungGalaxyS205G"
    },
    {
        "model": "SM-G998B",
        "phonename": "SamsungGalaxyS21Ultra5G"
    },
    {
        "model": "CPH1727",
        "phonename": "OPPOF5pro"
    },
    {
        "model": "K30",
        "phonename": "红米K30"
    },
    {
        "model": "4A",
        "phonename": "荣耀4A"
    },
    {
        "model": "MiNote10Lite",
        "phonename": "小米note10Lite"
    },
    {
        "model": "ATMANX20(X9S)",
        "phonename": "创星X20"
    },
    {
        "model": "A1Q",
        "phonename": "AGMA1Q"
    },
    {
        "model": "ZTEA2022H",
        "phonename": "中兴Axon30Pro"
    },
    {
        "model": "FRD-AL00",
        "phonename": "华为荣耀8"
    },
    {
        "model": "LenovoTB-8704N",
        "phonename": "联想Tab4/Plus"
    },
    {
        "model": "MX20Plus",
        "phonename": "米语mx20plus"
    },
    {
        "model": "R11",
        "phonename": "oppoR11"
    },
    {
        "model": "V2057A",
        "phonename": "VIVOY52s"
    },
    {
        "model": "V2020CA",
        "phonename": "VIVOS7"
    },
    {
        "model": "BTV-W09",
        "phonename": "华为M3平板"
    },
    {
        "model": "TYH611M",
        "phonename": "华为麦芒10se"
    },
    {
        "model": "JDN-AL00",
        "phonename": "华为荣耀平板2"
    },
    {
        "model": "M20",
        "phonename": "SamsungGalaxyM20"
    },
    {
        "model": "VTR-L29",
        "phonename": "华为P10"
    },
    {
        "model": "V2156A",
        "phonename": "vivoY76s"
    },
    {
        "model": "ANA-NX9",
        "phonename": "华为P40"
    },
    {
        "model": "JDN-W09",
        "phonename": "华为荣耀平板2"
    },
    {
        "model": "TET-AN10",
        "phonename": "华为荣耀X10"
    },
    {
        "model": "LM-Q815L",
        "phonename": "LGQ8"
    },
    {
        "model": "ZTEA2020N2Pro",
        "phonename": "中兴天机10pro"
    },
    {
        "model": "CDY-NX9A",
        "phonename": "华为P40lite5G"
    },
    {
        "model": "DT1901A",
        "phonename": "锤子坚果pro3"
    },
    {
        "model": "KONKAD18",
        "phonename": "康佳D18"
    },
    {
        "model": "ZTE8010",
        "phonename": "中兴ZTE8010"
    },
    {
        "model": "V2022",
        "phonename": "中兴BladeV2022"
    },
    {
        "model": "LYA-L09",
        "phonename": "华为Mate20Pro"
    },
    {
        "model": "MuMu",
        "phonename": "mumu安卓模拟器"
    },
    {
        "model": "LenovoTB-8705F",
        "phonename": "联想TabM8"
    },
    {
        "model": "SM-A326W",
        "phonename": "SamsungGalaxyA325G"
    },
    {
        "model": "i12ProMax",
        "phonename": "iPhone12ProMax"
    },
    {
        "model": "SM-G9287",
        "phonename": "SamsungGlaxyS6edgePlus"
    },
    {
        "model": "CPH1901",
        "phonename": "oppoA7"
    },
    {
        "model": "SM-A217F",
        "phonename": "SamsungGalaxyA21s"
    },
    {
        "model": "LG-US998",
        "phonename": "LGV30"
    },
    {
        "model": "OPPOA73t",
        "phonename": "OPPOA73t"
    },
    {
        "model": "CPH1911",
        "phonename": "oppoF11"
    },
    {
        "model": "koobeeS106",
        "phonename": "酷比S106m"
    },
    {
        "model": "ZTEA2022P",
        "phonename": "中兴Axon30Ultra"
    },
    {
        "model": "x600",
        "phonename": "SamsungX600"
    },
    {
        "model": "NokiaX20",
        "phonename": "诺基亚X20"
    },
    {
        "model": "M6",
        "phonename": "魅族魅蓝M6"
    },
    {
        "model": "VIE-L29",
        "phonename": "华为P9plus海外版"
    },
    {
        "model": "XQ-AU52",
        "phonename": "索尼XQ-AU52"
    },
    {
        "model": "11promax",
        "phonename": "iPhone11promax"
    },
    {
        "model": "T1",
        "phonename": "vivoT1"
    },
    {
        "model": "RMX3161",
        "phonename": "oppoRealmeQ3"
    },
    {
        "model": "V2056A",
        "phonename": "VivoX60Pro+"
    },
    {
        "model": "V2099A",
        "phonename": "VivoY302021"
    },
    {
        "model": "SM-J530L",
        "phonename": "SamsungGalaxyJ5"
    },
    {
        "model": "V2069A",
        "phonename": "VIVOY53S"
    },
    {
        "model": "V2059A",
        "phonename": "vivoX60曲屏"
    },
    {
        "model": "GLK-TL00",
        "phonename": "HUAWEInova5i"
    },
    {
        "model": "MED-LX9",
        "phonename": "HuaweiY6P"
    },
    {
        "model": "ONEPLUSA6013",
        "phonename": "OnePlus6T"
    },
    {
        "model": "JDN2-W09",
        "phonename": "华为M5"
    },
    {
        "model": "21091116UC",
        "phonename": "红米Note11Pro+"
    },
    {
        "model": "P40Pro",
        "phonename": "华为P40Pro"
    },
    {
        "model": "iPlay_20",
        "phonename": "酷比魔方iPlay20"
    },
    {
        "model": "HL2001",
        "phonename": "九爱V1S"
    },
    {
        "model": "G0515D",
        "phonename": "格力1W"
    },
    {
        "model": "CPH1907",
        "phonename": "OPPO-Reno2"
    },
    {
        "model": "SM-T295C",
        "phonename": "SamsungGalaxyTabA"
    },
    {
        "model": "XHF-M001",
        "phonename": "小黄蜂XHF-M001"
    },
    {
        "model": "SM-G960N",
        "phonename": "SamsungS9"
    },
    {
        "model": "CPH2219",
        "phonename": "OppoF19"
    },
    {
        "model": "E910",
        "phonename": "海信E910"
    },
    {
        "model": "BOS-A0",
        "phonename": "酷派BOS-A0"
    },
    {
        "model": "P027",
        "phonename": "华硕P027"
    },
    {
        "model": "GIONEEM50Pro",
        "phonename": "金立M50Pro"
    },
    {
        "model": "AGM3-AL09HN",
        "phonename": "荣耀(honor)平板电脑平板7"
    },
    {
        "model": "SM-G960U1",
        "phonename": "SamsungGalaxyS9"
    },
    {
        "model": "VOG-L04",
        "phonename": "华为(HUAWEI)P30Pro"
    },
    {
        "model": "HL3001",
        "phonename": "九爱HL3001"
    },
    {
        "model": "BZT-AL10",
        "phonename": "华为C510"
    },
    {
        "model": "SM-F916N",
        "phonename": "SamsungGalaxyFold2"
    },
    {
        "model": "SHARKMBU-A0",
        "phonename": "XiaomiBlackShark3Pro"
    },
    {
        "model": "vivo1908",
        "phonename": "vivoY90"
    },
    {
        "model": "S410J",
        "phonename": "Philips/飛利浦M9S"
    },
    {
        "model": "FZ-S05",
        "phonename": "EXSECURTEL手机FZ-S05"
    },
    {
        "model": "Q18",
        "phonename": "万利达q18"
    },
    {
        "model": "GIONEEF6L",
        "phonename": "金立F6L"
    },
    {
        "model": "Nokia8Sirocco",
        "phonename": "诺基亚8Sirocco"
    },
    {
        "model": "JD-PLUS(移动版)",
        "phonename": "小辣椒红辣椒JD-Plus"
    },
    {
        "model": "SM-T385C",
        "phonename": "SamsungGalaxyTabA"
    },
    {
        "model": "PDSM00",
        "phonename": "OPPOReno5Pro"
    },
    {
        "model": "TFY-AN00",
        "phonename": "华为荣耀X30i"
    },
    {
        "model": "TYH211U",
        "phonename": "沃尔驴天翼一号"
    },
    {
        "model": "VP001",
        "phonename": "U-Magic优畅享20Plus"
    },
    {
        "model": "SM-A5260",
        "phonename": "SamsungA52"
    },
    {
        "model": "RMX2117",
        "phonename": "OPPORealmeQ25G"
    },
    {
        "model": "RMX2201",
        "phonename": "OPPORealmeV35G"
    },
    {
        "model": "SM-A5160",
        "phonename": "SamsungGalaxyA515G"
    },
    {
        "model": "EML-L29",
        "phonename": "HuaweiP20EML-L29"
    },
    {
        "model": "ZUKZ1",
        "phonename": "联想ZUKZ1"
    },
    {
        "model": "AGM3-W09HN",
        "phonename": "荣耀平板7"
    },
    {
        "model": "R40Pro",
        "phonename": "小辣椒R40pro"
    },
    {
        "model": "CPH1723",
        "phonename": "OPPOF5"
    },
    {
        "model": "NokiaC3",
        "phonename": "NokiaC3"
    },
    {
        "model": "HUAWEIMLA-L12",
        "phonename": "华为Novaplus"
    },
    {
        "model": "LE2120",
        "phonename": "一加9pro"
    },
    {
        "model": "CPH1937",
        "phonename": "OppoA92020"
    },
    {
        "model": "angelcare_F20",
        "phonename": "中兴angelcare守护宝F20Pro"
    },
    {
        "model": "GIONEEF40",
        "phonename": "金立F40"
    },
    {
        "model": "G1701",
        "phonename": "吉客猫glocalmeg1701"
    },
    {
        "model": "LenovoTB-J607F",
        "phonename": "小新PadPlus"
    },
    {
        "model": "CMCM5S",
        "phonename": "厘米cm5s"
    },
    {
        "model": "SM-A2070",
        "phonename": "SAMSUNG三星GalaxyA20s"
    },
    {
        "model": "DN2103",
        "phonename": "OPPOOnePlus"
    },
    {
        "model": "SM-F9160",
        "phonename": "三星GalaxyZFold2"
    },
    {
        "model": "CPH1979",
        "phonename": "OPPOOneZ"
    },
    {
        "model": "V2045A",
        "phonename": "VivoX60"
    },
    {
        "model": "Mi9SE",
        "phonename": "小米9SE"
    },
    {
        "model": "WGR-W09",
        "phonename": "HUAWEIMatePadPro平板"
    },
    {
        "model": "SM-G610L",
        "phonename": "GALAXYOn7"
    },
    {
        "model": "XQ-AS72",
        "phonename": "xperia5ii"
    },
    {
        "model": "HUAWEIVNS-L31",
        "phonename": "HUAWEIP9LITE"
    },
    {
        "model": "ChanghongR9",
        "phonename": "长虹R9"
    },
    {
        "model": "TAH-N29m",
        "phonename": "华为mateXs"
    },
    {
        "model": "V2048A",
        "phonename": "vivos9e"
    },
    {
        "model": "CHL-AL00",
        "phonename": "荣耀Play5T"
    },
    {
        "model": "RMX2205",
        "phonename": "REALMEQ3PRO"
    },
    {
        "model": "JAD-AL50",
        "phonename": "华为P50Pro"
    },
    {
        "model": "NAT-TN70",
        "phonename": "鼎桥NAT-TN70"
    },
    {
        "model": "RMX3366",
        "phonename": "realme真我"
    },
    {
        "model": "RMX3461",
        "phonename": "RealmeRMX3461"
    },
    {
        "model": "FDR-A01w",
        "phonename": "华为揽阅M2青春版"
    },
    {
        "model": "Joyar_62_64",
        "phonename": "3GPAD"
    },
    {
        "model": "V2023EA",
        "phonename": "vivoX70"
    },
    {
        "model": "M40SE(M5T3)",
        "phonename": "台电M40SE"
    },
    {
        "model": "MIPAD3",
        "phonename": "小米平板3"
    },
    {
        "model": "M1",
        "phonename": "小米M1"
    },
    {
        "model": "SM-A530N",
        "phonename": "三星GalaxyA8"
    },
    {
        "model": "MiMIX35G",
        "phonename": "小米MIX35G"
    },
    {
        "model": "SM-G9980",
        "phonename": "三星GalaxyS21Ultra"
    },
    {
        "model": "BAH3-AN10",
        "phonename": "华为MatePad5G"
    },
    {
        "model": "LDOX-2121",
        "phonename": "天语MT40"
    },
    {
        "model": "SM-A730F",
        "phonename": "三星A730F"
    },
    {
        "model": "SM-G960F",
        "phonename": "SamsungGalaxyS9"
    },
    {
        "model": "S27MIX",
        "phonename": "欧加S27MIX"
    },
    {
        "model": "HTC_VR_V1",
        "phonename": "HtcViveVR"
    },
    {
        "model": "GM1913",
        "phonename": "ONEPLUS7PRO"
    },
    {
        "model": "M10",
        "phonename": "小米10"
    },
    {
        "model": "vivox6a",
        "phonename": "vivox6a"
    },
    {
        "model": "WII-AL00",
        "phonename": "华为畅享20e"
    },
    {
        "model": "oppoa83",
        "phonename": "oppoa83"
    },
    {
        "model": "TablePC",
        "phonename": "Table平板"
    },
    {
        "model": "CPH2061",
        "phonename": "OPPOA52"
    },
    {
        "model": "LenovoL70081",
        "phonename": "LENOVOL70081整机拯救者2"
    },
    {
        "model": "i7S(YP7S)",
        "phonename": "誉品（YEPEN）i7s"
    },
    {
        "model": "HTCDesire10pro",
        "phonename": "HTCDesire10pro"
    },
    {
        "model": "PEGM10",
        "phonename": "OPPOReno5K"
    },
    {
        "model": "V2133A",
        "phonename": "VIVOX70"
    },
    {
        "model": "PENM00",
        "phonename": "OPPOReno6"
    },
    {
        "model": "RMX3041",
        "phonename": "realmeV13"
    },
    {
        "model": "V19",
        "phonename": "vivoV19"
    },
    {
        "model": "TYH201H",
        "phonename": "天翼1号"
    },
    {
        "model": "V2145A",
        "phonename": "VIVOX70"
    },
    {
        "model": "MIPAD4",
        "phonename": "小米平板4"
    },
    {
        "model": "RNE-L22",
        "phonename": "华为荣耀9i"
    },
    {
        "model": "PFJM10",
        "phonename": "OPPOReno7"
    },
    {
        "model": "HLK-AL00a",
        "phonename": "荣耀9X"
    },
    {
        "model": "X50Pro",
        "phonename": "vivoX50Pro5G版"
    },
    {
        "model": "DT2002C",
        "phonename": "锤子科技坚果R2"
    },
    {
        "model": "M2102K1AC",
        "phonename": "小米11Pro"
    },
    {
        "model": "SUGARS30",
        "phonename": "SUGARS30"
    },
    {
        "model": "SM-G991N",
        "phonename": "三星GalaxyS21"
    },
    {
        "model": "SOAPR11",
        "phonename": "SUGARSOAPR11lite"
    },
    {
        "model": "T1-823L",
        "phonename": "华为T1-823L平板"
    },
    {
        "model": "BDS2Plus",
        "phonename": "北斗复兴BDS2"
    },
    {
        "model": "MOA-AL20",
        "phonename": "华为荣耀畅玩9A"
    },
    {
        "model": "V30",
        "phonename": "荣耀V30"
    },
    {
        "model": "ivviP60",
        "phonename": "依偎（ivvi）P60"
    },
    {
        "model": "V2026",
        "phonename": "vivoY12s"
    },
    {
        "model": "X12pro",
        "phonename": "小辣椒X12pro"
    },
    {
        "model": "V2046A",
        "phonename": "vivoX60"
    },
    {
        "model": "V2002A",
        "phonename": "vivoY70s"
    },
    {
        "model": "vivoX6D",
        "phonename": "vivoX6D"
    },
    {
        "model": "SEA-AL10",
        "phonename": "HUAWEInova5pro"
    },
    {
        "model": "JKM-AL00a",
        "phonename": "HUAWEI畅享9Plus"
    },
    {
        "model": "DUB-TL0",
        "phonename": "HUAWEI畅享9"
    },
    {
        "model": "DUB-AL20",
        "phonename": "HUAWEI荣耀8x"
    },
    {
        "model": "PACT00",
        "phonename": "OPPOr15"
    },
    {
        "model": "PCAM10",
        "phonename": "OPPOA9"
    },
    {
        "model": "PADM00",
        "phonename": "OPPOA3"
    },
    {
        "model": "PBBM30",
        "phonename": "OPPOA5"
    },
    {
        "model": "RedmiK20Pro",
        "phonename": "RedmiK20Pro"
    },
    {
        "model": "PCAM00",
        "phonename": "OPPOReno"
    },
    {
        "model": "V1930A",
        "phonename": "vivo Y3"
    },
    {
        "model": "PAAM00",
        "phonename": "oppo R15"
    },
    {
        "model": "ART-AL00x",
        "phonename": "华为畅享10"
    },
    {
        "model": "DUB-AL00",
        "phonename": "华为畅享9"
    },
    {
        "model": "ASK-AL00x",
        "phonename": "荣耀Play3"
    },
    {
        "model": "LRA-AL00",
        "phonename": "华为荣耀20"
    },
    {
        "model": "STK-AL00",
        "phonename": "畅享10Plus"
    },
    {
        "model": "BND-AL10",
        "phonename": "荣耀畅玩7X"
    },
    {
        "model": "ELE-AL00",
        "phonename": "华为p30"
    },
    {
        "model": "V1934A",
        "phonename": "vivoy5s"
    },
    {
        "model": "FIG-AL10",
        "phonename": "华为畅享7S"
    },
    {
        "model": "DVC-AN20",
        "phonename": "手机畅享20Pro"
    },
    {
        "model": "V1911A",
        "phonename": "vivoZ5X"
    },
    {
        "model": "V1732A",
        "phonename": "vivoY81S"
    },
    {
        "model": "V1965A",
        "phonename": "vivoY50"
    },
    {
        "model": "PDBM00",
        "phonename": "OPPOA8"
    },
    {
        "model": "V1901A",
        "phonename": "vivoy3全网通版"
    },
    {
        "model": "V1813A",
        "phonename": "vivoY97"
    },
    {
        "model": "PEMM20",
        "phonename": "OPPOA55"
    },
    {
        "model": "V1818A",
        "phonename": "vivoY93"
    },
    {
        "model": "JSN-AL00a",
        "phonename": "荣耀8X"
    },
    {
        "model": "PBAT00",
        "phonename": "oppoA5"
    },
    {
        "model": "PBBM00",
        "phonename": "A7x"
    },
    {
        "model": "PEHM00",
        "phonename": "oppo A93"
    },
    {
        "model": "HLK-AL00",
        "phonename": "荣耀9x"
    },
    {
        "model": "TEL-TN00",
        "phonename": "荣耀10x"
    },
    {
        "model": "CDY-AN00",
        "phonename": "nova7 SE"
    },
    {
        "model": "荣耀Play4T",
        "phonename": "荣耀Play4T"
    },
    {
        "model": "HMA-AL00",
        "phonename": "HUAWEI mate20"
    },
    {
        "model": "MED-AL00",
        "phonename": "畅享 10e"
    }
]

            # res = [{"packinfo": "中台_计步_V1.0.4_兜底", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_HW", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_OP", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_VI", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_HW_【合规调整+D】", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_计步_V1.0.0", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_计步_V1.0.7.3_datax", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_计步_V1.0.4_VI【弹出优化】", "adinfo": "splash,game_awaken,newfriend_video,newfriend_msg,5yuan_video,5yuan_msg,3mao_msg,8888_first_video,8888_second_video,8888_third_video,load_msg,double_mfzs,extra_mfzs,tx_video,wmtx_video,switch_plaque,auto_video,txym_msg,djhb_video,lqbx_video,lqhb_video,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_清理、wifi、省电_V1.0.0", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_wifi_【穿山甲平台广告合规化】", "adinfo": "scratch_video,make_video,bottom_msg,switch_plaque"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_兜底", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_HW", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_OP", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_VI", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_清理、wifi、省电_V2.0.2_【合规调整】HW", "adinfo": "splash,game_awaken,recommend_msg,clean_landing,level_win,scan_plaque,htend_plaque,dsshome_msg,adjust_video,jkzs_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_大字报_V1.0.0", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_兜底", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_HW", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_OP", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_VI", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_大字报_V1.0.3_VI【弹出优化】", "adinfo": "splash,game_awaken,adjust_video,exit_msg,leave_splash,zxtc_msg,jkzs_plaque,weather_msg,news_landing,my_msg,lqbx_video,lqhb_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_V1.0.0", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_【测试】V1.0.1", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_【测试】V1.0.2", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_充电_【穿山甲平台广告合规化】", "adinfo": "powersaving_video,speedup_video,care_msg,set_video,switch_plaque"}, {"packinfo": "中台_充电_V1.0.4_兜底", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_HW", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_OP", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_VI", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_VI【弹出优化】", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_OP【1466插件版1.0.12】", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.4_【1466】HW", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_充电_V1.0.0_【1466】HW-电池好卫士", "adinfo": "splash,game_awaken,powersaving_video,speedup_video,care_msg,set_video,switch_plaque,news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_天气_V1.0.0", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_兜底", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_HW", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_OP", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_VI", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8_VI【弹出优化】", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "中台_天气_V1.1.8【1466插件版1.0.12】", "adinfo": "splash,game_awaken,news_msg,more_video,check_video,jkzs_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化+带D+1463】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化+带D+1466+合规调整】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【HW定制化+小D】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "shelf_通用_v1.0.0【兜底包】", "adinfo": "news_landing,game_clean,game_video,game_ad,olanding_msg"}, {"packinfo": "GATE_计步_V1.0.7.3", "adinfo": "splash,2_plaque,game_awaken,first_msg,new_first_mix,first_bp_plaque,new_more_mix,tx_button,txbp_plaque,result_msg,sign_video,add_video,wx_video,2_tx_mix,limit_msg,succ_msg,2_queue_mix,2_bp_plaque,shared_ad_video,shared_ad_msg,lottery_plaque,news_landing,adjust_video,game_clean,game_video,game_ad,olanding_msg"}]

            for i in range(len(res)):
                phonemobile = res[i]['model']
                phonename = res[i]['phonename']
                sql =f"insert into device_info(phone_mobile, phone_name)value('{phonemobile}','{phonename}');"

            # 执行SQL语句
            # 执行后的结果都保存在cursor中
                cursor.execute(sql)

            # 1-从cursor中获取全部数据用fetchall
            # datas = cursor.fetchall()
            # print("获取的数据：\n",datas)

            # 2-从cursor中获取一条数据用fetchall
            # data = cursor.fetchone()
            # print("获取的数据：\n",data)

            # 3-想要从cursor中获取几条数据用fetchmany
            # datas = cursor.fetchmany(3)
            # print("获取的数据：\n", datas)
            # 执行玩SQL语句要提交
                con.commit()
                print("提交成功")

    except Exception as e:
        con.rollback()
        print("数据库异常：\n", e)
    finally:
        # 不管成功还是失败，都要关闭数据库连接
        con.close()


if __name__ == '__main__':
    mysql_db()