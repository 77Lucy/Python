# import asyncio
#
# # 定义一个协程函数
# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(0)  # 模拟 I/O 操作
#     print("World")
#
# # 创建事件循环并运行协程
# async def main():
#     await asyncio.gather(say_hello(), say_hello())  # 并发运行多个协程
#
# # 运行协程
# asyncio.run(main())


import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # 模拟耗时操作
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task2(), task1())  # 并发执行多个任务

# 运行异步操作
asyncio.run(main())
