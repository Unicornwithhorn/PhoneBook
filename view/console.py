from .text import *

def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)

def print_message(message: str):
    length = len(message)
    print('\n' + '='*length)
    print(message)
    print('=' * length + '\n')

def show_contacts(book: list[dict[str, str]]):
    if book:
        print('\n' + '='*67)
        for contact in book:
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            contact.values()
            print(f'{uid:>3}. {name:>20}. {phone:>20}. {comment:>20}')
        print('='*67 + '\n')
    else:
        print_message(book_error)

def input_contact(message: str) -> dict[str, str]:
    print(message)
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите коммент: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def multiresult(result: list[dict[str, str]]):
    print('Были найдены следующие контакты: ')
    for i in range(len(result)):
        print(f"{i+1}) {result[i].get('name')} ({result[i].get('comment')})")
    while True:
        multiresult_choice = input('введите номер интересующего вам контакта или 0 для выхода в главное меню: ')
        if multiresult_choice == '0':
            break
        elif multiresult_choice.isdigit() and 0 < int(multiresult_choice) <= len(result):
            return result[int(multiresult_choice)-1]
        else:
            print_message(input_error_for_find(len(result)))

def find(book: list[dict[str, str]]):
    something_to_find = input('введите искомый контакт: ')
    find_result = []
    for string in book:
        if something_to_find.lower() in string.get('name').lower():
            find_result.append(string)
    if len(find_result) == 0:
        return 'Искомый контакт не найден'
    elif len(find_result) == 1:
         return find_result[0]
    else:
        return multiresult(find_result)

