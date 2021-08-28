from random import randint
from unit import Unit
from int_checker import int_checker

def hire_list(System):
    menu = []
    while len(menu) < 5:
        new_unit = Unit("", randint(1, 15))
        if new_unit.worth < System.money * 0.85:
            menu.append(new_unit)
    for i in range(len(menu)):
        print(str(i + 1) + ":")
        menu[i].short_description()
    return menu


def hiring_board(System):
    lst = hire_list(System)
    while True:
        print("\nBudget:", str(System.money) + "$")
        choice = input("Which one do you want to hire? Press 0 to exit.\n")
        choice = int_checker(choice)
        if choice == "":
          print("Error, try again.")
        elif choice > len(lst):
          print("The heck are ye talking about, kid?")
          pass
        elif 0 < choice < len(lst) + 1 and lst[choice - 1].calculate_worth() <= System.money:
            choice2 = input("You want " + lst[choice - 1].name + "? (1 for yes, 0 for no)\n")
            choice2 = int_checker(choice2)
            if choice2 == 1:
                break
        elif choice == 0:
            return
        elif lst[choice - 1].calculate_worth() > System.money:
          print("\nSorry,", System.roster[0].name + ". I can't give credit! Come back when you're a little... MMMMMMM... Richer!")
        else:
            print("Error, try again.")
    return lst[choice - 1]
