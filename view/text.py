main_menu = '''
    Главное меню
    1.Открыть файл
    2.Сохранить файл
    3.Показать все контакты
    4.Создать новый контакт
    5.Найти контакт
    6.Изменить контакт
    7.Удалить контакт
    8.Выход
    '''

menu_choice = ' Выберете пункт меню '
input_error = 'Некорректный ввод. Введите от одного до восьми'
def input_error_for_find(max_point):
    return f'Некорректный ввод. Введите номер пункта из найденных вариантов (от 1 до {max_point}) или 0 для выхода в главное меню'

book_error = 'Телефонная книга пуста или файл не открыт'

open_successful = 'Телефонная книга успешно открыта'

input_new_contact = 'Введите данные нового контакта'
saved_successful = 'Файл успешно сохранён'
nothing_to_save = 'Вы не внесли в телефонную книгу никаких изменений'
def change_manifistation(point_for_change):
    print(f'Вы выбрали для изменения контакт {point_for_change.get("name")} ({point_for_change.get("comment")})')
def oneresult(result):
    if result == 'Искомый контакт не найден':
        return result
    return 'Был найден контакт {} ({}) телефон: {}'.format(result.get('name'), result.get('comment'), result.get('phone'))

def contact_saved(name: str):
    return f'Контакт {name} успешно сохранён'