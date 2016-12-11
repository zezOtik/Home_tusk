# -*- coding: utf-8 -*-

from Main_algoritm import randominfeik
from Main_algoritm import kolvo_elem

def main():


    hashtable = dict([(1,1),(6,3),(4,4),(9,7)])

    i = randominfeik(hashtable)

    if (i == 1) or (i == 6) or (i == 4) or (i == 9):
        print("Test7 is correct")
    else:
        print("Test7 is not correct")

if __name__ == '__main__':
    main()

    
    

    
