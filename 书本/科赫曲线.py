import turtle


def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)


def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.tracer(0)  # 禁用屏幕更新以提高速度

    t = turtle.Turtle()
    t.speed(0)  # 设置最快速度
    t.penup()
    t.goto(-150, 0)  # 设置起始位置
    t.pendown()

    # 定义颜色列表
    colors = ["red", "blue", "green", "orange", "purple"]

    # 绘制雪花
    depth = 4
    length = 300
    for i in range(3):
        t.color(colors[i % len(colors)])  # 设置颜色
        koch_curve(t, length, depth)
        t.right(120)

    window.update()  # 更新屏幕以显示绘制结果
    window.mainloop()


if __name__ == "__main__":
    main()
