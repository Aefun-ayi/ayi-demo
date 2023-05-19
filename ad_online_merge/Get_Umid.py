import subprocess
import re
def UmId():
    # 执行adb命令
    process = subprocess.Popen(['adb', 'logcat'], stdout=subprocess.PIPE)
    # 循环读取输出并过滤日志信息
    while True:
        # 读取输出
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            # 将输出转换为字符串
            output_str = output.decode('utf-8').strip()
            # 过滤日志信息
            if '友盟id' in output_str:
                id = "友盟id: (.+)"
                umid = re.findall(id,output_str)
                # print(umid)
                if len(umid) > 0:
                    return umid[0]
                else:
                    continue

# a = UmId()
# print(a)
