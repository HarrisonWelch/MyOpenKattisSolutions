# vauvau.py

a, b, c, d = map(int, input().split(' '))

p, m, g = map(int, input().split(' '))

ls = [p, m, g]

p_atks = 0
m_atks = 0
g_atks = 0

# postman

# 2 2 3 3
# 1 3 4

for i in range(len(ls)):

  if ls[i] <= a and ls[i] <= c:
    print("both")
  elif ls[i] <= a or ls[i] <= c:
    print("one")
  else:
    print('none')

