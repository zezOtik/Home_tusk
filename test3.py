# -*- coding: utf-8 -*-

from Main_algoritm import proverka_sosed

def main():

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
              

    
if __name__ == '__main__':
    main()

    
