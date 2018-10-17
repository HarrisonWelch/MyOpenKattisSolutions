# Cetiri

# https://open.kattis.com/problems/cetiri

inp = map(int, input().split(' '))

inp_sorted = sorted(inp)

# print(inp_sorted)

diffs = []

for i in range(len(inp_sorted)-1):
  diffs.append( inp_sorted[i+1] - inp_sorted[i] )

# print(diffs)

if diffs[1] > diffs[0]:
  print(inp_sorted[1] + (diffs[1]//2))
elif diffs[0] > diffs[1]:
  print(inp_sorted[0] + (diffs[0]//2))
else:
  print(inp_sorted[2] + (diffs[0]) )