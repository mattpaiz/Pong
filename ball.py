from graphics import *

BALL_WIDTH = 10.0

class Ball:
  x = 0.0
  y = 0.0
  vx = 0.0
  vy = 0.0
  color = None

  shape = None

  def __init__(self, x, y, vx, vy, color):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vx
    self.color = color

  def update(self, dt):

    dx = dt * self.vx
    dy = dt * self.vy

    self.x += dx
    self.y += dy
    
    self.shape.move(dx, dy)


  def draw(self, window):
    self.shape = Circle(Point(self.x, self.y), BALL_WIDTH)
    self.shape.setFill(self.color)
    self.shape.draw(window)

  def printMessage(self):
    print("Position: ", self.x, self.y, self.vx, self.vy)