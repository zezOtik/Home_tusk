# -*- coding: utf-8 -*-
import random
import math
import sys
import time

def port(self):#считывания из файла значения
    p = open(self,'r',encoding = 'utf-8')
    strok=[]
    for line in p:
        line = line[:(len(line) - 1)] 
        strok.append(line)
    n = int(strok[0])
    m = int(strok[1])
    vershiny = int(strok[2])
    p.close()
    return n,m,vershiny

def outport(self,hashtable):#запись в файл значения
    p = open(self,'w',encoding = 'utf-8')
    p.write(str(hashtable))
    p.close()
    
    
def generate_lab_step_one(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m):#Шаг 1 , строим проход от 0 до н*м -1
    
    labirint_ne_posetil.pop(0)#Отметили, что вершину 0 посетили

    labirint_posetil[0] = 1#Отметили, что вершину 0 посетили
    
    i = 0#старт работы алгоритма
    
    while(i != size_n * size_m - 1 ):#пока не равны значения работать
        #проверка на возможную ошибку 
        (i,j) = randomstep(labirint_posetil,i,size_n,size_m)#выбор случайного значения прохода
        
        if j != 0:           
            labirint_main = brok_wall(labirint_main, size_n, size_m, i, j)#сломали стенку
            labirint_posetil[i] = 1#Отметили вершину i-посещенной
            labirint_ne_posetil.pop(i)#Отметили вершину i-посещенной
        else:
            continue

    return labirint_main,labirint_posetil,labirint_ne_posetil
    


def step_2(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m,vershiny):#Шаг 2 от прошедших вершин идем(Здесь настраивается сложность)
        while(vershiny != 0):
            i = randominfeik(labirint_posetil,size_n,size_m)
            p = random.randint(1,math.ceil(math.pow(size_n*size_m,0.25)))

            while(p != 0):
                (i,j) = randomstep(labirint_posetil,i,size_n,size_m)
                
                if (j == 0):
                    break
                
                else:
                    labirint_main = brok_wall(labirint_main,size_n,size_m,i,j)
                    
                    if labirint_ne_posetil[i] == None:
                        break
                    else:
                        labirint_ne_posetil.pop(i)
                        labirint_posetil[i] = 1
                        
                p -= 1
            vershiny -= 1
            
        return labirint_main,labirint_posetil,labirint_ne_posetil


def step_3(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m):
    if kolvo_elem(labirint_ne_posetil) != 0:
        i = randominfeik1(labirint_ne_posetil,size_n,size_m)
       

        labirint_posetil = invertor_step(labirint_posetil,i,size_n,size_m)

        (i,j) = randomstep(labirint_posetil,i,size_n,size_m)
        
        labirint_posetil = re_invertor_step(labirint_posetil,i,j,size_n,size_m)
        
        
        labirint_main = brok_wall(labirint_main,size_n,size_m,i,j)
        (labirint_ne_posetil,labirint_posetil) = vypystit(i,j,labirint_ne_posetil,size_m,labirint_posetil)

        return step_3(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m)
    else:
        return labirint_main
      

def kolvo_elem(hashtable):#получение количество значений в хэш-таблице
    kol_vo = len(list(hashtable.keys()))
    return kol_vo


def invertor_step(hashtable,i,size_n,size_m):#инвертирование набора
    try:
        if hashtable.get(i+1) == None and i % size_m != size_m - 1:
            hashtable[i+1] = 1
        elif hashtable.get(i+1) != None and i % size_m != size_m - 1:
            hashtable.pop(i+1)
    except KeyError:
        pass
    
    try:    
        if hashtable.get(i-1) == None and i % size_m != 0:
            hashtable[i-1] = 1
        elif hashtable.get(i-1) != None and i % size_m != 0:
            hashtable.pop(i-1)
    except KeyError:
        pass
    
    try:
        if hashtable.get(i-size_m) == None and i - size_m >= 0:
            hashtable[i-size_m] = 1
        elif hashtable.get(i-size_m) != None and i - size_m >= 0:
            hashtable.pop(i-size_m)
    except KeyError:
        pass
    
    try:
        if hashtable.get(i+size_m) == None and i + size_m <= size_n*size_m - 1:
            hashtable[i+size_m] = 1
        elif hashtable.get(i+size_m) != None and i + size_m <= size_n*size_m - 1:
            hashtable.pop(i+size_m)
    except KeyError:
        pass

    return hashtable


