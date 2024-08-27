def compute():
  num = pow(2, 1000)
  s = sum([int(digit) for digit in str(num)])
  # s = sum(int(digit) for digit in str(num))
  print(s)

compute()