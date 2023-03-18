# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


try:
    p = float(input("input number P (p=x*y): "))
    s = float(input("input number s (p=x+y): "))
except ValueError:
    print("only number allowed (int or float). restart")
    exit()

dis = s ** 2 - 4 * p
y1 = (s + dis ** 0.5) / 2
y2 = (s - dis ** 0.5) / 2
x1 = s - y1
x2 = s - y2

if dis < 0:
    print('Kate says: "Sorry no solutions, It is impossible"')
elif dis == 0:
    print('Kate says: "One solution possible"', x1, y1)
else:
    print(f'Kate says: "I have to variants:" \n 1) {x1=:.4f}, {y1=:.4f} \n 2) {x2=:.4f}, {y2=:.4f} ')
