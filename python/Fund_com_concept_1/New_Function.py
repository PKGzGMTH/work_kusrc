#1
def f(x,i,n):
    if n > 1:
        result = i * f(x,i,n-1)
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
