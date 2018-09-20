"""
A todo list
"""
from colorama import init, Fore, Back
init(autoreset=True)

__author__ = 'venkatesh bellale'
__version__ = 0.1
# color for items

Todo = []

print "REMOVE:to remove some item."
print "SHOW:to show the list."
print "exit or quit to leave the program\n"

print("Items in your list {}" .format(len(Todo)))

want_items = str(raw_input("Want to add item: y/n >>"))

if want_items.lower() == 'y':
    while True:

        add_item = str(raw_input(Fore.LIGHTGREEN_EX + "INPUT>>"))

        if add_item == 'remove' or add_item == 'delete':
            remove_item = str(raw_input(Fore.LIGHTRED_EX + "REMOVE>>"))
            Todo.remove(remove_item)
            print("Item now your list {} , {}") .format(len(Todo), Todo)

        elif add_item == 'show':
            print "Your list has {} item as {}" .format(len(Todo), Todo)

        elif add_item == 'quit' or add_item == 'exit':
            print("Number of item in your list {} ") .format(len(Todo))
            for items in Todo:
                print(Fore.YELLOW + '*' + '\t' + "%s"+'\n') % (items)
            quit()

        else:
            Todo.append(add_item)

elif want_items.lower() == 'n':
    print("Enjoy your day !!")

else:
    print("BYE!!")
