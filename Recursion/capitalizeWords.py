# Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each
# word capitalized.

def capitalizeWords(arr):
    l1 = []
    if len(arr) == 0:
        return l1
    l1.append(arr[0].upper())
    return l1 + capitalizeWords(arr[1:])


words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words))
