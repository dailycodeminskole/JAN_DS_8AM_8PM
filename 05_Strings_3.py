#################################################
#  13.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
# 👉Indexing
# 👉String Slicing
# 👉String Slicing with step values
#################################################


# Indexing
    # Positive
    # Negative - limited use only


#    0123
name = "AMOL"


# Neg-Indexing	-6	-5	-4	-3	-2	-1
# Indexing	    0	1	2	3	4	5
# STRING	    P	Y	T	H	O	N
# Counting	    1	2	3	4	5	6

# Accessing the string using positive indexing
# eg.1
skill = "PYTHON"

print(skill)
print(type(skill)) #finding the data type using type()

# syntax
# variable[index_value]
print(skill[0])
print(skill[5])
print(skill[2])


#eg.2
mailid = "naveen1991.coep@gmail.com"

print(mailid[15]) # we need to print "@"

# slicing 
# syntax
# variable[start:end] end-1 i.e n-1

print(mailid[11:15]) # we want slice of mail id as  o/p "coep"
print(mailid[16:21]) # we want slice of mail id as  o/p "gmail"


# slicing with jump/step values
# syntax
# variable[start:stop:step/jump] n-1 will be considered

phrase = "The sun is very bright and lively"

print(phrase[4:7]) #sun
print(phrase[0:21:3]) # one characters and two skip values




# if values are not provided in [::]

# Neg-Indexing	-6	-5	-4	-3	-2	-1
# Indexing	    0	1	2	3	4	5
# STRING	    P	Y	T	H	O	N
# Counting	    1	2	3	4	5	6

skill = "PYTHON"
print(skill[2:]) # default last*
print(skill[:5]) # default start i.e 0
print(skill[:]) # default start i.e 0 and default last*
print(skill[0:6]) # default start i.e 0 and default last*


print("**********")
print(skill[::]) # All default values jump default = 1
print(skill[::1]) # All default values jump default = 1
# print(skill[::0]) # ValueError : slice step cannot be zero


# neg indexing 
    # to print the last element
    # to reverse the string


print(skill[-1])
# string reversal
# variable[::-1]
print(skill[::-1])


# string Methods tomorrow

#  HW
'''
sentence = " My email ID is nikhil.pune@yahoo.com $"

use indexing to print 
1. the 1st character
2. @
3. yahoo
4. $
5. slice with 3 characters to be skip
6. print the sentence in reverse order using neg indexing

character from the given sentence
'''


