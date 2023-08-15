import re

CONTACTS = dict()


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me correct name and phone please ..."
    return wrap


def parser_command(command):
    pattern_add_conact = r'^[aAdD]{3}\s{1}'
    if re.findall(pattern_add_conact, command):
        x = [x.lower() for x in command.split(' ') if x.lower() != 'add']
        return handler_add_contact(x)

    elif command.lower() == 'show all':
        print(f'CONTACTS -> {CONTACTS}')
        return handler_show_all_contacts()

    else:
        return f'Incorrect command "{command}"'


@input_error
def handler_add_contact(contact: str):
    print(f'contact -> {contact}')
    CONTACTS[contact[0].title()] = contact[1]
    return f'Contact with name {contact[0].title()} and number {contact[1]} has been added'


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
