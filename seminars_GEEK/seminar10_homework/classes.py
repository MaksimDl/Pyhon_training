import controller


class Contact:
    def __init__(self, name: str, phone: str, comment: str = ''):
        self.name = name
        self.phone = phone
        self.comment = comment

    def edit(self, name: str, phone: str, comment: str):
        self.name = name if name else self.name
        self.phone = phone if phone else self.phone
        self.comment = comment if comment else self.comment

    def cnt_to_str(self):
        return f'{self.name}:{self.phone}:{self.comment}'

    def __str__(self) -> str:
        return f'{self.name:<20} | {self.phone:<20} | {self.comment:<20}'


class Phonebook:
    def __init__(self, path: str):
        self.path = path
        self.phone_book: list[Contact] = []
        self.start_phone_book: list[Contact] = []

    def get_pb(self):
        return self.phone_book

    def load_file(self):
        #  if len(self.phone_book) == 0:    # check  rebuild
        self.phone_book.clear()
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            self.phone_book.append(Contact(contact[0], contact[1], contact[2]))
        self.start_phone_book = self.phone_book.copy()

    def save_file(self):
        data = []
        for contact in self.phone_book:
            data.append(contact.cnt_to_str())
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.start_phone_book = self.phone_book.copy()

    def add_contact(self, new_contact: Contact) -> None:
        self.phone_book.append(new_contact)

    def get_serach_pb(self, contact: Contact) -> list[Contact]:
        search_result = []
        matches = set()
        for field in self.phone_book:
            # add check for empty search string => ignore field (if field = empty - we don't check it)
            # разделение на 3 if -> для того, чтобы отобразить по какому полю совпадение
            # иначе можно было бы вызвать: cnt_to_str(self): и 1 поиск в возращаемой строке
            if contact.name.lower() in field.name.lower():
                # print("debug: name found", field['name'])
                search_result.append(field)
                matches.add(controller.txt.name)
            elif contact.phone.lower() in field.phone.lower():
                # print("debug:phone found", field['phone'])
                search_result.append(field)
                # if "phone" not in matches:
                #     matches.append('phone')
                matches.add(controller.txt.phone)
            elif contact.comment.lower() in field.comment.lower():
                # print("debug:comment found", field['comment'])
                search_result.append(field)
                matches.add(controller.txt.comment)
            else:
                pass
                # print('debug:Not found')
        # print("debug: search_result = ", search_result)
        # print("debug: matches ", matches)
        return (matches, search_result)

    # pb -> list[Contats](search result - several values possible)
    # choose - [index-1] of contact to edit
    # contact -> object Contact values to replace in object phonebook
    def change_contact(self, pb, contact_new, choice) -> bool:
        if len(pb) < choice or choice < 1:
            # print("debug: out of range!")
            return False  # ошибка - out of range
        contact_old = pb[choice-1]  # object Contact - which contact to change

        for index, n in enumerate(self.phone_book):
            if (contact_old.name == n.name and
                contact_old.phone == n.phone and
                    contact_old.comment == n.comment):   # Exact match in class Phonebook
                print("debug: we change to-> ", contact_new.name,
                      contact_new.phone, contact_new.comment)
                self.phone_book[index].edit(
                    contact_new.name, contact_new.phone, contact_new.comment)
        # print('result =', phone_book)
        return True
    # check for correct work = false

    def del_contact(self, pb, choice) -> bool:
        if len(pb) < choice or choice < 1:

            return False  # ошибка - out of range
        contact_del = pb[choice-1]  # class - which contact to del
        for index, n in enumerate(self.phone_book):
            if (contact_del.name == n.name and
                contact_del.phone == n.phone and
                    contact_del.comment == n.comment):   # find the contact match of search to phonebook
                self.phone_book.pop(index)
                break

        # print('result =', phone_book)
        return True

    def exit_pb(self) -> bool:
        # global phone_book, start_phone_book
        if self.phone_book == self.start_phone_book:
            return False
        else:
            return True
        # check
