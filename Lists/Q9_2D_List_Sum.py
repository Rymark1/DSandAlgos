# Given 2D list calculate the sum of diagonal elements.

# myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sumDiagonal(myList2D)  # 15  [1 + 5 + 9]


def sumDiagonal(a):
    answer = 0
    for i in range(len(a)):
        answer += a[i][i]
    return answer


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sumDiagonal(myList2D))  # 15  [1 + 5 + 9]
