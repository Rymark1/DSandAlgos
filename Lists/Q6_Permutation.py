#  Check if 2 strings are permutations of each other.

l11 = ("taser")
l22 = ("resta")
l33 = ("taser")
l44 = ("restac")


def permutationdicts(l1, l2):
    d1 = {}
    d2 = {}
    for i in l1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for j in l2:
        if j in d2:
            d2[j] += 1
        else:
            d2[j] = 1
    for item in d1:
        if item in d2:
            if d2[item] != d1[item]:
                return False
        else:
            return False
    for item in d2:
        if item in d1:
            if d2[item] != d1[item]:
                return False
        else:
            return False
    return True


def permutationsorted(l1,l2):
    if sorted(l1) == sorted(l2):
        return True
    else:
        return False


print(permutationdicts(l11,l22))
print(permutationdicts(l33,l44))
print(permutationsorted(l11,l22))
print(permutationsorted(l33,l44))
