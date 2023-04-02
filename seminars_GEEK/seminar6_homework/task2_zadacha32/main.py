# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
#заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

min = 40
max = 60
size = 20
min_rand = 0
max_rand = 100

array = [random.randint(min_rand,max_rand) for _ in range(size)]

print(array)

for index, i in enumerate(array):
    if max > i > min:
        print (f"array[{index}] = {i} ")
