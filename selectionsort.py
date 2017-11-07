#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

def selection_sort(lista, n):
    i = 0
    while(i<n):
        j=i+1
        min = i
        while(j<n):
            if(lista[j] < lista[min]):
                min = j 
            j+=1

        lista[i], lista[min] = lista[min], lista[i]
        i+=1

