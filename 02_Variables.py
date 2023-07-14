#################################################
#  08.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
# 👉 Variables
# 👉 Variables assignmnet
# 👉 Exploring print Function
# 👉 Finding the address of variable
#################################################

# Variables
# variables are containers
# they hold the value/data

# this is new line , ignore

# eg : 
x = 100
one = 111
name = "Rakesh"
one_1 = "Five"


# allowed variables in Python

i_am = 100
iam_ = 100
_i_am = 100
_iam_ = 100

# not allowed variables in Python
'''
@123 = 100
#123 = 100
$123$123 = 100

'''

# allowed but not recommended
# dunder  = double underscore
# they are reserved for future use

__iam__ = 100
__shafik__ = 100

# place holder
# mostly used in unpacking a tuple


_  = 100
print(_)
_ = 500
print(_)



# print function contd...
#  as a calculator

print("Ramesh")
# print("Ramesh) # SyntaxError

print(100+100)
print(100-100)
print(100/100)
print(100*100)
print(100%100)
print(101%100)
print(105%100)
# HW 
print(93%100)
print(87%80)
print(25%25)
print(255%50)
print(501%500)

x = 300
print(x) #print the value stored inside the variable
print('x') # print x as it is


# assigning values to variables

print("**********************")

x = 100
y = 100
z = 100
x ,y ,z = 100 , 100 ,100

print(x)
print(y)
print(z)



x = 100
y = 200
z = 300
x ,y ,z = 100 , 200 ,300 #not recommended , poor readibility

print(x)
print(y)
print(z)


print("common variable")
x = y = z = 100
# id() is a function for getting the address of a variable

print(id(x))
print(id(y))
print(id(z))


print("after each variable having same value")
x ,y ,z = 100 , 100 ,100
#  all will have same addr 
#  to save memory 

print(id(x))
print(id(y))
print(id(z))

# HW
x = 500

print("after changn x")
print(id(x))
print(id(y))
print(id(z))




print("after each variable having different  value")
x ,y ,z = 100 , 200 ,300 
print(id(x))
print(id(y))
print(id(z))
