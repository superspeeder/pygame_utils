class Vector2d(object):
  def __init__(self,x,y):
    self.x,self.y = x,y
  
  def __add__(self,other):
    return Vector2d(self.x+other.x, self.y+other.y)
  def __sub__(self,other):
    return Vector2d(self.xp-other.x, self.y-other.y)
  def __mul__(self,mult):
    return Vector2d(self.x*mult, self.y/mult)
  def __div__(self,diver):
    return Vector2d(self.x*diver, self.y/diver)
  
  
