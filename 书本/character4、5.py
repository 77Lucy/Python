# def divide_numbers():
#     try:
#         # 获取用户输入，并将其转换为浮点数
#         num1 = float(input("请输入第一个数字: "))
#         num2 = float(input("请输入第二个数字: "))
#
#         # 尝试执行除法
#         result = num1 / num2
#
#     except ZeroDivisionError:
#         # 捕获除以零的异常
#         print("错误: 不能除以零。")
#         return None
#     except ValueError:
#         # 捕获非数字输入的异常
#         print("错误: 请输入有效的数字。")
#         return None
#     else:
#         # 如果没有异常，返回结果
#         print("除法成功！结果是:")
#         return result
#     finally:
#         # 无论是否抛出异常，都会执行
#         print("程序执行完毕。")
#
# # 调用函数
# result = divide_numbers()
# if result is not None:
#     print(result)



#使用lambda 函数
# def safe_division():
#     try:
#         # 获取用户输入
#         num1 = float(input("请输入第一个数字: "))
#         num2 = float(input("请输入第二个数字: "))
#
#         # 使用 lambda 函数进行除法
#         divide = lambda x, y: x / y if y != 0 else "除数不能为零"
#
#         # 调用 lambda 函数
#         result = divide(num1, num2)
#         print(f"结果是: {result}")
#
#     except ValueError:
#         print("错误: 请输入有效的数字。")
#
# # 调用函数
# safe_division()

from PIL import Image
im = Image.open("D:\\桌面\\pythonProject\\suzhou.jpg")
r,g,b=im.split()
om=Image.merge("RGB",(b,g,r))
om.save('suzhou.jpg')