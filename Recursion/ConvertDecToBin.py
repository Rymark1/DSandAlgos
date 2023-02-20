def decToBin(n):
    assert int(n) == n and n >= 0, "Number must be a postive integer"
    if n == 0:
        return 0
    return n % 2 + 10 * decToBin(n // 2)


print(decToBin(10))
print(decToBin(11))
