from view import menu, show_contacts, print_message, input_contact, find, oneresult
import model
from view import text
def start() :
    model.open_file()
    print_message(text.open_successful)
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_successful)
            case 2:
                if model.phone_book != []:
                    print_message(text.saved_successful)
                    model.save_file()
                else:
                    print_message(text.nothing_to_save)
            case 3:
                show_contacts(model.phone_book)
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                print_message(oneresult(find(model.phone_book)))
            case 6:
                model.change(model.phone_book)
            case 7:
                model.delete(model.phone_book)
            case 8:
                break
