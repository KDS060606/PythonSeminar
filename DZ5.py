# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# Задача №1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as r
# # задаем колличество конфет и вводим имена игроков
# value = int(input("Введите колличество конфет, которые будут на столе:"))
# name1= input("Введите имя первого игрока:")
# name2= input("Введите имя второго игрока:")

# # жеребьевка
# flag = r(0,2)
# if flag==1: print(f"По результатам жеребьевки первый ход делает {name1}")
# else: print(f"По результатам жеребьевки первый ход делает {name2}")

# # контроль колличества взятых конфет за один ход
# def input_dat(name):
#     x= int(input(f" {name} введите колличество конфет, которое возьмете от 1 до 28:"))
#     while 1< x > 28: print(f" {name} введите колличество конфет от 1 до 28:")
#     return x

# # вывод результатов по итогам хода
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


# # алгоритм игры
# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(name1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(name1, k, counter1, value)
#     else:
#         k = input_dat(name2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(name2, k, counter2, value)

# # печать результатов
# if flag:
#     print(f"Выиграл {name1}")
# else:
#     print(f"Выиграл {name2}")

# Задача №2. Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом




# Инициализация карты
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# # Инициализация победных линий
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# # Вывод карты на экран
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
 
# # Сделать ход в ячейку
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# # Получить текущий результат игры
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 
# # Основная программа
# game_over = False
# player1 = True
 
# while game_over == False:
 
#     # 1. Показываем карту
#     print_maps()
 
#     # 2. Спросим у играющего куда делать ход
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))
 
#     step_maps(step,symbol) # делаем ход в указанную ячейку
#     win = get_result() # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
 
# # Игра окончена. Покажем карту. Объявим победителя.        
# print_maps()
# print("Победил", win)

# Задача №3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

str1 = "aaaaabbbcccc"

def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: 
        return '' 
    for char in data: 
        if char != prev_char: 
            if prev_char: encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding
    


print(rle_encode(str1))