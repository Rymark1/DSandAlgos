#  Is Unique: Implement an alogrithm to determine if ta list has all unique characters, using a python list
import time

myList = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
myList1 = range(30001)


def isUniquelists(l1):
    a = time.perf_counter()
    for idx,i in enumerate(l1):
        for j in l1[idx+1:]:
            if i == j:
                b = time.perf_counter()
                print(f"Time taken = {b-a}")
                return True
    b = time.perf_counter()
    print(f"Time taken = {b - a}")
    return False


def isUniquedicts(l1):
    a = time.perf_counter()
    d1 = {}
    for idx,i in enumerate(l1):
        if i in d1:
            b = time.perf_counter()
            print(f"Time taken = {b - a}")
            return True
        else:
            d1[i] = i
    b = time.perf_counter()
    print(f"Time taken = {b - a}")
    return False


print(sorted(myList))
print(isUniquelists(myList))
print(isUniquelists(myList1))

print(isUniquedicts(myList))
print(isUniquedicts(myList1))
