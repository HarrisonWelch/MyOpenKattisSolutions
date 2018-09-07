# hissing_microphone.py

inp = input()

letter = '~'
old_letter = '~'
hiss_flag = False

for i in range(len(inp)):
  letter = inp[i]
  if letter == old_letter and letter == 's':
    hiss_flag = True
  old_letter = letter

if hiss_flag:
  print('hiss')
else:
  print('no hiss')