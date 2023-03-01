# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.

# myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
# firstSecond(myList)  # 90 87

def firstSecond(l1):
    val_score = 0
    sal_score = 0
    for grade in l1:
        if val_score < grade:
            sal_score = val_score
            val_score = grade
        elif sal_score < grade:
            sal_score = grade
    return (val_score, sal_score)


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(firstSecond(myList))  # 90 87
