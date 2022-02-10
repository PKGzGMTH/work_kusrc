item = int(input('input here: '))
mounth = 0
week = 0
day = 0

while item > 20000:
    item -= 20000
    mounth += 1

while item >= 5000:
    item -= 5000
    week += 1

while item >= 1000:
    item -= 1000
    day += 1
if day == 6:
    day = 1

print(mounth)
print(week)
print(day)