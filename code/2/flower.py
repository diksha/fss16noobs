from swampy.TurtleWorld import *
from polygon import *

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)

def makePetal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def makeFlower(t, n, r, angle):
    for i in range(n):
        makePetal(t, r, angle)
        lt(t, 360.0/n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
move(bob, -100)
makeFlower(bob, 7, 60.0, 60.0)
move(bob, 100)
makeFlower(bob, 10, 20.0, 80.0)
move(bob, 100)
makeFlower(bob, 20, 140.0, 20.0)
die(bob)
world.canvas.dump()
wait_for_user()
