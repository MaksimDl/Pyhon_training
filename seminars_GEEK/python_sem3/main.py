# Дана упорядоченная последовательность an чисел от 1 до N. Из копии данной последовательности bn удалили
#  одно число, а оставшиеся перемешали. Найти удаленное число.
import random


n = int(input("Введите длинну последовательности "))

numb_list = []
for i in range (n+1):
    numb_list.append(i)

print(numb_list)
set_etalon = set(numb_list)
numb_list.pop(int(input("Какой элемент удалить? ")))
print(numb_list)

random.shuffle(numb_list)

print(numb_list)

set1 = set(numb_list)

print(set1)

print (set_etalon.difference(set1))


