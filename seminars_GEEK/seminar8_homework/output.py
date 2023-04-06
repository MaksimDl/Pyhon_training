import global_vars
from os import system, name  

menu = ['1. Открыть файл. ',
        '2. Сохранить файл. ',
        '3. Посмотреть контакты. ',
        '4. Создать контакт. ',
        '5. Найти контакт. ',
        '6. Изменить контакт. ',
        '7. Удалить контакт. ',
        '8. Выход. ',
        '9. Main menu']

def show_menu() -> None:
    for index, line in enumerate(menu):
        print(line + global_vars.menu_modifiers[index]) 


def clear() -> None:   # clears the console
    # for windows  
    if name == 'nt':  
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')  
    else:   # haven't checked for correct work 
        _ = system('clear') 
