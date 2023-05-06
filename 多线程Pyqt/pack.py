from pyaxmlparser import APK

# 使用pyaxmlparser获取apk信息
apk_file = input("输入地址：")
path = apk_file.replace('\\','/')
apk = APK(path)

# 获取包名和activity名
package_name = apk.package
main_activity = apk.get_main_activity()

print('Package name:', package_name)
print('Main activity:', main_activity)