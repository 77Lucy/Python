#斐波那契数列
# a,b=0,1
# while a<1000:
#     print(a,end=',')
#     a,b=b,a+b

#画圆
# import turtle
# turtle.pensize(2)
# turtle.circle(10)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)

#时间和日期的输出
# from datetime import datetime
# now=datetime.now()
# print(now)
# now.strftime("%x")
# now.strftime("%X")

# n=input("please input a number N:")
# sum=0
# for i in range(int(n)):
#     sum+=i+1
# print("1到N求和结果：",sum)

#打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={:2}".format(j,i,i*j),end='')
#     print('')

# n=1
# for i in range(5,0,-1):
#     n=(n+1)<<1
# print(n)

#绘制太阳花
# from turtle import *
# color('red','yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos())<1:
#         break
# end_fill()
# done()

# from turtle import *
# import colorsys  # 用于颜色渐变
#
# # 设置画布和背景颜色
# bgcolor('black')
#
# # 画笔速度和线条宽度
# speed(0)  # 设置为最快
# pensize(2)  # 设置画笔宽度为 2
#
# # 颜色渐变设置
# n = 36  # 图案的复杂度
# hue = 0  # 起始颜色
# colors = [colorsys.hsv_to_rgb(hue + i / n, 1.0, 1.0) for i in range(n)]  # 使用HSV颜色空间
#
# # 开始绘图
# for i in range(n):
#     color(colors[i])  # 使用渐变颜色
#     begin_fill()
#
#     forward(300)  # 前进固定的距离
#     left(123)  # 固定左转角度，形成对称性
#     forward(300)
#
#     end_fill()
#
# done()

# import turtle
# # 设置屏幕
# screen = turtle.Screen()
# screen.bgcolor("white")  # 设置背景颜色
#
# # 创建 turtle 对象
# spiral = turtle.Turtle()
# spiral.speed(0)  # 设置绘图速度为最快
# spiral.pensize(2)  # 设置画笔的宽度
#
# # 绘制正方形螺旋线
# size = 1  # 初始边长
# increment = 5  # 每次增加的边长
#
# for _ in range(120):  # 绘制100次
#     spiral.forward(size)  # 向前移动
#     spiral.right(90)  # 右转90度
#     size += increment  # 增加边长
#
# # 完成绘制
# turtle.done()

# weekstr = "星期一星期二星期三星期四星期五星期六星期日"
# weekid = eval(input("请输入星期数字(1-7): "))  # 让用户输入1-7之间的数字
# pos = (weekid-1) * 3  # 计算星期几在字符串中的起始位置
# print(weekstr[pos])
# print(weekstr[pos: pos+3])  # 打印对应的星期几

# import time
# for i in range(101):
#     print("\r{:2}%".format(i),end="")
#     time.sleep(0.05)







