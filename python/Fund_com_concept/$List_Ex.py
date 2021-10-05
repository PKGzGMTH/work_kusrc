### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

#1
FoodMenu = ['ต้มยำกุ้ง', 'แกงส้ม', 'ต้นข่าไก่', 'ขนมจีนน้ำยา', 'แกงเขียวหวานไก่', 'มสัมั่นไก่', 'แพนงหมู', 'แกงจืดหมูสับ']

#2
print("Lucky!!! You found your choice." if input('Food here : ') in FoodMenu else "Sorry, you miss your choice. ")

#3
FoodMenu.append(input('New Food menu : '))
print(f'Total : {len(FoodMenu)} Menu.')
print('Food Menu : '+' '.join(FoodMenu))

#4
for i in range(len(FoodMenu)):
    print(f' [{i+1}]  {FoodMenu[i]}')
pos = int(input('Enter Number of menu you want to delete : '))-1
if 0 <= pos <= len(FoodMenu)+1 :
    FoodMenu.pop(pos)
    for i in range(len(FoodMenu)):
        print(f' [{i+1}]  {FoodMenu[i]}')
else :
    print('Invalid position.')

#5
for i in range(len(FoodMenu)):
    print(f' [{i+1}]  {FoodMenu[i]}')
pos = int(input('Enter Number of menu : '))-1
if 0 <= pos <= len(FoodMenu)+1 :
    menu = input('Enter food name : ')
    FoodMenu[pos] = menu
    for i in range(len(FoodMenu)):
        print(f' [{i+1}]  {FoodMenu[i]}')
else :
    print('Invalid position.')