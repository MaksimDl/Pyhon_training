# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и 
#возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
import recurs_methods as from_module


if __name__ == "__main__":
    a = 2
    b = 10
    print(f"{a} to the power of {b} is {from_module.power(a,b)}")
