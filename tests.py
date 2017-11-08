#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import time
from quicksort import quick_sort
from selectionsort import selection_sort
from insertionsort import insertion_sort

def quick_vs_tim():
    # PIOR CASO 
    lista =[]
    lista2 = []

    # 40MILHOES DE INTEIROS 
    for i in range(40000000):
        lista.append(i)

    lista2 = lista

    tempo = time.time()
    lista2.sort()
    fim = time.time()

    print "tim sort: " + str(fim - tempo) # BIG O NO PIOR CASO É O(NlogN)

    tempo = time.time()
    main_quicksort(lista)
    fim = time.time()

    print "meu quicksort : " + str(fim - tempo) # BIG O NO PIOR CASO É O(N²)

def quick_vs_merge():
    pass


if __name__ == "__main__":
    pass

    #lista = [10, 20, 30, 2]
    #quicksort(lista, 0, len(lista)-1)
    #print(lista)