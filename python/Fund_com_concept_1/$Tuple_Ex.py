### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

#6
Faculty = ("Management", "Engineering", "Science", "Marine", "Economic")

#7
start = int(input('Enter start position : ')) - 1
end = int(input('Enter end position : ')) - 1
if 0 <= start <= len(Faculty) and 0 <= end <= len(Faculty):
    print('List : '+' '.join(Faculty[start:end]))
else:
    print('Invalid start or end position.')

#8
findFaculty = input('Enter Faculty name : ')
print('You are studying at KU Sriracha campus.' if findFaculty in Faculty else 'Sorry, you aren’t studying there.')