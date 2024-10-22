from threading import Thread

class MyThread(Thread):  # 创建一个继承自 Thread 的类
    def run(self):  # 重写 run() 方法，线程启动时执行的就是这个方法
        for i in range(1000):
            print("子线程", i)  # 输出 "子线程" 以及计数

if __name__ == '__main__':  # 主程序入口
    t = MyThread()  # 创建线程对象

    # t.run()  # 如果直接调用 t.run()，这其实是单线程执行，不会启动新的线程
    t.start()  # 调用 start() 启动新线程，会并行执行 run() 方法中的代码

    for i in range(1000):
        print("主线程", i)  # 主线程的输出
