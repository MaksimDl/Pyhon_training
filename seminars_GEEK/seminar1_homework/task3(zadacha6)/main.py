# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с
# номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


ticket = input("Input ticket number: ")

half = int(len(ticket) / 2) - 1
left_part = ticket[:half + 1]
right_part = ticket[len(ticket) - half - 1:]
# print(half)
# print(left_part)
# print(right_part)
# print(len(right_part))

if len(ticket) != 6:
    print(
        "it isn't the same as we were suggested to solve in task (6 dig_number, but we solved for all positive numbers")

try:
    ticket = int(ticket)
except ValueError:
    print("You are supposed to write int number! Shame on you")
    print("Restart the script with correct values!")
    exit()

summ = 0
for i in range(0, len(right_part)):
    summ += int(right_part[i]) - int(left_part[i])

print()
if summ == 0:
    print("yes, lucky number")
else:
    print("no, not lucky")
