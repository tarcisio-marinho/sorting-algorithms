#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

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

