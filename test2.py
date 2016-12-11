# -*- coding: utf-8 -*-

from Main_algoritm import kolvo_elem

def main():
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

if __name__ == '__main__':
    main()
        
    
    
