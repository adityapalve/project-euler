"""
Problem 7: What is the 10001st prime number?
"""
# find nth prime
def compute(n):
  if n <= 0:
    return None
  
  primes = [2]
  num = 3
  
  while len(primes)< n:
    is_prime = True
    
    for prime in primes:
      if prime*prime > num:
        break
      if num % prime == 0:
        is_prime = False
        break 
    
    if is_prime:
      primes.append(num)
    
    num += 2
    
  return primes[-1]

print(compute(10001))
