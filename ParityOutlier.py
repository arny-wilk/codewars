"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised
of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)

"""

# First way (Pythoniste Way)

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

# Second Way (THE BEST WAY TO FIND THE OUTLIER)

''' Firstly, I am seeing if this list is either all odds, or all evens,
bar the outlier. Then if it is even, it goes through the list looking
for an odd number, the same for if the list is all odd. However,
if the outlier is in the first two numbers, then it checks to see whether
the outlier is the first number or the second number by comparing the modulos*
to the modulo of the third number in the list '''

def find_outlier2(lstOfints):
    if lstOfints[0] % 2 == 1 and lstOfints[1] % 2 == 1:
        for integer in lstOfints[2::]:
            if integer % 2 == 0:
                return integer
    elif lstOfints[0] % 2 == 0 and lstOfints[1] % 2 == 0:
        for integer in lstOfints[2::]:
            if integer % 2 == 1:
                return integer
    else:
        if lstOfints[0] % 2 == lstOfints[2] % 2:
            return lstOfints[1]
        else:
            return lstOfints[0]

print(find_outlier2([2, 4, 0, 100, 4, 11, 2602, 36]))

# Third Way

def find_outlier3(lst):
    mods = [n % 2 for n in lst]
    return lst[mods.index(0)] if sum(mods[:3]) > 1 else lst[mods.index(1)]

print(find_outlier3([5, 31, 57, 45, 9, 17, 8, 37, 123, 67])) # --> 8

print(find_outlier3([4, 30, 56, 44, 8, 16, 7, 36, 122, 66])) # --> 7


# Fourth way (Barely the same as the third way)

def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


# Fifth Way

def find_outlier(integers):
    listEven = []
    listOdd = []
    for n in integers:
        if n % 2 == 0:
            listEven.append(n)
        else:
            listOdd.append(n)

    if len(listEven) == 1:
        return listEven[0]
    else:
        return listOdd[0]

# Sixth way

def find_outlier(nums):

  base_parity = sum( x%2 for x in nums[:3] ) // 2

  for i in range(len(nums)):
    if nums[i] % 2 != base_parity:
      return nums[i]
