# How to check if an array contains a number in Python
# This assumes the array is unsorted

import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def findNumber(array, nbr):
    for i in range(len(array)):
        if array[i] == nbr:
            print(i)


def findNumber1(array, nbr):
    for idx, i in enumerate(array):
        if i == nbr:
            print(idx)


findNumber(myArray,5)
findNumber1(myArray,5)
