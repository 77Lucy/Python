# import requests
#
# url = "https://fanyi.baidu.com/sug"
#
# s=input("请输入你要翻译的英文单词:")
# dat={
#     "kw":s
# }
#
# resp=requests.post(url,data=dat)
# print(resp.json())

import requests

# 百度翻译接口
url = "https://fanyi.baidu.com/sug"

# 用户输入
s = input("请输入你要翻译的英文单词: ")

# 发送请求的数据
dat = {
    "kw": s
}

try:
    # 发送POST请求
    resp = requests.post(url, data=dat)

    # 检查响应的状态码是否为200（成功）
    if resp.status_code == 200:
        # 解析JSON响应
        result = resp.json()

        # 提取翻译结果
        if "data" in result and len(result["data"]) > 0:
            print("翻译结果:")
            for item in result["data"]:
                # 每个结果单独输出在新的一行
                print(f"{item['k']} - {item['v']}\n")
        else:
            print("未找到翻译结果。")
    else:
        print(f"请求失败，状态码: {resp.status_code}")
except Exception as e:
    print(f"发生错误: {e}")
