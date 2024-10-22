import requests
from bs4 import BeautifulSoup
import time

url = "https://www.4kdesk.com/"
resp = requests.get(url)
resp.encoding ="utf-8"

main_page = BeautifulSoup(resp.text,"html.parser")
alist=main_page.find("div",class_="clearfix pic-auto pic-list").find_all("a")
# print(alist)
for a in alist:
    href=a.get('href')
    #拿到子页面源代码
    child_page_resp=requests.get(href)#直接通过get就可以拿到属性的值
    child_page_resp.encoding = "utf-8"
    child_page_text=child_page_resp.text

    #从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text,"html.parser")
    p = child_page.find("div",class_="layout pic-con")
    # print(p)
    img = p.find("img")
    src = (img.get("src"))

    #下载图片
    img_resp = requests.get(src)
    img_resp.content #这里拿到的是字节
    img_name = src.split("/")[-1] #拿到url中最后一个/以后的内容
    with open("img/"+img_name, mode="wb") as f:
        f.write(img_resp.content)#图片内容写入文件

    print("over!!", img_name)
    time.sleep(1)

print("all over!!!")



#chatgpt改进代码


