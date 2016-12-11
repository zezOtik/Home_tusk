# -*- coding: utf-8 -*-

from Main_algoritm import proverka_i_ogo

def main():

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
    


    
if __name__ == '__main__':
    main()
    
    

    
