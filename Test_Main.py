# -*- coding: utf-8 -*-

from Main_algoritm import *

def test_port():

    (n,m,vershiny) = port("Enter.txt")

    Ntrue = 10
    Mtrue = 10
    Vtrue = 5

    if n != Ntrue or m != Mtrue or vershiny != Vtrue:
        print("Your values is incorrect")
    else:
        print("test_port great")

def test_kolvo():
    hashtable1 = {i: 11 for i in range(4*5)}

    hashtable2 = {}
    
    kol_vo1 = kolvo_elem(hashtable1)

    kol_vo2 = kolvo_elem(hashtable2)

    if(kol_vo1 != 20):
        print("test_kolvo is not correct for values 4 & 5")
    else:
        print("test_kolve is correct for values 4 & 5")

    if(kol_vo2 != 0):
        print("test_kolve is not correct for hash-table is empty")
    else:
        print("test_kolvo is correct for for hash-table is empty")

def test_if_I():

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
        print("Test_if_I is not correct for values are i = 7 and j = 3 and n = 4 and m = 5, need 8 for true")
    else:
        print("Test_if_I is correct for values are i = 7 and j = 3 and n = 4 and m = 5")


    if i1 != 3:
        print("Test_if_I is not correct for values are i = 8 and j = 2 and n = 4 and m = 5, need 3 for true")
    else:
        print("Test_if_I is correct for values are i = 8 and j = 2 and n = 4 and m = 5")


    if i2 != 8:
        print("Test_if_I is not correct for values are i = 9 and j = 1 and n = 4 and m = 5, need 8 for true")
    else:
        print("Test3 is correct for values are i = 9 and j = 1 and n = 4 and m = 5")


    if i3 != 19:
        print("Test_if_I is not correct for values are i = 14 and j = 4 and n = 4 and m = 5, need 19 for true")
    else:
        print("Test_if_I is correct for values are i = 19 and j = 4 and n = 4 and m = 5")

def test_randomstep():

    size_n = 4
    size_m = 5

    i1 = 7

    i2 = 1
    
    hashtable = dict([(2,1),(6,3),(8,1)])

    (i1,j) = randomstep(hashtable,i1,size_n,size_m)
    
    if i1 == 12 and j == 4:
        print('Test_randomstep is correct for values are i = 7, n = 4, m = 5 and blocks(2,6,8) are not empty')
    else:
        print("Test_randomstep is not correct")

    (i2,j) = randomstep(hashtable,i2,size_n,size_m)

    if (i2 == 0 and j == 1) or (i2 == 2 and j == 3):
        print('Test_randomstep is correct for values are i = 1, n = 4, m = 5 and blocks(6) are not empty')
    else:
        print('Test_randomstep is not correct')
    
def test_randominfeik():

    hashtable = dict([(0,1),(2,3),(3,4),(1,7)])
    size_n = 2
    size_m = 2
    i = randominfeik(hashtable,size_n,size_m)

    if (i == 1) or (i == 0) or (i == 2) or (i == 3):
        print("Test_randominfeik is correct")
    else:
        print("Test_randominfeik is not correct")

def test_brokwall():

    hashtable = dict([(6,11),(12,10),(8,11),(2,1),(7,11)])

    size_n = 4
    size_m = 5

    i = 7
    j = 1#пошли в 7 справа, сломали в 7 правую стенку из 11 в 1

    hashtable = brok_wall(hashtable,size_n,size_m,i,j)
    if hashtable[i] == 1:
        print("Test_brokwall is correct")
    else:
        print("Test_brokwall is not correct")

    j = 4
    hashtable = brok_wall(hashtable,size_n,size_m,i,j)
    if hashtable[i-size_m] == 0:
        print("Test_brokwall is correct")
    else:
        print("Test_brokwall is not correct")

