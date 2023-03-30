# current day  - текущая температура.
# Найти максимальное количество подряд идущих дней с температурой больше 0!

days = int(input("сколько дней?: "))

from random import randint

current_day = randint(-3, 3)
i = 0
max_days_period = 0
local_max = 0
while i < days:
    print(current_day, end=',')
    if current_day > 0:
        local_max += 1
    else:
        if local_max > max_days_period:
            max_days_period = local_max
        local_max = 0
    current_day += randint(-3, 3)
    i += 1
else:
    if local_max > max_days_period:
        max_days_period = local_max

print()
print("max warm days period ", max_days_period)
