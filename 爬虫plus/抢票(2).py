"""
[课程内容]: Python实现12306查票以及自动购票

[授课老师]: 青灯教育-自游  [上课时间]: 20:05  可以点歌, 可以问问题

[环境使用]:
    Python 3.8 比较稳定的版本
    Pycharm

    谷歌浏览器
    谷歌驱动

[模块使用]:
    requests   ---> pip install requests  数据请求模块
    prettytable ---> pip install prettytable 打印好看一些
    selenium  ---> pip install selenium==3.141.0  模拟人的行为去操作浏览器
    json ---> 内置模块 不需要安装
    time ---> 内置模块 不需要安装

课前素材: 可以去找木子老师微信领取
    city.json文件
    谷歌驱动安装教程

---------------------------------------------------------------------------------------------------
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找木子老师领取录播, 然后再写代码
    3. 不要早退, 课后签到领取福利代码以及课程录播
---------------------------------------------------------------------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：https://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：https://pypi.hustunique.com/
                山东理工大学：https://pypi.sdutlinux.org/
                豆瓣：https://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名

        - 失败三: cmd里面显示已经安装过了, 或者安装成功了, 但是在pycharm里面还是无法导入
            解决方法: 可能安装了多个python版本 (anaconda 或者 python 安装一个即可) 卸载一个就好
                    或者你pycharm里面python解释器没有设置好
---------------------------------------------------------------------------------------------------
如何配置pycharm里面的python解释器?
    1. 选择file(文件) >>> setting(设置) >>> Project(项目) >>> python interpreter(python解释器)
    2. 点击齿轮, 选择add
    3. 添加python安装路径
---------------------------------------------------------------------------------------------------
pycharm如何安装插件?
    1. 选择file(文件) >>> setting(设置) >>> Plugins(插件)
    2. 点击 Marketplace  输入想要安装的插件名字 比如:翻译插件 输入 translation / 汉化插件 输入 Chinese
    3. 选择相应的插件点击 install(安装) 即可
    4. 安装成功之后 是会弹出 重启pycharm的选项 点击确定, 重启即可生效
---------------------------------------------------------------------------------------------------

本节课案例分为: <爬虫相关知识点>
    1. 查票
    2. 自动下单购票

查票: 获取车次信息
    比如: 长沙到上海 12月14 这天相关车次信息 获取下来

- 分析 车次信息 是可以请求那个链接, 能够得到数据
    通过开发者工具, 进行抓包分析 ---> 开发者工具 会 1  不会 2
    1. 打开开发者工具
    2. 点击查询按钮
    https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-12-14&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=SHH&purpose_codes=ADULT

1. 发送请求
2. 获取返回数据内容
3. 解析数据, 提取数据里面车次信息
4. 输出打印车次信息

爬虫的代码 并不是统一使用, 每个网站数据结构都不一样, 处理方法就不一样

公开课主要讲解案例, 演示效果为主, 就告诉你能做什么

系统课程, 就是从零基础入门开始授课 一直教授到项目案例 --> 爬虫 数据分析 全栈开发

就业, 兼职 ---> 一定要系统学习

加清风老师微信: pythonmiss
    了解系统课程 服务 教学 活动优惠

12月12号, 双12

加清风老师微信: 预定 300 学费 <前5位>
    1. 300 可以直接减免 1212 学费

    2. 提供就业指导
        - 面试简历修改
        - 面试试题
        - 面试技巧
        - 工作之后遇到问题一样可以辅导
        - HR就业推荐

    3. 提供外包指导
        - 提供外包接单平台
        - 提供外包接单渠道
        - 提供外包问题解答
    你学了课程之后, 可以直接找我, 我直接提供外包,
        每个人两个外包


    4. 两个精品课程
        - 价值 1680元 自动化办公课程
        - 价值 2680元 人工智能算法课程


今天报名, 明天就直接上课程学习,  明天13号新班开班

下个月1月13 --> 2月13号, 过年之后, 你就可以开始接外包赚钱了 ---> 月收1-3K左右


跟着老师系统学习, 想要学习之后, 就业工作 薪资都可以达到 8000- 15000 左右

那你可以赶紧找清风老师预定 优惠名额 ---> 300 学费预定优惠.....

没学会? 不可能
只要跟着老师学习, 按时听课, 按时完成作业, 认真学习态度, 保证各位能够掌握学会

1. 课程是全部学完 7个月 从零基础安装软件开始教学
2. 全程直播授课 专业老师带你学习
    一周三节课 周135或者246 晚上8点-10点

3. 每节课后都有录播回放 ---> 课件源码笔记文档软件工具
    有资料, 你想要资料, 你都有...
    课程资料实时更新
    <公开课讲解selenium 3.0 VIP系统课程讲解的 4.0>

4. 多位专业老师, 对你进行辅导解答
    专门授课, 有专门解答辅导
    你跟着老师学习, 青灯教育所有老师, 都会对你进行服务

    你在前面学习, 你的背后整个青灯教育教学团队

5. 监督学习, 电话通知听课

6. 免费重修 --> 青灯教育教学目的就为了让你能够学会掌握, 之后可以实现技术变现
    标准: 1. 考核没通过, 强制重修免费
            2. 你想要学, 你觉得先要再学一遍, 完全OK
7. 提供培训合同
8. 提供发票

先预定 300 学费, 保留优惠名额 ---> 之后和父母好好商量

如果真的不学了, 父母不支持, 那这个300学费可以给你退的


"""
# 导入数据请求模块
import requests
# 导入格式化打印
import prettytable as pt
# 导入json
import json
# 导入自动化测试模块
from selenium import webdriver
# 导入账号密码
from password import account, Password
# 导入时间模块
import time
# 导入键盘控制
from selenium.webdriver.common.keys import Keys

