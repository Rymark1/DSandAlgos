# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider
# commutative pairs.
#
# Example
#
#     pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
#     Output : ['2+5', '4+3', '3+4', '-2+9']
#
# Note:
# 4+3 comes from second and third elements from the main list.
# 3+4 comes from third and seventh elements from the main list.

def pairSum_n_squared(myList, s1):
    l1 = []
    for idx, i in enumerate(myList):
        for j in myList[idx+1:]:
            if i+j == s1:
                l1.append("{}+{}".format(i,j))
    return l1


def pairSum_N(myList ,s1):
    l1 = []
    diff = {}
    for i in myList:
        remain = s1 - i
        if remain in diff:
            l1.append("{}+{}".format(i,remain))
        diff[i] = i
    return l1


print(pairSum_n_squared([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
print(pairSum_N([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
Output: ['2+5', '4+3', '3+4', '-2+9']