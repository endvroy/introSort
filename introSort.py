from heapSort import heapSort
from quickSort import quickSort
from math import log2


def introSort(array, begin, end, *, depth=0, length=None):
    if depth < log2(length):
        quickSort(array, begin, end)
