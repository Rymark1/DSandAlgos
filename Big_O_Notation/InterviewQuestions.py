# This is a brief rundown where I need to state the Big O notation and defend it.

################ Interview Questions #############
#Question1
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)

# this program has multiple O(1) executions, Su, = 0, product = 1, print statement, sum += `, product *= i.  There are
# 2 for loops so these become ignorable since there is a higher Big O.
# There are 2 for statements, They are not nested, so this would be O(N) + O(N), which can be simplifield to O(2N).
# We drop the constant, and we get O(N) as the time complexity.


#Question2

def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))

# This is O(N^2) because the 2 for statements are nested.


#Question3
def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(array[i] + "," + array[j])


# This is O(N^2) because the 2 for statements are nested.


#Question4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))


arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]

# This is O(a*b) because we have 2 different lengths of an array that are independent so they do not
# quadratically increase.


#Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))


# printUnorderedPairss(arrayA,arrayB)
# This is O(a*b*100000), however we drop constants so its O(a*b)


#Question6
def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)

# This is O(N) because the for loop is running at O(N/2) for half the array.  But since we drop constants, it becomes
# O(N)


# Question 7: Which of the following are equivalent to O(N)? Why?
# 1. O(N + P), where P < N/2    - This is O(N) because N and P are both constants, so we drop the P which is the
# lessor of the 2.
# 2. O(2N)                      -  We drop the constant 2 so Yes.
# 3. O(N+logN)                  - Yes because log n is going to only run a partial amount of operations,  however
# N will perform all of them.  Since log N is the lessor runtime, we drop it.
# 4. O(n + NlogN)               - No, because NlogN is a 2 part operation where we need to perform both N times
# and a partial run via Log N.
# 5. O(N+M)                     - No, because we are unsure the size comparison between the 2, we need to leave it as
# O(n+m) which means it is not O(N)


#Question8

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

# All statements except for the recursive call are O(1).  The recursive call is occuring n times, so the time
# complexity would be O(N).  The space complexity would also be O(N).


#Question9
def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


allFib(4)

# Fibonacci Complexity - This is double recursive call so for each extra number we increase exponentially.  This would
# be a time complexity of O(2^N)


#Question10
def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2
        print(curr)
        return curr

powersOf2(50)

# O(logN)