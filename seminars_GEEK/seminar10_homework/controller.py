from classes import Contact, Phonebook
import view
# import model
import text_fields as txt_rus
import text_fields_en as txt_en
txt = txt_rus

def start_pb():
    phonebook = Phonebook('seminars_GEEK\seminar10_homework\phone_book.txt')
    global txt
    while True:
        choice = view.main_menu()
        match choice:
            case 1:  # open file
                phonebook.load_file()
                view.print_info(txt.load_successful)
            case 2:  # save file
                phonebook.save_file()
                view.print_info(txt.save_successful)
            case 3: # show contacts
                pb = phonebook.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4: # add contact
                contact = view.new_search_contact()
                phonebook.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5: # search contact 
                view.print_info(txt.seraching_contact)
                contact = view.new_search_contact()
                matches,pb = phonebook.get_serach_pb(contact)
                view.show_contacts(pb, txt.no_serach_result, matches)
            case 6:  # edit contact
                view.print_info(txt.changing_contact)
                contact = view.new_search_contact()  # object of search strings
                matches,pb = phonebook.get_serach_pb(contact) # fields that mathes serach and result of search
                view.show_contacts(pb, txt.no_serach_result, matches) 
                choice, contact_new_value = view.change_contact() # chose what to edit and new values
                if phonebook.change_contact(pb, contact_new_value, choice): # apply changes
                    view.print_info(txt.change_successful)
                else:
                    view.print_info(txt.change_unsuccessful)
            case 7: # del contact
                view.print_info(txt.deleting_contact)
                contact = view.new_search_contact()
                matches,pb = phonebook.get_serach_pb(contact) # fields that mathes serach and result of search
                view.show_contacts(pb, txt.no_serach_result, matches) 
                choose = view.del_contact() # chose what to edit and new values
                if phonebook.del_contact(pb, choose): # apply changes
                    view.print_info(txt.del_successful)
                else:
                    view.print_info(txt.del_unsuccessful)
            case 8: # russian lang
                txt = txt_rus
            case 9: #english
                #import text_fields_en as txt
                
                txt = txt_en
                pass
            case 10:  # exit
                if phonebook.exit_pb():
                    if view.confirm(txt.is_changed):
                        phonebook.save_file()
                view.print_info(txt.bye_bye)
                exit()