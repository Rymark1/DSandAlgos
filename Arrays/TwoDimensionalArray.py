# day 1 - 11,15,10,6
# day 2 - 10,14,11,5
# day 3 - 12,17,12,8
# day 4 - 15,18,14,9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# Axis 1 means add a new column.  Axis 0 means add new row.
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

# The append method doesn't require an index to insert it.  Automatically at end
newTwoDArray1 = np.append(newTwoDArray, [[5, 6, 7, 8]], axis=0)
print(newTwoDArray1)


def accessElements(array, row, col):
    if row >= len(array) and col >= len(array[0]):
        print("Incorrect index")
    print(array[row][col])


accessElements(newTwoDArray1, 1, 1)
print("*" * 80)


def twoDimTraversal(array):
    for x in range(len(array)):
        for y in range(len(array[0])):
            print(array[x][y])


twoDimTraversal(newTwoDArray1)

print("*" * 80)


def searchForValue(array, value):
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == value:
                return f"Element found at row {x} column {y}"
    return "The value was not found"


print(searchForValue(newTwoDArray1, 18))
print(searchForValue(newTwoDArray1, 10000))

print("*" * 80)
test1 = np.delete(newTwoDArray1, 0, axis=0)
test2 = np.delete(test1, 0, axis=1)
print(newTwoDArray1)
print(test1)
print(test2)

# time and space complexities for two-dimensional array
# M is number of Rows, N is number of Columns
# Operation                        time complexity         space complexity
# Creating empty array                      O(1)                    O(MN)
# inserting a value in an array             O(1)/O(MN)              O(1)
# Traversing a given array                  O(MN)                   O(1)
# Accessing a given                         O(1)                    O(1)
# searching a given value                   O(MN)                   O(1)
# deleting a given value                    O(1)/O(MN)              O(1)
#
