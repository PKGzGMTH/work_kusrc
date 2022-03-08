### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

#1
import numpy as np

FoodPrice = {
    'ต้มยำกุ้ง' : 90,
    'แกงส้ม' : 60,
    'ต้มข่าไก่' : 60,
    'ขนมจีนน้ำยา' : 40,
    'แกงเขียวหวานไก่' : 40,
    'มัสมั่นไก่' : 50,
    'แพนงหมู' : 40,
    'แกงจืดหมูสับ' : 30
}

#2
search = input('Enter Food name here :')
if search in FoodPrice:
    print(f'{search} มีราคาเท่ากับ {FoodPrice[search]}')
else : 
    print(f'เสียใจด้วย ไม่มีอาหารที่คุณต้องการ')

#3
new_food = input('Enter new Food here :')
if new_food not in FoodPrice:
    new_price = int(input('Enter new Food price here :'))
    FoodPrice[new_food] = new_price
else :
    print('มีรายการอาหารนี้อยู่แล้ว')

#4
num = 1
for n in FoodPrice:
    print(f'{num} : {n}')
    num+=1

remove_food = int(input('Enter Food that you want to remove :'))

try:
    Foodname = list(FoodPrice.keys())[remove_food-1]
    FoodPrice.pop(Foodname)
    print('ลบรายการอาหารนี้แล้ว')
except:
    print('ไม่พบรายการอาหารนี้')
print('#'*24)
print(FoodPrice)

#5
import numpy as np
num_student = np.array([[100,150],
                        [85,90,],
                        [75,70],
                        [60,55]])
print(num_student.shape)
print(num_student)

#6
num_major = np.array([0,0])
num_year = np.array([0,0,0,0])

for i in range(num_student.shape[0]):
    num_major[0] += num_student[i,0]
    num_major[1] += num_student[i,1]

for i in range(num_student.shape[1]):
    num_year[0] += num_student[0,i]
    num_year[1] += num_student[1,i]
    num_year[2] += num_student[2,i]
    num_year[3] += num_student[3,i]

print(num_major)
print(num_year)

#7
KUSRC = {"Management", "Engineering","Science", "Marine", "Economics"}
KUBKK = {"Agriculture", "Business","Fisheries", "Humanities", "Science", "Engineering", "Education", "Economics"}

#8
print('Union : ', KUBKK.union(KUSRC))
print('Same : ' , KUBKK.intersection(KUSRC))
print('Only SRC : ' , KUSRC.difference(KUBKK))

#9
faculty = input('Enter Faculty : ')
if faculty in KUBKK.intersection(KUSRC) :
    print("คุณมีโอกาสไดทั้งสองวิทยาเขต")
elif faculty in KUSRC:
    print("คุณเรียนที่วิทยาเขตศรีราชา")
elif faculty in KUBKK:
    print("คุณเรียนที่วิทยาเขตบางเขน")
else:
    print("เสียใจด้วย คุณไม่ได้เรียนที่วิทยาเขตบางเขนหรือศรีราชา")