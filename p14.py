"""
Problme 14: 
  n -> n/2
  n -> 3n+1
  Which starting number, under one million, produces the longest chain?
"""
def compute():
  limit = 1000000
  longest_chain = 0
  result = 0
  cache = {1: 1}
  
  for i in range(2, limit+1):
    chain_length = collatz_length(i,cache)
    if chain_length > longest_chain:
      longest_chain = chain_length
      result = i
  
  return result

def collatz_length(num, cache):
  if num in cache:
    return cache[num]
    
  if num % 2 == 0:
    length = 1 + collatz_length(num//2, cache)
  else:
    length = 1 + collatz_length((3*num) + 1, cache)
  
  cache[num] = length
  return length


print(compute())