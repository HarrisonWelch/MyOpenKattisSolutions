# Scaling Recipes

# https://open.kattis.com/problems/recipes

n = int( input())

for i in range(n):
  inp = input()
  r, p, d = map(int, inp.split(' '))

  # step1) determine the scaling factor by dividing the number of desired portions by the number of portions for which the recipe is written;
  scaling_factor = d / p
  # print('scaling_factor = ' + str(scaling_factor))


  ingredients = []
  scaled_ingredients = []

  for j in range(r):
    name, weight, perc = input().split(' ')

    ingredients.append((name, weight, perc))

  index_of_100_perc = -1

  for k in range(len(ingredients)):
    if ingredients[k][2] == '100.0':
      index_of_100_perc = k

  # print('index_of_100_perc = ' + str(index_of_100_perc))

  scaled_weight_of_main_ingredient = float(ingredients[index_of_100_perc][1]) * scaling_factor
  # print('scaled_weight_of_main_ingredient = ' + str(scaled_weight_of_main_ingredient))

  for l in range(len(ingredients)):
    if l != index_of_100_perc:
      # print('this --- ' + str( (float(ingredients[l][2]))) )
      # print('this --- ' + str( (float(ingredients[l][2])/100.0)) )
      # print('this --- ' + str( scaled_weight_of_main_ingredient * (float(ingredients[l][2])/100.0)) )
      scaled_ingredients.append( ( ingredients[l][0], scaled_weight_of_main_ingredient * (float(ingredients[l][2])/100.0)) )
    else:
      scaled_ingredients.append( ( ingredients[l][0], scaled_weight_of_main_ingredient ) )

  print('Recipe # ' + str(i+1))
  for m in range(len(scaled_ingredients)):
    print(str(scaled_ingredients[m][0]) + ' ' + '{:.1f}'.format((scaled_ingredients[m][1])))
  print('----------------------------------------')
  