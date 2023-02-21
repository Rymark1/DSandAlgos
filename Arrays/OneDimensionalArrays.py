# 1. Create an array and traverse.
# 2. Access individual elements through indexes
# 3. Append any value to the array using append() method
# 4. Insert value in an array using insert() method
# 5. Extend python array using extend() method
# 6. Add items from list into array using fromlist() method
# 7. Remove any array element using remove() method
# 8. Remove last array element using pop() method
# 9. Fetch any element through its index using index() method
# 10. Reverse a python array using reverse() method
# 11. Get array buffer information through buffer_info() method
# 12. Check for number of occurrences of an element using count() method
# 13. Convert array to string using tostring() method
# 14. Convert array to a python list with same elements using tolist() method
# 15. Append a string to char array using fromstring() method
# 16. Slice Elements from an array

from array import *


print("#1 - Create array and traverse")
arr1 = array("i", [1,2,3,4,5])

for i in arr1:
    print(i)

print("\n#2 - Access individual elements of Array")
print(arr1[1])
print(arr1[4])

print("\n#3 - Append value to end of array")
arr1.append(100)
print(arr1)

print("\n#4 - Insert value at beginning of array")
arr1.insert(0,1105)
print(arr1)

print("\n#5 - extend array using extend method")
arr1.extend([1,2,3])
print(arr1)

print("\n#6 - Add items using fromlist method")
arr1.fromlist([56,60])
print(arr1)

print("\n#7 - Remove any array element")
arr1.remove(1)  # It only removes the first item found.
print(arr1)

print("\n#8 - Remove last array element using pop method")
arr1.pop()
print(arr1)

print("\n#9 - Fetch item using index method")
print(arr1.index(100))

print("\n#10 - Reverse an array using the reverse method")
arr1.reverse()
print(arr1)
arr1.reverse()
print(arr1)

print("\n#11 - get buffer information using buffer_info method")
print(arr1.buffer_info())

print("\n#12 - use count method to get number of a specific element")
print(arr1.count(2))

print("\n#13 - Convert array to string using tostring() method")
temp_arr1 = arr1.tobytes()
print(temp_arr1)
temp_arr2 = array("i")
temp_arr2.frombytes(temp_arr1)
print(temp_arr2)

print("\n#14 - Convert array to a python list using the tolist method")
temp1 = arr1.tolist()
print(temp1)

print("\n#15 - Append a string to char array using from string() method")
# Skipping because deprecated.

print("\n#16 - Slice elements from an array")
print(arr1[1:5])
