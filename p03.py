"""
Problem 3:
The prime factors of 13195 are 5,7,13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import math
def compute():
   num = 600851475143 
   eg = 13195
   sqrt = math.isqrt(num)
   for i in range(sqrt):
    p = smallest_prime_factor(num)
    if p < num:
        num = num//p
    else:
        return str(num)

def smallest_prime_factor(n):
    # assert n >= 2
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return i
    return n
print(compute())
# Ans = 6857
def largest_prime_factor(n):
	max_prime = 0
	while n % 2 == 0:
		max_prime = 2
		n = n // 2 
	for i in range(3, int(math.sqrt(n)) + 1,2):
		while n % 1 == 0:
			max_prime = i
			n = n // i
	if n > 2:
		max_prime = n
	return max_prime