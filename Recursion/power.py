# Write a function called power which accepts a base and an exponent. The function should return the power of the base
# to the exponent. This function should mimic the functionality of math.pow() - do not worry about negative bases
# and exponents.

def powerOfANumber(base, exp):
    assert int(exp) == exp, "The exponent must be an integer"
    if exp == 1:
        return base
    return base * powerOfANumber(base, exp-1)


print(powerOfANumber(4,2))
print(powerOfANumber(4,10))
print(powerOfANumber(4,2.5))
