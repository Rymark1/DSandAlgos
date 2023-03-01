# Write a function to find the duplicate number on given integer array/list.

# removeDuplicates([1, 1, 2, 2, 3, 4, 5])
# Output: [1, 2, 3, 4, 5]

def removeDupCheating(l1):
    return list(set(l1))


def removeDuplicates(myList):
    l1 = []
    for i in myList:
        if i not in l1:
            l1.append(i)
    return l1


test = [1, 1, 2, 2, 3, 4, 5]

print(removeDuplicates(test))
print(removeDupCheating(test))
