# Harrison

notes = ["A","B","C","D","E","F","G"]
j = 1
for i in range(5):
  try:
    inp = input()
    if inp == '':
      break
  except:
    break

  inp = inp.split(' ')

  # print("len(inp[0]) = " + str(len(inp[0])))

  if len(inp[0]) == 1:
    print("Case " + str(j) + ": " + "UNIQUE")
    i = i + 1
    continue

  # print("inp[0][1] = " + str(inp[0][1]))
  
  if inp[0][1] == "#":
    index = notes.index(inp[0][0])
    if index == (len(notes) - 1):
      index = -1
    print("Case " + str(j) + ": " + str(notes[  index + 1  ]) + "b " + inp[1])
  if inp[0][1] == "b":
    index = notes.index(inp[0][0])
    if index == 0:
      index = len(notes)
    print("Case " + str(j) + ": " + str(notes[  index - 1  ]) + "# " + inp[1])

  j = j + 1
  # print("END OF LOOP")