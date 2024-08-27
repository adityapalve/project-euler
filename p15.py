"""
Problem 15: Lattice Paths
Starting in the top left corner of a grid, and only being able to move to the right and down,
to the bottom right corner, how much such routes are there in a 20x20 grid.
"""
import math
def compute():
  # directions = [[0,1],[1,0]]
  # for i in range(3):
  #   for j in range(3):
  n = 20
  paths = math.comb(2 * n, n)
  return paths    


print(compute())