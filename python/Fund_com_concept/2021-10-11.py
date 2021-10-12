### Github: https://github.com/PKGzGMTH
### Medium: https://peakungg.medium.com/
### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

################################################################

import random, numpy as np
from os import name, system

card = ['Red', 'Black']

def clear():
    if name == 'nt': system('cls')
    else : system('clear')

def pick_card():
    clear()
    roll = random.randint(0,1)
    print(f'You got {card[roll]} card')
    pass

def rsp_game():
    win_count = 0
    while win_count < 10:
        clear()
        print('You wins: ', win_count)
        print('-'*10, 'Choice', '-'*10)
        rsp_rand = random.randint(1,3)
        print('[1] Rock')
        print('[2] Paper')
        print('[3] Scissors')
        rsp_ = int(input('Enter your choice: '))
        if (rsp_rand == 3 and rsp_ == 1) or (rsp_rand == 2 and rsp_ == 3) or (rsp_rand == 1 and rsp_ == 2):
            print('You win!!')
            win_count += 1
            input('Press Anykey to continue.')
        elif rsp_rand == rsp_ :
            print('You Draw!!')
        else:
            print('You lose!!')
            input('Press Anykey to continue.')
    clear()
    print('Congratulations You win!!')

if __name__ == '__main__':
    while True:
        clear()
        print('-'*10, 'Choice', '-'*10)
        print('[1] pick red/black card.')
        print('[2] rock paper scissors.')
        print('[0] exit.')

        choice = int(input('Enter your choice : '))

        if choice == 0:
            break
        elif choice == 1:
            pick_card()
        elif choice == 2:
            rsp_game()

        input('Press Anykey to continue.')
    