def re_invertor_step(hashtable,i,j,size_n,size_m):#обратное инвертирование
    try:
        if j == 1:
            hashtable = invertor_step(hashtable,i+1,size_n,size_m)
            if hashtable[i+1] != None and i % size_m != size_m - 1:
                hashtable.pop(i+1)
            elif hashtable[i+1] == None and i % size_m != size_m - 1:
                hashtable[i+1] = 1

        if j == 2:
            hashtable = invertor_step(hashtable,i+size_m,size_n,size_m)
            if hashtable[i+size_m] != None and i % size_m != 0:
                hashtable.pop(i+size_m)
            elif hashtable[i+size_m] == None and i % size_m != 0:
                hashtable[i+size_m] = 1
    
        if j == 3:
            hashtable = invertor_step(hashtable,i-1,size_n,size_m)
            if hashtable[i-1] != None and i % size_m != 0:
                hashtable.pop(i-1)
            elif hashtable[i-1] == None and i % size_m != 0:
                hashtable[i-1] = 1
    

        if j == 4:
            hashtable = invertor_step(hashtable,i-size_m,size_n,size_m)
            if hashtable[i-size_m] != None and i + size_m <= size_n*size_m - 1:
                hashtable.pop(i-size_m)
            elif hashtable[i-size_m] == None and i + size_m <= size_n*size_m - 1:
                hashtable[i-size_m] = 1

        return hashtable

    except KeyError:
       return hashtable
        

def vypystit(i,j,labirint_ne_posetil,size_m,labirint_posetil):
    if j == 1:
        if labirint_ne_posetil.get(i+1) == None:
            return labirint_ne_posetil,labirint_posetil
        
        else:
            labirint_ne_posetil.pop(i+1)
            labirint_posetil[i+1] = 1
            return labirint_ne_posetil,labirint_posetil
        
    elif j == 2:
        if labirint_ne_posetil.get(i + size_m) == None:
            return labirint_ne_posetil,labirint_posetil
        
        else:
            labirint_ne_posetil.pop(i + size_m)
            labirint_posetil[i + size_m] = 1
            return labirint_ne_posetil,labirint_posetil
        
    elif j == 3:
        if labirint_ne_posetil.get(i-1) == None:
            return labirint_ne_posetil,labirint_posetil
        
        else:
            labirint_ne_posetil.pop(i-1)
            labirint_posetil[i-1] = 1
            return labirint_ne_posetil,labirint_posetil
        
    elif j == 4:
        if labirint_ne_posetil.get(i - size_m) == None:
            return labirint_ne_posetil,labirint_posetil
        
        else:
            labirint_ne_posetil.pop(i - size_m)
            labirint_posetil[i - size_m] = 1
            return labirint_ne_posetil,labirint_posetil

def randominfeik(hashtable,size_n,size_m):#Вывод рандомной уже посещенной клетки
    p = random.randint(0,kolvo_elem(hashtable)-1)
    i = list(hashtable.keys())[p]
    if i == size_n * size_m - 1:
        return randominfeik(hashtable,size_n,size_m)
    else:
        return i

def randominfeik1(hashtable,size_n,size_m):#Вывод рандомной уже посещенной клетки
    p = random.randint(0,kolvo_elem(hashtable)-1)
    i = list(hashtable.keys())[p]
    if ((hashtable.get(i-1) != None or i % size_m == 0)
        and (hashtable.get(i+1) != None or i % size_m == size_m - 1)
        and (hashtable.get(i-size_m) != None or i - size_m < 0)
        and (hashtable.get(i+size_m) != None or i + size_m >= size_n* size_m - 1)):
        return randominfeik1(hashtable,size_n,size_m)
    else:
        return i


