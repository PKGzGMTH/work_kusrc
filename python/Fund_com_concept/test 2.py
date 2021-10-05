i,sum = 0,0
while True:
    i+=1
    inputScore = int(input(f'Enter score of #{i} : '))
    if inputScore >= 0:
        sum += inputScore
    else:
        print(f'Sum of score : {sum}')
        print(f'Average score : {sum/i}')
        break