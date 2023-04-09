import output
import global_vars
import files
import time

def out_red(text=''):
     print(f"\033[31m {text} ", end = '')
     print("\033[0m", end = '')
     return ''
   

def sleep_message(message, sleep_time=1):
    output.clear()
    print()
    print(message)
    time.sleep(sleep_time)


def show_contacts(per_page = 5):
    output.clear()
    page = 0 # divede by pages?
    #if len(global_vars.base) > per_page:
    for key , value in global_vars.base.items():
        out_red(key)    
        print(*value)

def create_contact():
    list_keys = list(global_vars.base.keys())
    new_key = str(int(list_keys[len(list_keys)-1]) + 1)
    #print("list = ", list_keys)
    line = input('Введите разделяя ФИО, Телефон, комментарий  раздяляя ";": ').split(';')
    if len(line) !=3: 
        print("ошибка воода: введите 3 начения через ';' ") 
        return False
    else:
        global_vars.base[new_key] = line[0], line[1], line[2]
        return True
    #print(global_vars.base)


def find_contact():
    search_string = input("Введите данные для поиска: ").lower()
    found = 0
    for key, value in global_vars.base.items():
        #print(global_vars.base.values())
        #print(value[0], value[1], value[2])
        if search_string in value[0].lower():
            print("Совпадение по имени:", end = '')
            out_red(key)
            print(value)
            # print(f"Совпадение по имени:{out_red(key)}")  - печатает сначала выполнение функции =((
            
            found += 1
        elif search_string in value[1].lower():
            print("Совпадение по телефону:", end = '')
            out_red(key)
            print(value)
            found += 1
        elif search_string in value[2].lower():
            print("Совпадение по комментарию:", end = '')
            out_red(key)
            print(value)
            found += 1
    print()
    print(f"найдено {found} свопадений ")
    print("Введите 9, чтобы вернуться в главное меню ")

def change_contact():
    num = input("ВВедите номер для редактирования: ")
    if num in global_vars.base:
        line = input(f"ВВедите новые данные вместо контакта N{num}, разделяя';' : ").split(';')
        if len(line)!=3:
            sleep_message("incorrect input format! - 3 separated string expected")    
        else:
            global_vars.base[num] = line[0],line[1],line[2]
    else:
        sleep_message("input key not found!")
        return False
    return True

def del_contact():
    num = input("ВВедите номер для удаления: ")
    if num in global_vars.base:
        global_vars.base.pop(num)
        return True
    else: 
        sleep_message("input key not found! ")
        return False
        


def start():
    output.show_menu()
    while global_vars.loop:
        print()
        menu_choise =int(input("Выберите пункт меню: "))
        match menu_choise:
            case 1:  # open file and store to memory
                if (files.open_file()):
                    global_vars.menu_modifiers[0] = ' -> файл('+ global_vars.path +') открыт'
                    sleep_message("файл открыт")
                else:
                    sleep_message("Ошибка открытия файла")
                output.show_menu()
            case 2:   # save to file
                if(len(global_vars.base)==0):
                    sleep_message("файл базы не открыт")
                    print()
                elif (files.save_file()):
                    sleep_message("saving file")
                    global_vars.menu_modifiers[0] = ''  # remove sign that file is opened
                else:
                    print("ошибка открытия файла для записи")
                output.show_menu()
               
            case 3:  # show contacts
                if(len(global_vars.base)==0):
                    sleep_message("файл базы не открыт")
                else: 
                    sleep_message("Show all contacts!")
                    show_contacts(10)
                    print("press 9 to go back to main menu")
            case 4:
                output.clear()    
                if(len(global_vars.base)==0):
                    sleep_message("файл базы не открыт")
                elif (create_contact()):
                    sleep_message("Contact created")
                else:
                    sleep_message("Error! Can't create contact")
                output.show_menu()
            case 5:
                if(len(global_vars.base)==0):
                    sleep_message("файл базы не открыт")
                    print("Введите 9, чтобы вернуться в главное меню")
                else:
                    output.clear()   
                    find_contact()
                    
            case 6:
                if(len(global_vars.base)==0):
                    sleep_message("файл базы не открыт")
                    print("Введите 9, чтобы вернуться в главное меню")
                else: 
                    output.clear()   
                    change_contact()
                    output.show_menu()
            case 7:
                if(len(global_vars.base)==0):
                    sleep_message("файл базы не открыт")
                    print("Введите 9, чтобы вернуться в главное меню")
                else:
                    output.clear()   
                    if del_contact():
                        sleep_message("deleted")
                    else:
                        sleep_message("Error in deleting")
                    output.show_menu()
            case 8:
                if(len(global_vars.base)!=0):
                    sleep_message("You didn't save the base")
                    exit_progr = input("Exit without saving? (y, n): ")
                    if exit_progr == 'y':
                        output.clear()
                        sleep_message("Now exiting! Good bye!")
                        global_vars.loop = False
                    else:
                        output.show_menu()
                        output.show_menu()
                        
                else:
                    output.clear()
                    sleep_message("Now exiting! Good bye!")
                    global_vars.loop = False
            case 9:
                sleep_message("go back to main menu")
                output.clear()
                output.show_menu()



