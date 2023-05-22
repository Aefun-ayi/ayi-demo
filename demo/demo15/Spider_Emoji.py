import requests
import os
from lxml import etree

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 创建一个函数，用于爬取表情包
def spider(url):
    try:
        # 发送请求，获取响应
        response = requests.get(url, headers=headers)
        # 设置响应的编码格式
        response.encoding = response.apparent_encoding
        # 使用lxml解析页面内容
        html = etree.HTML(response.text)
        # 获取页面中所有的图片链接
        img_urls = html.xpath('//div[@class="bqppdiv"]/a/img/@data-original')
        # 遍历所有图片链接，依次下载图片
        for img_url in img_urls:
            # 发送请求，获取图片内容
            img_response = requests.get(img_url, headers=headers)
            # 获取图片的文件名
            img_name = os.path.basename(img_url)
            # 拼接完整的文件路径
            img_path = os.path.join(r'D:\ayi-demo\demo\demo15\img', img_name)
            # 保存图片文件
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
            print('{} 下载成功！'.format(img_name))
    except Exception as e:
        print('下载失败：', e)

if __name__ == '__main__':
    # 定义需要爬取的url
    url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'
    # 遍历需要爬取的页数
    for i in range(1, 3):
        # 拼接完整的url
        full_url = url.format(i)
        # 调用爬虫函数，爬取当前页的表情包
        spider(full_url)