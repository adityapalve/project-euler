def proper_divisors(n):
  divisors = [1]  # 1 is always a proper divisor
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:  # Avoid adding the same divisor twice for perfect squares
        divisors.append(n // i)
  return sorted(divisors)  # Return the list in sorted order
  
def compute():
  limit = 10000
  divisor_sums = {}
  amicable_sum = 0

  # Calculate sum of proper divisors for each number
  for i in range(1, limit):
    divisor_sums[i] = sum(proper_divisors(i))

  # Find amicable pairs and sum them
  for a in range(1, limit):
    b = divisor_sums[a]
    if b != a and b < limit and divisor_sums.get(b, 0) == a:
      amicable_sum += a
  return amicable_sum

print(compute())