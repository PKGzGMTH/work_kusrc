#x = '''Albedo,Aloy,Amber,Barbara,Beidou,Bennett,Chongyun,Diluc,Diona,Eula,Fischl,Ganyu,Hu Tao,Jean,Kaedehara Kazuha,Kaeya,Kamisato Ayaka,Keqing,Klee,Kujou Sara,Lisa,Mona,Ningguang,Noelle,Qiqi,Raiden Shogun,Razor,Rosaria,Sayu,Sucrose,Tartaglia,Traveler,Venti,Xiangling,Xiao,Xingqiu,Xinyan,Yanfei,Yoimiya,Zhongli,Dainsleif,Gorou,Sangonomiya Kokomi,Thoma,Yae Miko'''
#print(list(x.split(',')))

#x = "['Albedo', 'Aloy', 'Amber', 'Barbara', 'Beidou', 'Bennett', 'Chongyun', 'Diluc', 'Diona', 'Eula', 'Fischl', 'Ganyu', 'Hu Tao', 'Jean', 'Kaedehara Kazuha', 'Kaeya', 'Kamisato Ayaka', 'Keqing', 'Klee', 'Kujou Sara', 'Lisa', 'Mona', 'Ningguang', 'Noelle', 'Qiqi', 'Raiden Shogun', 'Razor', 'Rosaria', 'Sayu', 'Sucrose', 'Tartaglia', 'Traveler', 'Venti', 'Xiangling', 'Xiao', 'Xingqiu', 'Xinyan', 'Yanfei', 'Yoimiya', 'Zhongli', 'Dainsleif', 'Gorou', 'Sangonomiya Kokomi', 'Thoma', 'Yae Miko']"


'''
checknumber = lambda x: True if str(x).isnumeric() else False
print(f"Check number : {checknumber('123')}")'''

import serial, time, numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animation
baudrate = 921600
port = 'COM4'  # set the correct port before run it
list = []
ser = serial.Serial(port=port, baudrate=baudrate)
ser.timeout = 2
if ser.is_open:
    while ord(ser.read()) != 0:
        continue
    while True:
        readByte = ord(ser.read())
        if readByte == 0: break
        else:
            list.append(int(readByte))
    print(list)
    print(len(list))

else:
    print ('serial not open')
