from heapSort import heapSort
from quickSort import partition
from math import log2


def introSort(array, begin=0, end=None, depth=0, *, reverse=False):
    if end is None:
        end = len(array) - 1

    if depth < log2(len(array)):
        if begin < end:
            mid = partition(array, begin, end, reverse=reverse)
            introSort(array, begin, mid - 1, depth + 1, reverse=reverse)
            introSort(array, mid + 1, end, depth + 1, reverse=reverse)
    else:
        array[begin:end + 1] = heapSort(array[begin:end + 1], reverse=reverse)


if __name__ == '__main__':
    a = [3, 4, 6, 3, 1, 2, 5, 9]
    introSort(a)
    print(a)
