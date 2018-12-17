# Задача-1
#
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".

sentence = "How are you? Eh, ok. Low or Lower? Ohhh."
new_word = ""
for letter in sentence:
    if letter.isupper():
        word = []
        word += str(letter)
        for i in word:
            new_word += str(i)
print(new_word)

# Задача-2
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.

array = [int(i) for i in input().split()]
if array:
    last = array[-1]
    multiple = sum(array[::2]) * last
    print(multiple)
else:
    print("List is empty")

# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все

import re

text = "  .... Don't, watch this film"
first_word = re.findall(r"[\w']+", text)[0]
#first_word = lambda text: text.replace('.', '').replace(',', '').strip().split(' ')[0]
print("First word is: ", first_word)


# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.

word = input()
word_list = list(word)
shuffle = word_list[0], word_list[-1]
word_list[0] = shuffle[1]
word_list[-1] = shuffle[0]
print(''.join(word_list))

# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') == 'exercises

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print("Task 5: " , ''.join(tup))


# **Задача-6 (Не обязательно, для тех кто скучает)
# You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
#  1) it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
#  2) there should be an even number of letters;
#  3) there should be an odd number of digits.
# You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces.
# The goal is to choose the longest word that is a valid password.
# You can assume that if there are K spaces in string S then there are exactly K + 1 words.
#
# For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007".
# Thus the longest password is "pass007" and its length is 7.
# Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).
