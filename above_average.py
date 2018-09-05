# above_average.py

n = input()

for i in range(int(n)):
  inp = input().split(' ')
  num_stu = inp[0]
  sum = 0
  for j in range(1, int(num_stu)+1):
    sum = sum + int(inp[j])
    # print("sum = " + str(sum))
  avg = sum / int(num_stu)
  # print("int(num_stu) = " + str(int(num_stu)))
  # print("avg = " + str(avg))
  # print("avg = " + str(avg))
  num_abv_avg = 0
  for k in range(1, int(num_stu)+1):
    # print("int(inp[k]) = " + str(int(inp[k])))
    if int(inp[k]) > avg:
      num_abv_avg = num_abv_avg + 1
  print('{:2.3%}'.format(float(num_abv_avg)/float(num_stu)))
  
