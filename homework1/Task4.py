import numpy as np

array = np.array([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1])

#Без повторяющихся элементов
def del_repeating(array):
    print("Array with unique elements: ", set(array))

#Три наибольших элемента в массиве
def maximum(array):
    max = np.argpartition(array, -3)[-3:]
    print("Three max elements: ", array[max])

#Индекс минимального числа
def min_index(array):
    minIndex = np.argmin(array, axis = 0)
    #minIndex = np.argpartition(array, 1)[18:]
    print("Index of min element: ", minIndex)

#Обратный порядок исходного массива
def reverse(array):
    print("Reverse order of array: ", array[::-1])

del_repeating(array)
maximum(array)
min_index(array)
reverse(array)
