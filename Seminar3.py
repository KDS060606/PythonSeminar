# Как делить строку
# my_string = "Питон самый лучший язык в мире"
# # вариант №1, поделить список по нужному нам знаку
# # my_string = my_string.split(" ") #создает из строки список и делит его по пробелу

# # вариант №2, замена символов в строке
# my_string = my_string.replace(" ", "-")
# my_string = my_string.replace(" ", "-").replace("и", "И") #можно вставлять несколько парметров разделения

# вариант №3, перевод всех слов в нижний|верхний регистр
# my_string = my_string.lower() #перевод в нижний регистр
# my_string = my_string.upper() #перевод в верхний регистр

# проверка с чего начинается строка
# my_string = my_string.startswith("Пит")
# проверка с чего начинается строка
# my_string = my_string.endswith("Пит")

# образка строки
# print(my_string[2:8]) # со 2 символа до 8
# print(my_string[10:]) # с 10 до конца
# print(my_string[:-2]) # 2 последних символа
# print(my_string[::-1]) # перевернуть строку задом на перед

# склеить список
# my_list = ["123", "123", "123", "123"]
# add = "-"
# print(add.join(my_list))

#  создаем пустой словарь и добавляем туда элемент
# my_dict={}
# my_dict[1]= "Один"
# print(my_dict)

# заполняем пустой словарь
# my_dict={}
# n = 5
# for i in range(1, n+1):
#     my_dict[i] = 3*i+1
# print(my_dict)

# выводим значение по ключу из словаря
# my_dict = {1:"123", 2:"123", 3:"123", 4:"123"}
# # print(my_dict.get(3)) # нужно ставить get  для того, чтобы если не будет такого ключа программа не выдавала ошибку
# print(my_dict.get(7, "Такого ключа нет")) # можем поставить в скобках что будет выдаваться если такого ключа нет


# проверяем каждый элемент списка является он цифрой, символом или буковой и добавляем в разные списки
# new_string= "123fjrier39!r39irf9-4hg84fgh"
# leter_list=[]
# num_list=[]
# dot_list=[]

# for char in new_string:
#     if char.isdigit():
#         num_list.append(char)
#     elif char in ["-", "!"]:
#         dot_list.append(char)
#     else: leter_list.append(char)

# print(num_list)
# print(leter_list)
# print(dot_list)

# задача выдернуть из строки числа
# new_equation = "3*x**2 - 12*x + 6 = 0"


# def equation(string: str):
#     eq=[]
#     string = string.replace(" ", "").replace("=0", "").replace("+", " ").replace("-", " -").split(" ")
#     print(string)
#     for item in string:
#         if item.startswith('x'):
#             eq.append(1)
#         elif item.startswith('-x'):
#             eq.append(-1)
#         else:
#             eq.append(int(item.split("*x")[0]))
#     return eq

# print(equation(new_equation))

# a, b, c = equation(new_equation)
# print(a, b, c)


# сделать из строки лист с целыми числами
# s = "1 2 7 4 5 10 15 6 4 6"
# my_list = s.split(" ")
# my_list2 = list(map(int, my_list))

