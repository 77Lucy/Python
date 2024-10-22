
import requests
import os
from lxml import etree

# 创建目录方法
def create_file(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

url = 'https://wenku.baidu.com/tfview/e25794269b8fcc22bcd126fff705cc1754275f10?fr=hp_sub&_wkts_=1726637150402'

# 请求网页内容
resp = requests.get(url)
text = resp.text

# 解析 HTML
html = etree.HTML(text)

# 提取所有图片
img_list = html.xpath('//img')

# 计数
cnt = 1

# 文件保存路径
file_path = './wendang/'
create_file(file_path)

# 获取图片
for i in img_list:
    try:
        img_url = i.xpath('./@src')[0]
    except IndexError:
        img_url = i.xpath('./@data-src')[0]  # 如果没有 src，尝试 data-src

    if img_url.startswith('//'):
        img_url = 'https:' + img_url  # 补全 URL

    # 文件名称
    file_name = f'{file_path}page_{cnt}.jpg'
    print(file_name, img_url)

    # 下载保存图片
    img_resp = requests.get(img_url)
    with open(file_name, 'wb') as f:
        f.write(img_resp.content)

    cnt += 1
