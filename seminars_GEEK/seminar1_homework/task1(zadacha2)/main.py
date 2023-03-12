# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input("Input 3 digit number")

try:
    number = int(number)
except ValueError:
    print("You are supposed to write int number! Shame on you")
    print("Restart the script with correct values!")
    exit()

number = abs(number)  # it doesn't  matter for us positive or negative number

if 99 < number < 1000:
    digs = [0, 0, 0]
    digs[0] = number // 100
    digs[1] = (number - digs[0] * 100) // 10
    digs[2] = number % 10
    # print(digs[0] + digs[1] + digs[2], "()")
    print(f'{digs[0] + digs[1] + digs[2]} ({digs[0]} + {digs[1]} + {digs[2]})')

else:
    print("You are supposed to inter 3dig number. Restart with correct number")
    exit()
