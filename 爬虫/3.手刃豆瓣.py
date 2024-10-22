# import requests
# import re
#
# url = "https://movie.douban.com/top250"
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
# }
#
# resp = requests.get(url, headers=headers)
# # print(resp.text)
# page_content = resp.text
#
# #解析数据
# obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)
#
# result = obj.finditer(page_content)
# for it in result:
#     print(it.group("name"))



#chatgpt给的改进代码：
import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# 发送请求并获取网页内容
resp = requests.get(url, headers=headers)
page_content = resp.text

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(page_content, 'html.parser')

# 查找所有包含电影名称的 <span class="title"> 标签
movie_titles = soup.find_all('span', class_='title')

# 输出电影名称
for title in movie_titles:
    print(title.get_text())
