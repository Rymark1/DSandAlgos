# Write a program to find all pairs of integers whose sum is equal to a given number
# For our testing, we can assume the numbers are all positive, there is only 1 answer, and the list is unsorted.

# There are 2 answers that can work.
#
# The first is the brute force method which basically iterates over the list and
# then the remaining portion of the list.  This has a runtime of O(n^2) because its running through every item in 2
# separate lists.  This is the method twoSum below.
#
# The second solution is using a dictionary, which is more efficient and runs with O(n) time.  We check the different
# we would like to find, and then check to see if that difference exists as a key in the dicitionary.  The reason is
# dictionaries are unordered, however when we add an item to the dictionary, we add it with a key equal to the value
# from the list, and the data stored for that key is the actual index in the original list.  Lists require iterating
# over when finding a value, so we can't use it here otherwise the runtime is still O(n^2).  Dictionaries can check if a
# keyed value exists in O(1) so it is instant and allows us to only need to run through the list once.  The other
# benefit is this would work if we wanted to return all pairs that match up.
#
# You can see the difference in runtime is huge when dealing with a larger list.


import time

mylist = range(100001)


def twoSum(nums, target):
    a = time.perf_counter()
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] + nums[y] == target:
                b = time.perf_counter()
                print(b - a)
                return [x, y]


def twoSums1(nums, target):
    seen = {}
    a = time.perf_counter()
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in seen:
            b = time.perf_counter()
            print(b-a)
            return [seen[remaining], i]
        else:
            seen[nums[i]] = i


l2 = [2,7,11,15]
l3 = [3,2,4]
l4 = [3,3]

print(twoSum(l2, 9))
print(twoSum(l3, 6))
print(twoSum(l4, 6))

print(twoSums1(l2, 9))
print(twoSums1(l3, 6))
print(twoSums1(l4, 6))
print(twoSums1(mylist, 199999))
print(twoSum(mylist, 199999))
