import re

CONTACTS = dict()  # {'name': 'tel number'}


def handler_add_contact():
    pass


def handler_change_contact():
    pass


def handler_get_contact():
    pass


def handler_show_all_contacts():
    pass


def main():
    pattern_add_conact = r'^[add]{3}\s{1}'
    pattern_change_conact = r'^[change]{6}\s{1}'

    while True:
        result = input("Hi, what the command\n")
        if result.lower() in ("good bye", "close", "exit"):
            print(f'Good bye!')
            break

        elif result in ("hello"):
            print(f"How can I help you?")

        elif re.findall(pattern_add_conact, result):
            print('OK')


# def save_contacts(contacts: str):
if __name__ == "__main__":
    main()
