"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def compute():
  max_p = 0
  factors = [0,0]
  for i in range(999, 99, -1):
    for j in range(999, 99, -1):
      product = i*j
      if product <= max_p:
        break
      if check_palidrome(product):
        max_p = product
        factors = [i,j]
  return [factors, max_p]  

def check_palidrome(n):
  # Eg: 9009
  l = list(str(n))
  length = len(l)
  rptr = length-1
  for i in range(0, length//2+1):
    if l[i] != l[rptr-i]:
      return False
  return True

print(compute())
