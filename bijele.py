# Bijele.py

my_set = map(int, input().split(' '))

prop_set = [1, 1, 2, 2, 2, 8]

print(" ".join(map(str, ([a_i - b_i for a_i, b_i in zip(prop_set, my_set)]))))