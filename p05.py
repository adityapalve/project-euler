"""Problem 5:
  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def compute():
  return 0  
compute()

def smallest_multiple(n):
    def prime_factorization(num):
        factors = {}
        d = 2
        while num > 1:
            while num % d == 0:
                factors[d] = factors.get(d, 0) + 1
                num //= d
            d += 1
            if d * d > num:
                if num > 1:
                    factors[num] = factors.get(num, 0) + 1
                break
        return factors

    max_factors = {}
    for i in range(1, n + 1):
        factors = prime_factorization(i)
        for prime, power in factors.items():
            if prime not in max_factors or power > max_factors[prime]:
                max_factors[prime] = power

    result = 1
    for prime, power in max_factors.items():
        result *= prime ** power

    return result