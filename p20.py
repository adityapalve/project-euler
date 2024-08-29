def factorial(num):
  if num == 1:
    return 1
  return num * factorial(num-1)

ans = sum(int(i) for i in str(factorial(100)))
print(ans)