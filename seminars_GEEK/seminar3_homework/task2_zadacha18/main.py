# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
import math

size = input("Input size of array(will be randomly generated): ")
begin = input("Input min element number: ")
end = input("Input max element number: ")
the_num_x = input("Input the number to find(X): ")

if not size.isdigit():
    print("only natrural number allowed. Please restart")
    exit()
size = int(size)

try:
    begin = int(begin)
    end = int(end)
    the_num_x = int(the_num_x)
except ValueError:
    print("int numbers are supposed to be input")
    exit()


rand_array = [random.randint(begin, end) for _ in range(size)]
print("rand array:", rand_array)

if size == 0:
    print("impossible to determine, because array size is 0!")
    exit()

nearest = rand_array[0]
for i in range(1, size):
    if abs(the_num_x - rand_array[i]) < abs(the_num_x - nearest):
        nearest  = rand_array[i]

print("the neares number is", nearest)
