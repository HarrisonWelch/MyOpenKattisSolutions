# half_a_cookie.py
import math

inp = 'null'

while( True ):
  try:
    inp = input()
    r, x, y = map(float, inp.split(' '))
  except ValueError:
    break
  # area = (r**2 / 2.0) * (math.pi / 180.0) * angle * sin(angle)
  dist = ((x**2) + (y**2))**0.5
  if dist > r:
    print("miss")
    continue
  h = dist # distance from the center
  # print('h = ' + str(h))
  # print('math.cos(h/r) = ' + str(math.cos(h/r)))
  angle = (2 * math.acos(h/r))
  # print('angle = ' + str(angle))
  area = 0.5 * (r**2) * ( angle - (math.sin(angle)))
  # print('area = ' + str(area))
  tot_area = ( math.pi * (r**2))
  # print('tot_area = ' + str(tot_area))
  print(str(tot_area-area) + ' ' + str(area))