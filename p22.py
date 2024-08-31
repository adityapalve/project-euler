import string
with open("0022_names.txt", "r") as f:
  input = f.read()
# print(input)
names = []
for name in input.split(','):
  names.append(name.strip('"'))
  names.sort()

def compute(input):
  alphabet = {c:i+1 for i, c in enumerate(string.ascii_uppercase)}
  total_sum = 0
  for i, name in enumerate(input):
    name_val = 0
    for c in name:
      name_val += alphabet[c]
    total_sum += name_val*(i+1)
  return total_sum
  
print(compute(names))
