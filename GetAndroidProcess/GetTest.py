import subprocess

apk_path = r"D:\laying-file\39748005_com.forexample.indicates_1.0.0_viyy_20231110.apk"
command = ["aapt", "dump", "badging", apk_path]
output = subprocess.check_output(command).decode("utf-8")
print(output)