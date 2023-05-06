import os
import subprocess

apk_path = r"D:\laying-file\39383008_com.android.ypctszik.tectsguava_1.0.0_hwyy_20230416.apk"

cmd = 'aapt dump badging ' + apk_path
output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
package_name = output.split("'")[1]
activity_name = output.split("'")
print(package_name)
print(activity_name)