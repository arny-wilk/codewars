''' 
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

    Find the unique number (this kata)
    Find the unique string
    Find The Unique

'''

# Python program to check if two
# to get unique values from list
# using traversal

# FIRST WAY TO (NOT OPTIMIZED)

def find_uniq(arr):
    
    if len(arr) == 1 :
        return  arr[0]
    elif arr == [] :
        return -1
    for n in arr :
        if arr.count(n) == 1 :
            return n
    return -1


find_uniq([ 1, 1, 1, 2, 1, 1 ])
find_uniq([1])
find_uniq([])


# SECOND WAY (OPTIMIZED)

# Fast O(n) find_uniqValue using dictionary

def find_uniqValue(arr):
    counts = {}
    
    for item in arr :
        if item in counts :
            counts[item] += 1
        else :
            counts[item] = 1
    
    for item in arr :
        if counts[item] == 1 :
            return item
    
    return -1

print(find_uniqValue([1,2,1,3,2,5])) # prints 3
print(find_uniqValue([1,2,1,3,3,2,5])) # prints 5
print(find_uniqValue([1,2,1,3,3,2,5,5])) # prints -1
print(find_uniqValue([7])) # prints 7


# PYTHONISTE APPROACH

# 1 BEST PYTHONISTE WAY
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


# & BEST PYTHONISTE WAY
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]


# 2 BEST PYTHONISTE WAY
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e


# 3 BEST PYTHONISTE WAY
def find_uniq(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]


# 3 LESS GOOD APPROACH
def find_uniq(arr):
    if arr[0] != arr[1]:
        if arr[0] != arr[2]:
            return arr[0]
        else:
            return arr[1]           
    else:
        for i in arr[2:]:
            if i != arr[0]:
                return i


# BY USING METHOD COUNTER FROM COLLECTION LIBRARY
from collections import Counter

def find_uniq(a):
    return Counter(a).most_common()[-1][0]