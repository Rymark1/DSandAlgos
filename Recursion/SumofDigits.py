def sumOfDigits(n1):
    assert n1 >= 0 and int(n1) == n1, "The number must be a positive integer"
    if n1 <= 9:
        return n1
    return n1 % 10 + sumOfDigits(n1 // 10)


print(sumOfDigits(1234))