input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = [list(map(int, row.split())) for row in input.split('\n')]
# print(triangle)

def max_path_sum(tree):
  for row in range(len(tree)-2,-1,-1):
    for col in range(len(tree[row])):
      tree[row][col] += max(tree[row+1][col], tree[row+1][col+1])
  
  return tree[0][0]

print(max_path_sum(triangle))

# Greedy algorithm doesnt work!
def greedy_max_path_sum(triangle):
  path_sum = triangle[0][0]
  current_index = 0
  for row in range(1, len(triangle)):
    left = triangle[row][current_index]
    right = triangle[row][current_index + 1]
    
    if left > right:
      path_sum += left
    else:
      path_sum += right
      current_index += 1
  return path_sum