
from graphics import *
from ball import *
from simulation import *


import random


colors = [
  "green",
  "blue",
  "yellow",
  "pink",
  "white",
  "black",
  "brown"
]


def randomBall():
  return Ball(random.randint(0, 500), random.randint(0, 500), random.randint(40, 100), random.randint(40, 100), colors[random.randint(0, len(colors) - 1)])
win1= input("Enter a window size value, width: ")
win2= input("Enter a window size value height: ")
width=int(win1)
height=int(win2)
s = Simulation(width, height)



for i in range(0, 10):
  s.addBall(randomBall())
#s.addBall(Ball(50, 50, 25, 25, "green"))
#s.addBall(Ball(100, 100, -25, 25, "blue"))

s.start()

# pt = Point(100, 50)

# win = GraphWin("Pong", 500, 500)
# cir = Circle(pt, 25)

# cir.draw(win)

# print(win.getMouse())