# Recursion is a way of solivng a problem by the function calling itself.  A visual would be imagining Russian nesting
# dolls.  Each next step gets smaller each time until a base case is found.
#
# The requirements for recursion to work would be that we perform the same operation multiple times with different
# outputs.  We also need to make the problem smaller every single step.  Finally, you have a base condition that is used
# to stop recursion.
#
# sample code for the Russian Dolls:
def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)


openRussianDoll(5)


# Why do we need recursion
#
# 1. Recursive thinking is really important in programming because it allows us to break large problems into smaller
# ones
#
# 2. When do I choose Recursion?
# When the problem needs to use similar subprograms, then we can use recursion:
#   if you can divide the problem into similar sub problems
#   design an algorithm to compute the nth item
#   Write code to list the n
#   Implement a method to compute all
#   practice practice practice
#
# Recursion is useful for data structures like trees and graphs where you need to traverse the shortest path or check
# all nodes.
#
# 3. Interviews
# Most large companies expect some level of recursive knowledge and be able to perform basic recursive problems, or at
# least structure your mind to think properly.
#
# 4.  Quite a few algorithms use recursion to break down the complexity and perform the same action multiple times.
# For example, the divide and conquer, greedy, and dynamic programming algorithms use recursion, as well as tree
# traversal.
#


# How Recursion works?
# We need two conditions:
# 1. A method calls itself
# 2. There is a base case to exit the infinite loop
#
# Pseudocode:
# def recursionMethod(parameters):
#     if exit from condition satisfied or the base case is met:
#         return some value
#     else:
#         recursionMethod(modified parameters)
#
# supposed we have 4 functions, firstMethod, secondMethod, thirdMethod, fourthMethod
#
def firstMethod():
    secondMethod()
    print("I am the first Method")


def secondMethod():
    thirdMethod()
    print("I am the second Method")


def thirdMethod():
    fourthMethod()
    print("I am the third Method")


def fourthMethod():
    print("I am the fourth Method")


# The stack is maintained by the system and push method adds an item to the stack, and the pull removes an item from
# the stack.
#
# The first method gets pushed to the stack.  The first method calls the second method which gets pushed to the stack.
# The second method calls the third method and gets pushed to the stack.  The third calls the fourth and the third is
# pushed to the stack.  The fourth method gets performed, and now the system realizes it still has items on the call
# stack to resolve.  It then  pops the third method, completes it, and then pops the second method, then the first, and
# finally the call stack is empty.  Then the method is completed and nothing remains on the call stack.
#
#
#
#
#
#
#



def fib(n1):
    assert n1 >= 0 and int(n1) == n1, "The number must be a positive integer"
    if n1 <= 1:
        return n1
    else:
        return fib(n1-1) + fib(n1-2)


print(fib(5))
print(fib(13))


def factorial(n1):
    assert n1 >= 0 and int(n1) == n1, "The number must be a positive integer"
    if n1 == 0:
        return 1
    return n1 * factorial(n1-1)


print(factorial(-1))
print(factorial(4))
print(factorial(5))
print(factorial(10))
