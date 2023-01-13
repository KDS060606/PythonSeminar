# 4 функции: 
# 1. создать словарь 
# 2. закодировать строки
# 3. раскодировать словарь
# 4. сложить два словаря



# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random


k = int(input("Введите степень k:"))
my_dict1= {}
my_dict2= {}

def fill_dict1():
        
        for i in range(k+1):
                my_dict1[random.randint(1,100)]= i+1
        return my_dict1

def fill_dict2():
        
        for i in range(k+1):
                my_dict2[random.randint(1,100)]= i+1
        return my_dict2

fill_dict1()
fill_dict2()
# print(my_dict1)
# print(my_dict2)

# переворачиваем словарь1
item = list(my_dict1.items())
mydict_reversed1 = {k: v for k, v in reversed(item)}
# print(mydict_reversed1)

# переворачиваем словарь2
item = list(my_dict2.items())
mydict_reversed2 = {k: v for k, v in reversed(item)}
# print(mydict_reversed2)

# конвертируем словарь1 в строку и заменяем символы 
my_str1 = str(mydict_reversed1)
my_str1= my_str1.replace(": ", "x**").replace(", ", "+").replace("xˆ1", "x").replace("+-", "-")
my_str1=my_str1[1:-1:]
print(my_str1)

# конвертируем словарь2 в строку и заменяем символы 
my_str2 = str(mydict_reversed2)
my_str2= my_str2.replace(": ", "x**").replace(", ", "+").replace("xˆ1", "x").replace("+-", "-")
my_str2=my_str2[1:-1:]
print(my_str2)


# записывем 1 многочлен в файл1
my_file1 = open("my_file1.txt", "w")
my_file1.write(my_str1)
my_file1.close()

# записывем 2 многочлен в файл2
my_file2 = open("my_file2.txt", "w")
my_file2.write(my_str2)
my_file2.close()


# достаем многочлены из файла1
with open("my_file1.txt", "r") as f1:
    my_str1 = f1.read()
#     print(my_str1)

# # достаем многочлены из файла2
with open("my_file2.txt", "r") as f2:
    my_str2 = f2.read()
#     print(my_str2)

# разделяем многочлен1 на отдельные элементы
my_str1 = my_str1.replace("x**", " ").replace("+", " ").replace("-", " -")
my_list1 = my_str1.split()
print(my_list1)


# разделяем многочлен1 на отдельные элементы
my_str2 = my_str2.replace("x", " ").replace("*", " ").replace("+", " ").replace("-", " -")
my_list2= my_str2.split()
print(my_list2)

# делаем словарь 1 из списка 1
mylist1_dict={}
for i in range(len(my_list1[::2])): # могу понять почему он у меня не учитывает шаг 2
        mylist1_dict[int(my_list1[i])] = int(my_list1[i+1])
print(mylist1_dict)

print()

mylist2_dict={}
# делаем словарь 2 из списка 2
for i in range(len(my_list2[::2])):  # могу понять почему он у меня не учитывает шаг 2
        mylist2_dict[int(my_list2[i])] = int(my_list2[i+1])
print(mylist2_dict)


final_dict={}
# складываем два словаря  
def Final_Dict(mylist1_dict, mylist2_dict):
        for i in range(len(mylist1_dict)): # сложить два словаря по ключам (число оказалось в ключе) у меня не получилось
                final_dict.keys(mylist1_dict[i] + mylist2_dict[i])
        print(final_dict)
        

Final_Dict(mylist1_dict, mylist2_dict)

