from view import print_message, text, find, change_manifistation
phone_book = []
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    phone_book.clear()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})

def save_file():
    rewriting_file = open(path, 'w', encoding='UTF-8')
    for contact in phone_book:
        uid = contact.get('id')
        name = contact.get('name')
        phone = contact.get('phone')
        comment = contact.get('comment')
        space = ' '
        rewriting_file.writelines(f'{space*(3-len(str(uid)))}{uid}:{space*(20-len(name))}{name}:{space*(20-len(phone))}{phone}:{space*(20-len(comment))}{comment}\n')
def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list)+1}

def add_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)

def delete(book):
    point_for_delete = find(book)
    if point_for_delete == 'Искомый контакт не найден':
        print(point_for_delete)
    else:
        name_for_delete = point_for_delete.get('name')
        comment_for_delete = point_for_delete.get('comment')
        answer = input(f'Вы уверены, что хотите удалить контакт <<{name_for_delete} ({comment_for_delete})>>? (да/нет) ')
        if answer.lower() == 'да':
            del phone_book[int(point_for_delete.get('id'))-1]
            record_number = 1
            for record in phone_book:
                record['id'] = str(record_number)
                record_number+=1

            print('Контакт был удалён')
        else:
            print('Контакт не был удалён')

def change(book):
    point_for_change = find(book)
    if point_for_change == 'Искомый контакт не найден':
        print(point_for_change)
    else:
        print(change_manifistation(point_for_change))
        name_question = input(f'Вы хотите изменить имя контакта? (да/нет) ').lower()
        if name_question == 'да':
            point_for_change['name'] = input('Введите новое имя контакта: ')
            print('Имя контакта было изменено')
        else:
            print('Имя контакта не было изменено')
        phone_question = input(f'Вы хотите изменить телефон контакта? (да/нет) ').lower()
        if phone_question == 'да':
            point_for_change['phone'] = input('Введите новый телефон контакта: ')
            print('Номер контакта был изменен')
        else:
            print('Номер контакта не был изменен')
        comment_question = input(f'Вы хотите изменить комментарий к контакту? (да/нет) ').lower()
        if comment_question == 'да':
            point_for_change['comment'] = input('Введите новый комментарий к контакту: ')
            print('Комментарий к контакту был изменен')
        else:
            print('Комментарий к контакту не был изменен')