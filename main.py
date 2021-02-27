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
  return Ball(random.randint(0, 500), random.randint(0, 500), random.randint(10, 30), random.randint(10, 30), colors[random.randint(0, len(colors) - 1)])

s = Simulation(500, 500)


for i in range(0, 60):
  s.addBall(randomBall())
#s.addBall(Ball(50, 50, 25, 25, "green"))
#s.addBall(Ball(100, 100, -25, 25, "blue"))

s.start()

# pt = Point(100, 50)

# win = GraphWin("Pong", 500, 500)
# cir = Circle(pt, 25)

# cir.draw(win)

# print(win.getMouse())