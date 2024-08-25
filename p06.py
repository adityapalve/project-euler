"""
The sum of the squares of the first ten natural numbers is,
$$1^2 + 2^2 + ... + 10^2 = 385.$$
The square of the sum of the first ten natural numbers is,
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is $3025 - 385 = 2640$.
Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""
def compute(n):
  sum_squares = lambda n: sum(pow(x, 2) for x in range(1, n+1)) 
  sum_of_n = lambda n: (n/2)*(n+1)
  return str(abs(sum_squares(n)-(sum_of_n(n)**2)))
# Sum of n natural numbers = n(n+1)/2
# Sum of n**2 

print(compute(100))
