import turtle as t
import random

t.color("red")
t.shape("turtle")
t.shapesize(1)
# t.delay(20)
for i in range(100):
    r = random.randint(0,7)
    t.rt(-360+r*90)
    t.fd(i*5)


t.mainloop()