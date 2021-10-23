#x = '''Albedo,Aloy,Amber,Barbara,Beidou,Bennett,Chongyun,Diluc,Diona,Eula,Fischl,Ganyu,Hu Tao,Jean,Kaedehara Kazuha,Kaeya,Kamisato Ayaka,Keqing,Klee,Kujou Sara,Lisa,Mona,Ningguang,Noelle,Qiqi,Raiden Shogun,Razor,Rosaria,Sayu,Sucrose,Tartaglia,Traveler,Venti,Xiangling,Xiao,Xingqiu,Xinyan,Yanfei,Yoimiya,Zhongli,Dainsleif,Gorou,Sangonomiya Kokomi,Thoma,Yae Miko'''
#print(list(x.split(',')))

#x = "['Albedo', 'Aloy', 'Amber', 'Barbara', 'Beidou', 'Bennett', 'Chongyun', 'Diluc', 'Diona', 'Eula', 'Fischl', 'Ganyu', 'Hu Tao', 'Jean', 'Kaedehara Kazuha', 'Kaeya', 'Kamisato Ayaka', 'Keqing', 'Klee', 'Kujou Sara', 'Lisa', 'Mona', 'Ningguang', 'Noelle', 'Qiqi', 'Raiden Shogun', 'Razor', 'Rosaria', 'Sayu', 'Sucrose', 'Tartaglia', 'Traveler', 'Venti', 'Xiangling', 'Xiao', 'Xingqiu', 'Xinyan', 'Yanfei', 'Yoimiya', 'Zhongli', 'Dainsleif', 'Gorou', 'Sangonomiya Kokomi', 'Thoma', 'Yae Miko']"


'''
checknumber = lambda x: True if str(x).isnumeric() else False
print(f"Check number : {checknumber('123')}")'''

import serial, time, numpy as np, matplotlib.pyplot as plt
from matplotlib.pyplot import figure, draw, pause
baudrate = 115200
port = 'COM4'  # set the correct port before run it
count = 0

myserial = serial.Serial(port=port, baudrate=baudrate)
myserial.timeout = 2  # set read timeout
# print z1serial  # debug serial.
print (myserial.is_open)  # True for opened
if myserial.is_open:
    while True:
        read = False
        data = []
        index = 0
        size = myserial.inWaiting()
        if size:
            try:
                #print('finish')
                receivedata = myserial.read(size).decode('utf-8')
                print(receivedata)
                print('finish')

            except:
                continue
            
        else:
            continue
        time.sleep(1)
else:
    print ('serial not open')