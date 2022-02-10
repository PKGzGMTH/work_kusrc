t = input('pls input time in this type 09:20 or 5:00:  ')
time = t.split(':')
totalMin = (60*int(time[0]))+int(time[1])
print(totalMin)