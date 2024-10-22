import requests

# 原始页面 URL
url = "https://www.pearvideo.com/video_1693468"
contId = url.split("_")[1]  # 从 URL 中提取 contId

# 视频状态请求 URL
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8621858520649812"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "Referer": url  # 防盗链，设置为原始页面 URL
}

# 发起请求
resp = requests.get(videoStatusUrl, headers=headers)

# 解析响应为 JSON
data = resp.json()

# 从 JSON 中提取视频 URL 和系统时间
srcUrl = data['videoInfo']['videos']['srcUrl']
systemTime = data['systemTime']

# 替换系统时间为 contId
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# 输出最终的 srcUrl
print(srcUrl)

#下载视频
with open("a.mp4",mode="wb") as f :
    f.write(requests.get(srcUrl).content)



