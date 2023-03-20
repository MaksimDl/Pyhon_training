import text_fields

def show_menu() -> None:
    print(text_fields.main_menu)


def choice_menu() -> int:
    menu_length = len(text_fields.main_menu.split('\n'))-1
    while True:
        number = input('Choose menu number: ')
        if number.isdigit() and 0 < int(number) <= menu_length:
            return int(number)
        print(f"input number 1 -{menu_length}  :")

def show_contacts(phone_book: list[dict]):
    if not phone_book:
        print("phone book is empty or not opened")
        return False
    for index, contact in enumerate(phone_book,1):
            print(f"{index}.{contact.get('name'):.<20}"
                  f"{contact.get('phone'):.<20}"
                  f"{contact.get('comment'):<20}")
              