def test_outport():
    hashtable = dict([(6,0),(7,0),(10,0),(102,0)])
    
    outport("Exit.txt",hashtable)
    p = open("Exit.txt",'r',encoding = 'utf-8')
    
    strok = p.read()
    hashtable = str(hashtable)
    
    if strok == hashtable:
        print('Test_outport is great')
    else:
        print('Test_outport is bad')

def test_generate_lab_step_one():
    
    hashtable = dict([(3,1),(4,1),(5,1),(7,1),(8,1),(9,1),(11,1),(12,1),(13,1),(0,11),(1,11),(2,11),(15,11),(6,11),(10,11),(14,11)])
    hashtable_posetil = dict([(3,1),(4,1),(5,1),(7,1),(8,1),(9,1),(11,1),(12,1),(13,1)])
    hashtable_ne_posetil = dict([(0,1),(1,1),(2,1),(15,1),(6,1),(10,1),(14,1)])
    
    size_n = 4
    size_m = 4
    
    (hashtable,hashtable_posetil,hashtable_ne_posetil) = generate_lab_step_one(hashtable,hashtable_posetil,hashtable_ne_posetil,size_n,size_m)
    test_hashtable = dict([(3,1),(4,1),(5,1),(7,1),(8,1),(9,1),(11,1),(12,1),(13,1),(0,1),(1,1),(2,10),(15,11),(6,10),(10,10),(14,1)])
    if hashtable == test_hashtable:
        print('Test_generate_lab_step_one is correct')
    else:
        print('Test is not correct')
    
def test_vypystit():

    i = 3
    j = 3
    size_m = 4
    labirint_ne_posetil = dict([(0,1),(1,1),(2,1)])
    labirint_posetil = dict([(0,1),(1,1)])
    test_hashtable_ne_posetil = dict([(0,1),(1,1)])
    test_hashtable_posetil = dict([(0,1),(1,1),(2,1)])
    
    
    (labirint_ne_posetil,labirint_posetil) = vypystit(i,j,labirint_ne_posetil,size_m,labirint_posetil)
    if labirint_ne_posetil == test_hashtable_ne_posetil and labirint_posetil ==  test_hashtable_posetil:
        print('Test vypystit is correct')
    else:
        print('Test vypystit is not correct')

def test_check_soseda():
    
    size_n = 3
    size_m = 3

    i = 4
    j = 0
    
    hashtable = dict([(5,1),(7,1)])
    labirint_ne_posetil = dict([(1,1),(3,1)])

    (i,j) = check_soseda(hashtable,size_n,size_m,i,labirint_ne_posetil)
    if i == 5 and j == 3 or i == 7 and j == 4:
        print('Test_check_soseda is correct')
    else:
        print('Test_check_soseda is not correct')

def test_step3():

    labirint_main = dict([(0,1),(1,10),(2,11),(3,1),(4,0),(5,11),(6,1),(7,1),(8,11)])

    labirint_posetil = dict([(0,1),(1,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1)])

    labirint_ne_posetil = dict([(2,1)])

    size_n = 3
    size_m = 3

    test_labirint_main1 = dict([(0,1),(1,0),(2,11),(3,1),(4,0),(5,11),(6,1),(7,1),(8,11)])
    test_labirint_main2 = dict([(0,1),(1,10),(2,10),(3,1),(4,0),(5,11),(6,1),(7,1),(8,11)])

    labirint_main = step_3(labirint_main,labirint_posetil,labirint_ne_posetil,size_n,size_m)
    print(labirint_main)
    if labirint_main == test_labirint_main1 or labirint_main == test_labirint_main2:
        print('Test_step3 is correct')
    else:
        print('Test_step3 is not correct')

def main():

    test_port()
    
    test_kolvo()
    
    test_if_I()
    
    test_randomstep()
    
    test_randominfeik()
    
    test_brokwall()
    
    test_outport()
    
    test_generate_lab_step_one()

    test_vypystit()

    test_check_soseda()

    test_step3()



if __name__ == '__main__':
    main()
