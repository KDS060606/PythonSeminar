phone_book = []
path = 'phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))
    

def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))
        
def search_contact(search: str):
    global phone_book
    search_resault = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_resault.append(line)
                break
    return search_resault

def delete_contact(search: str):
    global phone_book
    for line in phone_book:
        for field in line:
            if search in field:
                phone_book.remove(line)
                print(f"{search} удален из телефонного справочника")
                break

def change_contact(search: str, change: str):
    global phone_book
    for line in phone_book:
        for field in range(len(line)):
            if line[field] == search:
                line[1]= change
                print(f"Контакт: {search} изменен на: {change}")
                break