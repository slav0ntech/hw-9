import re

CONTACTS = dict()


def handler_add_contact(contact: str):
    list_item_add_remove = [x for x in contact.split(' ') if x != 'add']
    CONTACTS[list_item_add_remove[0]] = list_item_add_remove[1]


def handler_change_contact(contact):
    dict_result = {}
    list_item_change_remove = [x for x in contact.split(' ') if x != 'change']
    dict_result[list_item_change_remove[0]] = list_item_change_remove[1]
    for key in CONTACTS.keys():
        if key in dict_result:
            CONTACTS[key] = dict_result[key]


def handler_get_contact(contact):
    str_item_phone_remove = contact.replace('phone', '').strip()
    if str_item_phone_remove in CONTACTS:
        print(CONTACTS.get(str_item_phone_remove))


def handler_show_all_contacts():
    print(f'{CONTACTS}')


def main():
    pattern_add_conact = r'^[add]{3}\s{1}'
    pattern_change_conact = r'^[change]{6}\s{1}'
    pattern_get_contact = r'[phone]{5}\s{1}'

    while True:
        result = input("waiting command -> ...\n")
        if result.lower() in ("good bye", "close", "exit"):
            print(f'Good bye!')
            break

        elif result.lower() == "hello":
            print(f"How can I help you?")

        elif re.findall(pattern_add_conact, result):
            handler_add_contact(result)

        elif re.findall(pattern_change_conact, result):
            handler_change_contact(result)

        elif re.findall(pattern_get_contact, result):
            handler_get_contact(result)

        elif result.lower() == "show all":
            handler_show_all_contacts()


if __name__ == "__main__":
    main()
