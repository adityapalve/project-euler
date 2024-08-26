"""
Problem 9: There exists exactly one Pythagorean triplet for which 
a + b + c = 1000
Find the product abc 
"""
def brute_force():
  for i in range(1,1001):
    for j in range(1,1001):
      for k in range(1,1001):
        if (i**2+j**2 == k**2) and (i+j+k == 1000):
          return i*j*k
          
def compute():
  target = 1000
  for a in range(1, target // 3):  # a can't be more than 1/3 of target
    for b in range(a + 1, (target - a) // 2):  # b is always greater than a
      c = target - a - b  # We know c directly
      if a*a + b*b == c*c:  # Check if it's a Pythagorean triplet
        return a * b * c
print(compute())