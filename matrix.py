class Matrix:

  def __init__(self,width=1,height=1):
    #Matrix is a 2D array
    self.matrix = [[None for x in range(width)] for y in range(height)]
    self.height = height
    self.width = width

  def set_element(self, x, y, value):
    self.matrix[y][x] = value

  def zero_intersections(self):
    zero_tuples = []
    #scan matrix for zeroes
    for y in range(self.height):
      for x in range(self.width):
        if self.matrix[y][x] == 0:
          zero_tuples.append((x,y))

    #Zero out columns and rows for discovered zero values
    for z in zero_tuples:
      (x,y) = z
      for h in range(self.height):
        print(x,h)
        self.set_element(x, h, 0)
      for w in range(self.width):
        self.set_element(w, y, 0) 

