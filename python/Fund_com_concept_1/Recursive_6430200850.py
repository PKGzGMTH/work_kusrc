### Github: https://github.com/PKGzGMTH
### Medium: https://peakungg.medium.com/
### Student ID: 6430200850
### Student name: นายพงศกร ทิพยสมเดช

################################ Ex 1. ################################
# 1
def fact(x:int):
  if x > 1:
    value = x * fact(x-1)
  elif x == 1:
    value = 1
  elif x < 1:
    value = 0
  return value

print(fact(15))

#2 
def remain_students(x:int, y:int):
  if y > 1:
    value = x * remain_students(x, y-1)
  elif y == 1:
    value = 100
  elif y < 1:
    value = 0
  return value

print(remain_students(0.9,5))

################################ Ex 2. ################################
money = [ 500, 1000, 300,  800] 

#1
print('-'*10,'1','-'*10)
discount = lambda x,y : x * (y/100)
print(discount (1000,5))

#2
print('-'*10,'2','-'*10)
checknumber = lambda x : True if str(x).isnumeric() else False
print(checknumber(1))
print(checknumber('a'))

#3
print('-'*10,'3','-'*10)
calDiscount = lambda x : x*0.1 if x >= 500 else x*0.05
print(calDiscount(2000))
print(calDiscount(200))

#4
print('-'*10,'4','-'*10)
calVAT = lambda i : i*1.07
print([calVAT(i) for i in money])

################################ Ex 3. ################################
A = [1, 6, 7, 3, 5, 8]
B = [2, 5, 7, 4, 6, 'A']
X = {'Alan': 100, 'Bob': 75, 'Clark': 60, 'David': 55}

#1 
def high(x):
  if x > 5: return True
  else : False

print('c = ',list(filter(high,A)))

#2 
def odd(x):
  if x%2 == 1: return True
  else : False
print('c = ',list(filter(odd,A)))

#3 
def charecter(x):
  x=str(x)
  if x.isalpha() : return True
  else : False
print('c = ',list(filter(charecter,B)))


#4
def f(x):
  if X[x] >= 75: return True
  else : return False
print('c = ',list(filter(f,X.keys())))

################################ Ex 4. ################################
from  functools import reduce
A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8, 10]

#1
product = reduce((lambda x, y: x + y), A)
print(product)

#2
product = reduce((lambda x,y : x if x>=y else y), B)
print(product)

#3
x = 1
product = list(map(lambda x: 3 * x , A))
print(product)
z = list(zip(A,B))
#print(z)
#product = list(map(lambda x: x[0] + x[1], z))
#print(product)

#4
product = list(map((lambda x : x if x%4 == 0 else 0),B))
product = list(filter(lambda x : True if x != 0 else False,product))
print(product)
#product = list(map((lambda x: x*2 ), B[:2]))
#print(product)

################################ Ex 5(ใบงาน). ################################
#1
def f(x,i,n):
    if n > 1:
        result = (1+i) * f(x,i,n-1)
    elif n == 1:
        result = x
    elif n < 1:
        result = 0
    return result

print(f(1000,1.02,10))


#2
from functools import reduce
x = 0
input_list = []

while x >= 0:
    x = int(input('Enter Number : '))
    if x >= 0:
        input_list.append(x)
print('input = ', input_list)

sum_ = reduce((lambda x,y : x+y), input_list)
print('Sum :',sum_)

max_ = reduce((lambda x,y : x if x>=y else y),input_list)
print('Max :', max_)

min_ = reduce((lambda x,y : x if x<=y else y),input_list)
print('Min :', min_)

low_ = list(filter((lambda x : True if x < 50 else False), input_list))
print('Low :', low_)