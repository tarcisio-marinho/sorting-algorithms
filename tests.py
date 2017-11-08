#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import time
from quicksort import quick_sort
from selectionsort import selection_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
from bubblesort import bubble_sort
from timsort import tim_sort


def quicksort_piorcaso():
    def teste1():
        lista =[]

        for i in range(400000):
            lista.append(i)
        
        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 400000 (400 mil) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    def teste2():
        lista = []

        for i in range(4000000):
            lista.append(i)

        tempo = time.time()
        quick_sort(lista, 0, len(lista)-1)
        fim = time.time()
        print("[TESTE] 4000000 (4 milhoes) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    def teste3():
        lista = []

        for i in range(40000000):
            lista.append(i)

        tempo = time.time()
        quick_sort(lista, 0, len(lista)-1)
        fim = time.time()
        print("[TESTE] 400000000 (40 milhoes) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    print("Testando o pior caso do quicksort - O(n^2) - [Lista já ordenada]\n")
    teste1()
    teste2()
    teste3()
    print("Fim dos testes")

def merge_sort_test():
    lista = []

        for i in range(40000000):
            lista.append(i)

        tempo = time.time()
        merge_sort(lista)
        fim = time.time()
        print(str(fim - tempo))

if __name__ == "__main__":
    pass
    #quicksort_piorcaso()
    merge_sort_test()