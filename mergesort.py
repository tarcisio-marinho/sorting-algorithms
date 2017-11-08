#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

''' BIG O
melhor caso - O(n log(n))
caso comum - O(n log(n))
pior caso - O(n log(n))
'''

def merge_sort(obj):
    if len(obj) > 1:
        mid = len(obj)/2
        left = obj[:mid]
        right = obj[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                obj[k] = left[i]
                i += 1
            else:
                obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            obj[k] = right[j]
            j += 1
            k += 1
