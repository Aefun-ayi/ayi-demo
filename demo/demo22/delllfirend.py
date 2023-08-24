import time
import uiautomator2 as u2

d = u2.connect()

for i in range(740):
    d.xpath(
        '//*[@resource-id="com.ss.android.ugc.aweme:id/recycler_view"]/android.widget.Button[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
    d(resourceId="com.ss.android.ugc.aweme:id/k52", text="移除朋友").click()
    time.sleep(1)
    # print(f'已删除{i+1}个')


