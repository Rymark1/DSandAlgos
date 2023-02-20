# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each
# string in the array.

def capitalizeFirst(arr):
    l1 = []
    if len(arr) == 0:
        return l1
    for x in arr:
        l1.append(x[0].upper() + x[1:])
        return l1 + capitalizeFirst(arr[1:])


print(capitalizeFirst(["car", "taco", "banana"]))
