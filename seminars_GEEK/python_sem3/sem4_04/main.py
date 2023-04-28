import random

my_list = [random.randint(0,10): str(i) for i in range(20)] 
print(my_list)

# for i in my_list.keys():   # пробегаем по ключам
for i in my_list.values():   # пробегаем по данным
    print(my_list.get(i))

for i, k in my_list.items():   # items -  пробегаем по кортежу
    print(f'Ключ......',i,k)   # проверить
    

# #2)  посчитать сколько раз встречается  элемент
# import random
# my_list = [random.randint(0,10) for _ in range(20)] 

# print(my_list)

# count_dic = {}

# for item in my_list:
#     count_dic[item] = count_dic.get(item, 0) + 1
# # если 

# print(count_dic)



# 1) my_dict = {1:"one", 2:"two", 3:"three"}

# # print(my_dict[0])  # лучше так не делать
# print(my_dict.get(4,"нет такого ключа"))  # вместо


# my_dict[4] = "four"  # но если 4 ключ есть - то перезапишет
# my_dict.setdefault(3, "четыре")  # если ключ 3 есть, - то не запишетб иначе запишет


# print (my_dict)

