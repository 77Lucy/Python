import requests

proxies = {
    "https": "https://8.130.90.177"
}

resp = requests.get("https://www.baidu.com",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)


