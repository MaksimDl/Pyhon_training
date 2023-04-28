# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номером)

import random

numb_list = [random.randint(0, 20) for _ in range(10)]
print(numb_list)

count = 0
for i in range(len(numb_list) - 1):
    if numb_list[i + 1] > numb_list[i]:
        count += 1

print("", count)
