# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В
# последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# # *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

size = input("Input size of array(will be randomly generated): ")
end = input("Input max element number: ")
the_num_x = input("Input the number to find(X): ")
if not size.isdigit() or not end.isdigit() or not the_num_x.isdigit():
    print("only natrural number allowed. Please restart")
    exit()
size = int(size)
end = int(end)
the_num_x = int(the_num_x)

rand_array = [random.randint(0, end) for _ in range(size)]
print("rand array:", rand_array)

count_the_num = 0
for i in range(0, size):
    if rand_array[i] == the_num_x:
        count_the_num += 1

print(f'{count_the_num} times we met the number {the_num_x}  ')
