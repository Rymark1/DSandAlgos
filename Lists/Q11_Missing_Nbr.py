#  Write a function to find the missing number in a given integer array of 1 to 100.

# missingNumber([1, 2, 3, 4, 6], 6)  # 5

def missingNumbersorted(myList, totalCount):
    for idx, i in enumerate(myList):
        if i != idx+1:
            return idx+1


def missingNumberunsorted(myList, totalCount):
    expectedsum = sum(range(len(myList)+2))
    actualsum = sum(myList)
    return expectedsum - actualsum


print(missingNumbersorted([1, 2, 3, 4, 6], 6))
print(missingNumberunsorted([1, 2, 3, 4, 6], 6))
