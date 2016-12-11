# -*- coding: utf-8 -*-
import random
import math

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

    
def generate_lab_step_one(labirint_main,labirint_posetil,labirint_ne_posetil,size_n, size_m):#Шаг 1 , строим проход от 0 до н*м -1
    
    labirint_ne_posetil.pop(0)#Отметили, что вершину 0 посетили

    labirint_posetil[0] = 1#Отметили, что вершину 0 посетили
    
    i = 0#старт работы алгоритма
    
    while(i != size_n * size_m - 1 ):#пока не равны значения работать
        #проверка на возможную ошибку 
        (i,j) = randomstep(labirint_posetil,i,size_n,size_m)#выбор случайного значения прохода
        if j != 0:           
            brok_wall(labirint_main, size_n, size_m, i, j)#сломали стенку
            labirint_posetil[i] = 1#Отметили вершину i-посещенной
            labirint_ne_posetil.pop(i)#Отметили вершину i-посещенной
            i = proverka_i_ogo(labirint_main,i,size_n,size_m,labirint_posetil)#проверка на то, что мы сломали много стенок и получилось область где 4 смежных ячейки с значениями 0
        else:
            i = proverka_i_ogo(labirint_main,i,size_n,size_m,labirint_posetil)

    return labirint_main,labirint_posetil,labirint_ne_posetil
    


def step_2(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m):#Шаг 2 от прошедших вершин идем(Здесь настраивается сложность)

    if kolvo_elem(labirint_ne_posetil) != -1:
        
        random_kol = math.trunc(math.sqrt(kolvo_elem(labirint_posetil)))
        
        while(random_kol != 0):

            i = randominfeik(labirint_posetil)
            
            i = proverka_sosed(labirint_posetil,i,size_n,size_m)

            while(i != -1):
                labirint_posetil[i] = 1
                
                (i,j) = randomstep(labirint_posetil,i,size_n,size_m)
             

                labirint_main = brok_wall(labirint_main, size_n, size_m, i, j)

                if labirint_ne_posetil.get(i) == None:

                    break
                else:
                    labirint_ne_posetil.pop(i)
                i = proverka_sosed(labirint_posetil,i,size_n,size_m)
            random_kol -= 1
        return labirint_main,labirint_posetil,labirint_ne_posetil
    else:
        return labirint_main,labirint_posetil,labirint_ne_posetil


def step_3(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m):

    while (kolvo_elem(labirint_ne_posetil) != -1):

        i =  randominfeik(labirint_ne_posetil)
 
        labirint_ne_posetil.pop(i)
        while(labirint_posetil.get(i) == None):
            labirint_posetil[i] = 1
            (i,j) = randomstep_for_last(i,size_n,size_m)
            labirint_main = brok_wall(labirint_main,size_n,size_m,i,j)
            
            if labirint_ne_posetil.get(i) == None:
                break
            else:
                labirint_ne_posetil.pop(i)            
    return labirint_main
      

def kolvo_elem(hashtable):#получение количество значений в хэш-таблице
    kol_vo = len(list(hashtable.keys()))
    if kol_vo == 0:
        kol_vo = -1
        return kol_vo
    else:
        return kol_vo
    


def randominfeik(hashtable):#Вывод рандомной уже посещенной клетки
    p = random.randint(0,kolvo_elem(hashtable)-1)
    i = list(hashtable.keys())[p]
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
          and ((i+size_m) > size_n*size_m -1 or hashtable.get(i+size_m) != None)):
            j = 0
            i = int(randominfeik(hashtable))
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
    
