#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

''' BIG O
melhor caso - O(n)
caso comum - O(n^2)
pior caso - O(n^2)
'''

def bubble_sort(lista, n):
    i = 0
    while(i < n-1):
        j = n-1
        while(j>i):
            if(lista[j] < lista[j - 1]):
                lista[j - 1], lista[j] = lista[j], lista[j - 1]
            j-=1
        i+=1

