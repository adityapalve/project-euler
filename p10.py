"""
Problem 10: Find the sum of all the primes below two million.
Sum of primes below 10 = 17
"""
def compute():
  limit = 2000000
  is_prime = [True] * limit
  is_prime[0] = is_prime[1] = False
  
  for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
      for j in range(i*i, limit, i):
        is_prime[j] = False
  
  prime_sum = sum(i for i in range(2, limit) if is_prime[i])
  
  return prime_sum

print(compute())