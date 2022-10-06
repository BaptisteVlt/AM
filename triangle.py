import math
import pytest
import sympy

def calculeDistance(X ,Z):
    return sympy.sqrt( ((Z[0] - X[0])**2) + ((Z[1] - X[1])**2) )

def isEquilateral(triangle : triangle):
  if ( calculeDistance(triangle.A, triangle.B) == calculeDistance(triangle.A ,triangle.C) and calculeDistance(triangle.B, triangle.C) == calculeDistance(triangle.A, triangle.B)):
   return True
  else:
    return False

def isIsosceles(triangle : triangle):
  if calculeDistance(triangle.A, triangle.B) ==  calculeDistance(triangle.A, triangle.C) or  calculeDistance(triangle.A, triangle.B) ==  calculeDistance(triangle.B, triangle.C) or  calculeDistance(triangle.B, triangle.C) ==  calculeDistance(triangle.A, triangle.C):
    return True
  else:
    return False
def isRectangle(triangle : triangle):
  return ((calculeDistance(triangle.A, triangle.B)**2 + calculeDistance(triangle.A, triangle.C)**2 == calculeDistance(triangle.B, triangle.C)**2) or (calculeDistance(triangle.A, triangle.B)**2 + calculeDistance(triangle.B, triangle.C)**2 == calculeDistance(triangle.A, triangle.C)**2) or (calculeDistance(triangle.A, triangle.C)**2 + calculeDistance(triangle.B, triangle.C)**2 == calculeDistance(triangle.A, triangle.B)**2))


class triangle :
  def __init__(self,A,B,C):
    self.A = A
    self.B = B
    self.C = C

def testEquilateral():
  Triangle1 = triangle([1, 1], [1,1],[1,1])
  assert isEquilateral(Triangle1) == True
  Triangle2 = triangle([0.5,0], [1,0],[0,1])
  assert isEquilateral(Triangle2) == False
  assert isIsosceles(Triangle2) == False
  Triangle3 = triangle([0,-1], [0,1],[2,1])
  assert isIsosceles(Triangle3) == True
  assert isRectangle(Triangle2) == False
  assert isRectangle(Triangle3) == True

testEquilateral()
