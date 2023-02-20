# Write a recursive function called reverse which accepts a string and returns a new string in reverse.

def reverse(strng):
    if len(strng) == 1:
        return strng
    return reverse(strng[1:]) +strng[0]


print(reverse('python'))
print(reverse('appmillers'))
