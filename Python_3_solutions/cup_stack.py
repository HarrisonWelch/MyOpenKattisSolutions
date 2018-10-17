n = input()
inp = ''
# a = input()
arr = []
for i in range(int(n)):
  inp = input().split(' ')
  # print(inp)
  if inp[1].isdigit():
    inp = [inp[1], inp[0]]
  arr.append(inp)
  
# print(arr)

for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    if int(arr[i][0]) > int(arr[j][0]):
      print('swapping i = ' + str(i) + ', ' + str(j))
      tmp = arr[i]
      arr[i] = arr[j]
      arr[j] = tmp
      print('res = ' + str(arr))

# print(arr)

for i in range(len(arr)):
  print(arr[i][1])