#x = '''Albedo,Aloy,Amber,Barbara,Beidou,Bennett,Chongyun,Diluc,Diona,Eula,Fischl,Ganyu,Hu Tao,Jean,Kaedehara Kazuha,Kaeya,Kamisato Ayaka,Keqing,Klee,Kujou Sara,Lisa,Mona,Ningguang,Noelle,Qiqi,Raiden Shogun,Razor,Rosaria,Sayu,Sucrose,Tartaglia,Traveler,Venti,Xiangling,Xiao,Xingqiu,Xinyan,Yanfei,Yoimiya,Zhongli,Dainsleif,Gorou,Sangonomiya Kokomi,Thoma,Yae Miko'''
#print(list(x.split(',')))

#x = "['Albedo', 'Aloy', 'Amber', 'Barbara', 'Beidou', 'Bennett', 'Chongyun', 'Diluc', 'Diona', 'Eula', 'Fischl', 'Ganyu', 'Hu Tao', 'Jean', 'Kaedehara Kazuha', 'Kaeya', 'Kamisato Ayaka', 'Keqing', 'Klee', 'Kujou Sara', 'Lisa', 'Mona', 'Ningguang', 'Noelle', 'Qiqi', 'Raiden Shogun', 'Razor', 'Rosaria', 'Sayu', 'Sucrose', 'Tartaglia', 'Traveler', 'Venti', 'Xiangling', 'Xiao', 'Xingqiu', 'Xinyan', 'Yanfei', 'Yoimiya', 'Zhongli', 'Dainsleif', 'Gorou', 'Sangonomiya Kokomi', 'Thoma', 'Yae Miko']"


'''
checknumber = lambda x: True if str(x).isnumeric() else False
print(f"Check number : {checknumber('123')}")'''

x = [1,2,3,4,4,5,6,7,7,7,8,8,9,7,10]
y = []

for i in range(15):
    for j in range(15):
        if i == j:
            continue
        elif x[i] == x[j]:
            if x[i] not in y:
                y.append(x[i])
                print(x[i])