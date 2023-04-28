# Дан список чисел. Определите, сколько в нем встречается различных чисел.
import random

numb_list = [random.randint(0, 20) for _ in range(40)]
print(numb_list)

my_set = set(numb_list)
print(len(my_set))

# my_tuple = (1,2,3,4)
# _, _ , c, _ = my_tuple  - если надо только 3-е значение
