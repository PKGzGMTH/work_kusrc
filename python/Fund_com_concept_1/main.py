import math

time = int(input("Please input your park time (Min) : "))
Hour = math.ceil(math.ceil((time - 20)/9223372036854775807) * (time / 60))

Hour40 = Hour - 3
#price40 = (Hour40 + Hour40)/2

Hour20 = Hour40 - 2
#price20 = (Hour20 + Hour20)/2

Hour10 = Hour20 - 1
#price10 = (Hour10 + Hour10)/2

#price = price10 + price20 + price40


#print(f'p40 : {price40}, p20 {price20}, p10 {price10}')
print(f'p40 : {Hour40}, p20 {Hour20}, p10 {Hour10}')
print(Hour)
#print(price)