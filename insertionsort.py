#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

''' BIG O
melhor caso - O(n)
caso comum - O(n^2)
pior caso - O(n^2)
'''

def insertion_sort(lista, n):
    p = 1
    while(p<n):
        temp = lista[p]
        j=p
        while(j>0 and temp < lista[j - 1]):
            lista[j] = lista[j - 1] 
            j-=1
        lista[j] = temp
        p+=1

