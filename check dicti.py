# -*- coding: utf-8 -*-
import random

def port(self):#считывания из файла значения
    p = open(self,'r',encoding = 'utf-8')
    strok=[]
    for line in p:
        line = line[:(len(line) - 1)] 
        strok.append(line)
    n = int(strok[0])
    m = int(strok[1])
    p.close()
    return n,m

    
def generate_lab_step_one(size_n,size_m):#нужно переписать проверку на полученную рандомное значение, если рандом привел нас втупик, выбросить нужно число
    labirint_vol_1 = dict()#создали хэш таблицу
    labirint_vol_1 = {i: 11 for i in range(size_n*size_m)}#забили ее 11

    s = []#переменная для считывания значений функции

    feiklab_st_1 = dict()#хэш-таблица для посещенных
    feiklab_st_1[0] = 1#отметили 0 -  посещенной
    
    i = 0#старт работы алгоритма
    j = 0
    p_random = 0#переменная для проверки random
    
    while(i != size_n * size_m - 1 ):#пока не равны значения работать
        #проверка на возможную ошибку 
        s = randomstep(feiklab_st_1,i,j,size_n,size_m)
        i = int(s[0])
        j = int(s[1])
        if j != 0:           
            brok_wall(labirint_vol_1, size_n, size_m, i, j)
            feiklab_st_1[i] = 1
            i = proverka_i_ogo(labirint_vol_1,i,size_n,size_m,feiklab_st_1)
        else:
            i = proverka_i_ogo(labirint_vol_1,i,size_n,size_m,feiklab_st_1)

    return (labirint_vol_1,feiklab_st_1)   


def step_2(labirint,feiklab):
    


def randominfeik(feiklab,i):
    p = random.randint(0,len(list(feiklab.keys()))-1)
    i = list(feiklab.keys())[p]
    return i


def randomstep(feiklab,i,j,n,m):
    
    #проверил(0,1,1,1)
    if (((i % m == 0) or feiklab.get(i-1) != None)
        and i - m >= 0 and feiklab.get(i-m) == None
        and (i % m != m-1) and feiklab.get(i+1) == None
        and (i+m) <= n*m -1 and feiklab.get(i+m) == None):
            j = random.randint(2,4)
            i = if_I(i,n,m,j)
            return i,j
        
    #wp(0,0,0,1)
    elif ((i % m == 0 or feiklab.get(i-1) != None)
          and (i - m < 0 or feiklab.get(i-m) != None)
          and (i % m == m-1 or feiklab.get(i+1) != None)
          and (i+m) <= n*m -1 and feiklab.get(i+m) == None):
            j = 4
            i = if_I(i,n,m,j)
            return i,j
        
    #wp(0,1,0,1)   
    elif ((i % m == 0 or feiklab.get(i-1) != None)
          and i - m >= 0 and feiklab.get(i-m) == None
          and ((i % m == m-1) or feiklab.get(i+1) != None)
          and (i+m) <= n*m -1 and feiklab.get(i+m) == None):
            j = random.choice([2,4])
            i = if_I(i,n,m,j)
            return i,j

    #(0,0,1,0)
    elif ((i % m == 0 or feiklab.get(i-1) != None)
          and (i - m < 0 or feiklab.get(i-m) != None)
          and i % m != m-1 and feiklab.get(i+1) == None
          and ((i+m) > n*m -1 or feiklab.get(i+m) != None)):
            j = 3
            i = if_I(i,n,m,j)
            return i,j
        
    #(0,1,0,0)
    elif ((i % m == 0 or feiklab.get(i-1) != None)
          and i - m >= 0 and feiklab.get(i-m) == None
          and (i % m == m-1 or feiklab.get(i+1) != None)
          and (i+m > n*m -1 or feiklab.get(i+m) != None)):
            j = 2
            i = if_I(i,n,m,j)
            return i,j
        
    #(0,1,1,0)
    elif (((i % m == 0) or feiklab.get(i-1) != None)
          and i - m >= 0 and feiklab.get(i-m) == None
          and (i % m != m-1) and feiklab.get(i+1) == None
          and (((i+m) > n*m -1) or feiklab.get(i+m) != None)):
            j = random.randint(2,3)
            i = if_I(i,n,m,j)
            return i,j
        
    #(0,0,1,1)
    elif (((i % m == 0) or feiklab.get(i-1) != None)
          and (i - m < 0 or feiklab.get(i-m) != None)
          and (i % m != m-1) and feiklab.get(i+1) == None
          and (i+m) <= n*m -1 and feiklab.get(i+m) == None):
            j = random.randint(3,4)
            i = if_I(i,n,m,j)
            return i,j
        
    #(0,0,0,0)
    elif (((i % m == 0) or feiklab.get(i-1) != None)
          and (i - m < 0 or feiklab.get(i-m) != None)
          and (i % m == m-1 or feiklab.get(i+1) != None)
          and ((i+m) > n*m -1 or feiklab.get(i+m) != None)):
            j = 0
            i = int(randominfeik(feiklab,i))
            return i,j

    #(1000)
    elif (((i % m != 0) and feiklab.get(i-1) == None)
        and (i - m < 0 or feiklab.get(i-m) != None)
        and ((i % m == m-1) or feiklab.get(i+1) != None)
        and ((i+m) > n*m -1 or feiklab.get(i+m) != None)):
            j = 1
            i = if_I(i,n,m,j)
            return i,j
            
        
    #1001
    elif (((i % m != 0) and feiklab.get(i-1) == None)
        and (i - m < 0 or feiklab.get(i-m) != None)
        and ((i % m == m-1) or feiklab.get(i+1) != None)
        and ((i+m) <= n*m -1) and feiklab.get(i+m) == None):
            j = random.choice([1,4])
            i = if_I(i,n,m,j)
            return i,j
        
        
    #(1010)
    elif (((i % m != 0) and feiklab.get(i-1) == None)
        and (i - m < 0 or feiklab.get(i-m) != None)
        and (i % m != m-1) and feiklab.get(i+1) == None
        and (((i+m) > n*m -1) or feiklab.get(i+m) != None)):
            j = random.choice([1,3])
            i = if_I(i,n,m,j)
            return i,j


    #(1011)
    elif (i % m != 0 and feiklab.get(i-1) == None
        and (i - m < 0 or feiklab.get(i-m) != None)
        and i % m != m-1 and (feiklab.get(i+1) == None
        and (i+m) <= n*m -1 and (feiklab.get(i+m) == None))):
            j = random.choice([1,3,4])
            i = if_I(i,n,m,j)
            return i,j
        

    #(1100)
    elif (((i % m != 0) and feiklab.get(i-1) == None)
        and (i - m >= 0 and feiklab.get(i-m) == None)
        and ((i % m == m-1) or feiklab.get(i+1) != None)
        and ((i+m) > n*m -1 or feiklab.get(i+m) != None)):
            j = random.randint(1,2)
            i = if_I(i,n,m,j)
            return i,j
        
        

    #(1101)
    elif ((i % m != 0) and feiklab.get(i-1) == None
        and i - m >= 0 and feiklab.get(i-m) == None
        and ( (i % m == m-1) or feiklab.get(i+1) != None)
        and i+m <= n*m -1 and feiklab.get(i+m) == None):
            j = random.choice([1,2,4])
            i = if_I(i,n,m,j)
            return i,j
            
        

    #(1110)
    elif (((i % m != 0) and feiklab.get(i-1) == None)
        and (i - m >= 0 and feiklab.get(i-m) == None)
        and ((i % m != m-1) and feiklab.get(i+1) == None)
        and (((i+m) > n*m -1) or feiklab.get(i+m) != None)):
            j = random.randint(1,3)
            i = if_I(i,n,m,j)
            return i,j
    



