#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import random
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

def quicksort_average():
    def teste1():
        lista = []

        for i in range(40000):
            aleatorio = random.randint(0, 40000)
            lista.append(aleatorio)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 40000 (40 mil) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    def teste2():
        lista = []

        for i in range(400000):
            aleatorio = random.randint(0, 400000)
            lista.append(aleatorio)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 400000 (400 mil) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")
    
    def teste3():
        lista = []

        for i in range(4000000):
            aleatorio = random.randint(0, 4000000)
            lista.append(aleatorio)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 4000000 (4 milhoes) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    def teste4():
        lista = []

        for i in range(40000000):
            aleatorio = random.randint(0, 40000000)
            lista.append(aleatorio)

        tempo = time.time()
        quick_sort(lista, 0, len(lista) - 1)
        fim = time.time()
        print("[TESTE] 40000000 (40 milhoes) inteiros\n[TEMPO] "+ str(fim - tempo))
        print("\n")

    print("Teste com numeros aleatórios - caso geral - O(n log(n))\n")
    print("Teste1: \n")
    teste1()
    print("Teste2: \n")
    teste2()
    print("Teste3: \n")
    teste3()
    print("Teste4: \n")
    teste4()
    print("Fim dos testes")



def quicksort_vs_bubble():
    lista = []

    for i in range(40000):
        aleatorio = random.randint(0, 40000)
        lista.append(aleatorio)

    tempo = time.time()
    quick_sort(lista, 0, len(lista) - 1)
    fim = time.time()
    print("[QUICKSORT] 40000 (40 mil) inteiros Aleatorios\n[TEMPO] "+ str(fim - tempo))
    
    lista = []

    for i in range(40000):
        aleatorio = random.randint(0, 40000)
        lista.append(aleatorio)

    tempo = time.time()
    bubble_sort(lista, len(lista))
    fim = time.time()
    print("[BUBBLESORT] 40000 (40 mil) inteiros Aleatorios\n[TEMPO] "+ str(fim - tempo))
    
    print("\n")


def quicksort_vs_mergesort():
    lista = []

    for i in range(4000000):
        aleatorio = random.randint(0, 4000000)
        lista.append(aleatorio)

    tempo = time.time()
    quick_sort(lista, 0, len(lista) - 1)
    fim = time.time()
    print("[QUICKSORT] 4000000 (4 milhoes) inteiros Aleatorios\n[TEMPO] "+ str(fim - tempo))
    
    lista = []

    for i in range(4000000):
        aleatorio = random.randint(0, 4000000)
        lista.append(aleatorio)

    tempo = time.time()
    merge_sort(lista)
    fim = time.time()
    print("[MERGESORT] 4000000 (4 milhoes) inteiros Aleatorios\n[TEMPO] "+ str(fim - tempo))
    print("\n")

def quick_vs_selec_vs_insr():
    lista = []

    for i in range(40000):
        aleatorio = random.randint(0, 40000)
        lista.append(aleatorio)
    
    tempo = time.time()
    quick_sort(lista, 0, len(lista) - 1)
    fim = time.time()
    print("[QUICKSORT] 40000 (40 mil) inteiros Aleatorios\n[TEMPO] "+ str(fim - tempo))
    
    lista = []

    for i in range(40000):
        aleatorio = random.randint(0, 40000)
        lista.append(aleatorio)
    
    tempo = time.time()
    selection_sort(lista, len(lista))
    fim = time.time()
    print("[SELECTIONSORT] 40000 (40 mil) inteiros Aleatorios\n[TEMPO] "+ str(fim - tempo))
    
    lista = []

    for i in range(40000):
        aleatorio = random.randint(0, 40000)
        lista.append(aleatorio)

    tempo = time.time()
    insertion_sort(lista, len(lista))
    fim = time.time()
    print("[INSERTIONSORT] 40000 (40 mil) inteiros Aleatorios\n[TEMPO] "+ str(fim - tempo))
    print("\n")

if __name__ == "__main__":
    quicksort_piorcaso()
    quicksort_average()
    quicksort_vs_bubble()
    quicksort_vs_mergesort()
    quick_vs_selec_vs_insr()