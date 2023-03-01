#  Write a function called middle that takes a list and returns a new list that contains all but the first and
#  last elements.
#
#     myList = [1, 2, 3, 4]
#     middle(myList)  # [2,3]

def middle(lst):
    temp = list.copy(lst)
    temp.pop()
    return temp[1:]


myList = [1, 2, 3, 4]
print(middle(myList))  # [2,3]
