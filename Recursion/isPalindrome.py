# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads
# the same forward and backward). Otherwise, it returns false.

def isPalindrome(strng):
    if len(strng) <= 1:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:len(strng) - 1])


print(isPalindrome('awesome'))
print(isPalindrome('foobar'))
print(isPalindrome('tacocat'))
print(isPalindrome('amanaplanacanalpanama'))
print(isPalindrome('amanaplanacanalpandemonium'))
