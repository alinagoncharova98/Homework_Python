# 1)Дан массив из словарей 
from itertools import groupby
from operator import itemgetter

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 1.1) отсортировать массив из словарей по значению ключа ‘age' 
# 1.2) сгруппировать данные по значению ключа 'city'
data = sorted(sorted(data, key=itemgetter('age')), key=itemgetter('city'))
result = []
for key, items in groupby(data, itemgetter('city')):
    print(key, ': ')
    for i in items:
        print (i)

# вывод должен быть такого вида :
result1 = {
    'Kiev': [
        {'name': 'Viktor', 'age': 30},
        {'name': 'Andrey', 'age': 34}],

    'Dnepr': [{'name': 'Maksim', 'age': 20},
              {'name': 'Artem', 'age': 50}],
    'Lviv': [{'name': 'Vladimir', 'age': 32},
             {'name': 'Dmitriy', 'age': 21}]
}


# =======================================================
# =======================================================
# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

def most_frequent(list_var):
    return max(set(list_var), key=list_var.count)


print("Enter sequence: ")

enter_string = input().split()

print(most_frequent(enter_string))

most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'


# =======================================================
# =======================================================
# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

print("Enter number to find its product: ")
number = input()
product = 1
for i in number:
    if int(i) != 0:
        product *= int(i)
print("Произведение цифр: ", product)


# =======================================================
# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.


def find_degree():
    print("Enter array: ")
    array = [int(i) for i in input().split()]
    print("Enter n: ")
    n = int(input())
    if n < len(array):
        print(array[n] ** n)
    else:
        print(-1)


find_degree()

# =======================================================
# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

print("Enter your string: ")
words = input().split()
count = 1
for i in words:
    if i.isalpha():
        count += 1
        if count == 3:
            print("String has three words in a row")
    else:
        count = 0