def randomstep(hashtable,i,size_n,size_m):#По входящим данным выбирает куда следует стрелка пробивания стенок.
    
    #проверил(0,1,1,1)
    if (((i % size_m == 0) or hashtable.get(i-1) != None)
        and i - size_m >= 0 and hashtable.get(i-size_m) == None
        and (i % size_m != size_m-1) and hashtable.get(i+1) == None
        and (i+size_m) <= size_n*size_m -1 and hashtable.get(i+size_m) == None):
            j = random.randint(2,4)
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #wp(0,0,0,1)
    elif ((i % size_m == 0 or hashtable.get(i-1) != None)
          and (i - size_m < 0 or hashtable.get(i-size_m) != None)
          and (i % size_m == size_m-1 or hashtable.get(i+1) != None)
          and (i+size_m) <= size_n*size_m -1 and hashtable.get(i+size_m) == None):
            j = 4
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #wp(0,1,0,1)   
    elif ((i % size_m == 0 or hashtable.get(i-1) != None)
          and i - size_m >= 0 and hashtable.get(i-size_m) == None
          and ((i % size_m == size_m-1) or hashtable.get(i+1) != None)
          and (i+size_m) <= size_n*size_m -1 and hashtable.get(i+size_m) == None):
            j = random.choice([2,4])
            i = if_I(i,size_n,size_m,j)
            return i,j

    #(0,0,1,0)
    elif ((i % size_m == 0 or hashtable.get(i-1) != None)
          and (i - size_m < 0 or hashtable.get(i-size_m) != None)
          and i % size_m != size_m-1 and hashtable.get(i+1) == None
          and ((i+size_m) > size_n*size_m -1 or hashtable.get(i+size_m) != None)):
            j = 3
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #(0,1,0,0)
    elif ((i % size_m == 0 or hashtable.get(i-1) != None)
          and i - size_m >= 0 and hashtable.get(i-size_m) == None
          and (i % size_m == size_m-1 or hashtable.get(i+1) != None)
          and (i+size_m > size_n*size_m -1 or hashtable.get(i+size_m) != None)):
            j = 2
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #(0,1,1,0)
    elif (((i % size_m == 0) or hashtable.get(i-1) != None)
          and i - size_m >= 0 and hashtable.get(i-size_m) == None
          and (i % size_m != size_m-1) and hashtable.get(i+1) == None
          and (((i+size_m) > size_n*size_m -1) or hashtable.get(i+size_m) != None)):
            j = random.randint(2,3)
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #(0,0,1,1)
    elif (((i % size_m == 0) or hashtable.get(i-1) != None)
          and (i - size_m < 0 or hashtable.get(i-size_m) != None)
          and (i % size_m != size_m-1) and hashtable.get(i+1) == None
          and (i+size_m) <= size_n*size_m -1 and hashtable.get(i+size_m) == None):
            j = random.randint(3,4)
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #(0,0,0,0)
    elif (((i % size_m == 0) or hashtable.get(i-1) != None)
          and (i - size_m < 0 or hashtable.get(i-size_m) != None)
          and (i % size_m == size_m-1 or hashtable.get(i+1) != None)
          and ((i+size_m) > size_n*size_m - 1 or hashtable.get(i+size_m) != None)):
            j = 0
            i = int(randominfeik(hashtable,size_n,size_m))
            return i,j
        
    #(1,1,1,1)
    elif (i % size_m != 0 and hashtable.get(i-1) == None
          and i - size_m >= 0 and hashtable.get(i-size_m) == None
          and i % size_m != size_m-1 and hashtable.get(i+1) == None
          and i+size_m <= size_n*size_m -1 and hashtable.get(i+size_m) == None):
            j = random.randint(1,4)
            i = if_I(i,size_n,size_m,j)
            return i,j

    #(1000)
    elif (((i % size_m != 0) and hashtable.get(i-1) == None)
        and (i - size_m < 0 or hashtable.get(i-size_m) != None)
        and ((i % size_m == size_m-1) or hashtable.get(i+1) != None)
        and ((i+size_m) > size_n*size_m -1 or hashtable.get(i+size_m) != None)):
            j = 1
            i = if_I(i,size_n,size_m,j)
            return i,j
            
        
    #1001
    elif (((i % size_m != 0) and hashtable.get(i-1) == None)
        and (i - size_m < 0 or hashtable.get(i-size_m) != None)
        and ((i % size_m == size_m-1) or hashtable.get(i+1) != None)
        and ((i+size_m) <= size_n*size_m -1) and hashtable.get(i+size_m) == None):
            j = random.choice([1,4])
            i = if_I(i,size_n,size_m,j)
            return i,j
        
        
    #(1010)
    elif (((i % size_m != 0) and hashtable.get(i-1) == None)
        and (i - size_m < 0 or hashtable.get(i-size_m) != None)
        and (i % size_m != size_m-1) and hashtable.get(i+1) == None
        and (((i+size_m) > size_n*size_m -1) or hashtable.get(i+size_m) != None)):
            j = random.choice([1,3])
            i = if_I(i,size_n,size_m,j)
            return i,j


    #(1011)
    elif (i % size_m != 0 and hashtable.get(i-1) == None
        and (i - size_m < 0 or hashtable.get(i-size_m) != None)
        and i % size_m != size_m-1 and (hashtable.get(i+1) == None
        and (i+size_m) <= size_n*size_m -1 and (hashtable.get(i+size_m) == None))):
            j = random.choice([1,3,4])
            i = if_I(i,size_n,size_m,j)
            return i,j
        

    #(1100)
    elif (((i % size_m != 0) and hashtable.get(i-1) == None)
        and (i - size_m >= 0 and hashtable.get(i-size_m) == None)
        and ((i % size_m == size_m-1) or hashtable.get(i+1) != None)
        and ((i+size_m) > size_n*size_m -1 or hashtable.get(i+size_m) != None)):
            j = random.randint(1,2)
            i = if_I(i,size_n,size_m,j)
            return i,j
        
        
    #(1101)
    elif ((i % size_m != 0) and hashtable.get(i-1) == None
        and i - size_m >= 0 and hashtable.get(i-size_m) == None
        and ( (i % size_m == size_m-1) or hashtable.get(i+1) != None)
        and i+size_m <= size_n*size_m -1 and hashtable.get(i+size_m) == None):
            j = random.choice([1,2,4])
            i = if_I(i,size_n,size_m,j)
            return i,j
            
        
    #(1110)
    elif (((i % size_m != 0) and hashtable.get(i-1) == None)
        and (i - size_m >= 0 and hashtable.get(i-size_m) == None)
        and ((i % size_m != size_m-1) and hashtable.get(i+1) == None)
        and (((i+size_m) > size_n*size_m -1) or hashtable.get(i+size_m) != None)):
            j = random.randint(1,3)
            i = if_I(i,size_n,size_m,j)
            return i,j


