# -*- coding: utf-8 -*-

from Main_algoritm import brok_wall

def main():

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

    
    


    
if __name__ == '__main__':
    main()
    
    

    
