import asyncio
import aiohttp
import aiofiles

urls = [
    "http://img.netbian.com/file/2020/0712/ccd6fce7874f4f9351ddf67c71ed4536.jpg",
    "http://img.netbian.com/file/2022/1222/155429YwtLg.jpg",
    "http://img.netbian.com/file/2023/0322/232520QuDUY.jpg"
]

async def aiodownload(url, session):
    # 发送请求，获取图片内容
    name = url.rsplit("/", 1)[1]  # 从右边切，获取文件名
    async with session.get(url) as resp:  # 使用同一会话获取内容
        if resp.status == 200:
            async with aiofiles.open(name, mode="wb") as f:  # 异步文件写入
                await f.write(await resp.read())  # 写入文件内容
    print(f"{name} 下载完成")

async def main():
    async with aiohttp.ClientSession() as session:  # 创建一个会话用于所有下载
        tasks = [aiodownload(url, session) for url in urls]
        await asyncio.gather(*tasks)  # 并行下载

# 运行主程序
asyncio.run(main())
