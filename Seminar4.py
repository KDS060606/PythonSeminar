## создать лист и список одной строкой

# my_list = [i for i in range(10)]
# my_dict = {i:i**2 for i in range(10)}

## команда map: сделать из списка строк список целых чисел

# str = "1 2 4 5 6 7 8 9"
# my_list = list(map(int, str.split()))
## или можно применить функцию к каждому элементу списка
# def plus_one(x):
#     return x + "1"
# my_list = list(map(plus_one, str.split()))

# # команда filter: создаем из строки список целых чисел из нечетных
# my_list = list(filter(lambda x: x%2!=0, list(map(int, str.split()))))
# # команда filter: создаем из строки список элементов где есть символ "с" 
# str2 = 'a ab abc bb bcb'
# my_list = list(filter(lambda x: 'c' in x, str2.split()))
# print(my_list)

# # команда enumerate: получаем значение индексов и самих занчений из списка
# str3 = 'a ab abc bb bcb'
# my_list = str3.split()

# for i, item in enumerate(my_list, 1):  # единицу можно не ставить, она нужна для того чтобы начать нумеровать с 1
#     print(i, item)

#  команда zip: соединяем два списка 
# str = [1, 2, 3, 4, 5]
# str2 = 'a ab abc bb bcb'
# new_list = list(zip(str, str2))
# print(new_list[1][0])

# команда lambda: безымянная функция
# func = lambda x, y: x+y
# print(func(3,6))

#Задание №1: удалить "абв" из текста
# origin_text = "Питон самабвый лучший иабвз худабвших язык"
# new_originallist = list(filter(lambda x: not 'абв' in x, origin_text.split()))
# print(new_originallist)

# Задание №2: найти недостающую цифру в файле
# str = '1 2 3 4 6 7 8 9'

# file = open("file.txt", "w")
# file.write(str)
# file.close()

# with open("file.txt", "r") as str:
#     my_str = str.read()

# my_str = list(map(int, my_str.split()))   
# print(my_str)

# my_str2=[]
# for i in range(1, len(my_str)):
#     if my_str[i] - my_str[i-1] != 1: my_str2.append(i+1)
# print(my_str2)

# Создать список из 20 случайных элементов и потом из него создать последовательные списки 

# from random import randint

# my_list = [randint(1, 9) for x in range(20)]
# new_list = []

# for i in range(len(my_list)):
#     curent = my_list[i]
#     sub_list = [curent]
#     for k in range(1, len(my_list)):
#         if curent + 1 == my_list[k]:
#             sub_list.append(my_list[k])
#             curent+=1
#     if len(sub_list) >=2:
#         new_list.append(sub_list)

# print()
# print(new_list)
    