def brok_wall(hashtable,size_n,size_m,i,j):#Пробивание лабиринта
        
    if j == 1 and hashtable[i] == 11:
        hashtable[i] = 1
        return hashtable
    
    elif j == 2 and hashtable[i] == 11:
        hashtable[i] = 10
        return hashtable
    
    elif j == 3 and hashtable[i-1] == 11:
        hashtable[i-1] = 1
        return hashtable
    
    elif j == 4 and hashtable[i-size_m] == 11:
        hashtable[i-size_m] = 10
        return hashtable
    
    elif j == 1 and hashtable[i] == 10:
        hashtable[i] = 0
        return hashtable
    
    elif j == 2 and hashtable[i] == 10:
        hashtable[i] = 10
        return hashtable
    
    elif j == 3 and hashtable[i-1] == 10:
        hashtable[i-1] = 0
        return hashtable
    
    elif j == 4 and hashtable[i-size_m] == 10:
        hashtable[i-size_m] = 10
        return hashtable
    
    elif j == 1 and hashtable[i] == 1:
        hashtable[i] = 1
        return hashtable
    
    elif j == 2 and hashtable[i] == 1:
        hashtable[i] = 0
        return hashtable
    
    elif j == 3 and hashtable[i-1] == 1:
        hashtable[i-1] = 1
        return hashtable
    
    elif j == 4 and hashtable[i-size_m] == 1:
        hashtable[i-size_m] = 0
        return hashtable
    
    elif j == 1 and hashtable[i] == 0:
        hashtable[i] = 0
        return hashtable
    
    elif j == 2 and hashtable[i] == 0:
        hashtable[i] = 0
        return hashtable
    
    elif j == 3 and hashtable[i-1] == 0:
        hashtable[i-1] = 0
        return hashtable
    
    elif j == 4 and hashtable[i-size_m] == 0:
        hashtable[i-size_m] = 0
        return hashtable

      
def if_I(i,size_n,size_m,j):#получение нового i-ого

    if j == 1:
        return i - 1
        
    elif j == 2:
        return i - size_m
        
    elif j == 3:
        return i + 1

    elif j == 4:
        return i + size_m   
    
def main():
    time.clock()
    file = sys.argv[1]
    file1 = sys.argv[2] 

    #receipt our params
    (size_n, size_m,vershiny) = port(file)

    labirint_main = dict()#создали хэш таблицу основная
    labirint_main = {i: 11 for i in range(size_n*size_m)}#забили ее 11

    labirint_ne_posetil = dict()#хэш-табл не посещенных
    labirint_ne_posetil = {i: 1 for i in range(size_n*size_m)}

    labirint_posetil = dict()#хэш-таблица для посещенных
   
    (labirint_main,labirint_posetil,labirint_ne_posetil) = (generate_lab_step_one(labirint_main,labirint_posetil,labirint_ne_posetil,size_n, size_m))

    (labirint_main,labirint_posetil,labirint_ne_posetil) = (step_2(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m,vershiny))
    
    labirint_main = step_3(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m)


    outport(file1,labirint_main)
    print(time.clock())
    

  

if __name__ == '__main__':
    main()
