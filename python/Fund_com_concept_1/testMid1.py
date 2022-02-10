queue = int(input('input : '))
day = (queue//1400)+1
round = ((queue%7)//200)+1
person = (queue%200)
print(day)
print(round)
print(person)