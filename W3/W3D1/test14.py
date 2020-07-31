import turtle as t
import random

t0 = t.Pen()
t0.shape('turtle')
t0.color('hotpink')

t2 = t.Pen()
t2.shape('turtle')
t2.color('violet')
t2.penup()
t2.goto(-200,100)
t2.pendown()
t2.begin_fill()
t2.fillcolor("red")
t2.circle(100)
t2.end_fill()



t3 = t.Pen()
t3.shape("turtle")
t3.shapesize(3)
t3.penup()
t3.goto(100,100)
t3.pendown()
for i in range(5):
    t3.fd(100)
    t3.rt(72)

t0.speed(1000)
t0.penup()
t0.goto(-300,0)
t0.pendown()
while True:
    t0.forward(600)
    t0.right(159-random.random())
    t0.forward(60)
    t0.left(162)
    t0.forward(13)
    t0.right(161)


t0.mainloop()
