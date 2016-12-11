# -*- coding: utf-8 -*-

from Main_algoritm import port

def main():

    (n,m) = port("Enter.txt")

    print(n,m)
    Ntrue = 4
    Mtrue = 5


    if n != Ntrue or m != Mtrue:
        print("Your values is incorrect")

    
    else:
        print("test1 great")

    

if __name__ == '__main__':
    main()
