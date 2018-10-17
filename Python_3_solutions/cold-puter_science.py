# cold-puter_science.py

n = input()
num_below_zero = 0

inp = list( map(int, input().split(' ')))

for i in range(int(n)):
  if inp[i] < 0:
    num_below_zero = num_below_zero + 1

print(num_below_zero)