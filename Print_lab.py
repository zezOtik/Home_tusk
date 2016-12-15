# -*- coding: utf-8 -*-
import ast

def port(self):#считывания из файла значения
    p = open(self,'r',encoding = 'utf-8')
    s = p.read()
    return s

def port1(self):#считывания из файла значения
    p = open(self,'r',encoding = 'utf-8')
    strok=[]
    for line in p:
        line = line[:(len(line) - 1)] 
        strok.append(line)
    n = int(strok[0])
    m = int(strok[1])
    xernya = int(strok[2])
    p.close()
    return n,m,xernya


def outport(self,stroka):#запись в файл значения
    p = open(self,'w',encoding = 'utf-8')
    p.write(stroka)
    p.close()
    

def printyxa(hashtable,i,stroka):
    if hashtable.get(i) == 0:
        stroka += '  '
        return stroka
    elif hashtable.get(i) == 1:
        stroka += '_ '
        return stroka
    elif hashtable.get(i) == 10:
        stroka += ' |'
        return stroka
    elif hashtable[i] == 11:
        stroka += '_|'
        return stroka
        
def main():
    stroka = ''
    p = ''
    s = port("Exit.txt")
    (n,m,xernya) = port1("Enter.txt")
    s = ast.literal_eval(s)
    i = 0
    while (i <= n*m - 1):
        if(i % m == m - 1):
            stroka += printyxa(s,i,p)
            stroka += '\n'
            p = ''
            i += 1
        else:
            stroka += printyxa(s,i,p)
            p = ''
            i += 1
    
    outport("123123.txt",stroka)
        
        
    

if __name__ == "__main__":
    main()
    
