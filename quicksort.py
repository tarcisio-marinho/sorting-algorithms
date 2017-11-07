#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import time

def swap(lista, esq, dir):
    lista[esq], lista[dir] = lista[dir], lista[esq]

def partition(lista, esq, dir, pivot):
    while(esq <= dir):
        while(lista[esq] < pivot):
            esq+=1

        while(lista[dir] > pivot):
            dir-=1

        if(esq <= dir):
            swap(lista, esq, dir)
            esq+=1
            dir-=1

    return esq

def quicksort(lista, esq, dir):
    if(esq >= dir):
        return
    pivot = lista[ (esq + dir) / 2]
    index = partition(lista, esq, dir, pivot)
    quicksort(lista, esq, index-1)
    quicksort(lista, index, dir)

def main_quicksort(lista):
    quicksort(lista, 0, len(lista)-1)

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