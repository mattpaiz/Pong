import time
from graphics import *

class Simulation:

  balls = list()
  width = 0.0
  height = 0.0
  window = None

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def addBall(self, ball):
    self.balls.append(ball)

  def start(self):
    self.window = GraphWin('Pong Game', self.width, self.height)
    self.drawInitial()

    while True:
      start = time.time()
      time.sleep(0.05)
      for ball in self.balls:
        
        ball.update(time.time() - start, self.width, self.height)
        
    # self.window.getMouse()

  def drawInitial(self):
    for ball in self.balls:
      ball.draw(self.window)