def brok_wall(labirint,n,m,i,p):#Пробивание лабиринта
        
    if p == 1 and labirint[i] == 11:
        labirint[i] = 1
        return labirint
    
    elif p == 2 and labirint[i] == 11:
        labirint[i] = 10
        return labirint
    
    elif p == 3 and labirint[i-1] == 11:
        labirint[i-1] = 1
        return labirint
    
    elif p == 4 and labirint[i-m] == 11:
        labirint[i-m] = 10
        return labirint
    
    elif p == 1 and labirint[i] == 10:
        labirint[i] = 0
        return labirint
    
    elif p == 2 and labirint[i] == 10:
        labirint[i] = 10
        return labirint
    
    elif p == 3 and labirint[i-1] == 10:
        labirint[i-1] = 0
        return labirint
    
    elif p == 4 and labirint[i-m] == 10:
        labirint[i-m] = 10
        return labirint
    
    elif p == 1 and labirint[i] == 1:
        labirint[i] = 1
        return labirint
    
    elif p == 2 and labirint[i] == 1:
        labirint[i] = 0
        return labirint
    
    elif p == 3 and labirint[i-1] == 1:
        labirint[i-1] = 1
        return labirint
    
    elif p == 4 and labirint[i-m] == 1:
        labirint[i-m] = 0
        return labirint
    
    elif p == 1 and labirint[i] == 0:
        labirint[i] = 0
        return labirint
    
    elif p == 2 and labirint[i] == 0:
        labirint[i] = 0
        return labirint
    
    elif p == 3 and labirint[i-1] == 0:
        labirint[i-1] = 0
        return labirint
    
    elif p == 4 and labirint[i-m] == 0:
        labirint[i-m] = 0
        return labirint

      
def if_I(i,n,m,j):#получение нового i-ого

    if j == 1:
        return i - 1
        
    elif j == 2:
        return i - m
        
    elif j == 3:
        return i + 1

    elif j == 4:
        return i + m
                

def proverka_i_ogo(labirint,i,n,m,feiklab):#Для избежания лишних действий
    if ((labirint[i] == 0) and (labirint.get(i-m-1) == None or labirint[i-m-1] == 0) and (labirint.get(i-m) == None or labirint[i-m] == 0) and (labirint.get(i-1) == None or labirint[i-1] == 0)
        or ((labirint[i] == 0) and (labirint.get(i-m) == None or labirint[i-m] == 0) and (labirint.get(i-m+1) == None or labirint[i-m+1] == 0) and (labirint.get(i+1) == None or labirint[i+1] == 0))
        or ((labirint[i] == 0) and (labirint.get(i-1) == None or labirint[i-1] == 0) and (labirint.get(i+m-1) == None or labirint[i+m-1] == 0) and (labirint.get(i+m) == None or labirint[i+m] == 0))
        or ((labirint[i] == 0) and (labirint.get(i+1) == None or labirint[i+1] == 0) and (labirint.get(i+m) == None or labirint[i+m] == 0) and (labirint.get(i+m+1) == None or labirint[i+m+1] == 0))):
            p = random.randint(0,len(list(feiklab.keys()))-1)
            i = list(feiklab.keys())[p]
            return i
    else:
        return i
        
        

def main():
    file = "Enter.txt"
    #receipt our params
    size_n = port(file)[0]
    size_m = port(file)[1]
    
    generate_lab_step_one(size_n, size_m)

  

if __name__ == '__main__':
    main()
