from urllib.request import urlopen

resp=urlopen("http://www.baidu.com")

with open("baidu.html",mode="w",encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))