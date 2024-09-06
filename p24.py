import math
def compute():
  perms = math.perm(10)
# print(compute())

def millionth_lexicographic_permutation():
  digits = list(range(10))  # 0-9
  permutation = []
  n = 1000000 - 1  # 0-based index

  for i in range(10, 0, -1):
    factorial = math.factorial(i - 1)
    position = n // factorial
    n = n % factorial
    
    permutation.append(str(digits[position]))
    digits.pop(position)
  return ''.join(permutation)

print(millionth_lexicographic_permutation())