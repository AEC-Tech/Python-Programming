import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
s.setup(700,800)
t.width(2)
t.speed(10)
t.hideturtle()
col = ['yellow','green','red','blue','white']
for i in range(150):
        t.pencolor(col[i % 5])
        t.forward((i*2))
        t.right(50)

turtle.done()