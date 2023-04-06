import output
import global_vars
import files
import time

def sleep_message(message, sleep_time=1):
    output.clear()
    print()
    print(message)
    time.sleep(sleep_time)


def show_contacts(per_page = 5):
    page = 0 # divede by pages?
    #if len(global_vars.base) > per_page:
    for key , value in global_vars.base.items():
        print("show: ", key, *value)

def create_contact():
    list_keys = list(global_vars.base.keys())
    new_key = str(int(list_keys[len(list_keys)-1]) + 1)
    #print("list = ", list_keys)
    line = input('Введите разделяя ФИО, Телефон, комментарий  раздяляя ";": ').split(';')
    global_vars.base[new_key] = line[0], line[1], line[2]
    #print(global_vars.base)


def find_contact():
    search_string = input("Введите данные для поиска: ").lower()
    for key, value in global_vars.base.items():
        #print(global_vars.base.values())
        #print(value[0], value[1], value[2])
        if search_string in value[0].lower():
            print("Совпадение по имени:", key, value)
        elif search_string in value[1].lower():
            print("Совпадение по телефону:", key, value)
        elif search_string in value[2].lower():
            print("Совпадение по комментарию:", key, value)

def change_contact():
    num = input("ВВедите номер для редактирования")
    line = input(f"ВВедите новые данные вместо контакта N{num}, разделяя';' : ").split(';')
    global_vars.base[num] = line[0],line[1],line[2]
    # print(global_vars.base)

def del_contact():
    num = input("ВВедите номер для удаления")
    global_vars.base.pop(num)
    print(global_vars.base)


def start():
    output.show_menu()
    while global_vars.loop:
        print()
        menu_choise =int(input("Выберите пункт меню: "))
        match menu_choise:
            case 1:
                sleep_message("файл открыт")
                output.clear()
                global_vars.menu_modifiers[0] = ' -> файл('+ global_vars.path +') открыт'
                output.show_menu()
                files.open_file()
            case 2:
                sleep_message("saving file")
                output.clear()
                global_vars.menu_modifiers[0] = ''  # remove sign that file is opened
                output.show_menu()
                files.save_file()
            case 3:
                sleep_message("Show all contacts!")
                output.clear()
                show_contacts(10)
            case 4:
                output.clear()    
                create_contact()
                sleep_message("Contact created")
                output.clear()
                output.show_menu()
            case 5:
                output.clear()   
                find_contact()
                output.show_menu()
            case 6:
                output.clear()   
                change_contact()
                output.show_menu()
            case 7:
                output.clear()   
                del_contact()
                sleep_message("deleted")
                output.show_menu()
            case 8:
                output.clear()
                sleep_message("Now exiting! Good bue!")
                global_vars.loop = False
            case 9:
                sleep_message("go back to main menu")
                output.clear()
                output.show_menu()



