import view
import model
import text_fields as txt_rus
import text_fields_en as txt_en
txt = txt_rus

def start_pb():
    global txt
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
            case 2:
                model.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_search_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5: # search contact
                view.print_info(txt.seraching_contact)
                contact = view.new_search_contact()
                matches,pb = model.get_serach_pb(contact)
                view.show_contacts(pb, txt.no_serach_result, matches)
            case 6:  # edit contact
                view.print_info(txt.changing_contact)
                contact = view.new_search_contact()  # dict of search strings
                matches,pb = model.get_serach_pb(contact) # fields that mathes serach and result of search
                view.show_contacts(pb, txt.no_serach_result, matches) 
                choose, contact_new_value = view.change_contact() # chose what to edit and new values
                if model.change_contact(pb, contact_new_value, choose): # apply changes
                    view.print_info(txt.change_successful)
                else:
                    view.print_info(txt.change_unsuccessful)
            case 7:
                view.print_info(txt.deleting_contact)
                contact = view.new_search_contact()
                matches,pb = model.get_serach_pb(contact) # fields that mathes serach and result of search
                view.show_contacts(pb, txt.no_serach_result, matches) 
                choose = view.del_contact() # chose what to edit and new values
                if model.del_contact(pb, choose): # apply changes
                    view.print_info(txt.del_successful)
                else:
                    view.print_info(txt.del_unsuccessful)
            case 8: # russian lang
                txt = txt_rus
            case 9: #english
                #import text_fields_en as txt
                
                txt = txt_en
                pass
            case 10:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                view.print_info(txt.bye_bye)
                exit()