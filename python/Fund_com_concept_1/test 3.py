goods = int(input('Enter string : '))
mounth = 0
week = 0
day = 0
while goods >= 20000:
    goods -= 20000
    mounth += 1
while goods >= 5000:
    goods -= 5000
    week += 1
while goods >= 1000:
    goods -= 1000
    day+=1
else:
    if goods >0:
        day +=1
#print(goods)
print(mounth)
print(week)
print(day)
