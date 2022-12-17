# Задача №1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num =input("Введите число:")
# str_num = num.replace('.', '')
# int_num = int(str_num)
# sum = 0
# print(int_num)

# while int_num != 0:
#     sum = sum + int_num % 10
#     int_num =  int_num // 10

# print(sum)

# Задача №2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n=int(input("Введите колличество чисел в списке:"))
# my_list = [(1 + 1/i)**i for i in range(1, n + 1)]
# res= sum(my_list)
# print("%.2f" % res)

# n=int(input("Введите колличество чисел в списке:"))
# my_list = []
# for i in range(1,n+1):
#     my_list[i]=(1 + 1/i)**i

# print(my_list)


# Задача №3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

# import random
# n = int(input("Введите колличество элементов:"))
# my_list = []
# for i in range(n+1):
#     my_list.append(random.randint(0,100))
# print(my_list)

# p = random.randint(0,n)
# for i in range(n+1):
#      my_list[i], my_list[p] = my_list[p], my_list[i]
# print(my_list)
