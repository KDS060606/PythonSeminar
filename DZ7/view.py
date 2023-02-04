# Телефонный справочник: 


def main_menu():
    commands = ['показать контакты',
                'открыть файл',
                'сохранить файл',
                'добавить новый контакт',
                'изменить контакт',
                'удалить контакт',
                'найти контакт',
                'выйти из программы']
    print('Выберете пункт меню:')

    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню:'))
    return user_input

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пуста или не загружена')

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохранена успешно')

def new_contact():
    name = input('Введите Имя и Фамилию контакта:')
    phone = input('Введите номер телефона контакта:')
    comment = input('Введите комментарий к контакту:')
    return name, phone, comment

def new_contact():
    new = []
    name = input('Введите имя и фамилию контакта:')
    phone = input('Введите номер телефона контакта:')
    comment = input('Введите комментарий к контакту:')
    return name, phone, comment

def find_contact():
    search = input("Введите искомое значение:")
    return search

def delete_contact():
    search = input("Введите контакт который следует удалить:")
    return search

def find_change_contact():
    search = input("Введите контакт который следует изменить:")
    return search

def change_contact():
    change = input("Введите новый номер:")
    return change