# alien numbers

n = int(input())

answs = []

for i in range(n):
  num, src, tgt = input().split(' ')

  num_index = 0
  shifts = 0
  decimal_number = 0
  for j in range(len(str(num))):
  
    chr_idx = src.index(num[j])
    # print('chr_idx  = ' + str(chr_idx))
    decimal_number = decimal_number + ( (chr_idx) * (len(src) ** (len(num)-j-1)) )
    # print('decimal_number = ' + str(decimal_number))

  # print('final decimal_number = ' + str(decimal_number))

  decimal_number = int(decimal_number)
  translation_number = ''
  while decimal_number > 0:
    d = decimal_number % len(tgt)
    decimal_number = int(decimal_number / len(tgt))
    translation_number = tgt[d] + translation_number

  print('Case #' + str(i+1) + ': ' + translation_number)
  # for i in range(int(decimal_number)):
