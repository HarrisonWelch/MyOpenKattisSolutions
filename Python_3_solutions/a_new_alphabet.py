# A New Alphabet

# https://open.kattis.com/problems/anewalphabet

inp = input()

# print(inp)
inp = inp.lower()

inp = inp.replace('a', '@')
inp = inp.replace('b', '8')
inp = inp.replace('c', '(')
inp = inp.replace('d', '|)')
inp = inp.replace('e', '3')

inp = inp.replace('f', '#')
inp = inp.replace('g', '6')
inp = inp.replace('h', '[-]')
inp = inp.replace('i', '|')
inp = inp.replace('j', '_|')

inp = inp.replace('k', '|<')
inp = inp.replace('l', '1')
inp = inp.replace('m', '[]\/[]')
inp = inp.replace('n', '[]\[]')
inp = inp.replace('o', '0')

inp = inp.replace('p', '|D')
inp = inp.replace('q', '(,)')
inp = inp.replace('r', '|Z')
inp = inp.replace('s', '$')
inp = inp.replace('t', '\'][\'')

inp = inp.replace('u', '|_|')
inp = inp.replace('v', '\/')
inp = inp.replace('w', '\/\/')
inp = inp.replace('x', '}{')
inp = inp.replace('y', '`/')

inp = inp.replace('z', '2')

print(inp)
