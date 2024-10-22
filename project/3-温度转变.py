#e1.1TempConvert.Py
# TempStr =input("请输入带有符号的温度值:")
# if TempStr[-1] in ['F','f']:
#     C=(eval(TempStr[0:-1])-32)/1.8
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C','c']:
#     F=1.8*eval(TempStr[0:-1])+32
#     print("转换后的温度是{:.2f}F".format(F))
# else :
#     print("输入格式错误")

#修改后
# 输出学号和姓名信息
print("姓名：王仪琳 学号：221402060422")

# 温度转换
TempStr = input("请输入带有符号的温度值:")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是{:.2f}°C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}℉".format(F))
else:
    print("输入格式错误")


