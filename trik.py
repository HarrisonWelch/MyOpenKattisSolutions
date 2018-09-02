def move_a(arr):
  x = arr[0]
  y = arr[1]
  return [y, x, arr[2]]

def move_b(arr):
  x = arr[1]
  y = arr[2]
  return [arr[0], y, x]

def move_c(arr):
  x = arr[0]
  y = arr[2]
  return [y, arr[1], x]

if __name__ == "__main__":
  inp = input()

  arr = [1, 0, 0]

  for i in range(len(inp)):
    letter = inp[i]
    if letter == 'A':
      # print('A')
      arr = move_a(arr)
    elif letter == 'B':
      arr = move_b(arr)
      # print('B')
    elif letter == 'C':
      arr = move_c(arr)
      # print('C')
    # print(arr)
  
  for i in range(len(arr)):
    if arr[i] == 1:
      print(i+1)