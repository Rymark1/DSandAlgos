#  How to find the maximum product of two integers in the array where all elements are positive.
import time

import numpy as np

myArray = np.array([1,20,30,44,5,56,57,8,9,-100,10,31,12,13,14,35,16,27,58,19,-99,21])
myArray1 = np.array(range(10001))


def jessSolution(array):
    max_product = 0
    max_a = max_b = 0
    a = time.perf_counter()
    for idx, i in enumerate(array):
        for idx1, j in enumerate(array):
            if idx == idx1:
                pass
            elif i * j > max_product:
                max_product = i * j
                max_a = i
                max_b = j
    print(f"The max product is {max_a} * {max_b} = {max_a * max_b}")
    b = time.perf_counter()
    print(f"Time taken: {b - a}")


def maximumProduct(array):
    max_a = max_b = 0
    neg_max_a = neg_max_b = 0
    for i in array:
        if i < 0:
            if i < neg_max_a and neg_max_a >= neg_max_b:
                neg_max_a = i
            elif i < neg_max_b:
                neg_max_b = i
        elif i > max_a and max_a <= max_b:
            max_a = i
        elif i > max_b:
            max_b = i
    if neg_max_a * neg_max_b > max_a * max_b:
        print(f"The max product is {neg_max_a} * {neg_max_b} = {neg_max_a * neg_max_b}")
    else:
        print(f"The max product is {max_a} * {max_b} = {max_a * max_b}")


jessSolution(myArray)
print()
jessSolution(myArray1)
print()
maximumProduct(myArray)
print()
maximumProduct(myArray1)