def randomstep_for_last(i,size_n,size_m):#По входящим данным выбирает куда следует стрелка пробивания стенок, для шага 3
    
    #проверил(0,1,1,1)
    if (i % size_m == 0) and (i - size_m >= 0) and (i % size_m != size_m-1) and (i+size_m <= size_n*size_m -1):
            j = random.randint(2,4)
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #wp(0,0,0,1)
    elif (i % size_m == 0) and (i - size_m < 0) and (i % size_m == size_m-1) and (i+size_m <= size_n*size_m -1):
            j = 4
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #wp(0,1,0,1)   
    elif (i % size_m == 0) and (i - size_m >= 0) and (i % size_m == size_m-1) and (i + size_m <= size_n*size_m -1):
            j = random.choice([2,4])
            i = if_I(i,size_n,size_m,j)
            return i,j

    #(0,0,1,0)
    elif (i % size_m == 0) and (i - size_m < 0) and (i % size_m != size_m-1) and (i + size_m > size_n*size_m -1):
            j = 3
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #(0,1,0,0)
    elif (i % size_m == 0) and (i - size_m >= 0) and (i % size_m == size_m-1) and (i+size_m > size_n*size_m -1):
            j = 2
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #(0,1,1,0)
    elif (i % size_m == 0) and (i - size_m >= 0) and (i % size_m != size_m-1) and (i + size_m > size_n*size_m -1):
            j = random.randint(2,3)
            i = if_I(i,size_n,size_m,j)
            return i,j
        
    #(0,0,1,1)
    elif (i % size_m == 0) and (i - size_m < 0) and (i % size_m != size_m-1) and (i + size_m <= size_n*size_m -1):
            j = random.randint(3,4)
            i = if_I(i,size_n,size_m,j)
            return i,j

    #(1000)
    elif (i % size_m != 0) and (i - size_m < 0) and (i % size_m == size_m-1) and (i + size_m > size_n*size_m -1):
            j = 1
            i = if_I(i,size_n,size_m,j)
            return i,j
            
        
    #1001
    elif (i % size_m != 0) and (i - size_m < 0) and (i % size_m == size_m-1) and (i+size_m <= size_n*size_m -1):
            j = random.choice([1,4])
            i = if_I(i,size_n,size_m,j)
            return i,j
        
        
    #(1010)
    elif (i % size_m != 0) and (i - size_m < 0) and (i % size_m != size_m-1) and (i+size_m > size_n*size_m -1):
            j = random.choice([1,3])
            i = if_I(i,size_n,size_m,j)
            return i,j


    #(1011)
    elif (i % size_m != 0) and (i - size_m < 0) and (i % size_m != size_m-1) and (i + size_m <= size_n*size_m -1):
            j = random.choice([1,3,4])
            i = if_I(i,size_n,size_m,j)
            return i,j
        

    #(1100)
    elif (i % size_m != 0) and (i - size_m >= 0) and (i % size_m == size_m-1) and (i+size_m > size_n*size_m -1):
            j = random.randint(1,2)
            i = if_I(i,size_n,size_m,j)
            return i,j
        
        
    #(1101)
    elif (i % size_m != 0) and (i - size_m >= 0) and (i % size_m == size_m-1) and (i+size_m <= size_n*size_m -1):
            j = random.choice([1,2,4])
            i = if_I(i,size_n,size_m,j)
            return i,j
            
        
    #(1110)
    elif (i % size_m != 0) and (i - size_m >= 0) and (i % size_m != size_m-1) and (i+size_m > size_n*size_m -1):
            j = random.randint(1,3)
            i = if_I(i,size_n,size_m,j)
            return i,j
    #(1111)
    elif (i % size_m != 0) and (i - size_m >= 0) and (i % size_m != size_m-1) and (i+size_m <= size_n*size_m -1):
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
        
def proverka_sosed(feiklab,i,n,m):
    if (((i % m == 0) or feiklab.get(i-1) != None) and (i - m < 0 or feiklab.get(i-m) != None) and (i % m == m-1 or feiklab.get(i+1) != None) and ((i+m) > n*m -1 or feiklab.get(i+m) != None)):
        i = -1
        return i
    else:
        return i

    
def main():
    file = "Enter.txt"

    #receipt our params
    (size_n, size_m) = port(file)

    labirint_main = dict()#создали хэш таблицу основная
    labirint_main = {i: 11 for i in range(size_n*size_m)}#забили ее 11

    labirint_ne_posetil = dict()#хэш-табл не посещенных
    labirint_ne_posetil = {i: 1 for i in range(size_n*size_m)}

    labirint_posetil = dict()#хэш-таблица для посещенных
   
    (labirint_main,labirint_posetil,labirint_ne_posetil) = (generate_lab_step_one(labirint_main,labirint_posetil,labirint_ne_posetil,size_n, size_m))

    (labirint_main,labirint_posetil,labirint_ne_posetil) = (step_2(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m))
    
    labirint_main = step_3(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m)

    print(labirint_main)
    

  

if __name__ == '__main__':
    main()
