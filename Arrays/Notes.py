# Arrays are limited by a certain type.  We store a specific type of data in each spot within the array.
# All items in the array are in a row within the array.
# Each item can be referenced individually by its location.
# The size of the box is fixed and cannot be modified.
#
# There are 2 types of arrays.  They can be one dimensional or multidimensional.
# One dimensional arrays have one row and are accessed based on their postiion number.
# 2 dimensional arrays have multiple arrays and a depth of 0.  You need to reference both the row and position number
# in order to access the data.
#
# Multidimensional arrays have multiple depths and to access their data, you must reference the depth path and the
# position.  Each level of array is made up of n-1 of the lower level arrays.  For example - 3 dimension arrays are
# made up of 3 2 dimensional arrays, which are made up of 1 dimension arrays.
#
# When one dim arrays get assigned to memory, they get put into a continuous section of memory for ease of reads.
# When multi dim arrays get assigned to memory, it flattens out the arrays and writes them into continous points in
# memory.  For example, if there are 3 rows in a 2 dim array, the memory would be written in order row1, row2, row3
# directly in order.
#
# To create an array, you must assign it to a variable, define the datatype, then define the size.
# In python, you import array into the program and then the constructor is:
# arrayName = array(typecode, [initalizers]
#

from array import *

arr1 = array("i",[1,2,3,4,5,6])
print(arr1)

arr2 = array("d",[1.1,2.2,3.3,4.4,5.5,6.6])
print(arr2)

print(arr1)
arr1.insert(0,0)
print(arr1)
arr1.insert(0,2)
print(arr1)

# Time complexity is O(N) if you insert at the beginning because it needs to iterate through all elements to shift them.
# Time complexity is O(1) if you insert at the end because nothing needs to shift.

def traverseArray(array):
    for i in array:
        print(i)


traverseArray(arr1)

# time and space complexities for one dimensional array
# Operation                        time complexity         space complexity
# Creating empty array                      O(1)                    O(N)
# inserting a value in an array             O(1)/O(N)               O(1)
# Traversing a given array                  O(N)                    O(1)
# Accessing a given                         O(1)                    O(1)
# searching a given value                   O(N)                    O(1)
# deleting a given value                    O(1)/O(N)               O(1)
#

