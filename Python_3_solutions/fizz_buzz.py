# fizz_buzz.py

x,y,n = input().split(' ')

for i in range(1,int(n)+1):
  if i % int(x) == 0 and not i % int(y) == 0:
    print("Fizz")
  elif i % int(y) == 0 and not i % int(x) == 0:
    print("Buzz")
  elif i % int(y) == 0 and i % int(x) == 0:
    print("FizzBuzz")
  else:
    print(str(i))