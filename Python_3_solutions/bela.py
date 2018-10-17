# bela.py

def get_value(num, suit, dom_suit):
  val = 0
  if num == 'A':
    val = 11
  elif num == 'K':
    val = 4
  elif num == 'Q':
    val = 3
  elif num == 'J':
    if suit == dom_suit:
      val = 20
      return val
    val = 2
  elif num == 'T':
    val = 10
  elif num == '9' and suit == dom_suit:
    val = 14

  return val

n, b = input().split(' ')

sum = 0

for i in range(4*int(n)):
  inp = input()
  num = inp[0]
  suit = inp[1]
  sum = sum + get_value(num, suit, b)

print(sum)