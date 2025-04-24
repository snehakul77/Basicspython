#WAP to load a json file with birthday calendar and add a new entry to json file

import json
import sys

birthday = {}
with open('birthdays.json', 'r') as f:
    birthday = json.load(f)

def add_birthday():
    name = input("Who\'s birthday do you wnat to add to calendar?\n").title()
    date = input("When is {} born?\n".format(name))
    birthday[name] = date
    print(birthday[name])
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print("{} was added to birthday calendar.".format(name))

def find_birthday():
    name = input("Who's birthday do you wnat to know?\n").title()
    try:
        if birthday[name]:
            print("{} is born on {}\n".format(name, birthday[name]))
    except KeyError:
        print("{} is not in the list of birthdays\n".format(name))

def list_entries():
    print("The current entries in the list are \n")
    for key in birthday:
        print(key , ':', birthday[key])
    print("\n")

while True:
    whats_next = input("What do you want to do next? you can : Add , Find , List or Quit\n").capitalize()
    if whats_next == 'Quit':
        print('Thank you and Good bye')
        raise sys.exit(0)
    elif whats_next == 'Add':
        add_birthday()
    elif whats_next == 'Find':
        find_birthday()
    elif whats_next == 'List':
        list_entries()