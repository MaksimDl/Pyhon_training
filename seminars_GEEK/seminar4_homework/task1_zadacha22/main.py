# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
size1 = int(input("input ammount of first numbers"))
size2 = int(input("input ammount of first numbers"))

rand_array1 = [random.randint(0, 20) for _ in range(size1)]
rand_array2 = [random.randint(0, 20) for _ in range(size2)]

print("rand generated list1: ",rand_array1)
print("rand generated list2: ",rand_array2)
rand_array1 = set(rand_array1)
rand_array2 = set(rand_array2)
print("only unique numbers in list1",rand_array1)
print("only unique numbers in list1",rand_array2)
result = rand_array1.intersection(rand_array2)
print("intersection of numbers 1 and numbers2(what is in both numbers:)", sorted(result))