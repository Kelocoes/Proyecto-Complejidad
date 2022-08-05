import numpy as np
import random

def optFunct(n):
    #y x
    # ciudades = [[0, 0], [0, 10], [10, 0], [10, 10]]
#     ciudades= [[9, 9]
# ,[9, 3]
# ,[8, 6]
# ,[3, 9]
# ,[0 ,6]
# ,[4, 2]
# ,[4, 0]
# ,[2, 0]
# ,[0, 9]
# ,[ 5, 2]]
    # ciudades=[
    # [0,1],
    # [2,4],
    # [3,8],
    # [4,1],
    # [6,3],
    # [6,4],
    # [6,5],
    # [8,7],
    # [9,3],
    # [9,10]]
    # ciudades=[[631, 583], [993, 911], [996, 373], [726, 717], [165, 353], [385, 218], [276, 69], [384, 97], [534, 697], [345,271], [50, 596], [984, 255], [92, 750], [677, 320], [406, 749], [308, 791], [379, 695], [761, 275], [100, 582], [994, 980]]
    ciudades=[[0,0]]
    distancias = [[]]
    pos=[]
    aux = 0
    for y in range(n+1):
        for x in range(n+1):
            for ciudad in ciudades:
                distancias[aux].append(abs(x - ciudad[0]) + abs(y - ciudad[1]))
            distancias.append([])
            #print(x,y , distancias[aux])
            if([x,y] not in ciudades):
                pos.append([x,y])
            aux += 1
            
    maximas=[] 
    distancias.pop()         
    for dist in distancias:
        maximas.append(max(dist))
    print((pos[maximas.index(min(maximas))]))
    print(maximas.count(min(maximas)))
    print(min(maximas))

    
    # caquita2=min(maximas)
    # caquita=[]
    # for j,x in enumerate(maximas):
    #    if x == caquita2:
    #        caquita.append(pos[j])
    # print(caquita,len(caquita))


optFunct(10)

def generatePrueba(n,m):
    values="["
    valArray=[]
    for i in range(n):
        a=random.randint(0,m)
        b=random.randint(0,m)
        values+="|{}, {}, ".format(a,b)
        valArray.append([a,b])
    values+='|]'
   
    return (values,valArray)
        
        
# print(generatePrueba(20,1000))