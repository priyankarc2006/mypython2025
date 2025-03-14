class shape:
  def area(self):
    pass
class rectangle(shape):
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
     return self.length * self.width
class circle(shape):
  def __init__(self,radius):
    self.radius = radius
  def area(self):
     return 3.14*self.radius*self . radius
shape = [rectangle(4,5), circle(3)]
for i in shape:
  print("area:",i.area()) 
