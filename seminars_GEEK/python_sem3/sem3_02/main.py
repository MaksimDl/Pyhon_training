# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

import random

n = int(input("введите N - длинна последовательности: "))
k = int(input("Введите к - сдвиг последовательности"))



numb_list = [i for i in range(n)]
# for i in range(len(numb_list)):
#     print (numb_list[i-k], end = " ")

# test_list = numb_list[-k:]
# test_list2 = numb_list[:- k]
# print(numb_list)
# print(test_list)
# print(test_list2)
# numb_list = test_list + test_list2
# print(numb_list)

# можно через pop - последний элемент убрали
# и вставить через insert в начало



