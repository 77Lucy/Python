import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("skyblue")

t.color("orange")
t.penup()
t.goto(0, -210)  # 将文字放置在底部，这里假设底部距离画布顶部210个单位
t.write("This is a beautiful house!", align="center", font=("华文行楷", 35, "normal"))
t.goto(0, -270)
t.color("black")
t.write("221402060422 王仪琳", align="center", font=("华文行楷", 20, "normal"))

def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_triangle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# house
t.penup()
t.goto(-100, -100)
t.pendown()
draw_rectangle(200, 150, "beige")

# roof
t.penup()
t.goto(-110, 50)
t.pendown()
draw_triangle(220, "red")

# door
t.penup()
t.goto(-30, -100)
t.pendown()
draw_rectangle(60, 100, "brown")

# doorknob
t.penup()
t.goto(15, -60)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(5)
t.end_fill()

# left window
t.penup()
t.goto(-75, 0)
t.pendown()
draw_rectangle(40, 40, "lightblue")

#  right window
t.penup()
t.goto(35, 0)
t.pendown()
draw_rectangle(40, 40, "lightblue")

def draw_window_panes(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.forward(40)
    t.penup()
    t.goto(x + 20, y + 20) # bars of the window
    t.pendown()
    t.setheading(270)
    t.forward(40)

draw_window_panes(-75, 20)
draw_window_panes(35, 20)
t.hideturtle()
turtle.done()