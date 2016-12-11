# -*- coding: utf-8 -*-

from Main_algoritm import port
from Main_algoritm import kolvo_elem
from Main_algoritm import proverka_sosed
from Main_algoritm import if_I
from Main_algoritm import randomstep
from Main_algoritm import randomstep_for_last
from Main_algoritm import randominfeik
from Main_algoritm import brok_wall
from Main_algoritm import proverka_i_ogo


def test1():

    (n,m) = port("Enter.txt")

    Ntrue = 4
    Mtrue = 5

    if n != Ntrue or m != Mtrue:
        print("Your values is incorrect")

    
    else:
        print("test1 great")


def test2():
    hashtable1 = {i: 11 for i in range(4*5)}

    hashtable2 = {}
    
    kol_vo1 = kolvo_elem(hashtable1)

    kol_vo2 = kolvo_elem(hashtable2)

    if(kol_vo1 != 20):
        print("test2 is not correct for values 4 & 5")
    else:
        print("test2 is correct for values 4 & 5")

    if(kol_vo2 != -1):
        print("test2 is not correct for hash-table is empty")
    else:
        print("test2 is correct for for hash-table is empty")


def test3():

    size_n = 3
    
    size_m = 4
    
    i1 = 5
    
    i2 = 6
    
    hashtable = dict([(1,1),(6,3),(4,4),(9,7)])

    i1 = proverka_sosed(hashtable,i1,size_n,size_m)
    if i1 != -1:
        print('Test3 is not correct, when algoritm can not take value')
    else:
        print('Test3 is correct, when algoritm can not take value')
              
    i2 = proverka_sosed(hashtable,i2,size_n,size_m)

    if i2 == 6:
        print('Test3 is correct, when algoritm can take value')
    else:
        print('Test3 is not correct, when algoritm can not take value')


def test4():

    size_n = 4
    size_m = 5

    i = 7
    j = 3

    i1 = 8
    j1 = 2

    i2 = 9
    j2 = 1

    i3 = 14
    j3 = 4

    i = if_I(i,size_n,size_m,j)
    
    i1 = if_I(i1,size_n,size_m,j1)
    
    i2 = if_I(i2,size_n,size_m,j2)
    
    i3 = if_I(i3,size_n,size_m,j3)
    
    if i != 8:
        print("Test4 is not correct for values are i = 7 and j = 3 and n = 4 and m = 5, need 8 for true")
    else:
        print("Test4 is correct for values are i = 7 and j = 3 and n = 4 and m = 5")


    if i1 != 3:
        print("Test4 is not correct for values are i = 8 and j = 2 and n = 4 and m = 5, need 3 for true")
    else:
        print("Test4 is correct for values are i = 8 and j = 2 and n = 4 and m = 5")


    if i2 != 8:
        print("Test4 is not correct for values are i = 9 and j = 1 and n = 4 and m = 5, need 8 for true")
    else:
        print("Test4 is correct for values are i = 9 and j = 1 and n = 4 and m = 5")


    if i3 != 19:
        print("Test4 is not correct for values are i = 14 and j = 4 and n = 4 and m = 5, need 19 for true")
    else:
        print("Test4 is correct for values are i = 19 and j = 4 and n = 4 and m = 5")


def test5():

    size_n = 4
    size_m = 5

    i1 = 7

    i2 = 1
    
    hashtable = dict([(2,1),(6,3),(8,1)])

    (i1,j) = randomstep(hashtable,i1,size_n,size_m)
    
    if i1 == 12 and j == 4:
        print('Test5 is correct for values are i = 7, n = 4, m = 5 and blocks(2,6,8) are not empty')
    else:
        print("Test5 is not correct")

    (i2,j) = randomstep(hashtable,i2,size_n,size_m)

    if (i2 == 0 and j == 1) or (i2 == 2 and j == 3):
        print('Test5 is correct for values are i = 1, n = 4, m = 5 and blocks(6) are not empty')
    else:
        print('Test5 is not correct')


def test6():

    size_n = 4
    size_m = 5

    i1 = 0

    i2 = 4
    
    (i1,j) = randomstep_for_last(i1,size_n,size_m)
    if i1 == 1 and j == 3 or i1 == 5 and j == 4:
        print("Test6 is correct")
    else:
        print("Test6 is not correct")

    (i2,j) = randomstep_for_last(i2,size_n,size_m)
    if i2 == 3 and j == 1 or i2 == 9 and j == 4:
        print("Test6 is correct")
    else:
        print("Test6 is not correct")

        
def test7():

    hashtable = dict([(1,1),(6,3),(4,4),(9,7)])

    i = randominfeik(hashtable)

    if (i == 1) or (i == 6) or (i == 4) or (i == 9):
        print("Test7 is correct")
    else:
        print("Test7 is not correct")


def test8():

    hashtable = dict([(6,11),(12,10),(8,11),(2,1),(7,11)])

    size_n = 4
    size_m = 5

    i = 7
    j = 1#пошли в 7 справа, сломали в 7 правую стенку из 11 в 1

    hashtable = brok_wall(hashtable,size_n,size_m,i,j)
    if hashtable[i] == 1:
        print("Test8 is correct")
    else:
        print("Test8 is not correct")

    j = 4
    hashtable = brok_wall(hashtable,size_n,size_m,i,j)
    if hashtable[i-size_m] == 0:
        print("Test8 is correct")
    else:
        print("Test8 is not correct")


def test9():

    hashtable = dict([(6,0),(11,0),(8,0),(12,0),(7,0),(13,0),(3,0),(2,0),(1,0)])

    feiklab = dict([(15,1)])
    size_n = 4
    size_m = 5

    i = 7
    i = proverka_i_ogo(hashtable,i,size_n,size_m,feiklab)

    if i != 15:
        print("Test9 is not correct")
    else:
        print("Test9 is correct")



def main():

    
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    



if __name__ == '__main__':
    main()
