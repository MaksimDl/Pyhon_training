# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

cranes = input("Input total number of cranes: ")

try:
    cranes = int(cranes)
except ValueError:
    print("You are supposed to write int number! Shame on you")
    print("Restart the script with correct values!")
    exit()

if cranes % 6 != 0:
    print("there is no solution in int Numbers!")
else:
    print(int(cranes / 6), int(4 * cranes / 6), int(cranes / 6))
