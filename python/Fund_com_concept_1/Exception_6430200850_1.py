### Github: https://github.com/PKGzGMTH
### Medium: https://peakungg.medium.com/
### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

################################ Ex 5(ใบงาน). ################################
from functools import reduce
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#1
def cal_f(x,i,n):
    if n > 1:
        result = (1+i) * cal_f(x,i,n-1)
    elif n == 1:
        result = x
    else :
        result = 0
    return result

def saving():
    try:
        money = float(input('Enter Money: '))
        interest = float(input('Enter interest: '))
        year = int(input('Enter year: '))
    except ValueError:
        print('Please Enter number only')
    else:
        print('Money:' ,cal_f(money, interest, year))
    finally:
        print('-'*10, 'Finish saving program', '-'*10)


#2
def score():
    score = 0
    score_list = []

    while score >= 0:
        try:
            score = int(input('Enter Number : '))
        except ValueError:
            print('Enter integer number only!')
        else:
            if score >= 0:
                score_list.append(score)

    print('input = ', score_list)
    print('Sum :', reduce(lambda x,y : x+y, score_list))
    print('Max :', reduce(lambda x,y : x if x>=y else y, score_list))
    print('Min :', reduce(lambda x,y : x if x<=y else y, score_list))
    print('Low :', list(filter(lambda x : True if x < 50 else False, score_list)))


if __name__ == '__main__':
    clear()
    while True:
        print('-'*10, 'Select choice', '-'*10)
        print('[0] exit')
        print('[1] save money')
        print('[2] score calculation')
        choice = int(input('Enter choice: '))

        if choice == 0:
            break
        elif choice == 1:
            saving()
        elif choice == 2:
            score()

        input('\npress Enter to continue.')
        clear()