sum = 1
val = 1
inc = 2
for inc in range(2, 5, 2):
  for c in range(4):
    val += inc
    sum += val
print(sum)