from turtle import *
import random

a = Turtle()
screen = Screen()
print(a)
print(screen)

screen.addshape("audience.gif")
screen.addshape("turtle.gif")
a.shape("audience.gif")
a.penup()
a.goto(0,250)
t1 = Turtle()
t1.speed(10)
t1.shape('turtle')
t1.color('hotpink')
t1.penup()
loc1 = -415
t1.goto(loc1,0)
t1.pendown()
t1.write("1번 꼬부기")


t2 = Turtle()
t2.speed(10)
t2.shape('turtle')
t2.color('lime')
t2.penup()
loc2 = -415
t2.goto(loc2,-70)
t2.pendown()
t2.write("2번 꼬부기")

t3 = Turtle()
t3.speed(10)
t3.shape('turtle')
t3.color('cyan')
t3.penup()
loc3 = -415
t3.goto(loc3,-140)
t3.pendown()
t3.write("3번 꼬부기")

t4 = Turtle()
t4.speed(10)
t4.shape('turtle')
t4.color('slateblue')
t4.penup()
loc4 = -415
t4.goto(loc4,-210)
t4.pendown()
t4.write("4번 꼬부기")

t5 = Turtle()
t5.speed(10)
t5.shape('turtle')
t5.color('indianred')
t5.penup()
loc5 = -415
t5.goto(loc5,-280)
t5.pendown()
t5.write("5번 꼬부기")

t6 = Turtle()
t6.speed(10)
t6.penup()
t6.goto(-400,35)
t6.pendown()
m = 0
for i in range(11):
    t6.write(str(m)+"cm")
    t6.rt(90)
    t6.fd(350)
    t6.penup()
    t6.bk(350)
    t6.lt(90)
    t6.fd(80)
    t6.pendown()
    m += 5
t6.fd(100)

n = textinput("골라","꼬부기를 골라요~")
while True:
    loc1 += random.randint(1,3)
    loc2 += random.randint(1,3)
    loc3 += random.randint(1,3)
    loc4 += random.randint(1,3)
    loc5 += random.randint(1,3)
    t1.goto(loc1,0)
    t2.goto(loc2,-70)
    t3.goto(loc3,-140)
    t4.goto(loc4,-210)
    t5.goto(loc5,-280)
    if loc1 > 395:
        t1.write("   1번 꼬부기 승리")
        t1.penup()
        t1.goto(0,0)
        t1.shape("turtle.gif")
        break
    if loc2 > 395:
        t2.write("   2번 꼬부기 승리")
        t2.penup()
        t2.goto(0,-70)
        t2.shape("turtle.gif")
        break
    if loc3 > 395:
        t3.write("   3번 꼬부기 승리")
        t3.penup()
        t3.goto(0,-140)
        t3.shape("turtle.gif")
        break
    if loc4 > 395:
        t4.write("   4번 꼬부기 승리")
        t4.penup()
        t4.goto(0,-210)
        t4.shape("turtle.gif")
        break
    if loc5 > 395:
        t5.write("   5번 꼬부기 승리")
        t5.penup()
        t5.goto(0,-280)
        t5.shape("turtle.gif")
        break

mainloop()