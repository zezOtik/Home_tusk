# -*- coding: utf-8 -*-

from Main_algoritm import if_I

def main():

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


if __name__ == '__main__':
    main()

    
