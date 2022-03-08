### Github: https://github.com/PKGzGMTH
### Medium: https://peakungg.medium.com/
### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

################################ แบบฝึกหัด Exception. ################################
import os
return_rate = 0.5
member_list = {}
chr_list = list('abcdefghijklmnopqrstuvwxyz ')

def cal_return(stock:int, rate:int):
    result = stock*rate
    return result

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class MemberName(Exception): pass
class ZeroStock(Exception): pass
class ZeroYear(Exception): pass

if __name__ == '__main__':
    try:
        clear()
        member = input('Enter user name: ')
        if member == '':
            raise MemberName('The member name must be only English alphabet and space!!!')
        for i in member :
            if i.lower() not in chr_list:
                raise MemberName('The member name must be only English alphabet and space!!!')

        stock = float(input('Enter stock: '))
        if stock <= 0:
            raise ZeroStock('The number of stock is more than zero !!!')

        year = float(input('Enter number of year: '))
        if year % 1 != 0 :
            raise TypeError('Enter int only')
        else:
            year = int(year)
        if year <= 0 :
            raise ZeroYear('The number of year is more than zero !!!')

    except ValueError:
        print('Enter number only!')

    except TypeError:
        print('Year must be integer')

    except MemberName:
        print('The member name must be only English alphabet and space!!!')
    
    except ZeroStock:
        print('The number of stock is more than zero !!!')
    
    except ZeroYear:
        print('The number of year is more than zero !!!')

    else:
        member_list.update({member : stock})
        for i in range(year):
            money = cal_return(stock,return_rate)
            print(f'Year: {i+1}: {money}')
            stock += money/10
    finally:
        print('---Exiting the program.---')    