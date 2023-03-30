# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# # Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.


num = int(input("Сколько всего арбузов"))

from random import randint

min_watermelon = 30000
max_watermelon = 0
if num == 1:
    max_watermelon = randint(500, 30000)
    min_watermelon = 0
elif num == 0:
    min_watermelon = 0
else:
    for i in range(0, num):
        current_watermelon = randint(500, 30000)
        print(current_watermelon, end=' ')

        if current_watermelon > max_watermelon:
            max_watermelon = current_watermelon
        if current_watermelon < min_watermelon:
            min_watermelon = current_watermelon

print()
print("Max weight = ", max_watermelon)
print("Min weight = ", min_watermelon)
