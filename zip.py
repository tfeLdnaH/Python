first = ['Anderson', 'Tati', 'Tom']
last = ['Morita', 'Asato', 'Hanks']

names = zip(first, last) # internal -> [('Anderson', 'Morita'), ('Tati', 'Asato')]

for a, b in names:
    print(a, b)