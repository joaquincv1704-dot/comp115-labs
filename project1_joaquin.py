import turtle
sc = turtle.Screen()
sc.setup(600, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_rect(x, y, width, hight, color):
    t.up()
    t.goto(x,y)
    t.down
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(hight)
        t.right(90)
    t.end_fill()
width = 600
hight = 600

draw_rect(-300, 300, 600, 300, 'black')
draw_rect(-300, 0, 600, 300, 'darkgreen')



t.up()
t.goto(0,-100)
t.setheading(90)
t.down()
t.color('grey')
t.begin_fill()
t.circle(50, 180)
t.left(90)
t.forward(100)
for _ in range(4):
    t.right(90)
    t.forward(100)
t.end_fill()


















sc.mainloop()
