# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

def check_int(in_string):
    try:
        result = int(in_string)
    except ValueError:
        print("You are supposed to write int number! Shame on you")
        print("Restart the script with correct values!")
        exit()
    return result


m = check_int(input("Input size m of chocolate: "))
n = check_int(input("Input size m of chocolate: "))
k = check_int(input("Input k - num of target pieces: "))

if (k % m == 0 or k % n == 0) and (k <= n * m):
    print("yes")
else:
    print("no")
