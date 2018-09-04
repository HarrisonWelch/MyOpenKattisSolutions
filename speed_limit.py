# Speed Limit

n = int(input())
trip = 0
frmr_elps = 0

while n != -1:
  for i in range(0, n):
    speed, elps = map(int,(input().split(' ')))
    trip = trip + (speed*(elps-frmr_elps))
    frmr_elps = elps
  print(str(trip) + ' miles')
  n = int(input())
  frmr_elps = 0
  trip = 0
