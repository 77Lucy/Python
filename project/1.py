#coding:utf-8
# a="please print a number1"
# b="please print a number2"
# print(a+b);
#
# what_he_does = ' plays '
# his_instrument = 'guitar'
# his_name = 'Robert Johnson'
# artist_intro = his_name + what_he_does + his_instrument
# print(artist_intro)
#
# print(type(a))
from importlib import import_module

#转换字符串
# num = 1
# string = '1'
# num2 = int(string)
# print(num + num2)

#字符串相乘
# words = "words" * 3
# print(words)
#
# word = 'a loooooong word'#空格也算
# num = 12
# string = 'bang!'
# total = string * (len(word) - num)
# print(total)

# name = 'My name is Mike'
# print(name[0])
# 'M'
# print(name[-4])
# 'M'
# print(name[11:14]) # from 11th to 14th, 14th one is excluded
# 'Mik'
# print(name[11:15]) # from 11th to 15th, 15th one is excluded
# 'Mike'
# print(name[5:])
# 'me is Mike'
# print(name[:5])
# 'My na'
#
# word = 'friends'
# find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
# print(find_the_evil_in_your_friends)

#号码遮挡
# phone_number = '1386-666-0006'
# hiding_number = phone_number.replace(phone_number[:9],'*')
# hiding_number2 = phone_number.replace(phone_number[:9],'*'*9)
# print(hiding_number)
# print(hiding_number2)

#模拟手机号码联想功能
# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
# print(search + ' is at ' + str(num_a.find(search)) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
# print(search + ' is at ' + str(num_b.find(search)) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')

#e2.1DrawPython.Pyimport
# import turtle
# turtle.setup(650,350,200,200)
# turtle.penup()
# turtle.fd(-250)
# turtle .pendown()
# turtle.pensize(25)
# turtle.pencolor("green" )
# turtle.seth(-40)
# for i in range(4):
#   turtle.circle(40,80)
#   turtle.circle(-40,80)
# turtle.circle(40,80/2)
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40*2/3)


# import asyncio
#
# # 定义一个协程函数
# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(10)  # 模拟 I/O 操作
#     print("World")
#
# # 创建事件循环并运行协程
# async def main():
#     await asyncio.gather(say_hello(), say_hello())  # 并发运行多个协程
#
# # 运行协程
# asyncio.run(main())


# name = input("")
# age = input("")
# s=f"我叫{name},我今年{age}"
# print(s)

# s="i am happy"
# print(s[1])
# print(s[-2])

# s = "我爱你"
# print(s[::-1])

# s2 = "abcdefghijklmn"
# print(s2[3:9:2])
# print(s2[-3:-9:-2])

# s = "I have a dream"
# s2 = s.title()
# s3 = s.upper() #变成大写字母
# s4 = s3.lower() #变成小写字母
# print(s3)
# print(s4)

#replace
# a = "hello world!"
# a1 = a.replace(" ","")
# a2 = a.replace("h","H")
# print(a1)
# print(a2)

#split
# a = "python_java_c"
# lst = a.split("_")
# print(lst)

#列表
# s = ["baby","you","are","so"]

# print(s[:2])
#
# for item in s:
#     print(item)

# s.append("pretty")
# s.extend(["good","or","bad"])
# s.insert(0,"hi")
# s.pop(3)
# s.remove("you")
# s[1] = "dudu"
# print(s)

#字典的循环
# dic={
#     "taylor":"she's a superstar!",
#     "justin":"he is so handsome!"
# }
#
# for key, value in dic.items():
#     print(key,value)

#字典的嵌套
# wangfeng = {
#     "name": "汪峰",
#     "age": "18",
#     "wife": {
#         "name": "章子怡",
#         "age": "18"
#     },
#     "kids": [
#         {"name": "kk", "age": "6"},
#         {"name": "kk", "age": "5"},
#     ]
# }
#
# # 获取汪峰妻子的名字
# name = wangfeng['wife']['name']
# print(name)
#
# # 汪峰第二个孩子年龄加1（先将字符串转换为整数，再加1）
# age = str(int(wangfeng["kids"][1]["age"]) + 1)
# print(age)
# print(wangfeng)


#字典的循环删除
# dic={
#     "taylor":"she's a superstar!",
#     "justin":"he is so handsome!"
# }
#
# # 存储要删除的键
# temp = []
# for key in dic:
#     if key.startswith("t"):
#         temp.append(key)
#
# # 逐个删除这些键
# for t in temp:
#     dic.pop(t)
#
# print(dic)

# s = slice(1,4,2)
# print("01234567"[s])

# a = 14
# print(format(a,"08b"))

# def guanjia(game):
#     def inner():
#         print("打开")
#         game()
#         print("关闭")
#     return inner
#
# @guanjia   #相当于 play_dnf = guanjia(play_dnf)
# def play_dnf():
#     print("你好")
#
# play_dnf()


# def order():
#     lst = []
#     for i in range(10000):
#         lst.append(f"衣服{i}")
#         if len(lst) == 50:
#             yield lst
#             #下一次拿数据
#             lst = []
#
# gen = order()
# print(gen.__next__())
# print(gen.__next__())

#推导式
# lst = [i for i in range(10)]
# print(lst)

# lst1 = ["杨佳宁","琳琳"]
# lst2 = ["80","18"]
# result = zip(lst1,lst2)
# lst = list(result)
# print(lst)

# lst = ["秋","大狗蛋","帅哥","超级无敌掌门狗月球野餐记"]
# #函数不能加括号
# #不复杂且别的地方用不着的函数，可以直接用lambda写入关键字
# s = sorted(lst,key=lambda x:len(x))
# print(s)









