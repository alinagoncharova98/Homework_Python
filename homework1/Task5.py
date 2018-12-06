dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}

for i in dict.keys(dict_one):
    for j in dict.keys(dict_two):
        if i == j:
            print(i)