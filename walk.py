import turtle
import random

angle = 360 # allow full circle
step = 50 # length of each step; modify to fit on screen
def walk(steps=100):
    for i in range(steps):
        turtle.left(random.randrange(angle))
        turtle.forward(step)

