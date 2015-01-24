from matrix import Matrix
import unittest

class Matrix_test(unittest.TestCase):

  def test_init(self):
    mat = Matrix()
    assert(mat)
    self.assertEqual(len(mat.matrix), 1)
    self.assertEqual(len(mat.matrix[0]), 1)
    self.assertEqual(mat.matrix[0][0], None)
    self.assertEqual(mat.height, 1)
    self.assertEqual(mat.width, 1)
    
    mat = Matrix(2,3)
    self.assertEqual(len(mat.matrix), 3)
    self.assertEqual(len(mat.matrix[0]), 2)
    self.assertEqual(mat.matrix[2][1], None)
    self.assertEqual(mat.height, 3)
    self.assertEqual(mat.width, 2)

  def test_set_element(self):
    mat = Matrix(5,5)
    mat.set_element(2,2,7)
    self.assertEqual(mat.matrix[2][2], 7) 

  def test_zero_intersections(self):
    mat = Matrix(5,5)
    mat.set_element(2,2,0)
    mat.zero_intersections()

    for x in range(5):    
      self.assertEqual(mat.matrix[x][2], 0) 
      self.assertEqual(mat.matrix[2][x], 0) 

    mat = Matrix(7,7)
    mat.set_element(2,2,0)
    mat.set_element(5,5,0)
    mat.zero_intersections()

    for x in range(7):    
      self.assertEqual(mat.matrix[x][2], 0) 
      self.assertEqual(mat.matrix[2][x], 0) 
      self.assertEqual(mat.matrix[x][5], 0) 
      self.assertEqual(mat.matrix[5][x], 0) 

    mat = Matrix(3,7)
    mat.set_element(1,5,0)
    mat.zero_intersections()

    for y in range(mat.height):    
      for x in range(mat.width):
        self.assertEqual(mat.matrix[5][x], 0)
      self.assertEqual(mat.matrix[y][1], 0)



if __name__ == '__main__':
  unittest.main()
