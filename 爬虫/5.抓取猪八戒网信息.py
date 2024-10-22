import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)

# 解析HTML
html = etree.HTML(resp.text)

# 获取每个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")
for div in divs:  # 每一个服务商信息
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[0]
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
    print(com_name)
