import math
def sum_of_proper_divisors(num):
  if num == 1:
    return 0
  total = 1
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      total += i
      if i != num // i:
        total += num // i
  return total

def compute():
  limit = 28124
  abundant_numbers = []
  for num in range(1, limit):
    if sum_of_proper_divisors(num) > num:
      abundant_numbers.append(num)

  can_be_written = [False] * limit
  for i in abundant_numbers:
    for j in abundant_numbers:
      if i + j < limit:
        can_be_written[i + j] = True
      else:
        break

  return sum(i for i in range(1, limit) if not can_be_written[i])

print(compute())