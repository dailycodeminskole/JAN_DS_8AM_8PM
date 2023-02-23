#################################################
#  23.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
#  👉For Loop...
#  👉range()
#################################################


# revision
# syntax
# if condition:
#     code
# elif condition:
#     code
# else:
#     code


score = 55
'''
A > 90
B > 80
C > 70
D > 60
FAIL
'''


if score>90:
    print("Cleard the exam with Grade A")
elif score>80:
    print("Cleard the exam with Grade B")
elif score>70:
    print("Cleard the exam with Grade C")
elif score>60:
    print("Cleard the exam with Grade D")
else:
    print("FAILED")


# For loop
# eg.1
#                   0           1       2       3       4
pass_students = ["Ramesh","Suresh","Mukesh","Jenish","Saket"]

# too many lines of code to retrieve the list elements
print(pass_students[0])
print(pass_students[1])
print(pass_students[2])
print(pass_students[3])
print(pass_students[4])

# Syntax
# for i in iterable:
    # code

print("********************")
#eg.
for i in pass_students:
    print(i)

#eg.2

mailid = "naveen1991.coep@gmail.com"


for j in mailid:
    print(j)

#eg 3.

list_even = [11,22,33,44,55,66]

for num in list_even:
    print(num*2) #performing operation on each element , double

for num in list_even:
    print(num**3) # taking cube of each element

# understanding range()
# to generate list of numbers
# last element is not included

print(list(range(10)))#typecasting range to list

print(list(range(0,10))) # default start will be zero

print(list(range(10,20))) # last element is not included

print(list(range(5,51,5))) # last element is not included

# for neagtive values
print(list(range(0,-10,-1))) # last element is not included

print(list(range(0,-10,1))) # last element is not included
print(list(range(0,-10))) # last element is not included
print(list(range(10,1))) # last element is not included

# read xrange

print(list(range(1,10,5)))


# for i in range(1,11):
#     print(i)














