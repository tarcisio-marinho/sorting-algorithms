#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# based on insertion sort and merge sort

''' BIG O
melhor caso - O(n)
caso comum - O(n log(n))
pior caso - O(n log(n))
'''

def insertion_sort(lista, esq, dir):
    i = esq + 1
    while(i <= dir):
        temp = lista[i]

        j = i - 1
        while(lista[j] > temp and j >= esq):
            lista[j + 1] = lista[j]
            j-=1
        lista[j + 1] = temp
        i+=1

def merge(lista, l, m, r):
    len1 = m - l + 1
    len2 = r - m
    left = []
    right = []
    for i in range(len1 + 1):
        left[i] = lista[l + i]
    for i in range(len2 + 1):
        right[i] = lista[m + l + i]

    i = 0
    j = 0
    k = l
    while(i < len1 and j < len2):
        if(left[i] <= right[j]):
            lista[k] = left[i]
            i+=1
        else:
            lista[k] = right[j]
            j+=1
        k+=1

    while(i < len1):
        lista[k] = left[i]
        k+=1
        i+=1

    while(j < len2):
        lista[k] = right[j]
        k+=1
        j+=1




def tim_sort(lista, n):
    i = 0
    while(i < n):
        insertion_sort(lista, i, min((i+31), (n-1)))
        i+=32

    size = 32
    while(size < n):
        left = 0
        while(left < n):
            mid = left + size -1
            right = min((left + 2*size - 1), (n-1))

            merge(lista, left, mid, right)

            left+= 2*size

        size = 2*size

