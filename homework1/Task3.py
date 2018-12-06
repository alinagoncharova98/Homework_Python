import random

word = "python"
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for i in word:
    if i in vowels:
        word = word.replace(i, random.choice(consonants),  1)
    elif i in consonants:
        word = word.replace(i, random.choice(vowels), 1)
print(word)
