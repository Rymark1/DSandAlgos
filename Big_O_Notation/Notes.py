# Big O is the language and metric we use to describe the efficiency of algorithms.
#
# The 3 complexities that need to be monitored and accounted for are:
# 1. Time complexity.  An example would be determining if we should FTP or physically mail the file based on size.  For
# a small file, this doesn't make sense, but if you are dealing with a multi-TB file, it may make sense to just ship it
# on a plane for the fastest turnaround.
# When measuring time complexity, it isn't the physical amount of time that passes, it is the number of operations that
# is being performed per algorithm.
#
# 2.  Space complexity.  This is amount of space needed for the algorithm to run to completion.
#
# 3.
#
#
# There are 3 different notations that get used in Big O
#
# 1. Best case runtime(Omega)(Ω)
# 2. Average case runtime(theta)(Θ)
# 3. Worst case runtime(Big O)(0)
#
# An example would be a car driving down the road and measuring MPG.  Assume that the car gets 25 highway and 15 city
# traffic MPG.  The best case() would be all highway which results in 25 MPG.  The worst case() would be all city or 15
# MPG.  The average case() would be a 50/50 split which would result in 20 MPG.
#
#
# The most common forms of Big O time complexities are:
#
# O(1) - This is constant - It doesn't matter how many items are in the list, it will take exactly 1 execution
# to reach the desired result.  An example would be pulling a single random card from the deck.
# O(N) - This is linear - it is most common if you need to do a single loop through an array/list of elements.  An
# example would be needed to pull a specific card from a deck.  This grows linear to the number of elements in the list.
# O(LogN) - This is logarithmic - It is most common if you need to visit some, but not all elements in a list.  An
# example would be trying to find a certain item in a sorted list by splitting the list in half.  In a list of 4
# elements, you can find a specific element in 3 steps, but in a list of 1000 items, you can find it in simply 10 steps
# by continually splitting the list in half and discarding the incorrect half. Over 20 times the amount of items and
# only 7 extra steps.
# O(N^2) - quadratic time complexity - This is when you search every element in an array for a specific element in
# another array.  A way to show this would be printing out a multiplication table for the numbers 1-3.
# You would take 1*1, 1*2, 1*3, 2*1, 2*3, 3*1, 3*2, 3*3.  For 3 items, it requires 9 operations.  Similarly, if
# you perform the 12 times table, it requires 12*12 = 144 executions to finish.
# O(2^N) - Exponential  time complexity - An example would be the fibbonacci sequence which require 2 recursive methods
# that every single additional check results in double the amount of exponential executions.
#
# O(1) > O(LogN) > O(N)  > O(N^2) > O(2^N)
# Good - O(1), O(LogN)
# Fair - O(N)
# Bad - O(n LogN) - point to note, this is when a 2 part operation occurs where the first part needs to run through
# all elements and the second needs to only visit selected elements.
# Horrible - O(N^2), O(2^N), O(N!)
#
# You should aim to use the best possible time complexity for the given item you are working within.
#
#
# Space complexity - If you attempt to recursively call a sum program, each extra input adds an additional item
# to the stack which takes up extra space complexity.
#

def sum1(n):
    if n <= 0:
        return 0
    return n + sum1(n-1)


print(sum1(5))  # 15 - However this required 5 recursive calls to be added to the stack resulting in a
# space complexity of O(N)

# However, if you change the code and have it call a function or just perform an operation which simply adds 2 items
# together. This has a space complexity of O(1) because no additional memory is needed to make it run.


def sum2(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    return sum


print(sum2(5))  # 15 - This requires no additional memory and results in a space complexity of O(1).


# When discussing runtimes, if you perform a for loop and then perform a second for loop, this is O(A + B).
# If you perform a for loop nested in a for loop. then this is O(A*B).
#
#
#