# 实例化对象 1. 打开浏览器
driver = webdriver.Chrome()

# 绕过检测机制
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                       {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})
# 2. 输入网址
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
"""
3. 输入账号密码
    先找到账号密码输入框, 再进行输入操作
"""
try:
    # 输入账号
    driver.find_element_by_css_selector('#J-userName').send_keys(account)
    # 输入密码
    driver.find_element_by_css_selector('#J-password').send_keys(Password)
    # 点击登陆
    driver.find_element_by_css_selector('#J-login').click()
    # 延时
    driver.implicitly_wait(10)
    time.sleep(1)
    # 点击弹窗
    driver.find_element_by_css_selector('.btn').click()
    # 点击车票预定
    driver.find_element_by_css_selector('#link_for_ticket').click()
    # 延时
    driver.implicitly_wait(10)
    time.sleep(1)
    # 输入出发城市
    driver.find_element_by_css_selector('#fromStationText').click() # 点击输入框
    driver.find_element_by_css_selector('#fromStationText').clear() # 清空输入框
    driver.find_element_by_css_selector('#fromStationText').send_keys('长沙') # 输入内容
    driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.ENTER) # 模拟按键操作 回车
    # 输入到达城市
    driver.find_element_by_css_selector('#toStationText').click() # 点击输入框
    driver.find_element_by_css_selector('#toStationText').clear() # 清空输入框
    driver.find_element_by_css_selector('#toStationText').send_keys('上海') # 输入内容
    driver.find_element_by_css_selector('#toStationText').send_keys(Keys.ENTER) # 模拟按键操作 回车
    # 输入时间
    driver.find_element_by_css_selector('#train_date').click() # 点击输入框
    driver.find_element_by_css_selector('#train_date').clear() # 清空输入框
    driver.find_element_by_css_selector('#train_date').send_keys('2022-12-14')
    # 点击查询
    driver.find_element_by_css_selector('#query_ticket').click()
    # 点击预定
    driver.find_element_by_css_selector('#queryLeftTable tr:nth-child(1) .btn72').click()
    # 延时
    driver.implicitly_wait(10)
    time.sleep(1)
    # 选择坐车人
    driver.find_element_by_css_selector('#normalPassenger_1').click()
    # 提交订单
    driver.find_element_by_css_selector('#submitOrder_id').click()
    # 选择座位
    driver.find_element_by_css_selector('#erdeng1 > ul:nth-child(4) > li:nth-child(2)').click()
    # 点击提交订单
    time.sleep(3)
    driver.find_element_by_css_selector('#qr_submit_id').click()
    driver.find_element_by_css_selector('#qr_submit_id').click()

