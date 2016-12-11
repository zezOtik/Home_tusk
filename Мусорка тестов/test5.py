# -*- coding: utf-8 -*-

from Main_algoritm import randomstep
from Main_algoritm import if_I

def main():

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
    print(i2,j)
    if (i2 == 0 and j == 1) or (i2 == 2 and j == 3):
        print('Test5 is correct for values are i = 1, n = 4, m = 5 and blocks(6) are not empty')
    else:
        print('Test5 is not correct')
        

if __name__ == '__main__':
    main()

    
