# GLOBALS
import os
import re

from collection import Collection
from os import listdir
from os.path import isfile, join
import glob

indent_level = 1
max_len = 40


def greet():
    print("""
    
   _____ _____                                                
  / ____|  __ \                                               
 | |    | |  | |  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
 | |    | |  | | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |____| |__| | | | | | | | (_| | | | | (_| | (_| |  __/ |   
  \_____|_____/  |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                               __/ |          
                                              |___/           
    """)

def create_collection():
    globs = glob.glob('./*.txt')
    global collection

    if len(globs) == 0:
        confirmed = False
        while not confirmed:
            print("Hi there! to get started, please enter the name of your collection: ")
            name = input()
            print("Are you sure you want to create collection with name: " + name + "? (type y to confirm)")
            choice = input()
            if choice.lower() == "y" or choice == "yes":
                collection = Collection(name)
                collection.load()
                confirmed = True
    else:
        print("Found existing collections: ")
        index = 1
        for filename in globs:
            print(f"{index}. " + filename.split('.')[1].replace('\\', ''))
            index += 1
        print(f"{index}. Create new collection")

        print(' ' * indent_level + "Enter the number of the collection you want to load: ")
        choice = input()
        if  int(choice) == len(globs) + 1:
            print("Enter name of new collection: ")
            name = input()
            collection = Collection(name)
            collection.save()
        else:
            if re.match(r"^[0-9]+$", choice) and int(choice) <= len(globs):
                name = globs[int(choice) - 1].split('.')[1].replace('\\', '')
                collection = Collection(name)
                collection.load()
                print(collection)


    


def show_menu():
    print(f"{'=' * max_len}")
    print(f"|{indent_level * ' '}Please select an option:" + f"{' ' * (max_len - indent_level - len('Please select an option:') - 1)}|")
    print(f"| " + (max_len - 2) * ' ' + '|' )
    print(f"|{' ' * indent_level}1. Add new CD" + f"{' ' * (max_len - indent_level - len('Add new CD') - 4)}|")
    print(f"|{' ' * indent_level}2. Remove CD" + f"{' ' * (max_len  - indent_level - len('Remove CD') - 4)}|")
    print(f"|{' ' * indent_level}3. Edit CD" + f"{' ' * (max_len  - indent_level - len('Edit CD') - 4)}|")
    print(f"|{' ' * indent_level}4. List of CDs" + f"{' ' * (max_len  - indent_level - len('List of CDs') - 4)}|")
    print(f"|{' ' * indent_level}5. Find CD" + f"{' ' * (max_len  - indent_level - len('Find CD') - 4)}|")
    print(f"|{' ' * indent_level}6. Settings" + f"{' ' * (max_len  - indent_level - len('Settings') - 4)}|")
    print(f"|{' ' * indent_level}7. Exit" + f"{' ' * (max_len  -  indent_level - len('Exit') - 4)}|")
    print(f"| " + (max_len - 2) * ' ' + '|' )
    print(f"{'=' * max_len}")


def ask_artist():
    while True:
        print("Enter artist name: (letters only)")
        artist = input()
        if re.match(r"^[a-zA-Z ]+$", artist):
            return artist
        else:
            print("Please use letters only")
        if artist == "":
            print("Artist name cannot be empty")

def ask_title():
    while True:
        print("Enter title: (letters only)")
        title = input()
        if re.match(r"^[a-zA-Z ]+$", title):
            return title


def ask_year():
    while True:
        print("Enter year: ")
        year = input()
        if re.match(r"^[0-9]+$", year) and len(year) == 4 and int(year) > 1000:
            return year
        else:
            print("Please use numbers only")

def add_cd():
    artist = ask_artist()
    title = ask_title()
    year = ask_year()
    collection.add(artist, title, year)
    collection.save()


def remove_cd():
    found_cd = general_search()
    if found_cd:
        print("Are you sure you want to remove ", found_cd, "(type y to confirm)")
        choice = input()
        if choice.lower() == "y" or choice == "yes":
            collection.remove(found_cd)
            collection.save()

def edit_cd(cd = None):
    if cd is None:
        found_cd = general_search()

    else:
        found_cd = cd
    if found_cd:
        print("Are you sure you want to edit ", found_cd, "(type y to confirm)")
        choice = input()
        if choice.lower() == "y" or choice == "yes":
            arist, title, year = ask_artist(), ask_title(), ask_year()
            collection.edit(found_cd, arist, title, year)
            collection.save()
            

def list_cd():
    collection.print_all()


def general_search():
    print("Enter arist name, title or year: ")
    search_term = input()
    search_results = collection.general_search(search_term)
    if len(search_results) == 0:
        print("No results found")
        return

    selected_cd = False
    while not selected_cd:
        print("Found the following CD's: ")
        
        index = 1
        for cd in search_results:
            print(f"{index}. {cd}")
            index += 1
        print("Enter the number of the CD you want to see more information about: ")
        choice = input()
        if re.match(r"^[0-9]+$", choice) and int(choice) <= len(search_results):
            print(search_results[int(choice) - 1])
            selected_cd = search_results[int(choice) - 1]
        else:
            print("Please select a number between 1 and ", len(search_results))
    return selected_cd
def find_cd():
    selected_cd = general_search()
    
    print("What do you want to do with " + str(selected_cd) + "?")
    print("1. Edit")
    print("2. Remove")
    choice = input()
    if choice == "1":
        edit_cd(selected_cd)
    

def settings():
    print("Settings")
    print("1. Change line length")
    print("2. Change indent level")
    print("3. Change collection name")
    print("4. Exit")
    choice = input()
    if choice == "1":
        global max_len
        max_len = int(input("Enter new line length: "))
    elif choice == "2":
        global indent_level
        indent_level = int(input("Enter new indent level: "))
    elif choice == "3":
        old_name = collection.name
        new_name = input("Enter new collection name: ")
        collection.name = new_name
        collection.save()
        for filename in glob.glob(f"*{old_name}.txt"):
            os.remove(filename)


    elif choice == "4":
        return
    


def start_main_script():
    choice = 0
    greet()
    create_collection()
    while choice != 6:
        show_menu()
        print()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_cd()
        elif choice == "2":
            remove_cd()
        elif choice == "3":
            edit_cd()
        elif choice == "4":
            list_cd()
        elif choice == "5":
            find_cd()
        elif choice == "6":
            settings()
        elif choice == "7":
            exit()

if __name__ == "__main__":
    start_main_script()

