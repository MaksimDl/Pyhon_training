# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его 
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то 
# они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух 
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
# “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def count_vowels(in_phare) -> int:
    result = 0
    for char in in_phare:
        if char.lower() in vowels:
            result += 1
    #print(f"in phares {in_phare} there are {result} vowels")
    return result

vowels = "уеыаоэяиюё"
in_string = input("Введите фразу: ").split()
# print(in_string)
vowels_base = count_vowels(in_string[0]) # vowels in first pharse to compare others
vowels_local = 0 # vowels in current pharse
rythm = True
for index in range (1, len(in_string)):
    if count_vowels(in_string[index]) != vowels_base:
        rythm = False
        break
    
if rythm:
    print("Парам пам-пам (good rythm)")
else:
    print("Пам парам (no rytm)")
    

