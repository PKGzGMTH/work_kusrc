Mystring = input("Enter String : ")
keyword = input("Keyword : ")
lenght=len(keyword)
location = 0
awnser = ''
count = Mystring.count(keyword)
while Mystring.find(keyword)>=0:
    #print(Mystring.find(keyword))
    awnser += f'{Mystring.find(keyword)+location}-{Mystring.find(keyword)+location+lenght-1},'
    location += Mystring.find(keyword)+lenght
    Mystring = Mystring[Mystring.find(keyword)+lenght:]
    #print(Mystring)
print('find string at :',awnser[:len(awnser)-1])
print('count :', count)