# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random

try:
    num_coins = int(input("input number of coins(n): "))
except ValueError:
    print("You are supposed to input only int number>0")
    exit()
if num_coins < 0:
    print("You are supposed to input only int number>0")
    exit()

coins_array = [random.randint(0, 1) for _ in range(num_coins)]
# 1 - means ODD coin size, 0 - means EVEN coin size

print(coins_array)

count_zeros = 0
for i in range(0, num_coins):
    if coins_array[i] == 0:
        count_zeros += 1

if count_zeros >= num_coins - count_zeros:
    print("minimum coins to rotate for all to be same size is: ", num_coins - count_zeros)
else:
    print("minimum coins to rotate for all to be same size is: ", count_zeros)

