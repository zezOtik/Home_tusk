# -*- coding: utf-8 -*-
import random

def port(self):#считывание файла
    p = open(self,'r',encoding = 'utf-8')
    strok=[]
    for line in p:
        line = line[:(len(line) - 1)] 
        strok.append(line)
    n = int(strok[0])
    m = int(strok[1])
    p.close()
    return n,m
    
def generate_lab_step_one(n,m):#нужно переписать проверку на полученную рандомное значение, если рандом привел нас втупик, выбросить нужно число
    labirint1 = dict()#создали хэш таблицу
    labirint1 = {i: 11 for i in range(n*m)}#забили ее 11

    feiklab = dict()
    feiklab[0] = 1
    
    i = 0#старт работы алгоритма
    p = 0#переменная для проверки random
    
    while(i != n * m - 1 ):#пока не равны значения работать
        value = i#переменная для того, чтобы когда функция вернулась не было опять i
        while(i == value):#цикл для изменения выбора перед ошибкой
            
            value_random  = random.randint(1,4)#нарандомил проход в другую клетку
            
            if p != value_random:#случай когда прошлая клетка была в том же направление
                i = if_I(i, n, m, value_random)# создали объект, точнее новое i
                checkdictfeik(feiklab,i,n,m,value_random)#проверка на посещение выброс нового значения
                p = value_random#сохранили проход
                
            else:#в случае совпада перекинули еще раз
                value_random = random.randint(1,4)#зарандомили
                i = if_I(i, n, m, value_random)#получили новую точку
                checkdictfeik(feiklab,i,n,m,value_random)#проверка на посещение но выброс нового значения
                p = value_random#сохранили проход
                
            
        i_broken(i,p,labirint1,m)#измененный dict
        feiklab[i] = 1

        i = checknazaxlyst(feiklab,labirint1,i,m,n)
        
    print(labirint1)
    #print(feiklab)

    
def checkdictfeik(feiklab,i,n,m,j):#проверка на посещение
    if feiklab.get(i) == None:
       return 1
    else:
       return if_I(i,n,m,j)


def checknazaxlyst(feiklab,labirint1,i,m,n):#проверка, если мы оказались в тупике, то есть захлыстнуло нас
    if ((feiklab.get(i+1) != None or labirint1.get(i+1) == None)
        and (feiklab.get(i-1) != None or labirint1.get(i-1) == None)
        and (feiklab.get(i+m) != None or labirint1.get(i+m) == None)
        and (feiklab.get(i-m) != None or labirint1.get(i-m) == None)):
            p = random.randint(0,len(list(feiklab.keys()))-1)
            i = list(feiklab.keys())[p]
            return i
    elif i == n * m -1:
        return i
    else:
        return i

"""
def potnaysymma(labirint1,p,m,i,n,j):#здесь творится грязь забыл об этом, понял это недавно, думаю о фиксе, в общем если мы пришли в вершину, в которой уже что-то меняли, вот беда
    if (i - m < 0 or i - 1 == -1):
        if_I(i,n,m,j)
        
    elif labirint1[i] == 11 and p == 1:
        labirint1[i] = 1
        return labirint1
    
    elif labirint1[i] == 11 and p == 2:
        labirint1[i] = 10
        return labirint1
    
    elif p == 3 and labirint1[i-1] == 11 and i - 1 > -1:
        labirint1[i-1] = 1
        return labirint1
    
    elif labirint1[i-m] == 11 and p == 4 and i - m > 0:
        labirint1[i-m] = 10
        return labirint1
    
    elif labirint1[i] == 10 and p == 1:
        labirint1[i] = 0
        return labirint1
    
    elif labirint1[i] == 10 and p == 2:
        labirint1[i] = 10
        return labirint1
    
    elif labirint1[i-1] == 10 and p == 3 and i - 1 > -1:
        labirint1[i-1] = 0
        return labirint1
    
    elif labirint1[i-m] == 10 and p == 4 and i - m > 0:
        labirint1[i-m] = 10
        return labirint1
    
    elif labirint1[i] == 1 and p == 1:
        labirint1[i] = 1
        return labirint1
    
    elif labirint1[i] == 1 and p == 2:
        labirint1[i] = 0
        return labirint1
    
    elif labirint1[i-1] == 1 and p == 3 and i - 1 > -1:
        labirint1[i-1] = 1
        return labirint1
    
    elif labirint1[i-m] == 1 and p == 4 and i - m > 0:
        labirint1[i-m] = 0
        return labirint1
    
    elif labirint1[i] == 0 and p == 1:
        labirint1[i] = 0
        return labirint1
    
    elif labirint1[i] == 0 and p == 2:
        labirint1[i] = 0
        return labirint1
    
    elif labirint1[i-1] == 0 and p == 3 and i - 1 > -1:
        labirint1[i-1] = 0
        return labirint1
    
    elif labirint1[i-m] == 0 and p == 4 and i - m > 0:
        labirint1[i-m] = 0
        return labirint1"""    
      
def if_I(i,n,m,j):#получение нового i-ого
    if j == 1:
        if (i % m) == 0:
            return i
        else:
            return i - 1
    elif j == 2:
        if (i // n) == 0 or (i == n):
            return i
        else:
            return i - m
    elif j == 3:
        if (i % m) == (m - 1):
            return i
        else:
            return i + 1
    else:
        if (i + m) > n * m - 1:
            return i
        else:
            return i + m



def i_broken(i,p,labirint1,m):#пробивка лабиринта
    if p == 1:#здесь пробивается
        labirint1[i] = 1
        return(labirint1)
    
    elif p == 2:#здесь пробивается
        labirint1[i] = 10
        return(labirint1)
    
    elif p == 3:#здесь пробивается
        labirint1[i-1] = 1
        return(labirint1)
    
    else:#здесь пробивается
        labirint1[i-m] = 10
        return(labirint1)



def main():
    file = "Enter.txt"
    #receipt our params
    size_n = port(file)[0]
    size_m = port(file)[1]
    

    
    



    generate_lab_step_one(size_n, size_m)

  

if __name__ == '__main__':
    main()
