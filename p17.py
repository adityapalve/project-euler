from num2words import num2words
def compute():
  sum = 0
  for i in range(1, 1001):
    l = len(num2words(i).replace(" ","").replace("-",""))
    sum += l
  return sum

print(compute())