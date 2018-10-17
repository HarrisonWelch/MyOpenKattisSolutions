# time_bomb.py

nums = [
"""***
* *
* *
* *
***""",
"""  *
  *
  *
  *
  *""",
"""***
  *
***
*  
***""",
"""***
  *
***
  *
***""",
"""* *
* *
***
  *
  *""",
"""***
*  
***
  *
***""",
"""***
*  
***
* *
***""",
"""***
  *
  *
  *
  *""",
"""***
* *
***
* *
***""",
"""***
* *
***
  *
***"""
]

digits = [
  input(),
  input(),
  input(),
  input(),
  input()
]

num_digits = len(digits[0]) // 4 + 1

# print(num_digits)

entered_digits = ''

for i in range(0, num_digits*4, 4):
  num = ''
  for j in range(0, 5):
    if j != 4:
      num = str(num) + str(digits[j][i:i+3]) + "\n"
    else:
      num = str(num) + str(digits[j][i:i+3])
  # if i < num_digits*4 - 4:
  #   num = num[0:len(num)-1]
  # print("'"+num+"'")
  index = -1
  for k in range(0, len(nums)):
    # print('k = "' + str(k) + '"\n')
    if nums[k] == num:
      # print('1234567890')
      index = k
  # print('after index = ' + str(index))
  if index != -1:
    entered_digits = entered_digits + str(index)
  # print('now entered_digits = ' + str(entered_digits))

# print('entered_digits = ' + entered_digits)
# print('int(entered_digits) = ' + str(int(entered_digits)))

print("BEER!!" if int(entered_digits) % 6 == 0 else "BOOM!!")

# print(num)
# print(nums[8])
# print(num == nums[8])