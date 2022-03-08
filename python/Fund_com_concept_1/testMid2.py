#6430250342 วัชรพัฐ กงแก้ว

# 1
Foodmenu = ["ต้มยำกุ้ง", "แกงส้ม", "ต้มข่าไก่", "ขนมจีนนำ้ยา", "แกงเขียวหวานไก่", "มัสมั่นไก่", "แพนงหมู", "แกงจืดหมูสับ"]
print(Foodmenu)


# 4
for i in range(len(Foodmenu)):
    print (i, Foodmenu[i])


delete_item = int(input("Enter deleting choice:"))
check1 = B <= delete_item <= len(Foodmenu) - 1
check1 = (delete_item >= 0) and (delete_item <= len(Foodmenu) - 1)


'''
# 3

new_item = input("Enter new item :blush:
Foodmenu.append(new_item)
print("the number of item :", len(Foodmenu))
print(Foodmenu)



# 2
search = input("Enter your choice :blush:
if search in Foodmenu:
    print("Lucky!!! You found your choice.")
else:
    print("Sorry, you miss your choice.")'''