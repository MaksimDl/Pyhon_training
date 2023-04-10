import controller

def main_menu() -> int:
    print(controller.txt.main_menu)
    
    while True:
        choice = input(controller.txt.choose_menu)
        if choice.isdigit() and 0 < int(choice) < 11:
            return int(choice)
        else:
            print('Ввежите число от 1 до 10')


def print_info(message: str):
    print('\n' + '-'*len(message)) 
    print(message)
    print('-'*len(message) + '\n') 


def show_contacts(book: list[dict], message: str, matches=''):   
    if book:
        if matches:
            print('\n' + '-'*63)
            print(controller.txt.matches_on, ', '.join(map(str, matches)))  # output without brackets, but separated (almost same as*)
            #print(*matches)
        print('\n' + '-'*63)
        for n , contact in enumerate(book,1):
            print(f'{n:>3}. {contact.get("name"):<20}'
                  f' {contact.get("phone"):<20}'
                  f' {contact.get("comment"):<20}')
        print('-'*63 + '\n')
    else:
        print(message)

    

def new_search_contact()-> dict:
    print() 
    name = input(controller.txt.new_name)
    phone = input(controller.txt.new_phone)
    comment = input(controller.txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def change_contact()-> dict:
    print() 
    #choise = int(input(controller.txt.name_to_edit))  # check fo int?
    while True:
        choice = input(controller.txt.name_to_edit)
        if choice.isdigit():
            break
        else:
            print(controller.txt.only_int)

    name = input(controller.txt.new_name)
    phone = input(controller.txt.new_phone)
    comment = input(controller.txt.new_comment)
    print()
    return int(choice), {'name': name, 'phone': phone, 'comment': comment}


def del_contact()-> dict:
    print() 
    #choise = int(input(controller.txt.name_to_edit))  # check fo int?
    while True:
        choice = input(controller.txt.name_to_del)
        if choice.isdigit():
            break
        else:
            print(controller.txt.only_int)
    print()
    return int(choice)
    



def confirm(message: str) -> bool:
    print()
    answer = input(message + 'y/n')
    if answer.lower() == 'y':
        return True
    else:
        return False
    



