phone_book =[]
start_phone_book = []
import controller 
PATH = 'seminars_GEEK\seminar9_homework\phone_book.txt'


def get_pb():
    global phone_book
    return phone_book

def load_file():
    global phone_book, start_phone_book
    if len(phone_book) == 0:  
        with open(PATH, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            phone_book.append({'name': contact[0],
                               'phone': contact[1],
                               'comment': contact[2]})
        start_phone_book  = phone_book.copy()


def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)
    phone_book.clear()

def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)
    

def get_serach_pb(contact: dict):
    global phone_book
    search_result=[]
    matches = set()
    for field in phone_book:
        if  contact['name'].lower() in field['name'].lower():
            #print("debug: name found", field['name'])
            search_result.append(field)
            matches.add(controller.txt.name)
        elif  contact['phone'].lower() in field['phone'].lower():
            #print("debug:phone found", field['phone'])
            search_result.append(field)
            # if "phone" not in matches:
            #     matches.append('phone')
            matches.add(controller.txt.phone)
        elif contact['comment'].lower() in field['comment'].lower():
            #print("debug:comment found", field['comment'])
            search_result.append(field)
            matches.add(controller.txt.comment)
        else:
            pass
            #print('debug:Not found')
    #print("debug: search_result = ", search_result)
    #print("debug: matches ", matches)
    return(matches, search_result)


# pb -> list[dict](search result - several values possible)
# choose - [index-1] of contact to edit
# contact -> dict values to replace in global phonebook
def change_contact(pb, contact_new, choice) -> bool:  
    if len(pb) < choice or choice < 1:
        #print("out of range!")
        return False  # ошибка - out of range
    global phone_book
    contact_old = pb[choice-1]  # dict - which contact to change
    #print("debug: contact old", contact_old)
    #print("debug: contact new", contact_new)
    for n in phone_book:
        if (contact_old['name'] == n['name'] and
             contact_old['phone'] == n['phone'] and
             contact_old['comment'] == n['comment']):   # find the contact in phonebook
            if contact_new['name']: 
                n['name'] = contact_new['name'] 
            if contact_new['phone']:
                n['phone'] = contact_new['phone']
            if contact_new['comment']:   # if not empty (we want to change)
                n['comment'] = contact_new['comment']    # change the contact in phonebook
    #print('result =', phone_book)
    return True


def del_contact(pb, choice) -> bool:
    if len(pb) < choice or choice < 1:
        return False  # ошибка - out of range
    global phone_book
    contact_del = pb[choice-1]  # dict - which contact to del
    for index, n in enumerate(phone_book):
        if (contact_del['name'] == n['name'] and
             contact_del['phone'] == n['phone'] and
             contact_del['comment'] == n['comment']):   # find the contact in phonebook
            phone_book.pop(index)
            break
            
    #print('result =', phone_book)
    return True


def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else: 
        return True


