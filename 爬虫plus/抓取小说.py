# import requests  # 第三方的模块
# import parsel  # 第三方的模块
# import os  # 内置模块 文件或文件夹
#
# filename = '小说\\'
# if not os.path.exists(filename):
#     os.mkdir(filename)
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
# }
#
# rid = input('输入书名ID：')
# link = f'https://www.bqg70.com/book/{rid}/'
#
# html_data = requests.get(url=link, headers=headers).text
# # print(html_data)
# selector_2 = parsel.Selector(html_data)
# divs = selector_2.css('.listmain dd')
# for div in divs:
#     title = div.css('a::text').get()
#     href = div.css('a::attr(href)').get()
#     url = 'https://www.bqg70.com' + href
#
#     try:
#         response = requests.get(url=url, headers=headers)
#         selector = parsel.Selector(response.text)
#         # getall 返回的是一个列表 []
#         book = selector.css('#chaptercontent::text').getall()
#         book = '\n'.join(book)
#         # 数据保存
#         with open(filename + title + '.txt', mode='a', encoding='utf-8') as f:
#             f.write(book)
#             print('正在下载章节:  ', title)
#     except Exception as e:
#         print(e)


#异步下载，超级无敌快，但章节顺序会乱

import aiohttp  # 用于异步 HTTP 请求
import asyncio  # 用于管理异步任务
import parsel  # 用于解析 HTML 内容
import os  # 用于文件或目录操作

# 保存小说章节的文件夹路径
filename = '小说\\'
# 如果目录不存在，则创建该目录
if not os.path.exists(filename):
    os.mkdir(filename)

# 请求头，用于模拟浏览器的请求，避免被网站屏蔽
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}


# 异步函数：下载单个章节
async def fetch_chapter(session, url, title):
    try:
        # 使用 aiohttp 的 session 发送异步 GET 请求
        async with session.get(url) as response:
            # 等待响应并获取页面内容作为文本
            response_text = await response.text()

            # 解析响应内容，提取章节的文本
            selector = parsel.Selector(response_text)
            book = selector.css('#chaptercontent::text').getall()  # 获取章节中的所有文本
            book = '\n'.join(book)  # 将文本列表合并为一个字符串

            # 将章节文本保存到 .txt 文件中，文件名为章节标题
            with open(filename + title + '.txt', mode='a', encoding='utf-8') as f:
                f.write(book)
                print('正在下载章节: ', title)  # 打印当前下载的章节
    except Exception as e:
        # 处理下载过程中出现的异常
        print(f"下载章节 {title} 时出错: {e}")


# 异步函数：获取所有章节的链接并开始下载
async def fetch_chapters():
    rid = input('输入书名ID：')  # 获取用户输入的书名 ID
    link = f'https://www.bqg70.com/book/{rid}/'  # 构建书籍主页面的链接

    # 创建一个异步会话，使用预定义的请求头
    async with aiohttp.ClientSession(headers=headers) as session:
        # 异步请求书籍的主页面
        async with session.get(link) as response:
            # 等待响应并获取 HTML 数据
            html_data = await response.text()

            # 解析 HTML 数据，提取所有章节的链接
            selector_2 = parsel.Selector(html_data)
            divs = selector_2.css('.listmain dd')  # 选择所有包含章节的 <dd> 元素

            # 创建一个列表，用于存储所有下载任务
            tasks = []

            # 遍历每个章节的 <dd> 元素
            for div in divs:
                title = div.css('a::text').get()  # 获取章节标题
                href = div.css('a::attr(href)').get()  # 获取章节链接
                url = 'https://www.bqg70.com' + href  # 构建完整的章节 URL

                # 创建一个异步任务，用于下载章节
                task = fetch_chapter(session, url, title)
                tasks.append(task)  # 将任务添加到任务列表中

            # 等待并执行所有任务，进行并发下载
            await asyncio.gather(*tasks)


# 启动事件循环，开始异步下载章节
asyncio.run(fetch_chapters())
