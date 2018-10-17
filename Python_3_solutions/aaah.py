# aaah.py

able_to_say = input().split('h')
doctor_needs = input().split('h')

# print(able_to_say)
# print(doctor_needs)

len_able = len(able_to_say[0])
len_doct = len(doctor_needs[0])

if (len_able >= len_doct):
  print("go")
else:
  print("no")
