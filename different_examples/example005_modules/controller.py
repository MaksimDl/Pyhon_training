import view
import model

def start():
    while True:
        view.show_menu()
        menu_choice = view.choice_menu()
        match menu_choice:
            case 1:
                model.open_file()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pb = model.get_phone_book()
                view.show_contacts(pb)
            case 5:
                pass

