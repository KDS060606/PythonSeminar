# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# sum = 0

# for i in range(len(my_list)):
#     if i%2!=0:
#         sum=sum+my_list[i]
# print(sum)

# # 2. Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:
# # [2, 3, 4, 5, 6] => [12, 15, 16];
# # [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 4, 5, 6]
# # my_list = [2, 3, 5, 6]
# my_list2=[]

# if len(my_list) %2 != 0: num = int(len(my_list) // 2 +1)
# else: num = int(len(my_list) // 2)
# print(num)


# for i in range(num):
#     my_list2.append(my_list[i]*my_list[len(my_list) - i - 1])
# print(my_list2)


# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# nul=0.0000000

# for i in range(len(my_list)):
#     my_list[i] =  my_list[i] % 1
# print(my_list)


# for i in range(len(my_list)):
#     if 0 in my_list:
#         my_list.remove(0)
# print(my_list)

# sum=min(my_list) * max(my_list)
# print(min(my_list), max(my_list))
# print(sum)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


# num = int(input("Введите натуральное число: "))
# new_num = ""

# while num > 0:
#     new_num = str(num % 2) + new_num
#     num //= 2

# print (new_num)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

num = int(input("Введите размер:"))
my_list=[0, 1]
my_list2=[]


for i in range(num-1):
    my_list.append(my_list[i] + my_list[i+1])
print(my_list)



for i in range(num+1):
    my_list2.append(-(my_list[i]))
my_list2=list(reversed(my_list2))

print(my_list2)

print(my_list2 + my_list)

