# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

first_class = int(input("Введите количество учеников первого класса "))
second_class = int(input("Введите количество учеников первого класса "))
third_class = int(input("Введите количество учеников первого класса "))

num_desks = first_class // 2 + first_class % 2 + second_class //\
            2 + second_class % 2 + third_class // 2 + third_class % 2

print("Минимальное количество парт требуется: ", num_desks)

sum = 0
for i in range(0, 10):
    sum += i