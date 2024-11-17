def compute():
  res = []
  for a in range(2,101):
    for b in range(2,101):
      res.append(pow(a,b))
  
  return len(set(res))

print(compute())