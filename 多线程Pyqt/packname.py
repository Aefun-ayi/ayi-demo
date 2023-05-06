import os
import re

path = input('路径：')
f = os.popen(fr'aapt dump badging {path}').read()
p1 = "package: name='(.+?)'"
p2 = "launchable-activity: name='(.+?)'"
results1 = re.findall(p1, f)
results2 = re.findall(p2, f)
print(f)
print(results2[0])
print(results1)
