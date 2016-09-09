import math
from swampy.TurtleWorld import *

def square(t, len):
    for i in range(4):
        fd(t, len)
        lt(t)

def polygon(t, n, len):
    ang = 360.0/n
    for i in range(n):
        fd(t, len)
        lt(t, ang)

def arc(t, r, ang):
    arcLen = 2 * math.pi * r * abs(ang) / 360
    n = int(arcLen / 4) + 1
    steppingLen = arcLen / n
    steppingAng = float(ang) / n

    lt(t, steppingAng/2)
    for i in range(n):
        fd(t, steppingLen)
        lt(t, steppingAng)
    rt(t, steppingAng/2)

def circle(t, r):
    arc(t, r, 360)

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)
    wait_for_user()
