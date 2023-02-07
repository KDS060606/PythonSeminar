


# path = r'file.txt'
# data = "Новый текст в этом файле"

# with open(path, 'r', encoding='UTF-8') as file: # чтобы записать в файл ставим "w", чтобы считать ставим "r"
#     new_file = file.readlines()
# #     new_file = file.write(data) # записать в файл 
# #     new_file = file.read() # считать весь документ
# #     new_file = file.readline() # считать первую строку документа
# #     new_file = file.readlines() # считать все строки документа и вывести их как список
# #     # символ \n - означает переход на следущую строку

    
# for i in range(len(new_file)):
#     new_file[i] = new_file[i] # переводим в строку
#     print(new_file[i].strip()) # если переводит в строку то strip отрезает все пропуски и проблелы
#     new_file[i] = int(new_file[i]) # переводим в целые числа
#     print(new_file[i])

# #  Задача: убрать повторяющийся элемент
# my_list =[1, 2, 3, 5, 1, 5, 3, 10]
# my_list = list(filter(lambda x: my_list.count(x) ==1, my_list)) # проверяем если наш элемент повторяется больше одного раза (каунт вхождение больше 1), то записываем в новый списко
# print(my_list)

my_str = '2-2*2/2+2/2'

my_str = my_str.replace("*", " * ").replace("+", " + ").replace("-", " - ").replace("/", " / ")
my_str = my_str.split()
print(my_str)

while len(my_str) > 1:
    i=0
    while '*' in my_str or '/' in my_str:
        if my_str[i] =='*': 
            my_str[i-1] = int(my_str[i-1]) * int(my_str[i+1])
            my_str.pop(i)
            my_str.pop(i)
        elif my_str[i] =='/': 
            my_str[i-1] = int(my_str[i-1]) // int(my_str[i+1])
            my_str.pop(i)
            my_str.pop(i)
        else:
            i+=1
    i=0
    while '+' in my_str or '-' in my_str:
        if my_str[i] =='+': 
            my_str[i-1] = int(my_str[i-1]) + int(my_str[i+1])
            my_str.pop(i)
            my_str.pop(i)
        elif my_str[i] =='-': 
            my_str[i-1] = int(my_str[i-1]) - int(my_str[i+1])
            my_str.pop(i)
            my_str.pop(i)
        else:
            i+=1
print(my_str)




