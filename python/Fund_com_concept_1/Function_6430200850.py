### Github: https://github.com/PKGzGMTH
### Medium: https://peakungg.medium.com/
### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

from os import system, name

#1
FoodPrice = {
    'ต้มยำกุ้ง' : 90,
    'แกงส้ม' : 60,
    'ต้มข่าไก่' : 60,
    'ขนมจีนน้ำยา' : 40,
    'แกงเขียวหวานไก่' : 40,
    'มัสหมั่นไก่' : 50,
    'แพนงหมู' : 40,
    'แกงจืดหมูสับ' : 30}

def clear():
    if name == 'nt':
        #os.system('cls')
        _ = system('cls')   # for windows
    else:
        #os.system('clear')
        _ = system('clear') # for mac and linux

def list_Menu():
    count = 1
    print('---- Selecte Menu ----')
    for i,j in FoodPrice.items():
        print(f' [{count}] : {i} : Price {j}')
        count += 1

#2
def search(name):
    if name in FoodPrice.keys() :
        return 1
    else :
        return 0

#3
def add(name, price:int):
    if name not in FoodPrice.keys():
        FoodPrice.update({name:price})
        print('Add new Menu Successful.')
    else:
        print(f'{name} is in the Menu, You can try to edit Menu.')
    print_total()

#4
def edit(num:int, name, price:int):
    num -= 1
    if 0 <= num <= len(FoodPrice) -1:
        old_name = list(FoodPrice.keys())[num]
        FoodPrice.pop(old_name)
        FoodPrice.update({name:price})
        print('Edit Menu Successful.')
    else :
        print('number is Out of range, Please Try again.')
    print_total()

#5
def remove(num:int):
    num -= 1
    if 0 <= num <= len(FoodPrice) -1:
        old_name = list(FoodPrice.keys())[num]
        FoodPrice.pop(old_name)
        print('Remove Menu Successful.')
    else :
        print('number is Out of range, Please Try again.')
    print_total()

def print_total():
    print(f'total {len(FoodPrice)} Menu.')
    print(FoodPrice)

#1
def select_choice(): 
    print(FoodPrice)
    print('-'*10+' Option '+'-'*10)
    print(" [0] search ----")
    print(" [1] add    ----")
    print(" [2] edit   ----")
    print(" [3] delete ----")
    print(" [4] exit   ----")
    
    choice = int(input('Enter your choice : '))

    #2
    if choice == 0:
        clear()
        food = input('Enter Menu name : ')
        if search(food):
            print(f'{food}\'Price is {FoodPrice[food]} baht')
        else:
            print(f'Sorry not found {food} in the Menu.')   

    #3
    elif choice == 1:
        clear()
        name = input('Enter Menu name : ')
        price = int(input('Enter Menu Price : '))
        add(name, price)
    
    #4
    elif choice == 2:
        clear()
        list_Menu()
        num = int(input('Enter Menu naumber : '))
        name = input('Enter new Menu name : ')
        price = int(input('Enter Menu Price : '))
        edit(num, name, price)

    #5
    elif choice == 3:
        clear()
        list_Menu()
        num = int(input('Enter Menu naumber to delete : '))
        remove(num)

    elif choice == 4:
        clear()
        exit()

clear()
while True:
    select_choice()
    input('Press Enter to continue. ')
    clear()