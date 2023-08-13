def compute():
  sum = 0
  for i in range(1000):
      if i % 15 == 0:
          sum = sum - i
      if i % 3 == 0:
        sum = sum + i
      if i % 5 == 0:
          sum = sum + i
  return sum

'''
More pythonic solution:
def compute():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)
'''

print(compute())
