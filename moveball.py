import turtle
def go_up():
    ball.sety(ball.ycor() + 10)
def go_down():
    ball.sety(ball.ycor() - 10)
def go_left():
    ball.setx(ball.xcor() - 10)
def go_right():
    ball.setx(ball.xcor() + 10)


wn = turtle.Screen()
wn.title("Maze Game")
wn.bgcolor("cyan")
wn.setup(600,600)

ball = turtle.Turtle()
ball.shape("circle")
ball.color('blue')
ball.penup()
ball.setpos(0,0)

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

wn.mainloop()