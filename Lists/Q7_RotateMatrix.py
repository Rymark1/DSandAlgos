# Given an NxN matrix, rotate it 90 degrees
#
#   1  2  3         7  4  1
#   4  5  6    ->   8  5  2
#   7  8  9         9  6  3
#
#
import numpy as np

def rotateMatrix(m1):
    n = len(m1)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top element
            top = m1[layer][i]
            # move left element to top
            m1[layer][i] = m1[-i-1][layer]
            # move bottom element to left
            m1[-i-1][layer] = m1[-layer-1][-i-1]
            # move right to bottom
            m1[-layer-1][-i-1] = m1[i][-layer-1]
            # move top to right
            m1[i][-layer-1] = top
    return m1


test1 = [[1,2,3],[4,5,6],[7,8,9]]
test2 = [[1,2],[3,4]]

print(test1)
rotateMatrix(test1)
print(test1)
rotateMatrix(test2)
print(test2)



#  m [0][0] -> m[0][2]
#  m [0][1] -> m[1][2]
#  m [0][2] -> m[2][2]
#  m [0][0] -> m[0][2]
#  m [0][0] -> m[0][2]
#  m [0][0] -> m[0][2]
#  m [0][0] -> m[0][2]
#  m [0][0] -> m[0][2]