except:
    pass







# # 输入地名
# from_city = input('输入你要出发城市: ')
# to_city = input('输入你要到达城市: ')
# # date = input('输入你要出发时间: ')
# date = '2022-12-14'
#
# # 读取文件
# f = open('city.json', encoding='utf-8')
# # f.read() 字符串 转成字典
# json_data = json.loads(f.read())
# # json_data[from_city] --> json_data['长沙']  json_data['上海']
# """
# 1. 发送请求, 模拟浏览器对于url地址发送请求
# """
# # 确定请求链接
# url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[from_city]}&leftTicketDTO.to_station={json_data[to_city]}&purpose_codes=ADULT'
# # 模拟浏览器 headers 请求头 字典数据类型 构建完整键值对
# headers = {
#     # User-Agent 用户代理 表示浏览器基本身份信息
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
# }
# # 发送请求
# response = requests.get(url=url, headers=headers)
# # <Response [200]> 响应对象, 表示请求成功
# print(response)
# """
# 2. 获取返回数据内容
#     response.json() 获取响应字典数据
# 3. 解析数据, 提取数据里面车次信息
#     键值对 --> 冒号左边的内容[键], 提取冒号右边的内容[值]
#
# dict = {
#     '键1': '值1',
#     '键2': '值2'
# }
#
# 批量替换：
#     1. 选中替换内容， ctrl + R
#     2. 勾选 .* 输入正则命令 匹配替换
#         :.*
#         ,
# 长沙到上海 12月14号
# """
# # 实例化对象
# tb = pt.PrettyTable()
# # 添加表头
# tb.field_names = [
#     '序号',
#     '车次',
#     '出发时间',
#     '到达时间',
#     '耗时',
#     '特等座',
#     '一等',
#     '二等',
#     '软卧',
#     '硬卧',
#     '硬座',
#     '无座',
# ]
# page = 0
# # 添加空列表里面
# lis = []
# # for循环遍历, 一个一个提取我们列表里面元素
# for i in response.json()['data']['result']:
#     # split 字符串的方法, 分割 --> 列表 根据列表索引位置取值
#     index = i.split('|')
#     num = index[3]  # 车次
#     start_time = index[8]  # 出发时间
#     end_time = index[9]  # 到达时间
#     use_time = index[10]  # 耗时
#     topGrade = index[32]  # 特等座
#     first_class = index[31]  # 一等
#     second_class = index[30]  # 二等
#     hard_sleeper = index[28]  # 硬卧
#     hard_seat = index[29]  # 硬座
#     no_seat = index[26]  # 无座
#     soft_sleeper = index[23]  # 软卧
#     # 自己创建字典
#     dit = {
#         '车次': num,
#         '出发时间': start_time,
#         '到达时间': end_time,
#         '耗时': use_time,
#         '特等座': topGrade,
#         '一等': first_class,
#         '二等': second_class,
#         '软卧': soft_sleeper,
#         '硬卧': hard_sleeper,
#         '硬座': hard_seat,
#         '无座': no_seat,
#     }
#     lis.append(dit)
#     tb.add_row([page, num, start_time, end_time, use_time, topGrade, first_class,
#                 second_class,
#                 soft_sleeper,
#                 hard_sleeper,
#                 hard_seat,
#                 no_seat, ])
#     # print(dit)
#     page += 1
#
# print(tb)
# # 输入内容, 返回字符串
# a = input('请输入你想要购买车票序号: ')
# # int() 把a转成整型  lis列表, 列表索引位置取值, 要是整型
# print(lis[int(a)]['车次'])
