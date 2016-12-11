# -*- coding: utf-8 -*-

from Main_algoritm import randomstep_for_last
from Main_algoritm import if_I

def main():

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

        

if __name__ == '__main__':
    main()
