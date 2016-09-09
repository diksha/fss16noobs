import math
from swampy.TurtleWorld import *

def drawPie(t, n, r):
    polygon(t, n, r)
    pu(t)
    fd(t, r*2 + 10)
    pd(t)

def polygon(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        iso(t, r, angle/2)
        lt(t, angle)

def iso(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
pu(bob)
bk(bob, 130)
pd(bob)
size = 40
drawPie(bob, 5, size)
drawPie(bob, 6, size)
drawPie(bob, 7, size)
drawPie(bob, 8, size)
die(bob)
world.canvas.dump()
wait_for_user()
