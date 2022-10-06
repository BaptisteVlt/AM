import math
import pytest

def calculeDistance(X,Z):
    math.sqrt( ((Z[0] - X[0])**2) + ((Z[1] - X[1])**2) )

def isEquilateral(triangle):
  if ( calculeDistance(triangle.A, triangle.B) == calculeDistance(triangle.A ,triangle.C) and calculeDistance(triangle.B, triangle.C) == calculeDistance(triangle.A, triangle.B)):
   return True
  else:
    return False

def isIsosceles(triangle):
  if calculeDistance(triangle.A, triangle.B) ==  calculeDistance(triangle.A, triangle.C) or  calculeDistance(triangle.A, triangle.B) ==  calculeDistance(triangle.B, triangle.C) or  calculeDistance(triangle.B, triangle.C) ==  calculeDistance(triangle.A, triangle.C):
    return True
  else:
    return False

class triangle :
  def __init__(self,A,B,C):
    self.A = A
    self.B = B
    self.C = C

def testEquilateral():
  Triangle1 = triangle([0,0], [1,0],[0,1])
  assert isEquilateral(Triangle1) == True
  Triangle2 = triangle([0.5,0], [1,0],[0,1])
  assert isEquilateral(Triangle2) == False


testEquilateral()
