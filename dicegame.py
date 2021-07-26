import turtle
import random
import time
positions = {}
k = 1
for x in range(-180,241,70):
    positions[k] = (x,-250)
    k += 1
for x in range(240,-190,-70):
    positions[k] =(x,-200)
    k += 1



t1 = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
s.setup(600,600)
t1.width(2)
t1.speed(20)
t1.color('yellow')
t1.hideturtle()
x = -298
y = -280
#TO DRAW HORIZONTAL LINES
for i in range(8):
    t1.penup()
    t1.setx(x)
    t1.sety(y)
    t1.pendown()
    t1.forward(585)
    y += 50

x = -290
y = -280
t1.left(90)
for i in range(11):
    t1.penup()
    t1.setx(x)
    t1.sety(y)
    t1.pendown()
    t1.forward(355)
    x += 72

t2 = turtle.Turtle()
t2.shape("circle")
t2.width(5)
t2.color('red')
t2.penup()
t2.setpos(-260,-250)
t3 = turtle.Turtle()
t3.shape("circle")
t3.width(5)
t3.color('blue')
t3.penup()
t3.setpos(-255,-250)
player = 1
pos1 = 0
pos2 = 0
while True:
    time.sleep(5)
    dice = random.randint(1,6)
    if player % 2 == 1:
        pos1 += dice
        t2.setpos(positions[pos1])
    else:
        pos2 += dice
        t3.setpos(positions[pos2])
    player += 1

turtle.done()