sp1 = []
sp2 = []
sp3 = []
sp1.append(int(input()))
sp1.append(int(input()))
sp2.append(int(input()))
sp2.append(int(input()))
sp3.append(int(input()))
sp3.append(int(input()))


def check_two(a, b):    # проверка на пересечение 2х (ессли пересекаются- сгорят)
    if a[0] <= b[0] <= a[1]:
        return 1
    elif a[0] <= b[1] <= a[1]:
        return 1
    return 0


def check_fire(s1, s2, s3):     #   Проверка сгорят ли без перестановки
    if check_two(s1, s2) and check_two(s1, s3):
        return 1
    elif check_two(s1, s2) and check_two(s2, s3):
        return 1
    elif check_two(s1, s3) and check_two(s3, s2):
        return 1
    else:
        return 0


def check_replace(m1, m2, m3):  # 1-ю спичку передвигаем (сливаем со 2-й или 3-й - оба варианта рассматриваем)
    len_match = m1[1] - m1[0]
    big1_m2 = m2.copy()
    big2_m2 = m2.copy()
    big1_m3 = m3.copy()
    big2_m3 = m3.copy()
    big1_m2[0] = m2[0] - len_match      # приклеиваем слева ко 2-й
    big2_m2[1] = m2[1] + len_match      # приклеиваем справа ко 2й
    big1_m3[0] = m3[0] - len_match
    big2_m3[1] = m3[1] + len_match

    if check_two(big1_m2, m3):
        return 1        # возврат 1 - значит пересекаются(сгорят) после передвижения спички (m1)
    elif check_two(big2_m2, m3):
        return 1
    elif check_two(big1_m3, m2):
        return 1
    elif check_two(big2_m3, m2):
        return 1
    else:
        return 0


if check_fire(sp1, sp2, sp3):    #  Проверка сгорят ли без перестановки
    print("0")
elif check_replace(sp1, sp2, sp3):  # Проверка сгорят ли если переставить 1-ю спичку
    print("1")
elif check_replace(sp2, sp1, sp3):  # Проверка сгорят ли если переставить 2-ю спичку
    print("2")
elif check_replace(sp3, sp1, sp2):   # Проверка сгорят ли если переставить 3-ю спичку
    print("3")
else:
    print("-1")    #   Если невозможно
