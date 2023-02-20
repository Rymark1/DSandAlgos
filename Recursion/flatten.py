# Write a recursive function called flatten which accepts an array of arrays and returns a new array with all
# values flattened.

def flatten(arr):
    l1 = []
    for x in arr:
        if type(x) is list:
            l1.extend(flatten(x))
        else:
            l1.append(x)
    return l1


print(flatten([1, 2, 3, [4, 5]]))
print(flatten([1, [2, [3, 4], [[5]]]]))
print(flatten([[1], [2], [3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))
