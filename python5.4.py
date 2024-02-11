def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."

    return inner

@input_error
def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Give me name and phone please."

@input_error
def show_contact(args, contacts):
    if not args:
        return "\n".join([f"{name}: {contacts[name]}" for name in contacts])
    else:
        name = args[0]
        if name in contacts:
            return f"{name}: {contacts[name]}"
        else:
            return "Contact not found."

@input_error
def delete_contact(args, contacts):
    try:
        name = args[0]
        del contacts[name]
        return "Contact deleted."
    except IndexError:
        return "Enter the name of the contact you want to delete."
    except KeyError:
        return "Contact not found."

contacts = {}

while True:
    command = input("Enter a command: ").split()
    if command[0] == "add":
        print(add_contact(command[1:], contacts))
    elif command[0] == "phone":
        print(show_contact(command[1:], contacts))
    elif command[0] == "delete":
        print(delete_contact(command[1:], contacts))
    elif command[0] == "all":
        print(show_contact([], contacts))
    else:
        print("Invalid command.")
