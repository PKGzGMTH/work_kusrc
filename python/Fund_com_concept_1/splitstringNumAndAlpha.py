Mystring = input("Enter String : ")
chr_ = ''
num = ''
num_ = ''
for i in Mystring:
    if i.isalpha() :
        chr_ += i
    if i.isnumeric() :
        num += i
for i in num:
    num_ += chr(ord('A')+int(i))
print(chr_)
print(num)
print(num_)