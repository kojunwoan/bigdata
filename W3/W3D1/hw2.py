import turtle as t
shape = int(input("몇각형? "))

t0 = t.Pen()
t0.speed(100)
t0.penup()
t0.goto(0,200)
t0.pendown()
for i in range(shape):
    t0.fd(1200/shape)
    t0.rt(360/shape)

t.mainloop()