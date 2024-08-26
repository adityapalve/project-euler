"""
Problem 9: There exists exactly one Pythagorean triplet for which 
a + b + c = 1000
Find the product abc 
"""
# Brute Force lol
def compute():
  for i in range(1,1001):
    for j in range(1,1001):
      for k in range(1,1001):
        if (i**2+j**2 == k**2) and (i+j+k == 1000):
          return i*j*k
          
print(compute())