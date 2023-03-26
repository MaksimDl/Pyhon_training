# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста 
# есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
#  число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит
#  из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
#  находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух 
# соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
bush_ammount = 20
min_berries = 0
max_berries = 20
import random

harvest = [random.randint(min_berries, max_berries) for _ in range(bush_ammount)]
print(harvest)


max = harvest[len(harvest)-1] + harvest[len(harvest)-2] + harvest[0]  # last element
max_index = len(harvest) -1 
for i in range(0,len(harvest)-1):
     local_max = harvest[i-1] + harvest[i] + harvest[i+1]
     #print(f"i = {i}, local max = {local_max}")
     if local_max > max:
        max = local_max
        max_index = i

print(f"Max harvested {max} will be near bush num {max_index+1} (count from 1) ")