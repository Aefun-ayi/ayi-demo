from openpyxl import Workbook




data = [
    {
        "packinfo": "HuaweiHONOR 10i",
        "adinfo": "HRY-LX1T"
    },
    {
        "packinfo": "HuaweiHONOR 20",
        "adinfo": "YAL-AL00"
    },
    {
        "packinfo": "HuaweiHONOR 20",
        "adinfo": "YAL-L21"
    },
    {
        "packinfo": "HuaweiHONOR 20",
        "adinfo": "YAL-TL00"
    },
    {
        "packinfo": "HuaweiHONOR 20 LITE",
        "adinfo": "MAR-LX1R"
    },
    {
        "packinfo": "HuaweiHONOR 20 PRO",
        "adinfo": "YAL-AL10"
    },
    {
        "packinfo": "HuaweiHONOR 20 PRO",
        "adinfo": "YAL-L41"
    },
    {
        "packinfo": "HuaweiHONOR 20S",
        "adinfo": "MAR-LX1H"
    },
    {
        "packinfo": "HuaweiHONOR 20e",
        "adinfo": "HRY-LX1T"
    },
    {
        "packinfo": "HuaweiHONOR 20i",
        "adinfo": "HRY-AL00Ta"
    },
    {
        "packinfo": "HuaweiHONOR 4X",
        "adinfo": "Che2-L12"
    },
    {
        "packinfo": "HuaweiHONOR 8A Pro",
        "adinfo": "JAT-L29"
    },
    {
        "packinfo": "HuaweiHONOR 8A Pro",
        "adinfo": "JAT-L41"
    },
    {
        "packinfo": "HuaweiHONOR 8A Pro",
        "adinfo": "JAT-LX1"
    },
    {
        "packinfo": "HuaweiHONOR 8A Pro",
        "adinfo": "JAT-LX3"
    },
    {
        "packinfo": "HuaweiHONOR 8S",
        "adinfo": "KSA-LX2"
    },
    {
        "packinfo": "HuaweiHONOR 8S",
        "adinfo": "KSA-LX3"
    },
    {
        "packinfo": "HuaweiHONOR 8S",
        "adinfo": "KSA-LX9"
    },
    {
        "packinfo": "HuaweiHONOR 9A",
        "adinfo": "DUB-LX1"
    },
    {
        "packinfo": "HuaweiHONOR 9X",
        "adinfo": "STK-L22"
    },
    {
        "packinfo": "HuaweiHONOR 9X",
        "adinfo": "STK-LX1"
    },
    {
        "packinfo": "HuaweiHONOR 9X",
        "adinfo": "STK-LX3"
    },
    {
        "packinfo": "HuaweiHONOR 9X Lite",
        "adinfo": "JSN-L21"
    },
    {
        "packinfo": "HuaweiHONOR 9X lite",
        "adinfo": "JSN-L21"
    },
    {
        "packinfo": "HuaweiHONOR 9X lite",
        "adinfo": "JSN-L22"
    },
    {
        "packinfo": "HuaweiHONOR 9X lite",
        "adinfo": "JSN-L23"
    },
    {
        "packinfo": "HuaweiHONOR V20",
        "adinfo": "PCT-TL10"
    },
    {
        "packinfo": "HuaweiHONOR View20",
        "adinfo": "PCT-AL10"
    },
    {
        "packinfo": "HuaweiHONOR View20",
        "adinfo": "PCT-L29"
    },
    {
        "packinfo": "HuaweiHUAWEI G Elite Plus",
        "adinfo": "SLA-L03"
    },
    {
        "packinfo": "HuaweiHUAWEI GR5 2017",
        "adinfo": "BLL-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI GR5 2017",
        "adinfo": "BLL-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI GR5 2017",
        "adinfo": "HUAWEI BLL-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI GR5 2017",
        "adinfo": "HUAWEI BLL-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 20",
        "adinfo": "HMA-L09"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 20",
        "adinfo": "HMA-L29"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 20 Pro",
        "adinfo": "LYA-L0C"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 20 Pro",
        "adinfo": "LYA-L29"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 20 X (5G)",
        "adinfo": "EVR-AN00"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 20 X (5G)",
        "adinfo": "EVR-N29"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 20 lite",
        "adinfo": "SNE-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 9 lite",
        "adinfo": "BLL-L23"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate 9 lite",
        "adinfo": "HUAWEI BLL-L23"
    },
    {
        "packinfo": "HuaweiHUAWEI Mate SE",
        "adinfo": "BND-L34"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M3 Lite",
        "adinfo": "701HW"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M3 Lite",
        "adinfo": "702HW"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M3 Lite",
        "adinfo": "CPN-AL00"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M3 Lite",
        "adinfo": "CPN-L09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M3 Lite",
        "adinfo": "CPN-W09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M3 Lite 10 wp",
        "adinfo": "HDN-L09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M3 Lite 10 wp",
        "adinfo": "HDN-W09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 10.8",
        "adinfo": "CMR-AL09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 10.8",
        "adinfo": "CMR-W09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 8.4",
        "adinfo": "SHT-AL09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 8.4",
        "adinfo": "SHT-W09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 Pro",
        "adinfo": "CMR-AL19"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 Pro",
        "adinfo": "CMR-W19"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 lite",
        "adinfo": "BAH2-L09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 lite",
        "adinfo": "BAH2-W19"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 lite",
        "adinfo": "JDN2-L09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad M5 lite",
        "adinfo": "JDN2-W09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad T3 10",
        "adinfo": "AGS-L03"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad T3 10",
        "adinfo": "AGS-L09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad T3 10",
        "adinfo": "AGS-W09"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad T3 7",
        "adinfo": "BG2-U03"
    },
    {
        "packinfo": "HuaweiHUAWEI MediaPad T5",
        "adinfo": "AGS2-W09"
    },
    {
        "packinfo": "HuaweiHUAWEI Nova 3i",
        "adinfo": "INE-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart",
        "adinfo": "FIG-LA1"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart",
        "adinfo": "FIG-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart",
        "adinfo": "FIG-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart 2019",
        "adinfo": "POT-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart 2019",
        "adinfo": "POT-LX1AF"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart 2019",
        "adinfo": "POT-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart 2020",
        "adinfo": "POT-LX1A"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart 2020",
        "adinfo": "POT-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart Pro",
        "adinfo": "STK-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart Pro",
        "adinfo": "STK-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart Z",
        "adinfo": "STK-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI P smart+ 2019",
        "adinfo": "POT-LX1T"
    },
    {
        "packinfo": "HuaweiHUAWEI P20 Lite",
        "adinfo": "ANE-LX2J"
    },
    {
        "packinfo": "HuaweiHUAWEI P20 Lite",
        "adinfo": "HWV32"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-AL00"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-L04"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-L09"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-L14"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-L29"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-L39"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-L49"
    },
    {
        "packinfo": "HuaweiHUAWEI P30",
        "adinfo": "ELE-TL00"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "HWV33"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX1A"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX1Am"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX1B"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX1M"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX1Mm"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX2B"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX2m"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX3A"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX3Am"
    },
    {
        "packinfo": "HuaweiHUAWEI P30 lite",
        "adinfo": "MAR-LX3Bm"
    },
    {
        "packinfo": "HuaweiHUAWEI P9 lite mini",
        "adinfo": "SLA-L02"
    },
    {
        "packinfo": "HuaweiHUAWEI P9 lite mini",
        "adinfo": "SLA-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI P9 lite mini",
        "adinfo": "SLA-L23"
    },
    {
        "packinfo": "HuaweiHUAWEI Y MAX",
        "adinfo": "ARS-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI Y3 2017",
        "adinfo": "CRO-L02"
    },
    {
        "packinfo": "HuaweiHUAWEI Y3 2017",
        "adinfo": "CRO-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI Y3 2017",
        "adinfo": "HUAWEI CRO-L02"
    },
    {
        "packinfo": "HuaweiHUAWEI Y3 2017",
        "adinfo": "HUAWEI CRO-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI Y3 2018",
        "adinfo": "CAG-L02"
    },
    {
        "packinfo": "HuaweiHUAWEI Y3 2018",
        "adinfo": "CAG-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2018",
        "adinfo": "DRA-L01"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2018",
        "adinfo": "DRA-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2018",
        "adinfo": "DRA-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2018",
        "adinfo": "DRA-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2019",
        "adinfo": "AMN-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2019",
        "adinfo": "AMN-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2019",
        "adinfo": "AMN-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 2019",
        "adinfo": "AMN-LX9"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 Prime 2018",
        "adinfo": "DRA-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 lite",
        "adinfo": "DRA-LX5"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 lite 2017",
        "adinfo": "CRO-L03"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 lite 2017",
        "adinfo": "CRO-L23"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 lite 2017",
        "adinfo": "HUAWEI CRO-L03"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 lite 2017",
        "adinfo": "HUAWEI CRO-L23"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 lite 2018",
        "adinfo": "CAG-L03"
    },
    {
        "packinfo": "HuaweiHUAWEI Y5 lite 2018",
        "adinfo": "CAG-L23"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2017",
        "adinfo": "MYA-L11"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2018",
        "adinfo": "ATU-L11"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2018",
        "adinfo": "ATU-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2018",
        "adinfo": "ATU-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2018",
        "adinfo": "ATU-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2019",
        "adinfo": "MRD-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2019",
        "adinfo": "MRD-LX1F"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2019",
        "adinfo": "MRD-LX1N"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 2019",
        "adinfo": "MRD-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 Prime 2018",
        "adinfo": "ATU-L31"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 Prime 2018",
        "adinfo": "ATU-L42"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6 Pro 2019",
        "adinfo": "MRD-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6II",
        "adinfo": "HUAWEI CAM-L53"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6s",
        "adinfo": "JAT-L29"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6s",
        "adinfo": "JAT-L41"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6s",
        "adinfo": "JAT-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y6s",
        "adinfo": "JAT-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 2018",
        "adinfo": "LDN-L01"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 2018",
        "adinfo": "LDN-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 2018",
        "adinfo": "LDN-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 2019",
        "adinfo": "DUB-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 2019",
        "adinfo": "DUB-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 Prime 2018",
        "adinfo": "LDN-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 Prime 2018",
        "adinfo": "LDN-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7 Pro 2019",
        "adinfo": "DUB-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7s",
        "adinfo": "DUB-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7s",
        "adinfo": "DUB-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y7s",
        "adinfo": "DUB-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y8s",
        "adinfo": "JKM-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y8s",
        "adinfo": "JKM-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y8s",
        "adinfo": "JKM-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9 2018",
        "adinfo": "FLA-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9 2018",
        "adinfo": "FLA-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9 2018",
        "adinfo": "FLA-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9 2019",
        "adinfo": "JKM-LX1"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9 2019",
        "adinfo": "JKM-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9 2019",
        "adinfo": "JKM-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9 Prime 2019",
        "adinfo": "STK-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9s",
        "adinfo": "STK-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9s",
        "adinfo": "STK-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI Y9s",
        "adinfo": "STK-LX3"
    },
    {
        "packinfo": "HuaweiHUAWEI nova 2 Plus",
        "adinfo": "BAC-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI nova 2 Plus",
        "adinfo": "BAC-L22"
    },
    {
        "packinfo": "HuaweiHUAWEI nova 2 lite",
        "adinfo": "LDN-LX2"
    },
    {
        "packinfo": "HuaweiHUAWEI nova 5T",
        "adinfo": "YAL-L21"
    },
    {
        "packinfo": "HuaweiHUAWEI nova 5T Pro",
        "adinfo": "YAL-L41"
    },
    {
        "packinfo": "HuaweiHUAWEI nova lite 2",
        "adinfo": "704HW"
    },
    {
        "packinfo": "HuaweiHUAWEI nova lite 3",
        "adinfo": "POT-LX2J"
    },
    {
        "packinfo": "HuaweiHUAWEI nova lite 3+",
        "adinfo": "POT-LX2J"
    },
    {
        "packinfo": "HuaweiHUAWEI nova lite for Y!mobile",
        "adinfo": "608HW"
    },
    {
        "packinfo": "HuaweiHUWEI MediaPad T3",
        "adinfo": "KOB-L09"
    },
    {
        "packinfo": "HuaweiHUWEI MediaPad T3",
        "adinfo": "KOB-W09"
    },
    {
        "packinfo": "HuaweiHW-03E",
        "adinfo": "HW-03E"
    },
    {
        "packinfo": "HuaweiHWT31",
        "adinfo": "HWT31"
    },
    {
        "packinfo": "HuaweiHol-T00",
        "adinfo": "Hol-T00"
    },
    {
        "packinfo": "HuaweiHol-U10",
        "adinfo": "Hol-U10"
    },
    {
        "packinfo": "HuaweiHol-U19",
        "adinfo": "Hol-U19"
    },
    {
        "packinfo": "HuaweiHonor 10",
        "adinfo": "COL-AL00"
    },
    {
        "packinfo": "HuaweiHonor 10",
        "adinfo": "COL-AL10"
    },
    {
        "packinfo": "HuaweiHonor 10",
        "adinfo": "COL-L29"
    },
    {
        "packinfo": "HuaweiHonor 10",
        "adinfo": "COL-TL10"
    },
    {
        "packinfo": "HuaweiHonor 10 Lite",
        "adinfo": "HRY-AL00"
    },
    {
        "packinfo": "HuaweiHonor 10 Lite",
        "adinfo": "HRY-AL00a"
    },
    {
        "packinfo": "HuaweiHonor 20i",
        "adinfo": "HRY-AL00Ta"
    },
    {
        "packinfo": "HuaweiHonor 4A",
        "adinfo": "SCC-U21"
    },
    {
        "packinfo": "HuaweiHonor 4A",
        "adinfo": "SCL-AL00"
    },
    {
        "packinfo": "HuaweiHonor 4A",
        "adinfo": "SCL-CL00"
    },
    {
        "packinfo": "HuaweiHonor 4A",
        "adinfo": "SCL-TL00"
    },
    {
        "packinfo": "HuaweiHonor 4A",
        "adinfo": "SCL-TL00H"
    },
    {
        "packinfo": "HuaweiHonor 5A",
        "adinfo": "HUAWEI LYO-L21"
    },
    {
        "packinfo": "HuaweiHonor 5A",
        "adinfo": "LYO-L21"
    },
    {
        "packinfo": "HuaweiHonor 5C",
        "adinfo": "NEM-L21"
    },
    {
        "packinfo": "HuaweiHonor 5C",
        "adinfo": "NEM-L22"
    },
    {
        "packinfo": "HuaweiHonor 5C",
        "adinfo": "NEM-L51"
    },
    {
        "packinfo": "HuaweiHonor 5X",
        "adinfo": "KIW-L21"
    },
    {
        "packinfo": "HuaweiHonor 5X",
        "adinfo": "KIW-TL00H"
    },
    {
        "packinfo": "HuaweiHonor 6A",
        "adinfo": "DLI-L22"
    },
    {
        "packinfo": "HuaweiHonor 6A",
        "adinfo": "DLI-TL20"
    },
    {
        "packinfo": "HuaweiHonor 6X",
        "adinfo": "BLN-L24"
    },
    {
        "packinfo": "HuaweiHonor 7",
        "adinfo": "PLK-AL10"
    },
    {
        "packinfo": "HuaweiHonor 7",
        "adinfo": "PLK-CL00"
    },
    {
        "packinfo": "HuaweiHonor 7",
        "adinfo": "PLK-L01"
    },
    {
        "packinfo": "HuaweiHonor 7",
        "adinfo": "PLK-TL00"
    },
    {
        "packinfo": "HuaweiHonor 7",
        "adinfo": "PLK-TL01H"
    },
    {
        "packinfo": "HuaweiHonor 7",
        "adinfo": "PLK-UL00"
    },
    {
        "packinfo": "HuaweiHonor 7A",
        "adinfo": "AUM-AL00"
    },
    {
        "packinfo": "HuaweiHonor 7A",
        "adinfo": "AUM-AL20"
    },
    {
        "packinfo": "HuaweiHonor 7A",
        "adinfo": "AUM-L29"
    },
    {
        "packinfo": "HuaweiHonor 7A",
        "adinfo": "AUM-L33"
    },
    {
        "packinfo": "HuaweiHonor 7A",
        "adinfo": "AUM-TL00"
    },
    {
        "packinfo": "HuaweiHonor 7A",
        "adinfo": "AUM-TL20"
    },
    {
        "packinfo": "HuaweiHonor 7A",
        "adinfo": "DUA-L22"
    },
    {
        "packinfo": "HuaweiHonor 7C",
        "adinfo": "AUM-L41"
    },
    {
        "packinfo": "HuaweiHonor 7C",
        "adinfo": "LND-AL30"
    },
    {
        "packinfo": "HuaweiHonor 7C",
        "adinfo": "LND-AL40"
    },
    {
        "packinfo": "HuaweiHonor 7C",
        "adinfo": "LND-L29"
    },
    {
        "packinfo": "HuaweiHonor 7C",
        "adinfo": "LND-TL30"
    },
    {
        "packinfo": "HuaweiHonor 7C",
        "adinfo": "LND-TL40"
    },
    {
        "packinfo": "HuaweiHonor 7S",
        "adinfo": "DRA-LX5"
    },
    {
        "packinfo": "HuaweiHonor 7S",
        "adinfo": "DUA-AL00"
    },
    {
        "packinfo": "HuaweiHonor 7S",
        "adinfo": "DUA-L22"
    },
    {
        "packinfo": "HuaweiHonor 7S",
        "adinfo": "DUA-LX3"
    },
    {
        "packinfo": "HuaweiHonor 7X",
        "adinfo": "BND-L21"
    },
    {
        "packinfo": "HuaweiHonor 7X",
        "adinfo": "BND-L24"
    },
    {
        "packinfo": "HuaweiHonor 7X",
        "adinfo": "BND-L31"
    },
    {
        "packinfo": "HuaweiHonor 7i",
        "adinfo": "ATH-AL00"
    },
    {
        "packinfo": "HuaweiHonor 7i",
        "adinfo": "ATH-CL00"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-AL00"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-AL10"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-DL00"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-L04"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-L09"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-L14"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-L19"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-L24"
    },
    {
        "packinfo": "HuaweiHonor 8",
        "adinfo": "FRD-TL00"
    },
    {
        "packinfo": "HuaweiHonor 8 Lite",
        "adinfo": "PRA-LX1"
    },
    {
        "packinfo": "HuaweiHonor 8 Pro",
        "adinfo": "DUK-L09"
    },
    {
        "packinfo": "HuaweiHonor 8 Smart",
        "adinfo": "VEN-L22"
    },
    {
        "packinfo": "HuaweiHonor 8A",
        "adinfo": "JAT-AL00"
    },
    {
        "packinfo": "HuaweiHonor 8A",
        "adinfo": "JAT-L29"
    },
    {
        "packinfo": "HuaweiHonor 8A",
        "adinfo": "JAT-L41"
    },
    {
        "packinfo": "HuaweiHonor 8A",
        "adinfo": "JAT-LX1"
    },
    {
        "packinfo": "HuaweiHonor 8A",
        "adinfo": "JAT-LX3"
    },
    {
        "packinfo": "HuaweiHonor 8C",
        "adinfo": "BKK-L21"
    },
    {
        "packinfo": "HuaweiHonor 8X",
        "adinfo": "JSN-L21"
    },
    {
        "packinfo": "HuaweiHonor 8X",
        "adinfo": "JSN-L22"
    },
    {
        "packinfo": "HuaweiHonor 8X",
        "adinfo": "JSN-L23"
    },
    {
        "packinfo": "HuaweiHonor 8X Max",
        "adinfo": "ARE-L22HN"
    },
    {
        "packinfo": "HuaweiHonor 8x",
        "adinfo": "JSN-L42"
    },
    {
        "packinfo": "HuaweiHonor 9",
        "adinfo": "STF-AL00"
    },
    {
        "packinfo": "HuaweiHonor 9",
        "adinfo": "STF-AL10"
    },
    {
        "packinfo": "HuaweiHonor 9",
        "adinfo": "STF-L09"
    },
    {
        "packinfo": "HuaweiHonor 9",
        "adinfo": "STF-L09S"
    },
    {
        "packinfo": "HuaweiHonor 9",
        "adinfo": "STF-TL10"
    },
    {
        "packinfo": "HuaweiHonor 9 Lite",
        "adinfo": "LLD-L21"
    },
    {
        "packinfo": "HuaweiHonor 9 Lite",
        "adinfo": "LLD-L31"
    },
    {
        "packinfo": "HuaweiHonor 9N",
        "adinfo": "LLD-AL20"
    },
    {
        "packinfo": "HuaweiHonor Box",
        "adinfo": "M321"
    },
    {
        "packinfo": "HuaweiHonor Box Pro",
        "adinfo": "HiTV-M1"
    },
    {
        "packinfo": "HuaweiHonor Box voice",
        "adinfo": "M311"
    },
    {
        "packinfo": "HuaweiHonor Magic",
        "adinfo": "HUAWEI NTS-AL00"
    },
    {
        "packinfo": "HuaweiHonor Magic",
        "adinfo": "NTS-AL00"
    },
    {
        "packinfo": "HuaweiHonor Magic 2",
        "adinfo": "TNY-AL00"
    },
    {
        "packinfo": "HuaweiHonor Magic 2",
        "adinfo": "TNY-TL00"
    },
    {
        "packinfo": "HuaweiHonor Note10",
        "adinfo": "RVL-AL09"
    },
    {
        "packinfo": "HuaweiHonor Play",
        "adinfo": "COR-AL00"
    },
    {
        "packinfo": "HuaweiHonor Play",
        "adinfo": "COR-AL10"
    },
    {
        "packinfo": "HuaweiHonor Play",
        "adinfo": "COR-L29"
    },
    {
        "packinfo": "HuaweiHonor Play",
        "adinfo": "COR-TL10"
    },
    {
        "packinfo": "HuaweiHonor V10",
        "adinfo": "BKL-AL00"
    },
    {
        "packinfo": "HuaweiHonor V10",
        "adinfo": "BKL-AL20"
    },
    {
        "packinfo": "HuaweiHonor V10",
        "adinfo": "BKL-TL10"
    },
    {
        "packinfo": "HuaweiHonor V8",
        "adinfo": "KNT-AL10"
    },
    {
        "packinfo": "HuaweiHonor V8",
        "adinfo": "KNT-AL20"
    },
    {
        "packinfo": "HuaweiHonor V8",
        "adinfo": "KNT-TL10"
    },
    {
        "packinfo": "HuaweiHonor V8",
        "adinfo": "KNT-UL10"
    },
    {
        "packinfo": "HuaweiHonor V9",
        "adinfo": "DUK-AL20"
    },
    {
        "packinfo": "HuaweiHonor V9",
        "adinfo": "DUK-TL30"
    },
    {
        "packinfo": "HuaweiHonor View 10",
        "adinfo": "BKL-L04"
    },
    {
        "packinfo": "HuaweiHonor View 10",
        "adinfo": "BKL-L09"
    },
    {
        "packinfo": "HuaweiHonor3",
        "adinfo": "H30-T10"
    },
    {
        "packinfo": "HuaweiHonor3",
        "adinfo": "H30-U10"
    },
    {
        "packinfo": "HuaweiHonor3",
        "adinfo": "HUAWEI HN3-U00"
    },
    {
        "packinfo": "HuaweiHonor3",
        "adinfo": "HUAWEI HN3-U01"
    },
    {
        "packinfo": "HuaweiHonor 8A",
        "adinfo": "JAT-AL00"
    },
    {
        "packinfo": "HuaweiHuawei Ascend XT2™",
        "adinfo": "H1711"
    },
    {
        "packinfo": "HuaweiHuawei Elate™",
        "adinfo": "H1711z"
    },
    {
        "packinfo": "HuaweiHuawei Mate 20 X",
        "adinfo": "EVR-L29"
    },
    {
        "packinfo": "HuaweiHuawei Mate 20 X",
        "adinfo": "EVR-TL00"
    },
    {
        "packinfo": "HuaweiHuawei Mate 20 X (5G)",
        "adinfo": "EVR-N29"
    },
    {
        "packinfo": "HuaweiHuawei MediaPad T5",
        "adinfo": "AGS2-L03"
    },
    {
        "packinfo": "HuaweiHuawei MediaPad T5",
        "adinfo": "AGS2-L09"
    },
    {
        "packinfo": "HuaweiHuawei MediaPad T5",
        "adinfo": "AGS2-W19"
    },
    {
        "packinfo": "HuaweiHuawei Nova 2",
        "adinfo": "PIC-LX9"
    },
    {
        "packinfo": "HuaweiHuawei P30",
        "adinfo": "ELE-L09"
    },
    {
        "packinfo": "HuaweiHuawei Y9 2019",
        "adinfo": "JKM-AL00a"
    },
    {
        "packinfo": "HuaweiHuawei Y9s",
        "adinfo": "STK-L21"
    },
    {
        "packinfo": "HuaweiHuwei Mate 20 X",
        "adinfo": "EVR-AL00"
    },
    {
        "packinfo": "HuaweiIDEOS",
        "adinfo": "Comet"
    },
    {
        "packinfo": "HuaweiIDEOS",
        "adinfo": "Ideos"
    },
    {
        "packinfo": "HuaweiIDEOS",
        "adinfo": "Ideos"
    },
    {
        "packinfo": "HuaweiIce-Twist",
        "adinfo": "Ice-Twist"
    },
    {
        "packinfo": "HuaweiIdeos X5",
        "adinfo": "Huawei U8800-51"
    },
    {
        "packinfo": "HuaweiIdeos X5",
        "adinfo": "IDEOS X5"
    },
    {
        "packinfo": "HuaweiIdeos X5",
        "adinfo": "U8800"
    },
    {
        "packinfo": "HuaweiIdeos X5",
        "adinfo": "U8800-51"
    },
    {
        "packinfo": "HuaweiKiwi-2",
        "adinfo": "H1622"
    },
    {
        "packinfo": "HuaweiLISZT",
        "adinfo": "HUAWEI M2-A01L"
    },
    {
        "packinfo": "HuaweiLISZT",
        "adinfo": "HUAWEI M2-A01W"
    },
    {
        "packinfo": "HuaweiM2",
        "adinfo": "HUAWEI M2-801L"
    },
    {
        "packinfo": "HuaweiM2",
        "adinfo": "HUAWEI M2-801W"
    },
    {
        "packinfo": "HuaweiM2",
        "adinfo": "HUAWEI M2-802L"
    },
    {
        "packinfo": "HuaweiM2",
        "adinfo": "HUAWEI M2-803L"
    },
    {
        "packinfo": "HuaweiM220",
        "adinfo": "M220"
    },
    {
        "packinfo": "HuaweiM220",
        "adinfo": "M220c"
    },
    {
        "packinfo": "HuaweiM220",
        "adinfo": "dTV01"
    },
    {
        "packinfo": "HuaweiM3",
        "adinfo": "BTV-DL09"
    },
    {
        "packinfo": "HuaweiM3",
        "adinfo": "BTV-W09"
    },
    {
        "packinfo": "HuaweiM310",
        "adinfo": "M310"
    },
    {
        "packinfo": "HuaweiM620",
        "adinfo": "M620"
    },
    {
        "packinfo": "HuaweiM620",
        "adinfo": "TB01"
    },
    {
        "packinfo": "HuaweiM835",
        "adinfo": "HUAWEI-M835"
    },
    {
        "packinfo": "HuaweiM860",
        "adinfo": "M860"
    },
    {
        "packinfo": "HuaweiM865",
        "adinfo": "M865"
    },
    {
        "packinfo": "HuaweiM865",
        "adinfo": "USCCADR3305"
    },
    {
        "packinfo": "HuaweiM868",
        "adinfo": "HUAWEI M868"
    },
    {
        "packinfo": "HuaweiMAIMANG 6",
        "adinfo": "RNE-AL00"
    },
    {
        "packinfo": "HuaweiMAIMANG 7",
        "adinfo": "SNE-AL00"
    },
    {
        "packinfo": "HuaweiMS4C",
        "adinfo": "MS4C"
    },
    {
        "packinfo": "HuaweiMT1",
        "adinfo": "HUAWEI MT1-U06"
    },
    {
        "packinfo": "HuaweiMT2-L01",
        "adinfo": "HUAWEI MT2-L01"
    },
    {
        "packinfo": "HuaweiMT2-L02",
        "adinfo": "HUAWEI MT2-L02"
    },
    {
        "packinfo": "HuaweiMT2-L03",
        "adinfo": "MT2L03"
    },
    {
        "packinfo": "HuaweiMT2-L05",
        "adinfo": "HUAWEI MT2-L05"
    },
    {
        "packinfo": "HuaweiMT2L03LITE",
        "adinfo": "MT2L03"
    },
    {
        "packinfo": "HuaweiMate",
        "adinfo": "HUAWEI MT1-T00"
    },
    {
        "packinfo": "HuaweiMate 10",
        "adinfo": "ALP-AL00"
    },
    {
        "packinfo": "HuaweiMate 10",
        "adinfo": "ALP-L09"
    },
    {
        "packinfo": "HuaweiMate 10",
        "adinfo": "ALP-L29"
    },
    {
        "packinfo": "HuaweiMate 10",
        "adinfo": "ALP-TL00"
    },
    {
        "packinfo": "HuaweiMate 10 Pro",
        "adinfo": "BLA-A09"
    },
    {
        "packinfo": "HuaweiMate 10 Pro",
        "adinfo": "BLA-AL00"
    },
    {
        "packinfo": "HuaweiMate 10 Pro",
        "adinfo": "BLA-L09"
    },
    {
        "packinfo": "HuaweiMate 10 Pro",
        "adinfo": "BLA-L29"
    },
    {
        "packinfo": "HuaweiMate 10 Pro",
        "adinfo": "BLA-TL00"
    },
    {
        "packinfo": "HuaweiMate 10 lite",
        "adinfo": "RNE-L01"
    },
    {
        "packinfo": "HuaweiMate 10 lite",
        "adinfo": "RNE-L03"
    },
    {
        "packinfo": "HuaweiMate 10 lite",
        "adinfo": "RNE-L21"
    },
    {
        "packinfo": "HuaweiMate 10 lite",
        "adinfo": "RNE-L23"
    },
    {
        "packinfo": "HuaweiMate 20",
        "adinfo": "HMA-AL00"
    },
    {
        "packinfo": "HuaweiMate 20",
        "adinfo": "HMA-L09"
    },
    {
        "packinfo": "HuaweiMate 20",
        "adinfo": "HMA-L29"
    },
    {
        "packinfo": "HuaweiMate 20",
        "adinfo": "HMA-TL00"
    },
    {
        "packinfo": "HuaweiMate 20 Pro",
        "adinfo": "LYA-AL00"
    },
    {
        "packinfo": "HuaweiMate 20 Pro",
        "adinfo": "LYA-AL10"
    },
    {
        "packinfo": "HuaweiMate 20 Pro",
        "adinfo": "LYA-L09"
    },
    {
        "packinfo": "HuaweiMate 20 Pro",
        "adinfo": "LYA-L29"
    },
    {
        "packinfo": "HuaweiMate 20 Pro",
        "adinfo": "LYA-TL00"
    },
    {
        "packinfo": "HuaweiMate 20 RS",
        "adinfo": "LYA-AL00P"
    },
    {
        "packinfo": "HuaweiMate 20 lite",
        "adinfo": "SNE-LX1"
    },
    {
        "packinfo": "HuaweiMate 20 lite",
        "adinfo": "SNE-LX2"
    },
    {
        "packinfo": "HuaweiMate 20 lite",
        "adinfo": "SNE-LX3"
    },
    {
        "packinfo": "HuaweiMate 7",
        "adinfo": "HUAWEI MT7-CL00"
    },
    {
        "packinfo": "HuaweiMate 7",
        "adinfo": "HUAWEI MT7-J1"
    },
    {
        "packinfo": "HuaweiMate 7",
        "adinfo": "HUAWEI MT7-L09"
    },
    {
        "packinfo": "HuaweiMate 7",
        "adinfo": "HUAWEI MT7-TL00"
    },
    {
        "packinfo": "HuaweiMate 7",
        "adinfo": "HUAWEI MT7-TL10"
    },
    {
        "packinfo": "HuaweiMate 7",
        "adinfo": "HUAWEI MT7-UL00"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "HUAWEI NXT-AL10"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "HUAWEI NXT-CL00"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "HUAWEI NXT-DL00"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "HUAWEI NXT-L09"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "HUAWEI NXT-L29"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "HUAWEI NXT-TL00"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "HUAWEI NXT-TL00B"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "NXT-AL10"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "NXT-CL00"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "NXT-DL00"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "NXT-L09"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "NXT-L29"
    },
    {
        "packinfo": "HuaweiMate 8",
        "adinfo": "NXT-TL00"
    },
    {
        "packinfo": "HuaweiMate 9",
        "adinfo": "MHA-AL00"
    },
    {
        "packinfo": "HuaweiMate 9",
        "adinfo": "MHA-L09"
    },
    {
        "packinfo": "HuaweiMate 9",
        "adinfo": "MHA-L29"
    },
    {
        "packinfo": "HuaweiMate 9",
        "adinfo": "MHA-TL00"
    },
    {
        "packinfo": "HuaweiMate 9 Pro",
        "adinfo": "LON-AL00"
    },
    {
        "packinfo": "HuaweiMate 9 Pro",
        "adinfo": "LON-L29"
    },
    {
        "packinfo": "HuaweiMate S",
        "adinfo": "HUAWEI CRR-CL00"
    },
    {
        "packinfo": "HuaweiMate S",
        "adinfo": "HUAWEI CRR-CL20"
    },
    {
        "packinfo": "HuaweiMate S",
        "adinfo": "HUAWEI CRR-L09"
    },
    {
        "packinfo": "HuaweiMate S",
        "adinfo": "HUAWEI CRR-TL00"
    },
    {
        "packinfo": "HuaweiMate S",
        "adinfo": "HUAWEI CRR-UL00"
    },
    {
        "packinfo": "HuaweiMate S",
        "adinfo": "HUAWEI CRR-UL20"
    },
    {
        "packinfo": "HuaweiMate2",
        "adinfo": "HUAWEI MT2-C00"
    },
    {
        "packinfo": "HuaweiMediaPad",
        "adinfo": "HUAWEI MediaPad T1 7.0 3G"
    },
    {
        "packinfo": "HuaweiMediaPad",
        "adinfo": "T1 7.0"
    },
    {
        "packinfo": "HuaweiMediaPad",
        "adinfo": "T1-701u"
    },
    {
        "packinfo": "HuaweiMediaPad",
        "adinfo": "T1-701ua"
    },
    {
        "packinfo": "HuaweiMediaPad",
        "adinfo": "T1-701us"
    },
    {
        "packinfo": "HuaweiMediaPad",
        "adinfo": "T1-701w"
    },
    {
        "packinfo": "HuaweiMediaPad",
        "adinfo": "Telpad QS"
    },
    {
        "packinfo": "HuaweiMediaPad 10 FHD",
        "adinfo": "MediaPad 10 FHD"
    },
    {
        "packinfo": "HuaweiMediaPad 10 Link",
        "adinfo": "MediaPad 10 LINK"
    },
    {
        "packinfo": "HuaweiMediaPad 10 Link",
        "adinfo": "dtab 01"
    },
    {
        "packinfo": "HuaweiMediaPad 10 Link+",
        "adinfo": "402HW"
    },
    {
        "packinfo": "HuaweiMediaPad 10 Link+",
        "adinfo": "MediaPad 10 Link+"
    },
    {
        "packinfo": "HuaweiMediaPad 10 Link+",
        "adinfo": "S10-232L"
    },
    {
        "packinfo": "HuaweiMediaPad 10 Link+",
        "adinfo": "SpeedTAB"
    },
    {
        "packinfo": "HuaweiMediaPad 7 Lite",
        "adinfo": "MediaPad 7 Lite"
    },
    {
        "packinfo": "HuaweiMediaPad 7 Lite Quad",
        "adinfo": "Telpad QS"
    },
    {
        "packinfo": "HuaweiMediaPad 7 Lite Quad",
        "adinfo": "Telpad Quad S"
    },
    {
        "packinfo": "HuaweiMediaPad 7 Vogue",
        "adinfo": "MediaPad 7 Vogue"
    },
    {
        "packinfo": "HuaweiMediaPad 7 Youth2",
        "adinfo": "MediaPad 7 Youth 2"
    },
    {
        "packinfo": "HuaweiMediaPad 7 Youth2",
        "adinfo": "S7-721u"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "403HW"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "CNPC Security Pad S1"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "HUAWEI MediaPad M1 8.0"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "MediaPad M1 8.0"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "MediaPad M1 8.0 (LTE)"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "MediaPad M1 8.0 (WIFI)"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "S8-303L"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "S8-303LT"
    },
    {
        "packinfo": "HuaweiMediaPad M1 8.0",
        "adinfo": "S8-306L"
    },
    {
        "packinfo": "HuaweiMediaPad M3 Lite 10",
        "adinfo": "BAH-AL00"
    },
    {
        "packinfo": "HuaweiMediaPad M3 Lite 10",
        "adinfo": "BAH-L09"
    },
    {
        "packinfo": "HuaweiMediaPad M3 Lite 10",
        "adinfo": "BAH-W09"
    },
    {
        "packinfo": "HuaweiMediaPad T2 10.0 Pro",
        "adinfo": "605HW"
    },
    {
        "packinfo": "HuaweiMediaPad T2 10.0 Pro",
        "adinfo": "606HW"
    },
    {
        "packinfo": "HuaweiMediaPad T2 10.0 Pro",
        "adinfo": "FDR-A05L"
    },
    {
        "packinfo": "HuaweiMediaPad T2 10.0 pro",
        "adinfo": "FDR-A01L"
    },
    {
        "packinfo": "HuaweiMediaPad T2 10.0 pro",
        "adinfo": "FDR-A01w"
    },
    {
        "packinfo": "HuaweiMediaPad T2 10.0 pro",
        "adinfo": "FDR-A03L"
    },
    {
        "packinfo": "HuaweiMediaPad T2 7.0",
        "adinfo": "BGO-DL09"
    },
    {
        "packinfo": "HuaweiMediaPad T2 7.0",
        "adinfo": "BGO-L03"
    },
    {
        "packinfo": "HuaweiMediaPad T2 8.0 Pro",
        "adinfo": "JDN-AL00"
    },
    {
        "packinfo": "HuaweiMediaPad T2 8.0 Pro",
        "adinfo": "JDN-L01"
    },
    {
        "packinfo": "HuaweiMediaPad T2 8.0 Pro",
        "adinfo": "JDN-W09"
    },
    {
        "packinfo": "HuaweiMediaPad T3 7",
        "adinfo": "BG2-U01"
    },
    {
        "packinfo": "HuaweiMediaPad T3 7",
        "adinfo": "BG2-W09"
    },
    {
        "packinfo": "HuaweiMediaPad Vogue",
        "adinfo": "MediaPad 7 Lite II"
    },
    {
        "packinfo": "HuaweiMediaPad Vogue",
        "adinfo": "MediaPad 7 Vogue"
    },
    {
        "packinfo": "HuaweiMediaPad X1 7.0",
        "adinfo": "7D-501u"
    },
    {
        "packinfo": "HuaweiMediaPad X1 7.0",
        "adinfo": "MediaPad X1"
    },
    {
        "packinfo": "HuaweiMediaPad X1 7.0",
        "adinfo": "MediaPad X1 7.0"
    },
    {
        "packinfo": "HuaweiMediaPad X1 7.0",
        "adinfo": "X1 7.0"
    },
    {
        "packinfo": "HuaweiMediaPad Youth",
        "adinfo": "MediaPad 7 Youth"
    },
    {
        "packinfo": "HuaweiMediaPad7",
        "adinfo": "MediaPad 7 Vogue"
    },
    {
        "packinfo": "HuaweiMediaQ M380",
        "adinfo": "M380-10"
    },
    {
        "packinfo": "HuaweiNexus 6P",
        "adinfo": "Nexus 6P"
    },
    {
        "packinfo": "HuaweiNova 3i",
        "adinfo": "INE-LX2r"
    },
    {
        "packinfo": "HuaweiP10",
        "adinfo": "VTR-AL00"
    },
    {
        "packinfo": "HuaweiP10",
        "adinfo": "VTR-L09"
    },
    {
        "packinfo": "HuaweiP10",
        "adinfo": "VTR-L29"
    },
    {
        "packinfo": "HuaweiP10",
        "adinfo": "VTR-TL00"
    },
    {
        "packinfo": "HuaweiP10 Plus",
        "adinfo": "VKY-AL00"
    },
    {
        "packinfo": "HuaweiP10 Plus",
        "adinfo": "VKY-L09"
    },
    {
        "packinfo": "HuaweiP10 Plus",
        "adinfo": "VKY-L29"
    },
    {
        "packinfo": "HuaweiP10 Plus",
        "adinfo": "VKY-TL00"
    },
    {
        "packinfo": "HuaweiP10 lite",
        "adinfo": "WAS-L03T"
    },
    {
        "packinfo": "HuaweiP10 lite",
        "adinfo": "WAS-LX1"
    },
    {
        "packinfo": "HuaweiP10 lite",
        "adinfo": "WAS-LX1A"
    },
    {
        "packinfo": "HuaweiP10 lite",
        "adinfo": "WAS-LX2"
    },
    {
        "packinfo": "HuaweiP10 lite",
        "adinfo": "WAS-LX2J"
    },
    {
        "packinfo": "HuaweiP10 lite",
        "adinfo": "WAS-LX3"
    },
    {
        "packinfo": "HuaweiP2",
        "adinfo": "HUAWEI P2-6070"
    },
    {
        "packinfo": "HuaweiP20",
        "adinfo": "EML-AL00"
    },
    {
        "packinfo": "HuaweiP20",
        "adinfo": "EML-L09"
    },
    {
        "packinfo": "HuaweiP20",
        "adinfo": "EML-L29"
    },
    {
        "packinfo": "HuaweiP20",
        "adinfo": "EML-TL00"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "HW-01K"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-AL00"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-AL00l"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-AL01"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-L04"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-L09"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-L29"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-TL00"
    },
    {
        "packinfo": "HuaweiP20 Pro",
        "adinfo": "CLT-TL01"
    },
    {
        "packinfo": "HuaweiP20 lite",
        "adinfo": "ANE-LX1"
    },
    {
        "packinfo": "HuaweiP20 lite",
        "adinfo": "ANE-LX2"
    },
    {
        "packinfo": "HuaweiP20 lite",
        "adinfo": "ANE-LX3"
    },
    {
        "packinfo": "HuaweiP20Pro",
        "adinfo": "CLT-L09"
    },
    {
        "packinfo": "HuaweiP20Pro",
        "adinfo": "CLT-L29"
    },
    {
        "packinfo": "HuaweiP30 Pro",
        "adinfo": "HW-02L"
    },
    {
        "packinfo": "HuaweiP30 Pro",
        "adinfo": "VOG-AL00"
    },
    {
        "packinfo": "HuaweiP30 Pro",
        "adinfo": "VOG-AL10"
    },
    {
        "packinfo": "HuaweiP30 Pro",
        "adinfo": "VOG-L04"
    },
    {
        "packinfo": "HuaweiP30 Pro",
        "adinfo": "VOG-L09"
    },
    {
        "packinfo": "HuaweiP30 Pro",
        "adinfo": "VOG-L29"
    },
    {
        "packinfo": "HuaweiP30 Pro",
        "adinfo": "VOG-TL00"
    },
    {
        "packinfo": "HuaweiP30 lite",
        "adinfo": "MAR-LX2J"
    },
    {
        "packinfo": "HuaweiP6",
        "adinfo": "HUAWEI P6-C00"
    },
    {
        "packinfo": "HuaweiP6",
        "adinfo": "HUAWEI P6-T00"
    },
    {
        "packinfo": "HuaweiP6",
        "adinfo": "HUAWEI P6-T00V"
    },
    {
        "packinfo": "HuaweiP6",
        "adinfo": "HUAWEI Ascend P6"
    },
    {
        "packinfo": "HuaweiP6",
        "adinfo": "HUAWEI P6-U06"
    },
    {
        "packinfo": "HuaweiP6",
        "adinfo": "HUAWEI P6-U06-orange"
    },
    {
        "packinfo": "HuaweiP6S",
        "adinfo": "P6 S-L04"
    },
    {
        "packinfo": "HuaweiP6S-L04",
        "adinfo": "302HW"
    },
    {
        "packinfo": "HuaweiP6S-U06",
        "adinfo": "HUAWEI P6 S-U06"
    },
    {
        "packinfo": "HuaweiP7",
        "adinfo": "HUAWEI P7-L00"
    },
    {
        "packinfo": "HuaweiP7",
        "adinfo": "HUAWEI P7-L05"
    },
    {
        "packinfo": "HuaweiP7",
        "adinfo": "HUAWEI P7-L07"
    },
    {
        "packinfo": "HuaweiP7",
        "adinfo": "HUAWEI P7-L10"
    },
    {
        "packinfo": "HuaweiP7",
        "adinfo": "HUAWEI P7-L11"
    },
    {
        "packinfo": "HuaweiP7",
        "adinfo": "HUAWEI P7-L12"
    },
    {
        "packinfo": "HuaweiP7 mini",
        "adinfo": "HUAWEI P7 mini"
    },
    {
        "packinfo": "HuaweiP7-L09",
        "adinfo": "HUAWEI P7-L09"
    },
    {
        "packinfo": "HuaweiP8",
        "adinfo": "HUAWEI GRA-CL00"
    },
    {
        "packinfo": "HuaweiP8",
        "adinfo": "HUAWEI GRA-CL10"
    },
    {
        "packinfo": "HuaweiP8",
        "adinfo": "HUAWEI GRA-L09"
    },
    {
        "packinfo": "HuaweiP8",
        "adinfo": "HUAWEI GRA-TL00"
    },
    {
        "packinfo": "HuaweiP8",
        "adinfo": "HUAWEI GRA-UL00"
    },
    {
        "packinfo": "HuaweiP8",
        "adinfo": "HUAWEI GRA-UL10"
    },
    {
        "packinfo": "HuaweiP8 Lite",
        "adinfo": "503HW"
    },
    {
        "packinfo": "HuaweiP8 Lite",
        "adinfo": "ALE-L02"
    },
    {
        "packinfo": "HuaweiP8 Lite",
        "adinfo": "ALE-L21"
    },
    {
        "packinfo": "HuaweiP8 Lite",
        "adinfo": "ALE-L23"
    },
    {
        "packinfo": "HuaweiP8 Lite",
        "adinfo": "Autana LTE"
    },
    {
        "packinfo": "HuaweiP8 Lite",
        "adinfo": "HUAWEI ALE-CL00"
    },
    {
        "packinfo": "HuaweiP8 Lite",
        "adinfo": "HUAWEI ALE-L04"
    },
    {
        "packinfo": "HuaweiP8 lite 2017",
        "adinfo": "PRA-LA1"
    },
    {
        "packinfo": "HuaweiP8 lite 2017",
        "adinfo": "PRA-LX1"
    },
    {
        "packinfo": "HuaweiP8 青春版",
        "adinfo": "ALE-TL00"
    },
    {
        "packinfo": "HuaweiP8 青春版",
        "adinfo": "ALE-UL00"
    },
    {
        "packinfo": "HuaweiP8max",
        "adinfo": "HUAWEI P8max"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-AL00"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-AL10"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-CL00"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-DL00"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-L09"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-L19"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-L29"
    },
    {
        "packinfo": "HuaweiP9",
        "adinfo": "EVA-TL00"
    },
    {
        "packinfo": "HuaweiP9 Lite PREMIUM",
        "adinfo": "HUAWEI VNS-L52"
    },
    {
        "packinfo": "HuaweiP9 Plus",
        "adinfo": "VIE-AL10"
    },
    {
        "packinfo": "HuaweiP9 Plus",
        "adinfo": "VIE-L09"
    },
    {
        "packinfo": "HuaweiP9 Plus",
        "adinfo": "VIE-L29"
    },
    {
        "packinfo": "HuaweiP9 lite",
        "adinfo": "HUAWEI VNS-L21"
    },
    {
        "packinfo": "HuaweiP9 lite",
        "adinfo": "HUAWEI VNS-L22"
    },
    {
        "packinfo": "HuaweiP9 lite",
        "adinfo": "HUAWEI VNS-L23"
    },
    {
        "packinfo": "HuaweiP9 lite",
        "adinfo": "HUAWEI VNS-L31"
    },
    {
        "packinfo": "HuaweiP9 lite",
        "adinfo": "HUAWEI VNS-L53"
    },
    {
        "packinfo": "HuaweiP9 lite",
        "adinfo": "HUAWEI VNS-L62"
    },
    {
        "packinfo": "HuaweiP9 lite smart",
        "adinfo": "DIG-L03"
    },
    {
        "packinfo": "HuaweiP9 lite smart",
        "adinfo": "DIG-L23"
    },
    {
        "packinfo": "HuaweiPE-CL00",
        "adinfo": "PE-CL00"
    },
    {
        "packinfo": "HuaweiPE-TL00M",
        "adinfo": "PE-TL00M"
    },
    {
        "packinfo": "HuaweiPE-TL10",
        "adinfo": "PE-TL10"
    },
    {
        "packinfo": "HuaweiPE-TL20",
        "adinfo": "PE-TL20"
    },
    {
        "packinfo": "HuaweiPE-UL00",
        "adinfo": "PE-UL00"
    },
    {
        "packinfo": "HuaweiPORSCHE DESIGN HUAWEI Mate RS",
        "adinfo": "NEO-AL00"
    },
    {
        "packinfo": "HuaweiPORSCHE DESIGN HUAWEI Mate RS",
        "adinfo": "NEO-L29"
    },
    {
        "packinfo": "HuaweiPrism II",
        "adinfo": "Prism II"
    },
    {
        "packinfo": "HuaweiQ22",
        "adinfo": "Q22"
    },
    {
        "packinfo": "HuaweiRIO-CL00",
        "adinfo": "HUAWEI RIO-CL00"
    },
    {
        "packinfo": "HuaweiS10",
        "adinfo": "MediaPad 10 FHD"
    },
    {
        "packinfo": "HuaweiS10",
        "adinfo": "MediaPad 10 LINK"
    },
    {
        "packinfo": "HuaweiS7",
        "adinfo": "MediaPad 7 Vogue"
    },
    {
        "packinfo": "HuaweiS7",
        "adinfo": "MediaPad 7 Vogue"
    },
    {
        "packinfo": "HuaweiS7",
        "adinfo": "MediaPad 7 Youth"
    },
    {
        "packinfo": "HuaweiS7",
        "adinfo": "Orinoquia Roraima S7-932u"
    },
    {
        "packinfo": "HuaweiS7",
        "adinfo": "MediaPad 7 Lite+"
    },
    {
        "packinfo": "HuaweiS7",
        "adinfo": "Telpad Dual S"
    },
    {
        "packinfo": "HuaweiSC-CL00",
        "adinfo": "HUAWEI SC-CL00"
    },
    {
        "packinfo": "HuaweiSC-UL10",
        "adinfo": "HUAWEI SC-UL10"
    },
    {
        "packinfo": "HuaweiSensa LTE",
        "adinfo": "H710VL"
    },
    {
        "packinfo": "HuaweiSensa LTE",
        "adinfo": "H715BL"
    },
    {
        "packinfo": "HuaweiShotX",
        "adinfo": "HUAWEI ATH-UL01"
    },
    {
        "packinfo": "HuaweiShotX",
        "adinfo": "HUAWEI ATH-UL06"
    },
    {
        "packinfo": "HuaweiT-Mobile Pulse",
        "adinfo": "Huawei_8100-9"
    },
    {
        "packinfo": "HuaweiT-Mobile Pulse",
        "adinfo": "Tactile internet"
    },
    {
        "packinfo": "HuaweiT-Mobile Pulse",
        "adinfo": "U8100"
    },
    {
        "packinfo": "HuaweiT-Mobile Pulse",
        "adinfo": "Videocon_V7400"
    },
    {
        "packinfo": "HuaweiT1",
        "adinfo": "T1-821L"
    },
    {
        "packinfo": "HuaweiT1",
        "adinfo": "T1-821W"
    },
    {
        "packinfo": "HuaweiT1",
        "adinfo": "T1-821w"
    },
    {
        "packinfo": "HuaweiT1",
        "adinfo": "T1-823L"
    },
    {
        "packinfo": "HuaweiT1",
        "adinfo": "T1-823L"
    },
    {
        "packinfo": "HuaweiT1 10",
        "adinfo": "HUAWEI MediaPad T1 10 4G"
    },
    {
        "packinfo": "HuaweiT1 10",
        "adinfo": "T1-A21L"
    },
    {
        "packinfo": "HuaweiT1 10",
        "adinfo": "T1-A21W"
    },
    {
        "packinfo": "HuaweiT1 10",
        "adinfo": "T1-A21w"
    },
    {
        "packinfo": "HuaweiT1 10",
        "adinfo": "T1-A22L"
    },
    {
        "packinfo": "HuaweiT1 10",
        "adinfo": "T1-A23L"
    },
    {
        "packinfo": "HuaweiT101",
        "adinfo": "T-101"
    },
    {
        "packinfo": "HuaweiT101",
        "adinfo": "T101 PAD"
    },
    {
        "packinfo": "HuaweiT102",
        "adinfo": "QH-10"
    },
    {
        "packinfo": "HuaweiT102",
        "adinfo": "T102 PAD"
    },
    {
        "packinfo": "HuaweiT801",
        "adinfo": "T801 PAD"
    },
    {
        "packinfo": "HuaweiT802",
        "adinfo": "MT-803G"
    },
    {
        "packinfo": "HuaweiT802",
        "adinfo": "T802 PAD"
    },
    {
        "packinfo": "HuaweiT8808D",
        "adinfo": "HUAWEI T8808D"
    },
    {
        "packinfo": "HuaweiTANGO",
        "adinfo": "HUAWEI TAG-AL00"
    },
    {
        "packinfo": "HuaweiTANGO",
        "adinfo": "HUAWEI TAG-CL00"
    },
    {
        "packinfo": "HuaweiTANGO",
        "adinfo": "HUAWEI TAG-TL00"
    },
    {
        "packinfo": "HuaweiU8120",
        "adinfo": "Vodafone 845"
    },
    {
        "packinfo": "HuaweiU8220",
        "adinfo": "Pulse"
    },
    {
        "packinfo": "HuaweiU8220",
        "adinfo": "U8220"
    },
    {
        "packinfo": "HuaweiU8220",
        "adinfo": "U8220PLUS"
    },
    {
        "packinfo": "HuaweiU8230",
        "adinfo": "U8230"
    },
    {
        "packinfo": "HuaweiU8652",
        "adinfo": "Huawei-U8652"
    },
    {
        "packinfo": "HuaweiU8652",
        "adinfo": "U8652"
    },
    {
        "packinfo": "HuaweiU8687",
        "adinfo": "Huawei-U8687"
    },
    {
        "packinfo": "HuaweiU8812D",
        "adinfo": "U8812D"
    },
    {
        "packinfo": "HuaweiU8832D",
        "adinfo": "U8832D"
    },
    {
        "packinfo": "HuaweiU8836D",
        "adinfo": "U8836D"
    },
    {
        "packinfo": "HuaweiU8850",
        "adinfo": "HUAWEI-U8850"
    },
    {
        "packinfo": "HuaweiU9000",
        "adinfo": "HUAWEI-U9000"
    },
    {
        "packinfo": "HuaweiUNION",
        "adinfo": "Y538"
    },
    {
        "packinfo": "HuaweiV858",
        "adinfo": "Huawei 858"
    },
    {
        "packinfo": "HuaweiV858",
        "adinfo": "MTC 950"
    },
    {
        "packinfo": "HuaweiV858",
        "adinfo": "MTC Mini"
    },
    {
        "packinfo": "HuaweiV858",
        "adinfo": "Vodafone 858"
    },
    {
        "packinfo": "HuaweiVogue7",
        "adinfo": "MediaPad 7 Classic"
    },
    {
        "packinfo": "HuaweiVogue7",
        "adinfo": "MediaPad 7 Lite II"
    },
    {
        "packinfo": "HuaweiVogue7",
        "adinfo": "MediaPad 7 Vogue"
    },
    {
        "packinfo": "HuaweiWATCH",
        "adinfo": "HUAWEI WATCH"
    },
    {
        "packinfo": "HuaweiWATCH",
        "adinfo": "HUAWEI-WATCH"
    },
    {
        "packinfo": "HuaweiWatch 2",
        "adinfo": "LEO-BX9"
    },
    {
        "packinfo": "HuaweiWatch 2",
        "adinfo": "LEO-DLXX"
    },
    {
        "packinfo": "HuaweiX2",
        "adinfo": "GEM-701L"
    },
    {
        "packinfo": "HuaweiX2",
        "adinfo": "GEM-702L"
    },
    {
        "packinfo": "HuaweiX2",
        "adinfo": "GEM-703L"
    },
    {
        "packinfo": "HuaweiX2",
        "adinfo": "GEM-703LT"
    },
    {
        "packinfo": "HuaweiY210",
        "adinfo": "Orinoquia Auyantepui Y210"
    },
    {
        "packinfo": "HuaweiY220",
        "adinfo": "Y220-U00"
    },
    {
        "packinfo": "HuaweiY220",
        "adinfo": "Y220-U05"
    },
    {
        "packinfo": "HuaweiY220",
        "adinfo": "Y220-U17"
    },
    {
        "packinfo": "HuaweiY220-T10",
        "adinfo": "HUAWEI Y220-T10"
    },
    {
        "packinfo": "HuaweiY220-U10",
        "adinfo": "Y220-U10"
    },
    {
        "packinfo": "HuaweiY220T",
        "adinfo": "HUAWEI Y 220T"
    },
    {
        "packinfo": "HuaweiY221-U03",
        "adinfo": "HUAWEI Y221-U03"
    },
    {
        "packinfo": "HuaweiY221-U03",
        "adinfo": "ORINOQUIA Auyantepui+Y221-U03"
    },
    {
        "packinfo": "HuaweiY221-U12",
        "adinfo": "HUAWEI Y221-U12"
    },
    {
        "packinfo": "HuaweiY221-U22",
        "adinfo": "HUAWEI Y221-U22"
    },
    {
        "packinfo": "HuaweiY221-U33",
        "adinfo": "HUAWEI Y221-U33"
    },
    {
        "packinfo": "HuaweiY221-U43",
        "adinfo": "HUAWEI Y221-U43"
    },
    {
        "packinfo": "HuaweiY221-U53",
        "adinfo": "HUAWEI Y221-U53"
    },
    {
        "packinfo": "HuaweiY300",
        "adinfo": "HUAWEI Ascend Y300"
    },
    {
        "packinfo": "HuaweiY300",
        "adinfo": "HUAWEI Y300-0100"
    },
    {
        "packinfo": "HuaweiY300",
        "adinfo": "HUAWEI Y300-0151"
    },
    {
        "packinfo": "HuaweiY300",
        "adinfo": "Pelephone-Y300-"
    },
    {
        "packinfo": "HuaweiY300-0000",
        "adinfo": "HUAWEI Y300-0000"
    },
    {
        "packinfo": "HuaweiY301A1",
        "adinfo": "Huawei Y301A1"
    },
    {
        "packinfo": "HuaweiY301A2",
        "adinfo": "Huawei Y301A2"
    },
    {
        "packinfo": "HuaweiY310-5000",
        "adinfo": "HUAWEI Y310-5000"
    },
    {
        "packinfo": "HuaweiY310-T10",
        "adinfo": "HUAWEI Y310-T10"
    },
    {
        "packinfo": "HuaweiY320",
        "adinfo": "HUAWEI Y320-C00"
    },
    {
        "packinfo": "HuaweiY320-T00",
        "adinfo": "HUAWEI Y320-T00"
    },
    {
        "packinfo": "HuaweiY320-U01",
        "adinfo": "HUAWEI Y320-U01"
    },
    {
        "packinfo": "HuaweiY320-U01",
        "adinfo": "Y320-U01"
    },
    {
        "packinfo": "HuaweiY320-U10",
        "adinfo": "HUAWEI Y320-U10"
    },
    {
        "packinfo": "HuaweiY320-U151",
        "adinfo": "HUAWEI Y320-U151"
    },
    {
        "packinfo": "HuaweiY320-U30",
        "adinfo": "HUAWEI Y320-U30"
    },
    {
        "packinfo": "HuaweiY320-U351",
        "adinfo": "HUAWEI Y320-U351"
    },
    {
        "packinfo": "HuaweiY321",
        "adinfo": "HUAWEI Y321-U051"
    },
    {
        "packinfo": "HuaweiY321",
        "adinfo": "HUAWEI Y321-C00"
    },
    {
        "packinfo": "HuaweiY325-T00",
        "adinfo": "HUAWEI Y325-T00"
    },
    {
        "packinfo": "HuaweiY330",
        "adinfo": "Bucare Y330-U05"
    },
    {
        "packinfo": "HuaweiY330",
        "adinfo": "HUAWEI Y330-U05"
    },
    {
        "packinfo": "HuaweiY330",
        "adinfo": "HUAWEI Y330-U21"
    },
    {
        "packinfo": "HuaweiY330-C00",
        "adinfo": "HUAWEI Y330-C00"
    },
    {
        "packinfo": "HuaweiY330-U01",
        "adinfo": "HUAWEI Y330-U01"
    },
    {
        "packinfo": "HuaweiY330-U01",
        "adinfo": "Luno"
    },
    {
        "packinfo": "HuaweiY330-U07",
        "adinfo": "HUAWEI Y330-U07"
    },
    {
        "packinfo": "HuaweiY330-U08",
        "adinfo": "HUAWEI Y330-U08"
    },
    {
        "packinfo": "HuaweiY330-U11",
        "adinfo": "HUAWEI Y330-U11"
    },
    {
        "packinfo": "HuaweiY330-U11",
        "adinfo": "V8510"
    },
    {
        "packinfo": "HuaweiY330-U15",
        "adinfo": "HUAWEI Y330-U15"
    },
    {
        "packinfo": "HuaweiY330-U17",
        "adinfo": "HUAWEI Y330-U17"
    },
    {
        "packinfo": "HuaweiY336-A1",
        "adinfo": "HUAWEI Y336-A1"
    },
    {
        "packinfo": "HuaweiY336-U02",
        "adinfo": "HUAWEI Y336-U02"
    },
    {
        "packinfo": "HuaweiY336-U12",
        "adinfo": "HUAWEI Y336-U12"
    },
    {
        "packinfo": "HuaweiY340-U081",
        "adinfo": "Y340-U081"
    },
    {
        "packinfo": "HuaweiY360-U03",
        "adinfo": "HUAWEI Y360-U03"
    },
    {
        "packinfo": "HuaweiY360-U103",
        "adinfo": "HUAWEI Y360-U103"
    },
    {
        "packinfo": "HuaweiY360-U12",
        "adinfo": "HUAWEI Y360-U12"
    },
    {
        "packinfo": "HuaweiY360-U23",
        "adinfo": "HUAWEI Y360-U23"
    },
    {
        "packinfo": "HuaweiY360-U31",
        "adinfo": "HUAWEI Y360-U31"
    },
    {
        "packinfo": "HuaweiY360-U42",
        "adinfo": "HUAWEI Y360-U42"
    },
    {
        "packinfo": "HuaweiY360-U61",
        "adinfo": "HUAWEI Y360-U61"
    },
    {
        "packinfo": "HuaweiY360-U72",
        "adinfo": "HUAWEI Y360-U72"
    },
    {
        "packinfo": "HuaweiY360-U82",
        "adinfo": "HUAWEI Y360-U82"
    },
    {
        "packinfo": "HuaweiY360-U93",
        "adinfo": "Delta Y360-U93"
    },
    {
        "packinfo": "HuaweiY360-U93",
        "adinfo": "HUAWEI Y360-U93"
    },
    {
        "packinfo": "HuaweiY3II",
        "adinfo": "HUAWEI LUA-L01"
    },
    {
        "packinfo": "HuaweiY3II",
        "adinfo": "HUAWEI LUA-L02"
    },
    {
        "packinfo": "HuaweiY3II",
        "adinfo": "HUAWEI LUA-L21"
    },
    {
        "packinfo": "HuaweiY3II",
        "adinfo": "HUAWEI LUA-U02"
    },
    {
        "packinfo": "HuaweiY3II",
        "adinfo": "HUAWEI LUA-U22"
    },
    {
        "packinfo": "HuaweiY3III",
        "adinfo": "CRO-U00"
    },
    {
        "packinfo": "HuaweiY3III",
        "adinfo": "CRO-U23"
    },
    {
        "packinfo": "HuaweiY3III",
        "adinfo": "HUAWEI CRO-U00"
    },
    {
        "packinfo": "HuaweiY3III",
        "adinfo": "HUAWEI CRO-U23"
    },
    {
        "packinfo": "HuaweiY5",
        "adinfo": "HUAWEI Y560-L02"
    },
    {
        "packinfo": "HuaweiY5",
        "adinfo": "HUAWEI Y560-L23"
    },
    {
        "packinfo": "HuaweiY5",
        "adinfo": "HUAWEI Y560-U03"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-AL00"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-L02"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-L03"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-L13"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-L22"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-L23"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-TL00"
    },
    {
        "packinfo": "HuaweiY5 2017",
        "adinfo": "MYA-U29"
    },
    {
        "packinfo": "HuaweiY500-T00",
        "adinfo": "HUAWEI Y500-T00"
    },
    {
        "packinfo": "HuaweiY511-T00",
        "adinfo": "HUAWEI Y511-T00"
    },
    {
        "packinfo": "HuaweiY511-T00",
        "adinfo": "Y511-T00"
    },
    {
        "packinfo": "HuaweiY511-U00",
        "adinfo": "Y511-U00"
    },
    {
        "packinfo": "HuaweiY511-U10",
        "adinfo": "HUAWEI Y511-U10"
    },
    {
        "packinfo": "HuaweiY511-U251",
        "adinfo": "HUAWEI Y511-U251"
    },
    {
        "packinfo": "HuaweiY511-U30",
        "adinfo": "HUAWEI Y511-U30"
    },
    {
        "packinfo": "HuaweiY511-U30",
        "adinfo": "VIETTEL V8506"
    },
    {
        "packinfo": "HuaweiY516-",
        "adinfo": "HUAWEI Y516-T00"
    },
    {
        "packinfo": "HuaweiY518-T00",
        "adinfo": "HUAWEI Y518-T00"
    },
    {
        "packinfo": "HuaweiY520-U03",
        "adinfo": "HUAWEI Y520-U03"
    },
    {
        "packinfo": "HuaweiY520-U12",
        "adinfo": "HUAWEI Y520-U12"
    },
    {
        "packinfo": "HuaweiY520-U22",
        "adinfo": "HUAWEI Y520-U22"
    },
    {
        "packinfo": "HuaweiY520-U33",
        "adinfo": "HUAWEI Y520-U33"
    },
    {
        "packinfo": "HuaweiY523-L076",
        "adinfo": "HUAWEI Y523-L076"
    },
    {
        "packinfo": "HuaweiY523-L176",
        "adinfo": "HUAWEI Y523-L176"
    },
    {
        "packinfo": "HuaweiY530",
        "adinfo": "HUAWEI Y530-U00"
    },
    {
        "packinfo": "HuaweiY530-U051",
        "adinfo": "HUAWEI Y530"
    },
    {
        "packinfo": "HuaweiY530-U051",
        "adinfo": "HUAWEI Y530-U051"
    },
    {
        "packinfo": "HuaweiY535",
        "adinfo": "HUAWEI Y535-C00"
    },
    {
        "packinfo": "HuaweiY535D-C00",
        "adinfo": "HUAWEI Y535D-C00"
    },
    {
        "packinfo": "HuaweiY536-A1",
        "adinfo": "HUAWEI Y536A1"
    },
    {
        "packinfo": "HuaweiY540-U01",
        "adinfo": "HUAWEI Y540-U01"
    },
    {
        "packinfo": "HuaweiY541-U02",
        "adinfo": "HUAWEI Y541-U02"
    },
    {
        "packinfo": "HuaweiY541-U02",
        "adinfo": "Y541-U02"
    },
    {
        "packinfo": "HuaweiY545-U05",
        "adinfo": "Y545-U05"
    },
    {
        "packinfo": "HuaweiY550-L01",
        "adinfo": "HUAWEI Y550-L01"
    },
    {
        "packinfo": "HuaweiY550-L02",
        "adinfo": "HUAWEI Y550-L02"
    },
    {
        "packinfo": "HuaweiY550-L02",
        "adinfo": "Y550-L02"
    },
    {
        "packinfo": "HuaweiY550-L03",
        "adinfo": "HUAWEI Y550"
    },
    {
        "packinfo": "HuaweiY550-L03",
        "adinfo": "HUAWEI Y550-L03"
    },
    {
        "packinfo": "HuaweiY550-L03",
        "adinfo": "Personal Huawei Y550"
    },
    {
        "packinfo": "HuaweiY550-L03",
        "adinfo": "Y550-L03"
    },
    {
        "packinfo": "HuaweiY560-CL00",
        "adinfo": "HUAWEI Y560-CL00"
    },
    {
        "packinfo": "HuaweiY560-L01",
        "adinfo": "HUAWEI Y560-L01"
    },
    {
        "packinfo": "HuaweiY560-L03",
        "adinfo": "HUAWEI Y560-L03"
    },
    {
        "packinfo": "HuaweiY560-U02",
        "adinfo": "HUAWEI Y560-U02"
    },
    {
        "packinfo": "HuaweiY560-U12",
        "adinfo": "HUAWEI Y560-U12"
    },
    {
        "packinfo": "HuaweiY560-U23",
        "adinfo": "HUAWEI Y560-U23"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "CUN-L22"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-L01"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-L02"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-L03"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-L21"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-L22"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-L23"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-L33"
    },
    {
        "packinfo": "HuaweiY5II",
        "adinfo": "HUAWEI CUN-U29"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCC-U21"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "SCC-U21"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCL-L01"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCL-L02"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCL-L03"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCL-L04"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCL-L21"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HW-SCL-L32"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "SCL-L01"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCL-U23"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "HUAWEI SCL-U31"
    },
    {
        "packinfo": "HuaweiY6",
        "adinfo": "SCL-U23"
    },
    {
        "packinfo": "HuaweiY6 2017",
        "adinfo": "MYA-L41"
    },
    {
        "packinfo": "HuaweiY6 Elite",
        "adinfo": "HUAWEI LYO-L02"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "HUAWEI TIT-AL00"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "HUAWEI TIT-AL00"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "HUAWEI TIT-CL10"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "HUAWEI TIT-L01"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "HUAWEI TIT-TL00"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "TIT-AL00"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "TIT-L01"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "HUAWEI TIT-CL00"
    },
    {
        "packinfo": "HuaweiY6 Pro",
        "adinfo": "HUAWEI TIT-U02"
    },
    {
        "packinfo": "HuaweiY6 Ⅱ Compact",
        "adinfo": "HUAWEI LYO-L01"
    },
    {
        "packinfo": "HuaweiY600",
        "adinfo": "HUAWEI Y600-U00"
    },
    {
        "packinfo": "HuaweiY600",
        "adinfo": "HUAWEI Y600-U151"
    },
    {
        "packinfo": "HuaweiY600",
        "adinfo": "HUAWEI Y600-U20"
    },
    {
        "packinfo": "HuaweiY600-U351",
        "adinfo": "HUAWEI Y600-U351"
    },
    {
        "packinfo": "HuaweiY600-U40",
        "adinfo": "HUAWEI Y600-U40"
    },
    {
        "packinfo": "HuaweiY600D-C00",
        "adinfo": "HUAWEI Y600D-C00"
    },
    {
        "packinfo": "HuaweiY610",
        "adinfo": "HUAWEI Y610-U00"
    },
    {
        "packinfo": "HuaweiY618",
        "adinfo": "HUAWEI Y618-T00"
    },
    {
        "packinfo": "HuaweiY625-U03",
        "adinfo": "Kavak Y625-U03"
    },
    {
        "packinfo": "HuaweiY625-U13",
        "adinfo": "HUAWEI Y625-U13"
    },
    {
        "packinfo": "HuaweiY625-U21",
        "adinfo": "HUAWEI Y625-U21"
    },
    {
        "packinfo": "HuaweiY625-U32",
        "adinfo": "HUAWEI Y625-U32"
    },
    {
        "packinfo": "HuaweiY625-U43",
        "adinfo": "HUAWEI Y625-U43"
    },
    {
        "packinfo": "HuaweiY625-U51",
        "adinfo": "HUAWEI Y625-U51"
    },
    {
        "packinfo": "HuaweiY635-CL00",
        "adinfo": "HUAWEI Y635-CL00"
    },
    {
        "packinfo": "HuaweiY635-L01",
        "adinfo": "Y635-L01"
    },
    {
        "packinfo": "HuaweiY635-L02",
        "adinfo": "HUAWEI Y635-L02"
    },
    {
        "packinfo": "HuaweiY635-L02",
        "adinfo": "Y635-L02"
    },
    {
        "packinfo": "HuaweiY635-L03",
        "adinfo": "HUAWEI Y635-L03"
    },
    {
        "packinfo": "HuaweiY635-L03",
        "adinfo": "Y635-L03"
    },
    {
        "packinfo": "HuaweiY635-L21",
        "adinfo": "Y635-L21"
    },
    {
        "packinfo": "HuaweiY635-TL00",
        "adinfo": "HUAWEI Y635-TL00"
    },
    {
        "packinfo": "HuaweiY635-TL00",
        "adinfo": "Y635-TL00"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "CAM-L03"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "CAM-L21"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "CAM-L23"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "CAM-U22"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "HUAWEI CAM-L03"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "HUAWEI CAM-L21"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "HUAWEI CAM-L23"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "HUAWEI CAM-U22"
    },
    {
        "packinfo": "HuaweiY6II",
        "adinfo": "CAM-L32"
    },
    {
        "packinfo": "HuaweiY6ⅡCompact",
        "adinfo": "HUAWEI LYO-L03"
    },
    {
        "packinfo": "HuaweiY7",
        "adinfo": "TRT-L21A"
    },
    {
        "packinfo": "HuaweiY7",
        "adinfo": "TRT-L53"
    },
    {
        "packinfo": "HuaweiY7",
        "adinfo": "TRT-LX1"
    },
    {
        "packinfo": "HuaweiY7",
        "adinfo": "TRT-LX2"
    },
    {
        "packinfo": "HuaweiY7",
        "adinfo": "TRT-LX3"
    },
    {
        "packinfo": "HuaweiY7 Prime 2019",
        "adinfo": "DUB-LX1"
    },
    {
        "packinfo": "HuaweiY7 Pro 2019",
        "adinfo": "DUB-AL20"
    },
    {
        "packinfo": "HuaweiY9 Prime 2019",
        "adinfo": "STK-L21"
    },
    {
        "packinfo": "HuaweiY9 Prime 2019",
        "adinfo": "STK-L22"
    },
    {
        "packinfo": "HuaweiY9 Prime 2019",
        "adinfo": "STK-LX3"
    },
    {
        "packinfo": "HuaweiYouth",
        "adinfo": "Orinoquia Gran Roraima S7-702u"
    },
    {
        "packinfo": "Huaweiascend-5w",
        "adinfo": "H1623"
    },
    {
        "packinfo": "Huaweid-01G",
        "adinfo": "d-01G"
    },
    {
        "packinfo": "Huaweid-01H",
        "adinfo": "d-01H"
    },
    {
        "packinfo": "Huaweid-02H",
        "adinfo": "d-02H"
    },
    {
        "packinfo": "HuaweieH811",
        "adinfo": "eH811"
    },
    {
        "packinfo": "Huaweihonor 10 Lite",
        "adinfo": "HRY-LX1"
    },
    {
        "packinfo": "Huaweihonor 10 Lite",
        "adinfo": "HRY-LX1MEB"
    },
    {
        "packinfo": "Huaweihonor 10 Lite",
        "adinfo": "HRY-LX2"
    },
    {
        "packinfo": "Huaweihonor 10 Lite",
        "adinfo": "HRY-AL00"
    },
    {
        "packinfo": "Huaweihonor 5X",
        "adinfo": "KIW-L22"
    },
    {
        "packinfo": "Huaweihonor 5X",
        "adinfo": "KIW-L23"
    },
    {
        "packinfo": "Huaweihonor 5X",
        "adinfo": "KIW-L24"
    },
    {
        "packinfo": "Huaweihonor 6A Pro",
        "adinfo": "DLI-L42"
    },
    {
        "packinfo": "Huaweihonor 6C",
        "adinfo": "DIG-L21HN"
    },
    {
        "packinfo": "Huaweihonor 6C Pro",
        "adinfo": "JMM-L22"
    },
    {
        "packinfo": "Huaweihonor 6x",
        "adinfo": "BLN-L21"
    },
    {
        "packinfo": "Huaweihonor 6x",
        "adinfo": "BLN-L22"
    },
    {
        "packinfo": "Huaweihonor 8C",
        "adinfo": "BKK-AL10"
    },
    {
        "packinfo": "Huaweihonor 8C",
        "adinfo": "BKK-L21"
    },
    {
        "packinfo": "Huaweihonor 8C",
        "adinfo": "BKK-L22"
    },
    {
        "packinfo": "Huaweihonor 8C",
        "adinfo": "BKK-LX2"
    },
    {
        "packinfo": "Huaweihuawei nova 2",
        "adinfo": "HWV31"
    },
    {
        "packinfo": "Huaweihw204HW",
        "adinfo": "204HW"
    },
    {
        "packinfo": "Huaweim881",
        "adinfo": "HUAWEI M881"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAN-AL10"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAN-L01"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAN-L02"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAN-L03"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAN-L11"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAN-L12"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAN-L13"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAZ-AL10"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAZ-AL00"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAZ-AL10"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAZ-TL10"
    },
    {
        "packinfo": "Huaweinova",
        "adinfo": "HUAWEI CAZ-TL20"
    },
    {
        "packinfo": "Huaweinova 2",
        "adinfo": "PIC-AL00"
    },
    {
        "packinfo": "Huaweinova 2",
        "adinfo": "PIC-TL00"
    },
    {
        "packinfo": "Huaweinova 2 Plus",
        "adinfo": "BAC-AL00"
    },
    {
        "packinfo": "Huaweinova 2 Plus",
        "adinfo": "BAC-L01"
    },
    {
        "packinfo": "Huaweinova 2 Plus",
        "adinfo": "BAC-L03"
    },
    {
        "packinfo": "Huaweinova 2 Plus",
        "adinfo": "BAC-L23"
    },
    {
        "packinfo": "Huaweinova 2 Plus",
        "adinfo": "BAC-TL00"
    },
    {
        "packinfo": "Huaweinova 2i",
        "adinfo": "RNE-L02"
    },
    {
        "packinfo": "Huaweinova 2i",
        "adinfo": "RNE-L22"
    },
    {
        "packinfo": "Huaweinova 2s",
        "adinfo": "HWI-AL00"
    },
    {
        "packinfo": "Huaweinova 2s",
        "adinfo": "HWI-TL00"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-AL00"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-L21"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-L29"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-LX1"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-LX1M"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-LX9"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-TL00"
    },
    {
        "packinfo": "Huaweinova 3",
        "adinfo": "PAR-TL20"
    },
    {
        "packinfo": "Huaweinova 3e",
        "adinfo": "ANE-AL00"
    },
    {
        "packinfo": "Huaweinova 3e",
        "adinfo": "ANE-TL00"
    },
    {
        "packinfo": "Huaweinova 3i",
        "adinfo": "INE-AL00"
    },
    {
        "packinfo": "Huaweinova 3i",
        "adinfo": "INE-LX1"
    },
    {
        "packinfo": "Huaweinova 3i",
        "adinfo": "INE-LX1r"
    },
    {
        "packinfo": "Huaweinova 3i",
        "adinfo": "INE-LX2"
    },
    {
        "packinfo": "Huaweinova 3i",
        "adinfo": "INE-TL00"
    },
    {
        "packinfo": "Huaweinova 4",
        "adinfo": "VCE-AL00"
    },
    {
        "packinfo": "Huaweinova 4",
        "adinfo": "VCE-L22"
    },
    {
        "packinfo": "Huaweinova 4",
        "adinfo": "VCE-TL00"
    },
    {
        "packinfo": "Huaweinova 4e",
        "adinfo": "MAR-AL00"
    },
    {
        "packinfo": "Huaweinova 4e",
        "adinfo": "MAR-TL00"
    },
    {
        "packinfo": "Huaweinova lite",
        "adinfo": "PRA-LX2"
    },
    {
        "packinfo": "Huaweinova lite",
        "adinfo": "PRA-LX3"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "HUAWEI MLA-L01"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "HUAWEI MLA-L02"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "HUAWEI MLA-L03"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "HUAWEI MLA-L11"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "HUAWEI MLA-L12"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "HUAWEI MLA-L13"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "MLA-L01"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "MLA-L02"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "MLA-L03"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "MLA-L11"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "MLA-L12"
    },
    {
        "packinfo": "Huaweinova plus",
        "adinfo": "MLA-L13"
    },
    {
        "packinfo": "Huaweinova 青春版本",
        "adinfo": "WAS-AL00"
    },
    {
        "packinfo": "Huaweinova 青春版本",
        "adinfo": "WAS-TL10"
    },
    {
        "packinfo": "Huaweit1_8p0",
        "adinfo": "MediaPad T1 8.0"
    },
    {
        "packinfo": "Huaweit1_8p0",
        "adinfo": "S8-701u"
    },
    {
        "packinfo": "Huaweit1_8p0",
        "adinfo": "S8-701w"
    },
    {
        "packinfo": "Huaweit1_8p0lte",
        "adinfo": "HUAWEI MediaPad T1 8.0 4G"
    },
    {
        "packinfo": "Huaweit1_8p0lte",
        "adinfo": "Honor T1 8.0"
    },
    {
        "packinfo": "Huaweit1_8p0lte",
        "adinfo": "MediaPad T1 8.0 Pro"
    },
    {
        "packinfo": "Huaweit1_8p0lte",
        "adinfo": "S8-821w"
    },
    {
        "packinfo": "Huaweit1_8p0lte",
        "adinfo": "T1-821w"
    },
    {
        "packinfo": "Huaweit1_8p0lte",
        "adinfo": "T1-823L"
    },
    {
        "packinfo": "Huawei华为G9青春版",
        "adinfo": "HUAWEI VNS-DL00"
    },
    {
        "packinfo": "Huawei华为G9青春版",
        "adinfo": "HUAWEI VNS-TL00"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "BZT-AL00"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "BZT-AL10"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "BZT-W09"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "BZW-AL00"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "BZW-AL10"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "MON-AL19"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "MON-AL19B"
    },
    {
        "packinfo": "Huawei华为平板 C5",
        "adinfo": "MON-W19"
    },
    {
        "packinfo": "Huawei华为平板 M5 青春版",
        "adinfo": "BAH2-AL00"
    },
    {
        "packinfo": "Huawei华为平板 M5 青春版",
        "adinfo": "BAH2-AL10"
    },
    {
        "packinfo": "Huawei华为平板 M5 青春版",
        "adinfo": "BAH2-W09"
    },
    {
        "packinfo": "Huawei华为平板M5青春版",
        "adinfo": "JDN2-AL00"
    },
    {
        "packinfo": "Huawei华为平板M5青春版",
        "adinfo": "JDN2-W09"
    },
    {
        "packinfo": "Huawei华为平板T3 8行业专享版",
        "adinfo": "BZK-L00"
    },
    {
        "packinfo": "Huawei华为平板T3 8行业专享版",
        "adinfo": "BZK-W00"
    },
    {
        "packinfo": "Huawei华为揽阅M2青春版7.0",
        "adinfo": "PLE-701L"
    },
    {
        "packinfo": "Huawei华为揽阅M2青春版7.0",
        "adinfo": "PLE-703L"
    },
    {
        "packinfo": "Huawei华为畅享 8e 青春",
        "adinfo": "DRA-AL00"
    },
    {
        "packinfo": "Huawei华为畅享 8e 青春",
        "adinfo": "DRA-TL00"
    },
    {
        "packinfo": "Huawei华为畅享 9S",
        "adinfo": "POT-AL00a"
    },
    {
        "packinfo": "Huawei华为畅享 9S",
        "adinfo": "POT-TL00a"
    },
    {
        "packinfo": "Huawei华为畅享 9e",
        "adinfo": "MRD-AL00"
    },
    {
        "packinfo": "Huawei华为畅享 9e",
        "adinfo": "MRD-TL00"
    },
    {
        "packinfo": "Huawei华为畅享 MAX",
        "adinfo": "ARS-AL00"
    },
    {
        "packinfo": "Huawei华为畅享 MAX",
        "adinfo": "ARS-TL00"
    },
    {
        "packinfo": "Huawei华为畅享10 Plus",
        "adinfo": "STK-AL00"
    },
    {
        "packinfo": "Huawei华为畅享10 Plus",
        "adinfo": "STK-TL00"
    },
    {
        "packinfo": "Huawei华为畅享6",
        "adinfo": "NCE-AL00"
    },
    {
        "packinfo": "Huawei华为畅享6",
        "adinfo": "NCE-AL10"
    },
    {
        "packinfo": "Huawei华为畅享6",
        "adinfo": "NCE-TL10"
    },
    {
        "packinfo": "Huawei华为畅享6S",
        "adinfo": "DIG-AL00"
    },
    {
        "packinfo": "Huawei华为畅享6S",
        "adinfo": "DIG-TL10"
    },
    {
        "packinfo": "Huawei华为畅享7",
        "adinfo": "SLA-AL00"
    },
    {
        "packinfo": "Huawei华为畅享7",
        "adinfo": "SLA-TL10"
    },
    {
        "packinfo": "Huawei华为畅享7S",
        "adinfo": "FIG-AL00"
    },
    {
        "packinfo": "Huawei华为畅享7S",
        "adinfo": "FIG-AL10"
    },
    {
        "packinfo": "Huawei华为畅享7S",
        "adinfo": "FIG-TL00"
    },
    {
        "packinfo": "Huawei华为畅享7S",
        "adinfo": "FIG-TL10"
    },
    {
        "packinfo": "Huawei华为畅享8",
        "adinfo": "LDN-AL00"
    },
    {
        "packinfo": "Huawei华为畅享8",
        "adinfo": "LDN-AL10"
    },
    {
        "packinfo": "Huawei华为畅享8",
        "adinfo": "LDN-AL20"
    },
    {
        "packinfo": "Huawei华为畅享8",
        "adinfo": "LDN-TL00"
    },
    {
        "packinfo": "Huawei华为畅享8",
        "adinfo": "LDN-TL10"
    },
    {
        "packinfo": "Huawei华为畅享8",
        "adinfo": "LDN-TL20"
    },
    {
        "packinfo": "Huawei华为畅享8 Plus",
        "adinfo": "FLA-AL00"
    },
    {
        "packinfo": "Huawei华为畅享8 Plus",
        "adinfo": "FLA-AL10"
    },
    {
        "packinfo": "Huawei华为畅享8 Plus",
        "adinfo": "FLA-AL20"
    },
    {
        "packinfo": "Huawei华为畅享8 Plus",
        "adinfo": "FLA-TL00"
    },
    {
        "packinfo": "Huawei华为畅享8 Plus",
        "adinfo": "FLA-TL10"
    },
    {
        "packinfo": "Huawei华为畅享8e",
        "adinfo": "ATU-AL10"
    },
    {
        "packinfo": "Huawei华为畅享8e",
        "adinfo": "ATU-TL10"
    },
    {
        "packinfo": "Huawei华为畅享9",
        "adinfo": "DUB-AL00"
    },
    {
        "packinfo": "Huawei华为畅享9",
        "adinfo": "DUB-AL00a"
    },
    {
        "packinfo": "Huawei华为畅享9",
        "adinfo": "DUB-AL20"
    },
    {
        "packinfo": "Huawei华为畅享9",
        "adinfo": "DUB-TL00"
    },
    {
        "packinfo": "Huawei华为畅享9",
        "adinfo": "DUB-TL00a"
    },
    {
        "packinfo": "Huawei华为畅享9 Plus",
        "adinfo": "JKM-AL00"
    },
    {
        "packinfo": "Huawei华为畅享9 Plus",
        "adinfo": "JKM-TL00"
    },
    {
        "packinfo": "Huawei华为畅享9 Plus",
        "adinfo": "JKM-AL00a"
    },
    {
        "packinfo": "Huawei华为畅享9 Plus",
        "adinfo": "JKM-AL00b"
    },
    {
        "packinfo": "Huawei华为畅享平板",
        "adinfo": "AGS2-AL00"
    },
    {
        "packinfo": "Huawei荣耀 8X",
        "adinfo": "JSN-AL00"
    },
    {
        "packinfo": "Huawei荣耀 8X",
        "adinfo": "JSN-TL00"
    },
    {
        "packinfo": "Huawei荣耀 8X",
        "adinfo": "JSN-AL00a"
    },
    {
        "packinfo": "Huawei荣耀 V9 play",
        "adinfo": "JMM-AL00"
    },
    {
        "packinfo": "Huawei荣耀 V9 play",
        "adinfo": "JMM-AL10"
    },
    {
        "packinfo": "Huawei荣耀 V9 play",
        "adinfo": "JMM-TL00"
    },
    {
        "packinfo": "Huawei荣耀 V9 play",
        "adinfo": "JMM-TL10"
    },
    {
        "packinfo": "Huawei荣耀10青春版",
        "adinfo": "HRY-TL00"
    },
    {
        "packinfo": "Huawei荣耀20i",
        "adinfo": "HRY-AL00T"
    },
    {
        "packinfo": "Huawei荣耀20i",
        "adinfo": "HRY-TL00T"
    },
    {
        "packinfo": "Huawei荣耀4A",
        "adinfo": "SCL-AL00"
    },
    {
        "packinfo": "Huawei荣耀5X",
        "adinfo": "KIW-AL10"
    },
    {
        "packinfo": "Huawei荣耀5X",
        "adinfo": "KIW-AL20"
    },
    {
        "packinfo": "Huawei荣耀5X",
        "adinfo": "KIW-CL00"
    },
    {
        "packinfo": "Huawei荣耀5X",
        "adinfo": "KIW-TL00"
    },
    {
        "packinfo": "Huawei荣耀5X",
        "adinfo": "KIW-UL00"
    },
    {
        "packinfo": "Huawei荣耀8X Max",
        "adinfo": "ARE-AL00"
    },
    {
        "packinfo": "Huawei荣耀8X Max",
        "adinfo": "ARE-TL00"
    },
    {
        "packinfo": "Huawei荣耀8X Max",
        "adinfo": "ARE-AL10"
    },
    {
        "packinfo": "Huawei荣耀8青春版",
        "adinfo": "PRA-AL00"
    },
    {
        "packinfo": "Huawei荣耀8青春版",
        "adinfo": "PRA-AL00X"
    },
    {
        "packinfo": "Huawei荣耀8青春版",
        "adinfo": "PRA-TL10"
    },
    {
        "packinfo": "Huawei荣耀9X",
        "adinfo": "HLK-AL00"
    },
    {
        "packinfo": "Huawei荣耀9i",
        "adinfo": "LLD-AL20"
    },
    {
        "packinfo": "Huawei荣耀9i",
        "adinfo": "LLD-AL30"
    },
    {
        "packinfo": "Huawei荣耀9青春版",
        "adinfo": "LLD-AL00"
    },
    {
        "packinfo": "Huawei荣耀9青春版",
        "adinfo": "LLD-AL10"
    },
    {
        "packinfo": "Huawei荣耀9青春版",
        "adinfo": "LLD-TL10"
    },
    {
        "packinfo": "Huawei荣耀Note8",
        "adinfo": "EDI-AL10"
    },
    {
        "packinfo": "Huawei荣耀Note8",
        "adinfo": "EDI-DL00"
    },
    {
        "packinfo": "Huawei荣耀Waterplay 8英寸",
        "adinfo": "HDL-AL09"
    },
    {
        "packinfo": "Huawei荣耀Waterplay 8英寸",
        "adinfo": "HDL-W09"
    },
    {
        "packinfo": "Huawei荣耀平板5",
        "adinfo": "AGS2-AL00HN"
    },
    {
        "packinfo": "Huawei荣耀平板5",
        "adinfo": "AGS2-W09HN"
    },
    {
        "packinfo": "Huawei荣耀平板5",
        "adinfo": "JDN2-AL00HN"
    },
    {
        "packinfo": "Huawei荣耀平板5",
        "adinfo": "JDN2-W09HN"
    },
    {
        "packinfo": "Huawei荣耀畅享7 Plus",
        "adinfo": "TRT-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅享7 Plus",
        "adinfo": "TRT-AL00A"
    },
    {
        "packinfo": "Huawei荣耀畅享7 Plus",
        "adinfo": "TRT-TL10"
    },
    {
        "packinfo": "Huawei荣耀畅享7 Plus",
        "adinfo": "TRT-TL10A"
    },
    {
        "packinfo": "Huawei荣耀畅玩 6X",
        "adinfo": "BLN-AL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩 6X",
        "adinfo": "BLN-AL20"
    },
    {
        "packinfo": "Huawei荣耀畅玩 6X",
        "adinfo": "BLN-AL30"
    },
    {
        "packinfo": "Huawei荣耀畅玩 6X",
        "adinfo": "BLN-AL40"
    },
    {
        "packinfo": "Huawei荣耀畅玩 6X",
        "adinfo": "BLN-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩 6X",
        "adinfo": "BLN-TL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩4C",
        "adinfo": "CHM-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩4C",
        "adinfo": "CHM-TL00H"
    },
    {
        "packinfo": "Huawei荣耀畅玩4C",
        "adinfo": "CHM-UL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩4X",
        "adinfo": "CHE-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩4X",
        "adinfo": "CHE-TL00H"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-TL00H"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-UL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-CL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-TL00H"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-UL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5A",
        "adinfo": "CAM-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5C",
        "adinfo": "NEM-AL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩5C",
        "adinfo": "NEM-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩5C",
        "adinfo": "NEM-TL00H"
    },
    {
        "packinfo": "Huawei荣耀畅玩5C",
        "adinfo": "NEM-UL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩6",
        "adinfo": "MYA-AL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩6",
        "adinfo": "MYA-TL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩6A",
        "adinfo": "DLI-AL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩7",
        "adinfo": "DUA-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩7",
        "adinfo": "DUA-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩7X",
        "adinfo": "BND-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩7X",
        "adinfo": "BND-AL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩7X",
        "adinfo": "BND-TL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩8",
        "adinfo": "KSA-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩8",
        "adinfo": "KSA-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩8A",
        "adinfo": "JAT-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩8A",
        "adinfo": "JAT-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩8C",
        "adinfo": "BKK-AL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩8C",
        "adinfo": "BKK-AL10"
    },
    {
        "packinfo": "Huawei荣耀畅玩8C",
        "adinfo": "BKK-TL00"
    },
    {
        "packinfo": "Huawei荣耀畅玩平板2 9.6",
        "adinfo": "BZA-L00"
    },
    {
        "packinfo": "Huawei荣耀畅玩平板2 9.6",
        "adinfo": "BZA-W00"
    },
    {
        "packinfo": "Huawei麦芒 8",
        "adinfo": "POT-AL00"
    },
    {
        "packinfo": "Huawei麦芒 8",
        "adinfo": "POT-AL10"
    },
    {
        "packinfo": "Huawei麦芒4",
        "adinfo": "HUAWEI RIO-AL00"
    },
    {
        "packinfo": "Huawei麦芒5",
        "adinfo": "HUAWEI MLA-AL00"
    },
    {
        "packinfo": "Huawei麦芒5",
        "adinfo": "HUAWEI MLA-AL10"
    },
    {
        "packinfo": "Huawei麦芒5",
        "adinfo": "MLA-AL00"
    },
    {
        "packinfo": "Huawei麦芒5",
        "adinfo": "MLA-AL10"
    },
    {
        "packinfo": "VivoV25",
        "adinfo": "V2202"
    },
    {
        "packinfo": "VivoV25",
        "adinfo": "V2228"
    },
    {
        "packinfo": "VivoV25 Pro",
        "adinfo": "V2158"
    },
    {
        "packinfo": "VivoV25e",
        "adinfo": "V2201"
    },
    {
        "packinfo": "VivoV25e",
        "adinfo": "V2209"
    },
    {
        "packinfo": "VivoV25e",
        "adinfo": "V2242"
    },
    {
        "packinfo": "VivoV27",
        "adinfo": "V2231"
    },
    {
        "packinfo": "VivoV27",
        "adinfo": "V2246"
    },
    {
        "packinfo": "VivoV27 Pro",
        "adinfo": "V2230"
    },
    {
        "packinfo": "VivoV27e",
        "adinfo": "V2237"
    },
    {
        "packinfo": "VivoV29",
        "adinfo": "V2250"
    },
    {
        "packinfo": "VivoV29 Lite 5G",
        "adinfo": "V2244"
    },
    {
        "packinfo": "VivoV3",
        "adinfo": "vivo V3"
    },
    {
        "packinfo": "VivoV3",
        "adinfo": "vivo V3"
    },
    {
        "packinfo": "VivoV3Lite",
        "adinfo": "vivo V3Lite"
    },
    {
        "packinfo": "VivoV3M A",
        "adinfo": "vivo PD1524B"
    },
    {
        "packinfo": "VivoV3Max",
        "adinfo": "vivo V3Max"
    },
    {
        "packinfo": "VivoV3Max + A",
        "adinfo": "vivo V3Max+ A"
    },
    {
        "packinfo": "VivoV3Max A",
        "adinfo": "vivo PD1523A"
    },
    {
        "packinfo": "VivoV5Plus",
        "adinfo": "vivo V5Plus"
    },
    {
        "packinfo": "VivoV9",
        "adinfo": "vivo 1727"
    },
    {
        "packinfo": "VivoV9 6GB",
        "adinfo": "vivo 1723"
    },
    {
        "packinfo": "VivoV9 Pro",
        "adinfo": "vivo 1851"
    },
    {
        "packinfo": "VivoX5",
        "adinfo": "vivo X5"
    },
    {
        "packinfo": "VivoX50",
        "adinfo": "vivo 2004"
    },
    {
        "packinfo": "VivoX50 Pro",
        "adinfo": "vivo 2006"
    },
    {
        "packinfo": "VivoX5M",
        "adinfo": "vivo X5M"
    },
    {
        "packinfo": "VivoX5Max",
        "adinfo": "vivo X5Max"
    },
    {
        "packinfo": "VivoX5Max S",
        "adinfo": "vivo X5Max S"
    },
    {
        "packinfo": "VivoX5MaxV",
        "adinfo": "vivo X5MaxV"
    },
    {
        "packinfo": "VivoX5Pro",
        "adinfo": "vivo X5Pro"
    },
    {
        "packinfo": "VivoX5Pro D",
        "adinfo": "vivo X5Pro D"
    },
    {
        "packinfo": "VivoX5Pro V",
        "adinfo": "vivo X5Pro V"
    },
    {
        "packinfo": "VivoX6A",
        "adinfo": "vivo PD1415A"
    },
    {
        "packinfo": "VivoX6D",
        "adinfo": "vivo X6D"
    },
    {
        "packinfo": "VivoX6Plus A",
        "adinfo": "vivo PD1515A"
    },
    {
        "packinfo": "VivoX6Plus D",
        "adinfo": "vivo PD1501D"
    },
    {
        "packinfo": "VivoX6S A",
        "adinfo": "vivo X6S A"
    },
    {
        "packinfo": "VivoX6SPlusA",
        "adinfo": "vivo PD1515BA"
    },
    {
        "packinfo": "VivoX7",
        "adinfo": "vivo X7"
    },
    {
        "packinfo": "VivoX7Plus",
        "adinfo": "vivo X7Plus"
    },
    {
        "packinfo": "VivoX80",
        "adinfo": "V2144"
    },
    {
        "packinfo": "VivoX80 Lite  5G",
        "adinfo": "V2208"
    },
    {
        "packinfo": "VivoX80 Pro",
        "adinfo": "V2145"
    },
    {
        "packinfo": "VivoX9",
        "adinfo": "vivo X9"
    },
    {
        "packinfo": "VivoX90",
        "adinfo": "V2218"
    },
    {
        "packinfo": "VivoX90 Pro",
        "adinfo": "V2219"
    },
    {
        "packinfo": "VivoX9i",
        "adinfo": "vivo X9i"
    },
    {
        "packinfo": "VivoXplay5A",
        "adinfo": "vivo PD1522A"
    },
    {
        "packinfo": "VivoXplay5A",
        "adinfo": "vivo Xplay5A"
    },
    {
        "packinfo": "VivoXplay6",
        "adinfo": "vivo Xplay6"
    },
    {
        "packinfo": "VivoY01A",
        "adinfo": "V2166"
    },
    {
        "packinfo": "VivoY02",
        "adinfo": "V2217"
    },
    {
        "packinfo": "VivoY02",
        "adinfo": "V2234_PK"
    },
    {
        "packinfo": "VivoY02",
        "adinfo": "V2236"
    },
    {
        "packinfo": "VivoY02A",
        "adinfo": "V2234"
    },
    {
        "packinfo": "VivoY02s",
        "adinfo": "V2203"
    },
    {
        "packinfo": "VivoY02s",
        "adinfo": "V2221"
    },
    {
        "packinfo": "VivoY02s",
        "adinfo": "V2229"
    },
    {
        "packinfo": "VivoY02t",
        "adinfo": "V2252"
    },
    {
        "packinfo": "VivoY02t",
        "adinfo": "V2254"
    },
    {
        "packinfo": "VivoY100",
        "adinfo": "V2239"
    },
    {
        "packinfo": "VivoY100A",
        "adinfo": "V2222"
    },
    {
        "packinfo": "VivoY11",
        "adinfo": "V2236A"
    },
    {
        "packinfo": "VivoY11",
        "adinfo": "vivo Y11"
    },
    {
        "packinfo": "VivoY15",
        "adinfo": "vivo Y15"
    },
    {
        "packinfo": "VivoY15C",
        "adinfo": "V2212"
    },
    {
        "packinfo": "VivoY15S",
        "adinfo": "vivo Y15S"
    },
    {
        "packinfo": "VivoY16",
        "adinfo": "V2204"
    },
    {
        "packinfo": "VivoY16",
        "adinfo": "V2214"
    },
    {
        "packinfo": "VivoY16",
        "adinfo": "V2305"
    },
    {
        "packinfo": "VivoY17",
        "adinfo": "vivo 1902"
    },
    {
        "packinfo": "VivoY17s",
        "adinfo": "V2310"
    },
    {
        "packinfo": "VivoY21",
        "adinfo": "vivo Y21"
    },
    {
        "packinfo": "VivoY21A",
        "adinfo": "V2149"
    },
    {
        "packinfo": "VivoY21L",
        "adinfo": "vivo Y21L"
    },
    {
        "packinfo": "VivoY22",
        "adinfo": "vivo Y22"
    },
    {
        "packinfo": "VivoY22s",
        "adinfo": "V2206"
    },
    {
        "packinfo": "VivoY27",
        "adinfo": "V2249"
    },
    {
        "packinfo": "VivoY27",
        "adinfo": "vivo Y27"
    },
    {
        "packinfo": "VivoY27 5G",
        "adinfo": "V2302"
    },
    {
        "packinfo": "VivoY27 5G",
        "adinfo": "V2302"
    },
    {
        "packinfo": "VivoY28",
        "adinfo": "vivo Y28"
    },
    {
        "packinfo": "VivoY30 5G",
        "adinfo": "V2160"
    },
    {
        "packinfo": "VivoY31",
        "adinfo": "vivo Y31"
    },
    {
        "packinfo": "VivoY31",
        "adinfo": "vivo Y31"
    },
    {
        "packinfo": "VivoY31L",
        "adinfo": "vivo Y31L"
    },
    {
        "packinfo": "VivoY31i",
        "adinfo": "vivo 1707"
    },
    {
        "packinfo": "VivoY31i",
        "adinfo": "vivo Y31"
    },
    {
        "packinfo": "VivoY31i",
        "adinfo": "vivo Y31i"
    },
    {
        "packinfo": "VivoY33",
        "adinfo": "vivo Y33"
    },
    {
        "packinfo": "VivoY33t",
        "adinfo": "V2236A"
    },
    {
        "packinfo": "VivoY35",
        "adinfo": "vivo Y35"
    },
    {
        "packinfo": "VivoY35",
        "adinfo": "V2230A"
    },
    {
        "packinfo": "VivoY35",
        "adinfo": "V2205"
    },
    {
        "packinfo": "VivoY35+",
        "adinfo": "V2279A"
    },
    {
        "packinfo": "VivoY35A",
        "adinfo": "vivo Y35A"
    },
    {
        "packinfo": "VivoY35m",
        "adinfo": "V2230A"
    },
    {
        "packinfo": "VivoY35m+",
        "adinfo": "V2279A"
    },
    {
        "packinfo": "VivoY36",
        "adinfo": "V2247"
    },
    {
        "packinfo": "VivoY36",
        "adinfo": "V2324"
    },
    {
        "packinfo": "VivoY36 5G",
        "adinfo": "V2248"
    },
    {
        "packinfo": "VivoY51",
        "adinfo": "vivo Y51"
    },
    {
        "packinfo": "VivoY51A",
        "adinfo": "vivo Y51A"
    },
    {
        "packinfo": "VivoY53",
        "adinfo": "vivo 1606"
    },
    {
        "packinfo": "VivoY53L",
        "adinfo": "vivo PD1628"
    },
    {
        "packinfo": "VivoY53t",
        "adinfo": "V2230A"
    },
    {
        "packinfo": "VivoY55",
        "adinfo": "vivo 1603"
    },
    {
        "packinfo": "VivoY55",
        "adinfo": "V2154"
    },
    {
        "packinfo": "VivoY55A",
        "adinfo": "vivo Y55"
    },
    {
        "packinfo": "VivoY55s",
        "adinfo": "vivo 1610"
    },
    {
        "packinfo": "VivoY55s",
        "adinfo": "V2164A"
    },
    {
        "packinfo": "VivoY56 5G",
        "adinfo": "V2225"
    },
    {
        "packinfo": "VivoY56 5G",
        "adinfo": "V2311"
    },
    {
        "packinfo": "VivoY66",
        "adinfo": "vivo Y66"
    },
    {
        "packinfo": "VivoY67",
        "adinfo": "vivo Y67"
    },
    {
        "packinfo": "VivoY71",
        "adinfo": "vivo 1801"
    },
    {
        "packinfo": "VivoY77t",
        "adinfo": "V2278A"
    },
    {
        "packinfo": "VivoY78",
        "adinfo": "V2278A"
    },
    {
        "packinfo": "VivoY78 5G",
        "adinfo": "V2244"
    },
    {
        "packinfo": "VivoY78+",
        "adinfo": "V2271A"
    },
    {
        "packinfo": "VivoY78m",
        "adinfo": "V2278A"
    },
    {
        "packinfo": "VivoY79A",
        "adinfo": "vivo PD1708"
    },
    {
        "packinfo": "VivoY79A",
        "adinfo": "vivo Y79A"
    },
    {
        "packinfo": "VivoY937",
        "adinfo": "vivo Y937"
    },
    {
        "packinfo": "VivoY93s",
        "adinfo": "V1818CA"
    },
    {
        "packinfo": "VivoY93标准版 64G",
        "adinfo": "V1818BA"
    },
    {
        "packinfo": "VivoY93标准版 64G",
        "adinfo": "V1818CA"
    },
    {
        "packinfo": "VivoY97",
        "adinfo": "V1813A"
    },
    {
        "packinfo": "VivoZ1",
        "adinfo": "vivo Z1"
    },
    {
        "packinfo": "VivoZ1 Pro",
        "adinfo": "vivo 1951"
    },
    {
        "packinfo": "VivoZ3i",
        "adinfo": "V1813A"
    },
    {
        "packinfo": "VivoZ3i",
        "adinfo": "V1813A"
    },
    {
        "packinfo": "VivoiQOO 10",
        "adinfo": "V2217A"
    },
    {
        "packinfo": "VivoiQOO 10 Pro",
        "adinfo": "V2218A"
    },
    {
        "packinfo": "VivoiQOO 11",
        "adinfo": "I2212"
    },
    {
        "packinfo": "VivoiQOO 11",
        "adinfo": "V2243A"
    },
    {
        "packinfo": "VivoiQOO 11 Pro",
        "adinfo": "V2254A"
    },
    {
        "packinfo": "VivoiQOO 11S",
        "adinfo": "V2304A"
    },
    {
        "packinfo": "VivoiQOO 9 Pro",
        "adinfo": "I2022"
    },
    {
        "packinfo": "VivoiQOO 9 SE",
        "adinfo": "I2019"
    },
    {
        "packinfo": "VivoiQOO 9T",
        "adinfo": "I2201"
    },
    {
        "packinfo": "VivoiQOO Neo5S",
        "adinfo": "V2154A"
    },
    {
        "packinfo": "VivoiQOO Neo6",
        "adinfo": "V2196A"
    },
    {
        "packinfo": "VivoiQOO Neo6 SE",
        "adinfo": "V2199A"
    },
    {
        "packinfo": "VivoiQOO Neo7",
        "adinfo": "I2214"
    },
    {
        "packinfo": "VivoiQOO Neo7",
        "adinfo": "V2231A"
    },
    {
        "packinfo": "VivoiQOO Neo7 Pro",
        "adinfo": "I2217"
    },
    {
        "packinfo": "VivoiQOO Neo7 SE",
        "adinfo": "V2238A"
    },
    {
        "packinfo": "VivoiQOO Neo7 竞速版",
        "adinfo": "V2232A"
    },
    {
        "packinfo": "VivoiQOO Neo7 竞速版",
        "adinfo": "V2232A"
    },
    {
        "packinfo": "VivoiQOO Neo8",
        "adinfo": "V2301A"
    },
    {
        "packinfo": "VivoiQOO Neo8 Pro",
        "adinfo": "V2302A"
    },
    {
        "packinfo": "VivoiQOO Pad",
        "adinfo": "iPA2375"
    },
    {
        "packinfo": "VivoiQOO Z5",
        "adinfo": "I2018"
    },
    {
        "packinfo": "VivoiQOO Z5 6000mAh",
        "adinfo": "V2188A"
    },
    {
        "packinfo": "VivoiQOO Z6",
        "adinfo": "I2203"
    },
    {
        "packinfo": "VivoiQOO Z6",
        "adinfo": "I2206"
    },
    {
        "packinfo": "VivoiQOO Z6 Lite 5G",
        "adinfo": "I2208"
    },
    {
        "packinfo": "VivoiQOO Z6 Pro",
        "adinfo": "I2126"
    },
    {
        "packinfo": "VivoiQOO Z6x",
        "adinfo": "V2164KA"
    },
    {
        "packinfo": "VivoiQOO Z7",
        "adinfo": "V2270A"
    },
    {
        "packinfo": "VivoiQOO Z7 5G",
        "adinfo": "I2207"
    },
    {
        "packinfo": "VivoiQOO Z7 5G",
        "adinfo": "I2213"
    },
    {
        "packinfo": "VivoiQOO Z7 Pro 5G",
        "adinfo": "I2301"
    },
    {
        "packinfo": "VivoiQOO Z7i",
        "adinfo": "V2230EA"
    },
    {
        "packinfo": "VivoiQOO Z7s 5G",
        "adinfo": "I2223"
    },
    {
        "packinfo": "VivoiQOO Z7x",
        "adinfo": "V2272A"
    },
    {
        "packinfo": "VivoiQOO Z7x (m)",
        "adinfo": "V2272A"
    },
    {
        "packinfo": "VivoiQOO Z7x 5G",
        "adinfo": "I2216"
    },
    {
        "packinfo": "VivoiQOO Z8x",
        "adinfo": "V2312A"
    },
    {
        "packinfo": "Vivovivo  1907",
        "adinfo": "vivo 1907"
    },
    {
        "packinfo": "Vivovivo  X21i  A",
        "adinfo": "vivo X21i A"
    },
    {
        "packinfo": "Vivovivo  Y75s",
        "adinfo": "vivo Y75s"
    },
    {
        "packinfo": "Vivovivo  Y85A",
        "adinfo": "vivo Y85A"
    },
    {
        "packinfo": "Vivovivo 1611",
        "adinfo": "vivo 1611"
    },
    {
        "packinfo": "Vivovivo 1714",
        "adinfo": "vivo 1714"
    },
    {
        "packinfo": "Vivovivo 1716",
        "adinfo": "vivo 1716"
    },
    {
        "packinfo": "Vivovivo 1718",
        "adinfo": "vivo 1718"
    },
    {
        "packinfo": "Vivovivo 1720",
        "adinfo": "vivo 1720"
    },
    {
        "packinfo": "Vivovivo 1721",
        "adinfo": "vivo 1721"
    },
    {
        "packinfo": "Vivovivo 1723",
        "adinfo": "vivo 1723"
    },
    {
        "packinfo": "Vivovivo 1724",
        "adinfo": "vivo 1724"
    },
    {
        "packinfo": "Vivovivo 1725",
        "adinfo": "vivo 1725"
    },
    {
        "packinfo": "Vivovivo 1726",
        "adinfo": "vivo 1726"
    },
    {
        "packinfo": "Vivovivo 1727",
        "adinfo": "vivo 1727"
    },
    {
        "packinfo": "Vivovivo 1802",
        "adinfo": "vivo 1802"
    },
    {
        "packinfo": "Vivovivo 1803",
        "adinfo": "vivo 1803"
    },
    {
        "packinfo": "Vivovivo 1804",
        "adinfo": "vivo 1804"
    },
    {
        "packinfo": "Vivovivo 1805",
        "adinfo": "vivo 1805"
    },
    {
        "packinfo": "Vivovivo 1806",
        "adinfo": "vivo 1806"
    },
    {
        "packinfo": "Vivovivo 1807",
        "adinfo": "vivo 1807"
    },
    {
        "packinfo": "Vivovivo 1807",
        "adinfo": "vivo 1807"
    },
    {
        "packinfo": "Vivovivo 1808",
        "adinfo": "vivo 1808"
    },
    {
        "packinfo": "Vivovivo 1811",
        "adinfo": "vivo 1811"
    },
    {
        "packinfo": "Vivovivo 1812",
        "adinfo": "vivo 1812"
    },
    {
        "packinfo": "Vivovivo 1813",
        "adinfo": "vivo 1813"
    },
    {
        "packinfo": "Vivovivo 1814",
        "adinfo": "vivo 1814"
    },
    {
        "packinfo": "Vivovivo 1815",
        "adinfo": "vivo 1815"
    },
    {
        "packinfo": "Vivovivo 1816",
        "adinfo": "vivo 1816"
    },
    {
        "packinfo": "Vivovivo 1817",
        "adinfo": "vivo 1817"
    },
    {
        "packinfo": "Vivovivo 1818",
        "adinfo": "vivo 1818"
    },
    {
        "packinfo": "Vivovivo 1818",
        "adinfo": "vivo 1818"
    },
    {
        "packinfo": "Vivovivo 1818",
        "adinfo": "V1832A"
    },
    {
        "packinfo": "Vivovivo 1819",
        "adinfo": "vivo 1819"
    },
    {
        "packinfo": "Vivovivo 1819",
        "adinfo": "vivo 1819"
    },
    {
        "packinfo": "Vivovivo 1820",
        "adinfo": "vivo 1820"
    },
    {
        "packinfo": "Vivovivo 1901",
        "adinfo": "vivo 1901"
    },
    {
        "packinfo": "Vivovivo 1902",
        "adinfo": "vivo 1902"
    },
    {
        "packinfo": "Vivovivo 1904",
        "adinfo": "vivo 1904"
    },
    {
        "packinfo": "Vivovivo 1906",
        "adinfo": "vivo 1906"
    },
    {
        "packinfo": "Vivovivo 1906",
        "adinfo": "vivo 2007"
    },
    {
        "packinfo": "Vivovivo 1907",
        "adinfo": "vivo 1907"
    },
    {
        "packinfo": "Vivovivo 1907",
        "adinfo": "vivo 1907"
    },
    {
        "packinfo": "Vivovivo 1909",
        "adinfo": "vivo 1909"
    },
    {
        "packinfo": "Vivovivo 1910",
        "adinfo": "vivo 1910"
    },
    {
        "packinfo": "Vivovivo 1910",
        "adinfo": "vivo 1910"
    },
    {
        "packinfo": "Vivovivo 1912",
        "adinfo": "vivo 1912"
    },
    {
        "packinfo": "Vivovivo 1913",
        "adinfo": "vivo 1913"
    },
    {
        "packinfo": "Vivovivo 1914",
        "adinfo": "vivo 1914"
    },
    {
        "packinfo": "Vivovivo 1915",
        "adinfo": "vivo 1915"
    },
    {
        "packinfo": "Vivovivo 1916",
        "adinfo": "vivo 1916"
    },
    {
        "packinfo": "Vivovivo 1917",
        "adinfo": "vivo 1917"
    },
    {
        "packinfo": "Vivovivo 1919",
        "adinfo": "vivo 1919"
    },
    {
        "packinfo": "Vivovivo 1920",
        "adinfo": "vivo 1920"
    },
    {
        "packinfo": "Vivovivo 1921",
        "adinfo": "vivo 1921"
    },
    {
        "packinfo": "Vivovivo 1929",
        "adinfo": "vivo 1929"
    },
    {
        "packinfo": "Vivovivo 1933",
        "adinfo": "vivo 1933"
    },
    {
        "packinfo": "Vivovivo 1935",
        "adinfo": "vivo 1935"
    },
    {
        "packinfo": "Vivovivo 1937",
        "adinfo": "vivo 1937"
    },
    {
        "packinfo": "Vivovivo 1938",
        "adinfo": "vivo 1938"
    },
    {
        "packinfo": "Vivovivo 1940",
        "adinfo": "vivo 1940"
    },
    {
        "packinfo": "Vivovivo 2005",
        "adinfo": "vivo 2005"
    },
    {
        "packinfo": "Vivovivo 2010",
        "adinfo": "vivo 1902"
    },
    {
        "packinfo": "Vivovivo 2010",
        "adinfo": "vivo 2010"
    },
    {
        "packinfo": "Vivovivo 2015",
        "adinfo": "vivo 2015"
    },
    {
        "packinfo": "Vivovivo 2015_21",
        "adinfo": "vivo 2015_21"
    },
    {
        "packinfo": "Vivovivo 2018",
        "adinfo": "vivo 2018"
    },
    {
        "packinfo": "Vivovivo 2019",
        "adinfo": "vivo 2019"
    },
    {
        "packinfo": "Vivovivo NEX A",
        "adinfo": "vivo NEX A"
    },
    {
        "packinfo": "Vivovivo NEX S",
        "adinfo": "vivo NEX S"
    },
    {
        "packinfo": "Vivovivo Pad Air",
        "adinfo": "PA2353"
    },
    {
        "packinfo": "Vivovivo Pad2",
        "adinfo": "PA2373"
    },
    {
        "packinfo": "Vivovivo S1",
        "adinfo": "V1831A"
    },
    {
        "packinfo": "Vivovivo S15 Pro",
        "adinfo": "V2207A"
    },
    {
        "packinfo": "Vivovivo S16",
        "adinfo": "V2244A"
    },
    {
        "packinfo": "Vivovivo S16 Pro",
        "adinfo": "V2245A"
    },
    {
        "packinfo": "Vivovivo S16e",
        "adinfo": "V2239A"
    },
    {
        "packinfo": "Vivovivo S17e",
        "adinfo": "V2285A"
    },
    {
        "packinfo": "Vivovivo T2",
        "adinfo": "V2199GA"
    },
    {
        "packinfo": "Vivovivo X Flip",
        "adinfo": "V2256A"
    },
    {
        "packinfo": "Vivovivo X Fold",
        "adinfo": "V2178A"
    },
    {
        "packinfo": "Vivovivo X Fold+",
        "adinfo": "V2229A"
    },
    {
        "packinfo": "Vivovivo X Fold2",
        "adinfo": "V2266A"
    },
    {
        "packinfo": "Vivovivo X Note",
        "adinfo": "V2170A"
    },
    {
        "packinfo": "Vivovivo X20",
        "adinfo": "vivo PD1709"
    },
    {
        "packinfo": "Vivovivo X20",
        "adinfo": "vivo X20A"
    },
    {
        "packinfo": "Vivovivo X20Plus",
        "adinfo": "vivo PD1710"
    },
    {
        "packinfo": "Vivovivo X20Plus",
        "adinfo": "vivo X20Plus A"
    },
    {
        "packinfo": "Vivovivo X20Plus UD",
        "adinfo": "vivo PD1721"
    },
    {
        "packinfo": "Vivovivo X20Plus UD",
        "adinfo": "vivo X20Plus UD"
    },
    {
        "packinfo": "Vivovivo X21A",
        "adinfo": "vivo X21A"
    },
    {
        "packinfo": "Vivovivo X21UD A",
        "adinfo": "vivo X21UD A"
    },
    {
        "packinfo": "Vivovivo X70 Pro+",
        "adinfo": "V2114"
    },
    {
        "packinfo": "Vivovivo X80",
        "adinfo": "V2183A"
    },
    {
        "packinfo": "Vivovivo X80 Pro",
        "adinfo": "V2185A"
    },
    {
        "packinfo": "Vivovivo X80 Pro 天玑9000版",
        "adinfo": "V2186A"
    },
    {
        "packinfo": "Vivovivo X90",
        "adinfo": "V2241A"
    },
    {
        "packinfo": "Vivovivo X90 Pro",
        "adinfo": "V2242A"
    },
    {
        "packinfo": "Vivovivo X90 Pro+",
        "adinfo": "V2227A"
    },
    {
        "packinfo": "Vivovivo X90s",
        "adinfo": "V2241HA"
    },
    {
        "packinfo": "Vivovivo X9Plus",
        "adinfo": "vivo X9Plus"
    },
    {
        "packinfo": "Vivovivo X9s",
        "adinfo": "vivo PD1616B"
    },
    {
        "packinfo": "Vivovivo X9s",
        "adinfo": "vivo X9s"
    },
    {
        "packinfo": "Vivovivo X9s Plus",
        "adinfo": "vivo PD1635"
    },
    {
        "packinfo": "Vivovivo X9s Plus",
        "adinfo": "vivo X9s Plus"
    },
    {
        "packinfo": "Vivovivo Y11",
        "adinfo": "vivo Y11"
    },
    {
        "packinfo": "Vivovivo Y22",
        "adinfo": "V2207"
    },
    {
        "packinfo": "Vivovivo Y22",
        "adinfo": "V2238"
    },
    {
        "packinfo": "Vivovivo Y22",
        "adinfo": "vivo Y22"
    },
    {
        "packinfo": "Vivovivo Y28",
        "adinfo": "vivo Y28"
    },
    {
        "packinfo": "Vivovivo Y65",
        "adinfo": "vivo 1719"
    },
    {
        "packinfo": "Vivovivo Y66i A",
        "adinfo": "vivo Y66i A"
    },
    {
        "packinfo": "Vivovivo Y69A",
        "adinfo": "vivo Y69A"
    },
    {
        "packinfo": "Vivovivo Y71A",
        "adinfo": "vivo Y71A"
    },
    {
        "packinfo": "Vivovivo Y75A",
        "adinfo": "vivo Y75A"
    },
    {
        "packinfo": "Vivovivo Y75s",
        "adinfo": "V2069BA"
    },
    {
        "packinfo": "Vivovivo Y77",
        "adinfo": "V2219A"
    },
    {
        "packinfo": "Vivovivo Y83A",
        "adinfo": "vivo Y83A"
    },
    {
        "packinfo": "Vivovivo Z1i",
        "adinfo": "vivo Y89"
    },
    {
        "packinfo": "Vivovivo Z1i",
        "adinfo": "vivo Z1i"
    },
    {
        "packinfo": "Vivovivo Z3x",
        "adinfo": "vivo Z3x"
    },
    {
        "packinfo": "VivoV1Max",
        "adinfo": "vivo Y37"
    },
    {
        "packinfo": "VivoS17",
        "adinfo": "V2283A"
    },
    {
        "packinfo": "VivoS17 Pro",
        "adinfo": "V2284A"
    },
    {
        "packinfo": "VivoT1",
        "adinfo": "V2153"
    },
    {
        "packinfo": "VivoT1",
        "adinfo": "V2154"
    },
    {
        "packinfo": "VivoT1",
        "adinfo": "V2168"
    },
    {
        "packinfo": "VivoT1 5G",
        "adinfo": "V2150"
    },
    {
        "packinfo": "VivoT1 Pro 5G",
        "adinfo": "V2151"
    },
    {
        "packinfo": "VivoT1x",
        "adinfo": "V2143"
    },
    {
        "packinfo": "VivoT2",
        "adinfo": "V2320"
    },
    {
        "packinfo": "VivoT2 5G",
        "adinfo": "V2240"
    },
    {
        "packinfo": "VivoT2x 5G",
        "adinfo": "V2253"
    },
    {
        "packinfo": "VivoT2x 5G",
        "adinfo": "V2312"
    },
    {
        "packinfo": "VivoU5x",
        "adinfo": "V2180GA"
    },
    {
        "packinfo": "VivoV1",
        "adinfo": "vivo V1"
    },
    {
        "packinfo": "OppoR5",
        "adinfo": "R8106"
    },
    {
        "packinfo": "OppoR5",
        "adinfo": "R8107"
    },
    {
        "packinfo": "OppoR5",
        "adinfo": "R8109"
    },
    {
        "packinfo": "OppoR6006",
        "adinfo": "R6006"
    },
    {
        "packinfo": "OppoR6007",
        "adinfo": "R6007"
    },
    {
        "packinfo": "OppoR7",
        "adinfo": "OPPO R7"
    },
    {
        "packinfo": "OppoR7",
        "adinfo": "R7"
    },
    {
        "packinfo": "OppoR7 Lite",
        "adinfo": "R7kf"
    },
    {
        "packinfo": "OppoR7 Plus",
        "adinfo": "R7Plus"
    },
    {
        "packinfo": "OppoR7 Plusf",
        "adinfo": "R7plusf"
    },
    {
        "packinfo": "OppoR7 Plusm",
        "adinfo": "R7Plusm"
    },
    {
        "packinfo": "OppoR7005",
        "adinfo": "R7005"
    },
    {
        "packinfo": "OppoR7007",
        "adinfo": "R7007"
    },
    {
        "packinfo": "OppoR7Plusf",
        "adinfo": "R7plusf"
    },
    {
        "packinfo": "OppoR7Plust",
        "adinfo": "R7Plust"
    },
    {
        "packinfo": "OppoR7c",
        "adinfo": "R7c"
    },
    {
        "packinfo": "OppoR7f",
        "adinfo": "R7f"
    },
    {
        "packinfo": "OppoR7g",
        "adinfo": "R7g"
    },
    {
        "packinfo": "OppoR7kc",
        "adinfo": "R7kc"
    },
    {
        "packinfo": "OppoR7kf",
        "adinfo": "R7kf"
    },
    {
        "packinfo": "OppoR7kt",
        "adinfo": "R7kt"
    },
    {
        "packinfo": "OppoR7s",
        "adinfo": "OPPO R7s"
    },
    {
        "packinfo": "OppoR7s",
        "adinfo": "R7s"
    },
    {
        "packinfo": "OppoR7s Plus",
        "adinfo": "OPPO R7sPlus"
    },
    {
        "packinfo": "OppoR7sf",
        "adinfo": "R7sf"
    },
    {
        "packinfo": "OppoR7sfg",
        "adinfo": "R7sf"
    },
    {
        "packinfo": "OppoR7sm",
        "adinfo": "R7sm"
    },
    {
        "packinfo": "OppoR7st",
        "adinfo": "R7st"
    },
    {
        "packinfo": "OppoR7t",
        "adinfo": "R7t"
    },
    {
        "packinfo": "OppoR8000",
        "adinfo": "R8000"
    },
    {
        "packinfo": "OppoR8001",
        "adinfo": "R8001"
    },
    {
        "packinfo": "OppoR8006",
        "adinfo": "R8006"
    },
    {
        "packinfo": "OppoR8007",
        "adinfo": "R8007"
    },
    {
        "packinfo": "OppoR809T",
        "adinfo": "R809T"
    },
    {
        "packinfo": "OppoR8106",
        "adinfo": "R8106"
    },
    {
        "packinfo": "OppoR815",
        "adinfo": "R815"
    },
    {
        "packinfo": "OppoR815T",
        "adinfo": "R815T"
    },
    {
        "packinfo": "OppoR815W",
        "adinfo": "R815W"
    },
    {
        "packinfo": "OppoR819",
        "adinfo": "R819"
    },
    {
        "packinfo": "OppoR819T",
        "adinfo": "R819T"
    },
    {
        "packinfo": "OppoR820",
        "adinfo": "R820"
    },
    {
        "packinfo": "OppoR8200",
        "adinfo": "R8200"
    },
    {
        "packinfo": "OppoR8201",
        "adinfo": "R8201"
    },
    {
        "packinfo": "OppoR8205",
        "adinfo": "R8205"
    },
    {
        "packinfo": "OppoR8206",
        "adinfo": "R8206"
    },
    {
        "packinfo": "OppoR8207",
        "adinfo": "R8207"
    },
    {
        "packinfo": "OppoR821",
        "adinfo": "R821"
    },
    {
        "packinfo": "OppoR821T",
        "adinfo": "R821T"
    },
    {
        "packinfo": "OppoR823T",
        "adinfo": "R823T"
    },
    {
        "packinfo": "OppoR827",
        "adinfo": "R827"
    },
    {
        "packinfo": "OppoR827T",
        "adinfo": "R827T"
    },
    {
        "packinfo": "OppoR829",
        "adinfo": "R829"
    },
    {
        "packinfo": "OppoR829T",
        "adinfo": "R829T"
    },
    {
        "packinfo": "OppoR830",
        "adinfo": "R830"
    },
    {
        "packinfo": "OppoR830S",
        "adinfo": "R830S"
    },
    {
        "packinfo": "OppoR831",
        "adinfo": "R831"
    },
    {
        "packinfo": "OppoR831",
        "adinfo": "R831T"
    },
    {
        "packinfo": "OppoR831K",
        "adinfo": "R831K"
    },
    {
        "packinfo": "OppoR831L",
        "adinfo": "R831L"
    },
    {
        "packinfo": "OppoR831S",
        "adinfo": "R831S"
    },
    {
        "packinfo": "OppoR831T",
        "adinfo": "R831T"
    },
    {
        "packinfo": "OppoR833T",
        "adinfo": "R833T"
    },
    {
        "packinfo": "OppoR850",
        "adinfo": "R850"
    },
    {
        "packinfo": "OppoR9",
        "adinfo": "OPPO R9"
    },
    {
        "packinfo": "OppoR9",
        "adinfo": "OPPO R9km"
    },
    {
        "packinfo": "OppoR9",
        "adinfo": "OPPO R9m"
    },
    {
        "packinfo": "OppoR9",
        "adinfo": "OPPO R9tm"
    },
    {
        "packinfo": "OppoR9 Plus",
        "adinfo": "OPPO R9 Plusm A"
    },
    {
        "packinfo": "OppoR9 Plus",
        "adinfo": "OPPO R9 Plustm A"
    },
    {
        "packinfo": "OppoR9 Plus A",
        "adinfo": "OPPO R9 Plus A"
    },
    {
        "packinfo": "OppoR9Plus",
        "adinfo": "X9079"
    },
    {
        "packinfo": "OppoR9PlusA",
        "adinfo": "OPPO R9 Plusm A"
    },
    {
        "packinfo": "OppoR9PlusA",
        "adinfo": "OPPO R9 Plustm A"
    },
    {
        "packinfo": "OppoR9PlusmA",
        "adinfo": "OPPO R9 Plusm A"
    },
    {
        "packinfo": "OppoR9PlustA",
        "adinfo": "OPPO R9 Plust A"
    },
    {
        "packinfo": "OppoR9PlustmA",
        "adinfo": "OPPO R9 Plustm A"
    },
    {
        "packinfo": "OppoR9k",
        "adinfo": "OPPO R9k"
    },
    {
        "packinfo": "OppoR9k",
        "adinfo": "OPPO R9km"
    },
    {
        "packinfo": "OppoR9k",
        "adinfo": "OPPO R9m"
    },
    {
        "packinfo": "OppoR9k",
        "adinfo": "OPPO R9tm"
    },
    {
        "packinfo": "OppoR9km",
        "adinfo": "OPPO R9km"
    },
    {
        "packinfo": "OppoR9m",
        "adinfo": "OPPO R9m"
    },
    {
        "packinfo": "OppoR9s",
        "adinfo": "CPH1607"
    },
    {
        "packinfo": "OppoR9s",
        "adinfo": "CPH1607fw"
    },
    {
        "packinfo": "OppoR9s",
        "adinfo": "OPPO R9s"
    },
    {
        "packinfo": "OppoR9s Plus",
        "adinfo": "CPH1611"
    },
    {
        "packinfo": "OppoR9s Plus",
        "adinfo": "OPPO R9s Plus"
    },
    {
        "packinfo": "OppoR9s Plus",
        "adinfo": "OPPO R9s Plust"
    },
    {
        "packinfo": "OppoR9s Plus",
        "adinfo": "OPPO R9sPlus"
    },
    {
        "packinfo": "OppoR9sk",
        "adinfo": "OPPO R9sk"
    },
    {
        "packinfo": "OppoR9sk",
        "adinfo": "OPPO R9skt"
    },
    {
        "packinfo": "OppoR9st",
        "adinfo": "OPPO R9st"
    },
    {
        "packinfo": "OppoR9t",
        "adinfo": "OPPO R9t"
    },
    {
        "packinfo": "OppoR9tm",
        "adinfo": "OPPO R9tm"
    },
    {
        "packinfo": "OppoReno",
        "adinfo": "CPH1917"
    },
    {
        "packinfo": "OppoReno",
        "adinfo": "CPH1917"
    },
    {
        "packinfo": "OppoReno 10x Room",
        "adinfo": "CPH1921"
    },
    {
        "packinfo": "OppoReno 10x Zoom",
        "adinfo": "CPH1919"
    },
    {
        "packinfo": "OppoReno 10x Zoom",
        "adinfo": "CPH1919RU"
    },
    {
        "packinfo": "OppoReno 10x Zoom",
        "adinfo": "CPH1919"
    },
    {
        "packinfo": "OppoReno 10x room",
        "adinfo": "CPH1921"
    },
    {
        "packinfo": "OppoReno 10倍变焦版",
        "adinfo": "PCCM00"
    },
    {
        "packinfo": "OppoReno 10倍变焦版",
        "adinfo": "PCCT00"
    },
    {
        "packinfo": "OppoReno 2",
        "adinfo": "CPH1907"
    },
    {
        "packinfo": "OppoReno 2 中国版",
        "adinfo": "PCKM00"
    },
    {
        "packinfo": "OppoReno 4Z 5G",
        "adinfo": "CPH2065"
    },
    {
        "packinfo": "OppoReno A",
        "adinfo": "CPH1983"
    },
    {
        "packinfo": "OppoReno Ace",
        "adinfo": "PCLM10"
    },
    {
        "packinfo": "OppoReno Ace2",
        "adinfo": "PDHM00"
    },
    {
        "packinfo": "OppoReno Z",
        "adinfo": "CPH1979"
    },
    {
        "packinfo": "OppoReno Z",
        "adinfo": "CPH1979"
    },
    {
        "packinfo": "OppoReno Z 中国版",
        "adinfo": "PCDM10"
    },
    {
        "packinfo": "OppoReno Z 中国版",
        "adinfo": "PCDT10"
    },
    {
        "packinfo": "OppoReno 标准版",
        "adinfo": "PCAM00"
    },
    {
        "packinfo": "OppoReno 标准版",
        "adinfo": "PCAT00"
    },
    {
        "packinfo": "OppoReno10 5G",
        "adinfo": "CPH2531"
    },
    {
        "packinfo": "OppoReno10 Pro 5G",
        "adinfo": "A302OP"
    },
    {
        "packinfo": "OppoReno10 Pro 5G",
        "adinfo": "CPH2525"
    },
    {
        "packinfo": "OppoReno10 Pro 5G",
        "adinfo": "CPH2541"
    },
    {
        "packinfo": "OppoReno10 Pro+ 5G",
        "adinfo": "CPH2521"
    },
    {
        "packinfo": "OppoReno2 Z",
        "adinfo": "CPH1945"
    },
    {
        "packinfo": "OppoReno2 Z",
        "adinfo": "CPH1951"
    },
    {
        "packinfo": "OppoReno2 Z 中国版",
        "adinfo": "PCKM80"
    },
    {
        "packinfo": "OppoReno3",
        "adinfo": "CPH2043"
    },
    {
        "packinfo": "OppoReno3 5G",
        "adinfo": "A001OP"
    },
    {
        "packinfo": "OppoReno3 5G 中国版",
        "adinfo": "PDCM00"
    },
    {
        "packinfo": "OppoReno3 A",
        "adinfo": "A002OP"
    },
    {
        "packinfo": "OppoReno3 A",
        "adinfo": "CPH2013"
    },
    {
        "packinfo": "OppoReno3 Pro",
        "adinfo": "CPH2009"
    },
    {
        "packinfo": "OppoReno3 Pro",
        "adinfo": "CPH2035"
    },
    {
        "packinfo": "OppoReno3 Pro",
        "adinfo": "CPH2036"
    },
    {
        "packinfo": "OppoReno3 Pro",
        "adinfo": "CPH2037"
    },
    {
        "packinfo": "OppoReno3 Pro 5G中国版",
        "adinfo": "PCRM00"
    },
    {
        "packinfo": "OppoReno3 元气版 5G",
        "adinfo": "PCLM50"
    },
    {
        "packinfo": "OppoReno4 5G",
        "adinfo": "CPH2091"
    },
    {
        "packinfo": "OppoReno4 F",
        "adinfo": "CPH2209"
    },
    {
        "packinfo": "OppoReno4 Lite",
        "adinfo": "CPH2125"
    },
    {
        "packinfo": "OppoReno4 Pro",
        "adinfo": "PDNT00"
    },
    {
        "packinfo": "OppoReno4 Pro",
        "adinfo": "CPH2089"
    },
    {
        "packinfo": "OppoReno4 Pro 5G",
        "adinfo": "CPH2089"
    },
    {
        "packinfo": "OppoReno4 Pro 中国版",
        "adinfo": "PDNM00"
    },
    {
        "packinfo": "OppoReno4 中国版",
        "adinfo": "PDPM00"
    },
    {
        "packinfo": "OppoReno4 中国版",
        "adinfo": "PDPT00"
    },
    {
        "packinfo": "OppoReno5",
        "adinfo": "CPH2159"
    },
    {
        "packinfo": "OppoReno5 A (eSIM)",
        "adinfo": "A103OP"
    },
    {
        "packinfo": "OppoReno5 F",
        "adinfo": "CPH2217"
    },
    {
        "packinfo": "OppoReno5 Lite",
        "adinfo": "CPH2205"
    },
    {
        "packinfo": "OppoReno5 Pro 5G",
        "adinfo": "PDSM00"
    },
    {
        "packinfo": "OppoReno6 Pro+ 5G",
        "adinfo": "PENM00"
    },
    {
        "packinfo": "OppoReno7 Z 5G/Reno7 Lite 5G/Reno8 Lite 5G",
        "adinfo": "CPH2343"
    },
    {
        "packinfo": "OppoReno7 中国版",
        "adinfo": "PFJM10"
    },
    {
        "packinfo": "OppoReno8 T 5G",
        "adinfo": "CPH2505"
    },
    {
        "packinfo": "OppoReno9 A",
        "adinfo": "A301OP"
    },
    {
        "packinfo": "OppoReno9 A",
        "adinfo": "CPH2523"
    },
    {
        "packinfo": "OppoU3",
        "adinfo": "U3"
    },
    {
        "packinfo": "OppoU707",
        "adinfo": "U707"
    },
    {
        "packinfo": "OppoU707T",
        "adinfo": "U707T"
    },
    {
        "packinfo": "OppoU708",
        "adinfo": "U708"
    },
    {
        "packinfo": "OppoUlike2",
        "adinfo": "U705W"
    },
    {
        "packinfo": "OppoUlike2",
        "adinfo": "U705T"
    },
    {
        "packinfo": "OppoX9000",
        "adinfo": "X9000"
    },
    {
        "packinfo": "OppoX9006",
        "adinfo": "X9006"
    },
    {
        "packinfo": "OppoX9007",
        "adinfo": "X9007"
    },
    {
        "packinfo": "OppoX9009",
        "adinfo": "X9009"
    },
    {
        "packinfo": "OppoX9009fw",
        "adinfo": "X9009fw"
    },
    {
        "packinfo": "OppoX9070",
        "adinfo": "X9070"
    },
    {
        "packinfo": "OppoX9076",
        "adinfo": "X9076"
    },
    {
        "packinfo": "OppoX9077",
        "adinfo": "X9077"
    },
    {
        "packinfo": "OppoX9077",
        "adinfo": "X9077"
    },
    {
        "packinfo": "OppoX9079",
        "adinfo": "X9079"
    },
    {
        "packinfo": "OppoX909",
        "adinfo": "X909"
    },
    {
        "packinfo": "OppoX909",
        "adinfo": "X909"
    },
    {
        "packinfo": "OppoX909",
        "adinfo": "X909T"
    },
    {
        "packinfo": "Opporealme 1",
        "adinfo": "CPH1859"
    },
    {
        "packinfo": "Opporealme 1",
        "adinfo": "CPH1861"
    },
    {
        "packinfo": "Opporealme 2",
        "adinfo": "RMX1805"
    },
    {
        "packinfo": "Opporealme 2",
        "adinfo": "RMX1809"
    },
    {
        "packinfo": "Opporealme 2 Pro",
        "adinfo": "RMX1803"
    },
    {
        "packinfo": "Opporealme 2 Pro",
        "adinfo": "RMX1807"
    },
    {
        "packinfo": "Opporealme 3",
        "adinfo": "RMX1821"
    },
    {
        "packinfo": "Opporealme 3",
        "adinfo": "RMX1822"
    },
    {
        "packinfo": "Opporealme 3",
        "adinfo": "RMX1825"
    },
    {
        "packinfo": "Opporealme 3Pro",
        "adinfo": "RMX1853"
    },
    {
        "packinfo": "Opporealme 3i",
        "adinfo": "RMX1827"
    },
    {
        "packinfo": "Opporealme 5",
        "adinfo": "RMX1911"
    },
    {
        "packinfo": "Opporealme C1",
        "adinfo": "RMX1811"
    },
    {
        "packinfo": "Opporealme C2",
        "adinfo": "RMX1941"
    },
    {
        "packinfo": "Opporealme C2",
        "adinfo": "RMX1942"
    },
    {
        "packinfo": "Opporealme C2",
        "adinfo": "RMX1943"
    },
    {
        "packinfo": "Opporealme C2",
        "adinfo": "RMX1945"
    },
    {
        "packinfo": "Opporealme U1",
        "adinfo": "RMX1831"
    },
    {
        "packinfo": "Opporealme U1",
        "adinfo": "RMX1833"
    },
    {
        "packinfo": "Opporealme X",
        "adinfo": "RMX1901"
    },
    {
        "packinfo": "Opporealme X Lite",
        "adinfo": "RMX1851"
    },
    {
        "packinfo": "Opporealme X50 5G",
        "adinfo": "RMX2051"
    },
    {
        "packinfo": "OppoR11",
        "adinfo": "OPPO R11"
    },
    {
        "packinfo": "OppoR11",
        "adinfo": "OPPO R11t"
    },
    {
        "packinfo": "OppoR11 Plus",
        "adinfo": "OPPO R11 Plus"
    },
    {
        "packinfo": "OppoR11 Plusk",
        "adinfo": "OPPO R11 Plusk"
    },
    {
        "packinfo": "OppoR11 Pluskt",
        "adinfo": "OPPO R11 Pluskt"
    },
    {
        "packinfo": "OppoR11 Plust",
        "adinfo": "OPPO R11 Plust"
    },
    {
        "packinfo": "OppoR11s",
        "adinfo": "OPPO R11s"
    },
    {
        "packinfo": "OppoR11sPlus",
        "adinfo": "OPPO R11s Plus"
    },
    {
        "packinfo": "OppoR11sPlust",
        "adinfo": "OPPO R11s Plust"
    },
    {
        "packinfo": "OppoR11st",
        "adinfo": "OPPO R11st"
    },
    {
        "packinfo": "OppoR15",
        "adinfo": "CPH1835"
    },
    {
        "packinfo": "OppoR15 Pro",
        "adinfo": "CPH1831"
    },
    {
        "packinfo": "OppoR15 Pro",
        "adinfo": "CPH1833"
    },
    {
        "packinfo": "OppoR15 Pro",
        "adinfo": "CPH1833"
    },
    {
        "packinfo": "OppoR15 中国版",
        "adinfo": "PACM00"
    },
    {
        "packinfo": "OppoR15 中国版",
        "adinfo": "PACT00"
    },
    {
        "packinfo": "OppoR15 梦境版",
        "adinfo": "PAAM00"
    },
    {
        "packinfo": "OppoR15 梦境版",
        "adinfo": "PAAT00"
    },
    {
        "packinfo": "OppoR15x",
        "adinfo": "PBCM10"
    },
    {
        "packinfo": "OppoR15x",
        "adinfo": "PBCT10"
    },
    {
        "packinfo": "OppoR17",
        "adinfo": "CPH1879"
    },
    {
        "packinfo": "OppoR17",
        "adinfo": "PBEM00"
    },
    {
        "packinfo": "OppoR17",
        "adinfo": "PBET00"
    },
    {
        "packinfo": "OppoR17 Pro",
        "adinfo": "CPH1877"
    },
    {
        "packinfo": "OppoR17 Pro",
        "adinfo": "PBDM00"
    },
    {
        "packinfo": "OppoR17 Pro",
        "adinfo": "PBDT00"
    },
    {
        "packinfo": "OppoOPPO A33",
        "adinfo": "CPH2137"
    },
    {
        "packinfo": "OppoOPPO A35",
        "adinfo": "PEFM00"
    },
    {
        "packinfo": "OppoOPPO A53 5G",
        "adinfo": "PECM30"
    },
    {
        "packinfo": "OppoOPPO A53 5G",
        "adinfo": "PECT30"
    },
    {
        "packinfo": "OppoOPPO A53s 5G",
        "adinfo": "CPH2321"
    },
    {
        "packinfo": "OppoOPPO A54",
        "adinfo": "PEZM00"
    },
    {
        "packinfo": "OppoOPPO A57s",
        "adinfo": "CPH2385"
    },
    {
        "packinfo": "OppoOPPO A74 5G",
        "adinfo": "CPH2197"
    },
    {
        "packinfo": "OppoOPPO A95 5G",
        "adinfo": "PELM00"
    },
    {
        "packinfo": "OppoOPPO F21 Pro 5G",
        "adinfo": "CPH2341"
    },
    {
        "packinfo": "OppoOPPO Pad",
        "adinfo": "OPD2101"
    },
    {
        "packinfo": "OppoOPPO Pad 2",
        "adinfo": "OPD2201"
    },
    {
        "packinfo": "OppoOPPO Pad 2",
        "adinfo": "OPD2202"
    },
    {
        "packinfo": "OppoOPPO Pad Air",
        "adinfo": "OPD2102"
    },
    {
        "packinfo": "OppoOPPO Reno10 5G",
        "adinfo": "PHW110"
    },
    {
        "packinfo": "OppoOPPO Reno10 Pro+ 5G",
        "adinfo": "PHU110"
    },
    {
        "packinfo": "OppoOPPO Reno5 A",
        "adinfo": "A101OP"
    },
    {
        "packinfo": "OppoOPPO Reno5 A",
        "adinfo": "CPH2199"
    },
    {
        "packinfo": "OppoOPPO Reno5 Pro+ 5G",
        "adinfo": "PDRM00"
    },
    {
        "packinfo": "OppoOPPO Reno5 pro",
        "adinfo": "CPH2201"
    },
    {
        "packinfo": "OppoOPPO Reno6 Z 5G",
        "adinfo": "CPH2237"
    },
    {
        "packinfo": "OppoOPPO Reno7",
        "adinfo": "CPH2363"
    },
    {
        "packinfo": "OppoOPPO Reno7 5G",
        "adinfo": "CPH2371"
    },
    {
        "packinfo": "OppoOPPO Reno7 5G/Find X5 Lite",
        "adinfo": "CPH2371"
    },
    {
        "packinfo": "OppoOPPO Reno7 A",
        "adinfo": "A201OP"
    },
    {
        "packinfo": "OppoOPPO Reno7 A",
        "adinfo": "CPH2353"
    },
    {
        "packinfo": "OppoOPPO Reno7 A",
        "adinfo": "OPG04"
    },
    {
        "packinfo": "OppoOPPO Reno7 Z 5G",
        "adinfo": "CPH2343"
    },
    {
        "packinfo": "OppoOPPO Reno7 Z 5G/F21 Pro 5G/Reno8 Lite 5G",
        "adinfo": "CPH2343"
    },
    {
        "packinfo": "OppoOPPO Reno7/F21 Pro",
        "adinfo": "CPH2363"
    },
    {
        "packinfo": "OppoOPPO Reno8 5G",
        "adinfo": "CPH2359"
    },
    {
        "packinfo": "OppoOPPO Reno8 Pro 5G",
        "adinfo": "CPH2357"
    },
    {
        "packinfo": "OppoOPPO Reno9 Pro 5G",
        "adinfo": "PGX110"
    },
    {
        "packinfo": "OppoOPPO Watch",
        "adinfo": "OPPO Watch"
    },
    {
        "packinfo": "OppoOPPO Watch",
        "adinfo": "OPPO Watch"
    },
    {
        "packinfo": "OppoF11",
        "adinfo": "CPH1911"
    },
    {
        "packinfo": "OppoF11",
        "adinfo": "CPH1913"
    },
    {
        "packinfo": "OppoF11",
        "adinfo": "CPH1915"
    },
    {
        "packinfo": "OppoF11 Pro",
        "adinfo": "CPH1969"
    },
    {
        "packinfo": "OppoF11 Pro",
        "adinfo": "CPH1987"
    },
    {
        "packinfo": "OppoF17 Pro",
        "adinfo": "CPH2119"
    },
    {
        "packinfo": "OppoF19 Pro",
        "adinfo": "CPH2285"
    },
    {
        "packinfo": "OppoF1f",
        "adinfo": "F1f"
    },
    {
        "packinfo": "OppoF1f",
        "adinfo": "F1fw"
    },
    {
        "packinfo": "OppoF1f",
        "adinfo": "F1w"
    },
    {
        "packinfo": "OppoF1fw",
        "adinfo": "F1f"
    },
    {
        "packinfo": "OppoF1fw",
        "adinfo": "F1fw"
    },
    {
        "packinfo": "OppoF1w",
        "adinfo": "F1f"
    },
    {
        "packinfo": "OppoF1w",
        "adinfo": "F1w"
    },
    {
        "packinfo": "OppoF7",
        "adinfo": "CPH1819"
    },
    {
        "packinfo": "OppoF7",
        "adinfo": "CPH1821"
    },
    {
        "packinfo": "OppoF9",
        "adinfo": "CPH1823"
    },
    {
        "packinfo": "OppoF9",
        "adinfo": "CPH1825"
    },
    {
        "packinfo": "OppoF9",
        "adinfo": "CPH1881"
    },
    {
        "packinfo": "OppoFind 5",
        "adinfo": "X909"
    },
    {
        "packinfo": "OppoFind N",
        "adinfo": "PEUM00"
    },
    {
        "packinfo": "OppoFind N2 Flip",
        "adinfo": "CPH2437"
    },
    {
        "packinfo": "OppoFind N2 Flip 中国版",
        "adinfo": "PGT110"
    },
    {
        "packinfo": "OppoFind X",
        "adinfo": "CPH1871"
    },
    {
        "packinfo": "OppoFind X",
        "adinfo": "CPH1875"
    },
    {
        "packinfo": "OppoFind X",
        "adinfo": "PAFM00"
    },
    {
        "packinfo": "OppoFind X",
        "adinfo": "PAFT00"
    },
    {
        "packinfo": "OppoFind X 兰博基尼",
        "adinfo": "PAHM00"
    },
    {
        "packinfo": "OppoFind X2",
        "adinfo": "CPH2023"
    },
    {
        "packinfo": "OppoFind X2 Lite",
        "adinfo": "CPH2005"
    },
    {
        "packinfo": "OppoFind X2 Neo/Reno3 Pro",
        "adinfo": "CPH2009"
    },
    {
        "packinfo": "OppoFind X2 Pro",
        "adinfo": "CPH2025"
    },
    {
        "packinfo": "OppoFind X2 Pro",
        "adinfo": "OPG01"
    },
    {
        "packinfo": "OppoFind X2 Pro 中国版",
        "adinfo": "PDEM30"
    },
    {
        "packinfo": "OppoFind X2 中国版",
        "adinfo": "PDEM10"
    },
    {
        "packinfo": "OppoFind X2 中国版",
        "adinfo": "PDET10"
    },
    {
        "packinfo": "OppoFind X3 Pro",
        "adinfo": "CPH2173"
    },
    {
        "packinfo": "OppoFind X3 Pro",
        "adinfo": "OPG03"
    },
    {
        "packinfo": "OppoFind X3 Pro 中国版",
        "adinfo": "PEEM00"
    },
    {
        "packinfo": "OppoFind X3 中国版",
        "adinfo": "PEDM00"
    },
    {
        "packinfo": "OppoFind X5",
        "adinfo": "CPH2307"
    },
    {
        "packinfo": "OppoFind X5 Pro",
        "adinfo": "CPH2305"
    },
    {
        "packinfo": "OppoFind X6",
        "adinfo": "PGFM10"
    },
    {
        "packinfo": "OppoFind X6 Pro",
        "adinfo": "PGEM10"
    },
    {
        "packinfo": "OppoFind5",
        "adinfo": "X909"
    },
    {
        "packinfo": "OppoFind5",
        "adinfo": "X909T"
    },
    {
        "packinfo": "OppoK1",
        "adinfo": "PBCM30"
    },
    {
        "packinfo": "OppoK3",
        "adinfo": "PCGM00"
    },
    {
        "packinfo": "OppoK3",
        "adinfo": "PCGT00"
    },
    {
        "packinfo": "OppoK3",
        "adinfo": "CPH1955"
    },
    {
        "packinfo": "OppoK5",
        "adinfo": "PCNM00"
    },
    {
        "packinfo": "OppoK7x 中国版",
        "adinfo": "PERM00"
    },
    {
        "packinfo": "OppoN1",
        "adinfo": "N1"
    },
    {
        "packinfo": "OppoN1 mimi",
        "adinfo": "N5111"
    },
    {
        "packinfo": "OppoN1 mimi",
        "adinfo": "N5116"
    },
    {
        "packinfo": "OppoN1T",
        "adinfo": "N1T"
    },
    {
        "packinfo": "OppoN1W",
        "adinfo": "N1W"
    },
    {
        "packinfo": "OppoN3",
        "adinfo": "N5206"
    },
    {
        "packinfo": "OppoN3",
        "adinfo": "N5207"
    },
    {
        "packinfo": "OppoN3",
        "adinfo": "N5209"
    },
    {
        "packinfo": "OppoN5110",
        "adinfo": "N5110"
    },
    {
        "packinfo": "OppoN5117",
        "adinfo": "N5117"
    },
    {
        "packinfo": "OppoA1 Pro 5G",
        "adinfo": "PHQ110"
    },
    {
        "packinfo": "OppoA11",
        "adinfo": "A11"
    },
    {
        "packinfo": "OppoA11 中国版",
        "adinfo": "PCHM10"
    },
    {
        "packinfo": "OppoA11 中国版",
        "adinfo": "PCHT10"
    },
    {
        "packinfo": "OppoA11f",
        "adinfo": "A11f"
    },
    {
        "packinfo": "OppoA11n中国版",
        "adinfo": "PCHM00"
    },
    {
        "packinfo": "OppoA11t",
        "adinfo": "A11t"
    },
    {
        "packinfo": "OppoA11w",
        "adinfo": "A11w"
    },
    {
        "packinfo": "OppoA11x 中国版",
        "adinfo": "PCHM30"
    },
    {
        "packinfo": "OppoA11x 中国版",
        "adinfo": "PCHT30"
    },
    {
        "packinfo": "OppoA13t",
        "adinfo": "A31t"
    },
    {
        "packinfo": "OppoA1601",
        "adinfo": "A1601"
    },
    {
        "packinfo": "OppoA1601",
        "adinfo": "A1601fw"
    },
    {
        "packinfo": "OppoA1601fw",
        "adinfo": "A1601fw"
    },
    {
        "packinfo": "OppoA1603",
        "adinfo": "A1603"
    },
    {
        "packinfo": "OppoA17",
        "adinfo": "CPH2477"
    },
    {
        "packinfo": "OppoA17k",
        "adinfo": "CPH2471"
    },
    {
        "packinfo": "OppoA1k",
        "adinfo": "CPH1923"
    },
    {
        "packinfo": "OppoA3",
        "adinfo": "CPH1837"
    },
    {
        "packinfo": "OppoA31",
        "adinfo": "A31"
    },
    {
        "packinfo": "OppoA31c",
        "adinfo": "A31c"
    },
    {
        "packinfo": "OppoA31u",
        "adinfo": "A31u"
    },
    {
        "packinfo": "OppoA32 中国版",
        "adinfo": "PDVM00"
    },
    {
        "packinfo": "OppoA33",
        "adinfo": "A33"
    },
    {
        "packinfo": "OppoA33f",
        "adinfo": "A33f"
    },
    {
        "packinfo": "OppoA33f",
        "adinfo": "A33fw"
    },
    {
        "packinfo": "OppoA33fw",
        "adinfo": "A33fw"
    },
    {
        "packinfo": "OppoA33m",
        "adinfo": "OPPO A33m"
    },
    {
        "packinfo": "OppoA33t",
        "adinfo": "A33t"
    },
    {
        "packinfo": "OppoA33w",
        "adinfo": "A33w"
    },
    {
        "packinfo": "OppoA35",
        "adinfo": "OPPO A35"
    },
    {
        "packinfo": "OppoA37",
        "adinfo": "OPPO A37"
    },
    {
        "packinfo": "OppoA37",
        "adinfo": "OPPO A37m"
    },
    {
        "packinfo": "OppoA37f",
        "adinfo": "A37f"
    },
    {
        "packinfo": "OppoA37f",
        "adinfo": "A37fw"
    },
    {
        "packinfo": "OppoA37fw",
        "adinfo": "A37fw"
    },
    {
        "packinfo": "OppoA37fw",
        "adinfo": "A37fw"
    },
    {
        "packinfo": "OppoA37fw-International",
        "adinfo": "A37f"
    },
    {
        "packinfo": "OppoA37m",
        "adinfo": "OPPO A37m"
    },
    {
        "packinfo": "OppoA37t",
        "adinfo": "OPPO A37t"
    },
    {
        "packinfo": "OppoA37tm",
        "adinfo": "OPPO A37tm"
    },
    {
        "packinfo": "OppoA39",
        "adinfo": "OPPO A39"
    },
    {
        "packinfo": "OppoA39m",
        "adinfo": "OPPO A39m"
    },
    {
        "packinfo": "OppoA39t",
        "adinfo": "OPPO A39t"
    },
    {
        "packinfo": "OppoA39tm",
        "adinfo": "OPPO A39tm"
    },
    {
        "packinfo": "OppoA3s",
        "adinfo": "CPH1803"
    },
    {
        "packinfo": "OppoA3s",
        "adinfo": "CPH1853"
    },
    {
        "packinfo": "OppoA3中国版",
        "adinfo": "PADM00"
    },
    {
        "packinfo": "OppoA3中国版",
        "adinfo": "PADT00"
    },
    {
        "packinfo": "OppoA5",
        "adinfo": "CPH1809"
    },
    {
        "packinfo": "OppoA5",
        "adinfo": "PBAM00"
    },
    {
        "packinfo": "OppoA5",
        "adinfo": "PBAT00"
    },
    {
        "packinfo": "OppoA5",
        "adinfo": "PBBM30"
    },
    {
        "packinfo": "OppoA5",
        "adinfo": "PBBT30"
    },
    {
        "packinfo": "OppoA5 2020",
        "adinfo": "CPH1931"
    },
    {
        "packinfo": "OppoA5 2020",
        "adinfo": "CPH1933"
    },
    {
        "packinfo": "OppoA5 2020",
        "adinfo": "CPH1943"
    },
    {
        "packinfo": "OppoA51",
        "adinfo": "A51"
    },
    {
        "packinfo": "OppoA51",
        "adinfo": "Lava A51"
    },
    {
        "packinfo": "OppoA51f",
        "adinfo": "A51f"
    },
    {
        "packinfo": "OppoA51fa",
        "adinfo": "A51f"
    },
    {
        "packinfo": "OppoA51kc",
        "adinfo": "A51kc"
    },
    {
        "packinfo": "OppoA51w",
        "adinfo": "A51w"
    },
    {
        "packinfo": "OppoA52",
        "adinfo": "CPH2061"
    },
    {
        "packinfo": "OppoA52",
        "adinfo": "CPH2069"
    },
    {
        "packinfo": "OppoA52 中国版",
        "adinfo": "PDAM10"
    },
    {
        "packinfo": "OppoA52 中国版",
        "adinfo": "PDAT10"
    },
    {
        "packinfo": "OppoA53",
        "adinfo": "OPPO A53"
    },
    {
        "packinfo": "OppoA53",
        "adinfo": "CPH2127"
    },
    {
        "packinfo": "OppoA53",
        "adinfo": "CPH2131"
    },
    {
        "packinfo": "OppoA53",
        "adinfo": "CPH2133"
    },
    {
        "packinfo": "OppoA53",
        "adinfo": "CPH2139"
    },
    {
        "packinfo": "OppoA53 5G",
        "adinfo": "PECM20"
    },
    {
        "packinfo": "OppoA53f",
        "adinfo": "A53f"
    },
    {
        "packinfo": "OppoA53fw",
        "adinfo": "A53fw"
    },
    {
        "packinfo": "OppoA53m",
        "adinfo": "OPPO A53m"
    },
    {
        "packinfo": "OppoA53s",
        "adinfo": "CPH2135"
    },
    {
        "packinfo": "OppoA53w",
        "adinfo": "A53w"
    },
    {
        "packinfo": "OppoA54 5G",
        "adinfo": "CPH2303"
    },
    {
        "packinfo": "OppoA55 5G",
        "adinfo": "PEMM00"
    },
    {
        "packinfo": "OppoA55 5G",
        "adinfo": "PEMT00"
    },
    {
        "packinfo": "OppoA55 5G",
        "adinfo": "PEMT20"
    },
    {
        "packinfo": "OppoA55s 5G",
        "adinfo": "A102OP"
    },
    {
        "packinfo": "OppoA57",
        "adinfo": "OPPO A57"
    },
    {
        "packinfo": "OppoA57",
        "adinfo": "OPPO A57t"
    },
    {
        "packinfo": "OppoA57",
        "adinfo": "CPH2387"
    },
    {
        "packinfo": "OppoA57",
        "adinfo": "CPH2407"
    },
    {
        "packinfo": "OppoA57s/A77",
        "adinfo": "CPH2385"
    },
    {
        "packinfo": "OppoA57t",
        "adinfo": "OPPO A57t"
    },
    {
        "packinfo": "OppoA58",
        "adinfo": "CPH2577"
    },
    {
        "packinfo": "OppoA59",
        "adinfo": "OPPO A59"
    },
    {
        "packinfo": "OppoA59",
        "adinfo": "OPPO A59m"
    },
    {
        "packinfo": "OppoA59",
        "adinfo": "OPPO A59s"
    },
    {
        "packinfo": "OppoA59m",
        "adinfo": "OPPO A59m"
    },
    {
        "packinfo": "OppoA59st",
        "adinfo": "OPPO A59st"
    },
    {
        "packinfo": "OppoA59t",
        "adinfo": "OPPO A59t"
    },
    {
        "packinfo": "OppoA59tm",
        "adinfo": "OPPO A59tm"
    },
    {
        "packinfo": "OppoA7",
        "adinfo": "CPH1901"
    },
    {
        "packinfo": "OppoA7",
        "adinfo": "CPH1905"
    },
    {
        "packinfo": "OppoA7",
        "adinfo": "PBFM00"
    },
    {
        "packinfo": "OppoA7",
        "adinfo": "PBFT00"
    },
    {
        "packinfo": "OppoA72",
        "adinfo": "CPH2067"
    },
    {
        "packinfo": "OppoA73",
        "adinfo": "OPPO A73"
    },
    {
        "packinfo": "OppoA73",
        "adinfo": "OPPO A73"
    },
    {
        "packinfo": "OppoA73t",
        "adinfo": "OPPO A73t"
    },
    {
        "packinfo": "OppoA73t",
        "adinfo": "OPPO A73t"
    },
    {
        "packinfo": "OppoA74",
        "adinfo": "CPH2219"
    },
    {
        "packinfo": "OppoA77",
        "adinfo": "OPPO A77"
    },
    {
        "packinfo": "OppoA77",
        "adinfo": "OPPO A77t"
    },
    {
        "packinfo": "OppoA77 5G",
        "adinfo": "CPH2339"
    },
    {
        "packinfo": "OppoA78 5G",
        "adinfo": "CPH2483"
    },
    {
        "packinfo": "OppoA78 5G",
        "adinfo": "CPH2495"
    },
    {
        "packinfo": "OppoA79",
        "adinfo": "OPPO A79"
    },
    {
        "packinfo": "OppoA79k",
        "adinfo": "OPPO A79k"
    },
    {
        "packinfo": "OppoA79kt",
        "adinfo": "OPPO A79kt"
    },
    {
        "packinfo": "OppoA79t",
        "adinfo": "OPPO A79t"
    },
    {
        "packinfo": "OppoA79t",
        "adinfo": "OPPO A79t"
    },
    {
        "packinfo": "OppoA7n",
        "adinfo": "PCDT00"
    },
    {
        "packinfo": "OppoA7x 中国版",
        "adinfo": "PBBM00"
    },
    {
        "packinfo": "OppoA7x 中国版",
        "adinfo": "PBBT00"
    },
    {
        "packinfo": "OppoA83",
        "adinfo": "OPPO A83"
    },
    {
        "packinfo": "OppoA83t",
        "adinfo": "OPPO A83t"
    },
    {
        "packinfo": "OppoA9 2020",
        "adinfo": "CPH1937"
    },
    {
        "packinfo": "OppoA9 2020",
        "adinfo": "CPH1941"
    },
    {
        "packinfo": "OppoA9 中国版",
        "adinfo": "PCAM10"
    },
    {
        "packinfo": "OppoA9 中国版",
        "adinfo": "PCAT10"
    },
    {
        "packinfo": "OppoA91",
        "adinfo": "PCPM00"
    },
    {
        "packinfo": "OppoA92",
        "adinfo": "CPH2059"
    },
    {
        "packinfo": "OppoA93",
        "adinfo": "CPH2121"
    },
    {
        "packinfo": "OppoA93",
        "adinfo": "CPH2123"
    },
    {
        "packinfo": "OppoA93 5G",
        "adinfo": "PEHM00"
    },
    {
        "packinfo": "OppoA94",
        "adinfo": "CPH2203"
    },
    {
        "packinfo": "OppoA96 5G",
        "adinfo": "PFUM10"
    },
    {
        "packinfo": "OppoA98 5G",
        "adinfo": "CPH2529"
    },
    {
        "packinfo": "OppoA9x",
        "adinfo": "PCEM00"
    },
    {
        "packinfo": "OppoA9x",
        "adinfo": "PCET00"
    },
    {
        "packinfo": "OppoAX5s",
        "adinfo": "CPH1920"
    },
    {
        "packinfo": "OppoAX7",
        "adinfo": "CPH1903"
    },
    {
        "packinfo": "XiaomiPOCO F1",
        "adinfo": "POCOPHONE F1"
    },
    {
        "packinfo": "XiaomiPOCO M5s",
        "adinfo": "2207117BPG"
    },
    {
        "packinfo": "XiaomiRedmi",
        "adinfo": "2013023"
    },
    {
        "packinfo": "XiaomiRedmi  Go",
        "adinfo": "Redmi Go"
    },
    {
        "packinfo": "XiaomiRedmi  Note  6  Pro",
        "adinfo": "Redmi Note 6 Pro"
    },
    {
        "packinfo": "XiaomiRedmi  Note  7 Pro",
        "adinfo": "Redmi Note 7 Pro"
    },
    {
        "packinfo": "XiaomiRedmi  S2",
        "adinfo": "Redmi S2"
    },
    {
        "packinfo": "XiaomiRedmi 3",
        "adinfo": "Redmi 3"
    },
    {
        "packinfo": "XiaomiRedmi 3",
        "adinfo": "ido"
    },
    {
        "packinfo": "XiaomiRedmi 3S",
        "adinfo": "Redmi 3S"
    },
    {
        "packinfo": "XiaomiRedmi 4",
        "adinfo": "Redmi 4"
    },
    {
        "packinfo": "XiaomiRedmi 4 Pro",
        "adinfo": "Redmi 4"
    },
    {
        "packinfo": "XiaomiRedmi 4A",
        "adinfo": "Redmi 4A"
    },
    {
        "packinfo": "XiaomiRedmi 4X",
        "adinfo": "Redmi 4X"
    },
    {
        "packinfo": "XiaomiRedmi 4X",
        "adinfo": "santoni"
    },
    {
        "packinfo": "XiaomiRedmi 5",
        "adinfo": "Redmi 5"
    },
    {
        "packinfo": "XiaomiRedmi 5 Plus",
        "adinfo": "Redmi 5 Plus"
    },
    {
        "packinfo": "XiaomiRedmi 5 Plus",
        "adinfo": "Redmi Note 5"
    },
    {
        "packinfo": "XiaomiRedmi 5A",
        "adinfo": "Redmi 5A"
    },
    {
        "packinfo": "XiaomiRedmi 6",
        "adinfo": "Redmi 6"
    },
    {
        "packinfo": "XiaomiRedmi 6 Pro",
        "adinfo": "Redmi 6 Pro"
    },
    {
        "packinfo": "XiaomiRedmi 6A",
        "adinfo": "Redmi 6A"
    },
    {
        "packinfo": "XiaomiRedmi 6Pro",
        "adinfo": "Redmi 6 Pro"
    },
    {
        "packinfo": "XiaomiRedmi 7",
        "adinfo": "ONC"
    },
    {
        "packinfo": "XiaomiRedmi 7",
        "adinfo": "Redmi 7"
    },
    {
        "packinfo": "XiaomiRedmi 7A",
        "adinfo": "Redmi 7A"
    },
    {
        "packinfo": "XiaomiRedmi 8",
        "adinfo": "Redmi 8"
    },
    {
        "packinfo": "XiaomiRedmi Go",
        "adinfo": "Redmi Go"
    },
    {
        "packinfo": "XiaomiRedmi K30 Pro Zoom Edition",
        "adinfo": "Redmi K30 Pro Zoom Edition"
    },
    {
        "packinfo": "XiaomiRedmi Note 3",
        "adinfo": "Redmi Note 3"
    },
    {
        "packinfo": "XiaomiRedmi Note 3",
        "adinfo": "Redmi Note 3"
    },
    {
        "packinfo": "XiaomiRedmi Note 3",
        "adinfo": "Redmi Note 3"
    },
    {
        "packinfo": "XiaomiRedmi Note 4",
        "adinfo": "Redmi Note 4"
    },
    {
        "packinfo": "XiaomiRedmi Note 4",
        "adinfo": "Redmi Note 4X"
    },
    {
        "packinfo": "XiaomiRedmi Note 4",
        "adinfo": "Redmi Note 4"
    },
    {
        "packinfo": "XiaomiRedmi Note 5",
        "adinfo": "Redmi Note 5"
    },
    {
        "packinfo": "XiaomiRedmi Note 5 Pro",
        "adinfo": "Redmi Note 5"
    },
    {
        "packinfo": "XiaomiRedmi Note 5 Pro",
        "adinfo": "Redmi Note 5 Pro"
    },
    {
        "packinfo": "XiaomiRedmi Note 5A",
        "adinfo": "Redmi Note 5A"
    },
    {
        "packinfo": "XiaomiRedmi Note 5A",
        "adinfo": "Redmi Y1"
    },
    {
        "packinfo": "XiaomiRedmi Note 5A",
        "adinfo": "Redmi Note 5A"
    },
    {
        "packinfo": "XiaomiRedmi Note 8",
        "adinfo": "Redmi Note 8"
    },
    {
        "packinfo": "XiaomiRedmi Pro",
        "adinfo": "Redmi Pro"
    },
    {
        "packinfo": "XiaomiRedmi S2",
        "adinfo": "Redmi S2"
    },
    {
        "packinfo": "XiaomiTELEBEE",
        "adinfo": "MIBOX3"
    },
    {
        "packinfo": "XiaomiXiaomi 11 Lite 5G NE",
        "adinfo": "2109119DG"
    },
    {
        "packinfo": "XiaomiXiaomi 11 Lite NE",
        "adinfo": "2109119DI"
    },
    {
        "packinfo": "XiaomiXiaomi 11T",
        "adinfo": "21081111RG"
    },
    {
        "packinfo": "XiaomiXiaomi 11T Pro",
        "adinfo": "2107113SG"
    },
    {
        "packinfo": "XiaomiXiaomi 11T Pro",
        "adinfo": "2107113SI"
    },
    {
        "packinfo": "XiaomiXiaomi 11T Pro",
        "adinfo": "2107113SR"
    },
    {
        "packinfo": "XiaomiXiaomi 11i",
        "adinfo": "21091116I"
    },
    {
        "packinfo": "XiaomiXiaomi 11i HyperCharge",
        "adinfo": "21091116UI"
    },
    {
        "packinfo": "XiaomiXiaomi 12",
        "adinfo": "2201123C"
    },
    {
        "packinfo": "XiaomiXiaomi 12",
        "adinfo": "2201123G"
    },
    {
        "packinfo": "XiaomiXiaomi 12 Lite",
        "adinfo": "2203129G"
    },
    {
        "packinfo": "XiaomiXiaomi 12 Pro",
        "adinfo": "2201122C"
    },
    {
        "packinfo": "XiaomiXiaomi 12 Pro",
        "adinfo": "2201122G"
    },
    {
        "packinfo": "XiaomiXiaomi 12 Pro Dimensity",
        "adinfo": "2207122MC"
    },
    {
        "packinfo": "XiaomiXiaomi 12S",
        "adinfo": "2206123SC"
    },
    {
        "packinfo": "XiaomiXiaomi 12S Pro",
        "adinfo": "2206122SC"
    },
    {
        "packinfo": "XiaomiXiaomi 12S Ultra",
        "adinfo": "2203121C"
    },
    {
        "packinfo": "XiaomiXiaomi 12T",
        "adinfo": "22071212AG"
    },
    {
        "packinfo": "XiaomiXiaomi 12T Pro",
        "adinfo": "22081212C"
    },
    {
        "packinfo": "XiaomiXiaomi 12T Pro",
        "adinfo": "22081212R"
    },
    {
        "packinfo": "XiaomiXiaomi 12T Pro",
        "adinfo": "22081212UG"
    },
    {
        "packinfo": "XiaomiXiaomi 12T Pro",
        "adinfo": "22200414R"
    },
    {
        "packinfo": "XiaomiXiaomi 12T Pro",
        "adinfo": "A201XM"
    },
    {
        "packinfo": "XiaomiXiaomi 12X",
        "adinfo": "2112123AC"
    },
    {
        "packinfo": "XiaomiXiaomi 13",
        "adinfo": "2211133C"
    },
    {
        "packinfo": "XiaomiXiaomi 13",
        "adinfo": "2211133G"
    },
    {
        "packinfo": "XiaomiXiaomi 13 Lite",
        "adinfo": "2210129SG"
    },
    {
        "packinfo": "XiaomiXiaomi 13 Pro",
        "adinfo": "2210132G"
    },
    {
        "packinfo": "XiaomiXiaomi 13 Ultra",
        "adinfo": "2304FPN6DC"
    },
    {
        "packinfo": "XiaomiXiaomi 13 Ultra",
        "adinfo": "2304FPN6DG"
    },
    {
        "packinfo": "XiaomiXiaomi 13 pro",
        "adinfo": "2210132C"
    },
    {
        "packinfo": "XiaomiXiaomi Civi",
        "adinfo": "2109119BC"
    },
    {
        "packinfo": "XiaomiXiaomi Civi 1S",
        "adinfo": "2109119BC"
    },
    {
        "packinfo": "XiaomiXiaomi MIX Fold",
        "adinfo": "M2011J18C"
    },
    {
        "packinfo": "XiaomiXiaomi MIX Fold 2",
        "adinfo": "22061218C"
    },
    {
        "packinfo": "XiaomiXiaomi MIX Fold 3",
        "adinfo": "2308CPXD0C"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 5",
        "adinfo": "21051182C"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 5",
        "adinfo": "21051182G"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 5 Pro",
        "adinfo": "22081281AC"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 5 Pro",
        "adinfo": "M2105K81AC"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 5 Pro 5G",
        "adinfo": "M2105K81C"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 6",
        "adinfo": "23043RP34C"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 6",
        "adinfo": "23043RP34G"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 6",
        "adinfo": "23043RP34I"
    },
    {
        "packinfo": "XiaomiXiaomi Pad 6 Max 14",
        "adinfo": "2307BRPDCC"
    },
    {
        "packinfo": "XiaomiHM 1SC",
        "adinfo": "HM 1AC"
    },
    {
        "packinfo": "XiaomiHM 1SC",
        "adinfo": "HM 1S"
    },
    {
        "packinfo": "XiaomiHM 1SC",
        "adinfo": "HM 1SC"
    },
    {
        "packinfo": "XiaomiHM 1SC",
        "adinfo": "HM 1SW"
    },
    {
        "packinfo": "XiaomiHM 1SLTETD",
        "adinfo": "2014501"
    },
    {
        "packinfo": "XiaomiHM 1STD",
        "adinfo": "2014011"
    },
    {
        "packinfo": "XiaomiHM 2A",
        "adinfo": "2014502"
    },
    {
        "packinfo": "XiaomiHM 2A",
        "adinfo": "HM 2A"
    },
    {
        "packinfo": "XiaomiHM 2LTE-BR",
        "adinfo": "2014819"
    },
    {
        "packinfo": "XiaomiHM 2LTE-CMCC",
        "adinfo": "2014813"
    },
    {
        "packinfo": "XiaomiHM 2LTE-CT",
        "adinfo": "2014812"
    },
    {
        "packinfo": "XiaomiHM 2LTE-CU",
        "adinfo": "2014811"
    },
    {
        "packinfo": "XiaomiHM 2LTE-IN",
        "adinfo": "2014818"
    },
    {
        "packinfo": "XiaomiHM 2LTE-SA",
        "adinfo": "2014817"
    },
    {
        "packinfo": "XiaomiHM NOTE 1LTETD",
        "adinfo": "HM NOTE 1LTE"
    },
    {
        "packinfo": "XiaomiHM NOTE 1LTETD",
        "adinfo": "HM NOTE 1LTETD"
    },
    {
        "packinfo": "XiaomiHM NOTE 1LTETD",
        "adinfo": "HM NOTE 1LTEW"
    },
    {
        "packinfo": "XiaomiHM NOTE 1S CT",
        "adinfo": "HM NOTE 1S"
    },
    {
        "packinfo": "XiaomiHM NOTE 1S CT",
        "adinfo": "gucci"
    },
    {
        "packinfo": "XiaomiHM NOTE 1TD",
        "adinfo": "HM NOTE 1TD"
    },
    {
        "packinfo": "XiaomiHM NOTE 1W",
        "adinfo": "HM NOTE 1W"
    },
    {
        "packinfo": "XiaomiHM Note 2",
        "adinfo": "Redmi Note 2"
    },
    {
        "packinfo": "XiaomiHong Mi",
        "adinfo": "2013022"
    },
    {
        "packinfo": "XiaomiK30 PRO",
        "adinfo": "Redmi K30 Pro 5G Zoom Edition"
    },
    {
        "packinfo": "XiaomiK30 pro",
        "adinfo": "Redmi K30 Pro 5G"
    },
    {
        "packinfo": "XiaomiMI  8  Explorer  Edition",
        "adinfo": "MI 8 Explorer Edition"
    },
    {
        "packinfo": "XiaomiMI  8  Pro",
        "adinfo": "MI 8 Pro"
    },
    {
        "packinfo": "XiaomiMI  8  Pro",
        "adinfo": "MI 8 UD"
    },
    {
        "packinfo": "XiaomiMI  MAX  3",
        "adinfo": "MI MAX 3"
    },
    {
        "packinfo": "XiaomiMI  PLAY",
        "adinfo": "MI PLAY"
    },
    {
        "packinfo": "XiaomiMI  PLAY",
        "adinfo": "lotus"
    },
    {
        "packinfo": "XiaomiMI 10",
        "adinfo": "Mi 10"
    },
    {
        "packinfo": "XiaomiMI 2",
        "adinfo": "MI 2"
    },
    {
        "packinfo": "XiaomiMI 2",
        "adinfo": "MI 2S"
    },
    {
        "packinfo": "XiaomiMI 2A",
        "adinfo": "MI 2A"
    },
    {
        "packinfo": "XiaomiMI 3W",
        "adinfo": "MI 3W"
    },
    {
        "packinfo": "XiaomiMI 4LTE",
        "adinfo": "MI 4C"
    },
    {
        "packinfo": "XiaomiMI 4LTE",
        "adinfo": "MI 4LTE"
    },
    {
        "packinfo": "XiaomiMI 4LTE",
        "adinfo": "MI 4W"
    },
    {
        "packinfo": "XiaomiMI 4LTE-CT",
        "adinfo": "MI 4LTE"
    },
    {
        "packinfo": "XiaomiMI 4s",
        "adinfo": "MI 4S"
    },
    {
        "packinfo": "XiaomiMI 5C",
        "adinfo": "MI 5C"
    },
    {
        "packinfo": "XiaomiMI 5C",
        "adinfo": "Meri"
    },
    {
        "packinfo": "XiaomiMI 5X",
        "adinfo": "MI 5X"
    },
    {
        "packinfo": "XiaomiMI 5s Plus",
        "adinfo": "MI 5s Plus"
    },
    {
        "packinfo": "XiaomiMI 6X",
        "adinfo": "MI 6X"
    },
    {
        "packinfo": "XiaomiMI 8",
        "adinfo": "MI 8"
    },
    {
        "packinfo": "XiaomiMI 8 Lite",
        "adinfo": "MI 8 Lite"
    },
    {
        "packinfo": "XiaomiMI 8 Lite",
        "adinfo": "Platina"
    },
    {
        "packinfo": "XiaomiMI 8 SE",
        "adinfo": "MI 8 SE"
    },
    {
        "packinfo": "XiaomiMI 8 SE",
        "adinfo": "sirius"
    },
    {
        "packinfo": "XiaomiMI 8 UD",
        "adinfo": "MI 8 Pro"
    },
    {
        "packinfo": "XiaomiMI 8 UD",
        "adinfo": "MI 8 UD"
    },
    {
        "packinfo": "XiaomiMI 8 UD",
        "adinfo": "equuleus"
    },
    {
        "packinfo": "XiaomiMI 9",
        "adinfo": "MI 9"
    },
    {
        "packinfo": "XiaomiMI 9 SE",
        "adinfo": "MI 9 SE"
    },
    {
        "packinfo": "XiaomiMI 9 SE",
        "adinfo": "Mi 9 SE"
    },
    {
        "packinfo": "XiaomiMI CC 9",
        "adinfo": "MI CC 9"
    },
    {
        "packinfo": "XiaomiMI CC 9",
        "adinfo": "Mi 9 Lite"
    },
    {
        "packinfo": "XiaomiMI CC 9",
        "adinfo": "Pyxis"
    },
    {
        "packinfo": "XiaomiMI CC 9e",
        "adinfo": "MI CC 9e"
    },
    {
        "packinfo": "XiaomiMI CC 9e",
        "adinfo": "laurus"
    },
    {
        "packinfo": "XiaomiMI CC9 Pro",
        "adinfo": "MI CC9 Pro"
    },
    {
        "packinfo": "XiaomiMI CC9 Pro",
        "adinfo": "Mi Note 10"
    },
    {
        "packinfo": "XiaomiMI MAX",
        "adinfo": "MI MAX"
    },
    {
        "packinfo": "XiaomiMI MAX",
        "adinfo": "MI MAX"
    },
    {
        "packinfo": "XiaomiMI MAX 2",
        "adinfo": "MI MAX 2"
    },
    {
        "packinfo": "XiaomiMI MAX 3",
        "adinfo": "MI MAX 3"
    },
    {
        "packinfo": "XiaomiMI MIX 2S",
        "adinfo": "Mi MIX 2S"
    },
    {
        "packinfo": "XiaomiMI NOTE LTE",
        "adinfo": "MI NOTE LTE"
    },
    {
        "packinfo": "XiaomiMI NOTE Pro",
        "adinfo": "MI NOTE Pro"
    },
    {
        "packinfo": "XiaomiMI Note 3",
        "adinfo": "Mi Note 3"
    },
    {
        "packinfo": "XiaomiMI PAD",
        "adinfo": "MI PAD"
    },
    {
        "packinfo": "XiaomiMI PAD 3",
        "adinfo": "MI PAD 3"
    },
    {
        "packinfo": "XiaomiMI PAD 4",
        "adinfo": "MI PAD 4"
    },
    {
        "packinfo": "XiaomiMI PLAY",
        "adinfo": "MI PLAY"
    },
    {
        "packinfo": "XiaomiMI6",
        "adinfo": "MI 6"
    },
    {
        "packinfo": "XiaomiMIBOXPRO",
        "adinfo": "MiBOX_PRO"
    },
    {
        "packinfo": "XiaomiMIPAD2",
        "adinfo": "MI PAD 2"
    },
    {
        "packinfo": "XiaomiMITV3S",
        "adinfo": "MiTV3S"
    },
    {
        "packinfo": "XiaomiMITV3S-55/60",
        "adinfo": "MiTV3S"
    },
    {
        "packinfo": "XiaomiMITV3S-55/60",
        "adinfo": "MiTV4"
    },
    {
        "packinfo": "XiaomiMIX",
        "adinfo": "MIX"
    },
    {
        "packinfo": "XiaomiMIX",
        "adinfo": "lithium"
    },
    {
        "packinfo": "XiaomiMIX 2",
        "adinfo": "MIX 2"
    },
    {
        "packinfo": "XiaomiMIX 2",
        "adinfo": "Mi MIX 2"
    },
    {
        "packinfo": "XiaomiMIX 2S",
        "adinfo": "MIX 2S"
    },
    {
        "packinfo": "XiaomiMIX 2S",
        "adinfo": "Mi MIX 2S"
    },
    {
        "packinfo": "XiaomiMIX 3",
        "adinfo": "MIX 3"
    },
    {
        "packinfo": "XiaomiMIX 3",
        "adinfo": "Mi MIX 3"
    },
    {
        "packinfo": "XiaomiMIX 4",
        "adinfo": "2106118C"
    },
    {
        "packinfo": "XiaomiMi 10",
        "adinfo": "Mi 10"
    },
    {
        "packinfo": "XiaomiMi 10",
        "adinfo": "Umi"
    },
    {
        "packinfo": "XiaomiMi 10 Lite 5G",
        "adinfo": "XIG01"
    },
    {
        "packinfo": "XiaomiMi 10 Lite zoom",
        "adinfo": "M2002J9E"
    },
    {
        "packinfo": "XiaomiMi 10 Pro",
        "adinfo": "Cmi"
    },
    {
        "packinfo": "XiaomiMi 10 Pro",
        "adinfo": "Mi 10 Pro"
    },
    {
        "packinfo": "XiaomiMi 10 Ultra",
        "adinfo": "M2007J1SC"
    },
    {
        "packinfo": "XiaomiMi 10 lite 5G",
        "adinfo": "M2002J9G"
    },
    {
        "packinfo": "XiaomiMi 10 lite 5G",
        "adinfo": "M2002J9S"
    },
    {
        "packinfo": "XiaomiMi 10S",
        "adinfo": "M2102J2SC"
    },
    {
        "packinfo": "XiaomiMi 10S",
        "adinfo": "Thyme"
    },
    {
        "packinfo": "XiaomiMi 10T",
        "adinfo": "M2007J3SP"
    },
    {
        "packinfo": "XiaomiMi 10T",
        "adinfo": "M2007J3SY"
    },
    {
        "packinfo": "XiaomiMi 10T Lite",
        "adinfo": "M2007J17G"
    },
    {
        "packinfo": "XiaomiMi 10T Pro",
        "adinfo": "M2007J3SG"
    },
    {
        "packinfo": "XiaomiMi 10T pro",
        "adinfo": "M2007J3SI"
    },
    {
        "packinfo": "XiaomiMi 10i",
        "adinfo": "M2007J17I"
    },
    {
        "packinfo": "XiaomiMi 11",
        "adinfo": "M2011K2C"
    },
    {
        "packinfo": "XiaomiMi 11",
        "adinfo": "M2011K2G"
    },
    {
        "packinfo": "XiaomiMi 11 LE",
        "adinfo": "2107119DC"
    },
    {
        "packinfo": "XiaomiMi 11 Lite",
        "adinfo": "M2101K9AG"
    },
    {
        "packinfo": "XiaomiMi 11 Lite",
        "adinfo": "M2101K9AI"
    },
    {
        "packinfo": "XiaomiMi 11 Lite 5G",
        "adinfo": "M2101K9C"
    },
    {
        "packinfo": "XiaomiMi 11 Lite 5G",
        "adinfo": "M2101K9G"
    },
    {
        "packinfo": "XiaomiMi 11 Pro",
        "adinfo": "M2102K1AC"
    },
    {
        "packinfo": "XiaomiMi 11 Ultra",
        "adinfo": "M2102K1C"
    },
    {
        "packinfo": "XiaomiMi 11 Ultra",
        "adinfo": "M2102K1G"
    },
    {
        "packinfo": "XiaomiMi 11X Pro",
        "adinfo": "M2012K11I"
    },
    {
        "packinfo": "XiaomiMi 11i",
        "adinfo": "M2012K11G"
    },
    {
        "packinfo": "XiaomiMi 3",
        "adinfo": "MI 3"
    },
    {
        "packinfo": "XiaomiMi 4c",
        "adinfo": "Mi-4c"
    },
    {
        "packinfo": "XiaomiMi 4i",
        "adinfo": "Mi 4i"
    },
    {
        "packinfo": "XiaomiMi 5",
        "adinfo": "MI 5"
    },
    {
        "packinfo": "XiaomiMi 5s",
        "adinfo": "MI 5s"
    },
    {
        "packinfo": "XiaomiMi 9 Lite",
        "adinfo": "Mi 9 Lite"
    },
    {
        "packinfo": "XiaomiMi 9 SE",
        "adinfo": "MI 9 SE"
    },
    {
        "packinfo": "XiaomiMi 9 SE",
        "adinfo": "Mi 9 SE"
    },
    {
        "packinfo": "XiaomiMi 9T",
        "adinfo": "Mi 9T"
    },
    {
        "packinfo": "XiaomiMi 9T Pro",
        "adinfo": "Mi 9T Pro"
    },
    {
        "packinfo": "XiaomiMi A1",
        "adinfo": "MI A1"
    },
    {
        "packinfo": "XiaomiMi A1",
        "adinfo": "Mi A1"
    },
    {
        "packinfo": "XiaomiMi A2",
        "adinfo": "Mi A2"
    },
    {
        "packinfo": "XiaomiMi A2 Lite",
        "adinfo": "Mi A2 Lite"
    },
    {
        "packinfo": "XiaomiMi A3",
        "adinfo": "Mi A3"
    },
    {
        "packinfo": "XiaomiMi Box",
        "adinfo": "MIBOX3"
    },
    {
        "packinfo": "Xiaomi\"Mi Laser Projector 150\"\"\"",
        "adinfo": "MiProjA1"
    },
    {
        "packinfo": "XiaomiMi Laser Projector 4K",
        "adinfo": "MiProjL1"
    },
    {
        "packinfo": "XiaomiMi MIX 3 5G",
        "adinfo": "Mi MIX 3 5G"
    },
    {
        "packinfo": "XiaomiMi Note",
        "adinfo": "MI NOTE LTE"
    },
    {
        "packinfo": "XiaomiMi Note 10",
        "adinfo": "Mi Note 10"
    },
    {
        "packinfo": "XiaomiMi Note 10 Lite",
        "adinfo": "Mi Note 10 Lite"
    },
    {
        "packinfo": "XiaomiMi Note 10 Lite",
        "adinfo": "toco"
    },
    {
        "packinfo": "XiaomiMi Note2",
        "adinfo": "Mi Note 2"
    },
    {
        "packinfo": "XiaomiMi TV Stick",
        "adinfo": "MiTV-AESP0"
    },
    {
        "packinfo": "XiaomiMi smart projector",
        "adinfo": "MiProjM05"
    },
    {
        "packinfo": "XiaomiMi9 Pro 5G",
        "adinfo": "Mi9 Pro 5G"
    },
    {
        "packinfo": "XiaomiMiBOX1S",
        "adinfo": "MiBOX1S"
    },
    {
        "packinfo": "XiaomiMiBOX2",
        "adinfo": "MiBOX2"
    },
    {
        "packinfo": "XiaomiMiBOX3S",
        "adinfo": "MiBOX3S"
    },
    {
        "packinfo": "XiaomiMiBOX_mini",
        "adinfo": "MiBOX_mini"
    },
    {
        "packinfo": "XiaomiMiBox S",
        "adinfo": "MIBOX4"
    }
]

wb = Workbook()
ws = wb.active

header = ["qymc", "tym"]
ws.append(header)

for row in data:
    qymc = row['adinfo']
    tym = row['packinfo']


    ws.append([qymc, tym])

wb.save(r'C:\Users\Administrator\Desktop\工作簿2.xlsx')
