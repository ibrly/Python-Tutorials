#####################################
# PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
# Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:

# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[1:4])

# Bonus: Use indexing to reverse the string

print(s[::-1])

###############
# Problem 2 ##
###############

# Given this nested list:
l = [3, 7, [1, 4, 'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
print(l)
###############
# Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])
d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
###############
# Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(set(mylist))
###############
# Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {} he is {} years old".format(name, age))


#####################################
# PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
# -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True


# CODE GOES HERE
def arrayCheck(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


print(arrayCheck([1, 1, 1, 2, 3, 4, 5, 6]))


#####################
# -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

# CODE GOES HERE

def stringBits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


#####################
# -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

# CODE GOES HERE
def end_other(a, b):
    a = a.lower()
    b = b.lower()

    # return (b.endswith(a) or a.endswith(b))

    return a[-(len(b)):] == b or a == b[-(len(a)):]


print(end_other('Hiabc', 'abc'))

print(end_other('AbC', 'HiaBc'))

print(end_other('abc', 'abXabc'))


#####################
# -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'


# CODE GOES HERE
def doubleChar(str):
    result = ""
    for char in str:
        result += char * 2
    return result


print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))


#####################
# -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3


# CODE GOES HERE

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    # another way without the "in" operator
    # if 13 <= n <= 14 or 17 <= n <= 19:
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


#####################
# -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

# CODE GOES HERE
def count_evens(nums):
    count = 0
    for element in nums:
        if element % 2 == 0:
            count += 1
    return count


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))