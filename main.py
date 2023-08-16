import re

CONTACTS = dict()


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me correct name and phone please ..."
        except KeyError:
            return "Enter correct user name please ..."
    return wrap


def parser_command(command):
    pattern_add_conact = r'^[aAdD]{3}\s{1}'
    pattern_change_conact = r'^[cChHaAnNgGeE]{6}\s{1}'
    pattern_get_contact = r'[PpHhOoNnEe]{5}\s{1}'

    if re.findall(pattern_add_conact, command):
        x = [x.lower() for x in command.split(' ') if x.lower() != 'add']
        return handler_add_contact(x)

    elif re.findall(pattern_change_conact, command):
        x = [x.lower() for x in command.split(' ') if x.lower() != 'change']
        return handler_change_contact(x)

    elif re.findall(pattern_get_contact, command):
        x = [x.lower() for x in command.split(' ') if x.lower() != 'phone']
        return handler_get_contact(x)

    elif command.lower() == 'show all':
        return handler_show_all_contacts()

    else:
        return f'Incorrect command "{command}"'


@input_error
def handler_add_contact(contact: str):
    CONTACTS[contact[0].title()] = contact[1]
    return f'Contact with name {contact[0].title()} and number {contact[1]} has been added'


@input_error
def handler_change_contact(contact: str):
    dict_result = {}
    dict_result[contact[0]] = contact[1]
    for key in CONTACTS.keys():
        if key.lower() in dict_result:
            CONTACTS[key] = dict_result[key.lower()]
            return f'Contact with name {contact[0].title()} and number {contact[1]} has been changed'


@input_error
def handler_get_contact(contact: str):
    return CONTACTS[contact[0].title()]


def handler_show_all_contacts():
    return CONTACTS


def main():
    while True:
        result = input("waiting command -> ...\n")
        if result.lower() in ("good bye", "close", "exit"):
            print(f'Good bye!')
            break
        elif not result:
            continue

        else:
            print(parser_command(result))


if __name__ == "__main__":
    main()
