def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime_quadratic():
    max_primes = 0
    max_a = 0
    max_b = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(n*n + a*n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                max_a = a
                max_b = b

    return max_a, max_b, max_primes

# Run the function
a, b, primes = find_max_prime_quadratic()
print(f"The quadratic n^2 + {a}n + {b} produces {primes} consecutive primes.")
print(f"The product of coefficients is {a * b}.")