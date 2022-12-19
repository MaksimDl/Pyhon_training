#На сковородку одновременно можно положить k котлет. Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно. За какое наименьшее время удастся поджарить с обеих сторон n котлет?
#Формат ввода
#
#Программа получает на вход три числа: k,m,n.
#
#Формат вывода
#Программа должна вывести одно число: наименьшее количество минут.

k, m, n = int(input()), int(input()), int(input())

if (k >= n):
    time = m * 2
else:
    side1_kotl = n
    side2_kotl = n
    time = (side1_kotl // k) * m  # full plates of kotl from one side.

    side2_kotl -= (k - (side1_kotl % k))
    time += m * bool(k - (side1_kotl % k))

    time += (side2_kotl // k) * m
    time += bool((side2_kotl % k)) * m

print(time)
