from os import remove, system, name
import os

FoodMenu = ["ต้มยำกุ้ง", "แกงส้ม", "ต้มข่าไก่", "ขนมจีนน้ำยา", "แกงเขียวหวานไก่", "มัสมั่นไก่", "แพนงหมู", "แกงจืดหมูสับ"]
print(name)
def clear():
    if name == 'nt':
        #os.system('cls')
        _ = system('cls')   # for windows
    else:
        #os.system('clear')
        _ = system('clear') # for mac and linux

def search(name_):
    if name_ in FoodMenu:
        return True
    else :
        return False

def add(name_):
    if name_ in FoodMenu :
        print(f'{name_} is in the Menu before.')
    else :
        FoodMenu.append(name_)
        print(f'add {name_} in the Menu Successful.')

def list_menu():
    count = 1
    print('Menu list :')
    for i in FoodMenu:
        print(f' [{count}] : {i}')
        count+=1
    
def edit(index,name_):
    try:
        FoodMenu[int(index)-1] = name_
        print('edit menu successful')
    except :
        print('Something went wrong try again')

def remove(index):
    try: FoodMenu.pop(index)
    except: print('Out of range')

choice = 1
while True:
    print(FoodMenu)
    print("--- menu ----")
    print(" 0. exit ----")
    print(" 1. search ----")
    print(" 2. add -----")
    print(" 3. edit ----")
    print(" 4. delete ----")

    choice = int(input("Enter your choice : "))
    if choice == 0:
        break

    elif choice == 1:
        search_menu = input("Enter your search menu : ")
        if search(search_menu):
            print(f'{search_menu} is in the Menu')
        else:
            print(f'{search_menu} is not in the Menu')
        
    elif choice == 2:
        add_menu = input("Enter your new menu : ")
        add(add_menu)

    elif choice == 3:
        list_menu()
        edit(input("Enter menu number : "), input("Enter your new menu name : "))

    elif choice == 4:
        list_menu()
        remove_menu = int(input("Enter your menu number to delete : ")) -1
        remove(remove_menu)


    print(FoodMenu)
    input("press enter to next choice..")
    clear()