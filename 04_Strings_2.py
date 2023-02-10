#################################################
#  10.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
# 👉 String formatting
#################################################


# HW Solution

# Modify quotes in below code wherever necessary for print() to work without error

print("Today is a good day")
# print("Mahatma gandhi said in his speech ,"we should work hard" ")
print('''Mahatma gandhi said in his speech ,"we should work hard"''')
print("It's a brand new car as the B'day gift")
# print("C:\Users\tanmay\docs")


#################################################
# ESCAPE SEQUENCE


# Escape Character Meaning
# \”                Double quote
# \’                Single quote
# \\                backslash
# \n                New line
# \r                Carriage Return
# \t                Horizontal tab
# \b                Backspace
# \f                form feed
# \v                vertical tab
# \0                Null character
# \N{name}          Unicode Character Database named Lookup
# \uxxxxxxxx        Unicode Character with 16-bit hex value XXXX
# \Uxxxxxxxx        Unicode Character with 32-bit hex value XXXXXXXX
# \ooo              Character with octal value OOO
# \xhh              Character with hex value HH




print("C:\sers\nanmay\docs")
print('''C:\sers\nanmay\docs''')#this wont work


print("rahul")
print("\\rahul")
print("\\tanmay")

print("C:\\Users\\tannmay\docs")



# using r-string i.e raw string
#  to ignore the Escape character

print(r"C:\Users\tanmay\docs")
print(R"C:\Users\tanmay\docs")


#string foramtting


zero = "Zero"
one = "One"
two = "Two"

print(zero,one,two)

print("The numbers are ",zero, "and", one , "and" ,two)
print("The numbers are  {0} and {1} and {2}".format(zero,one,two))


name = "Ramesh"
age = 25
area = "Pune"

print(name,age,area),
print("My name is : ",name, "and I am :", age, "years old", "I live in :",area)

print("My name is {0} and I am {1} years old and I live in {2}".format(name,age,area))
print("My name is {0} and I am {1} years old and I live in {2}".format(area,age,name))


print("My name is {} and I am {} years old and I live in {}".format(name,age,area)) #default sequence is considered
print("My name is {} and I am {} years old and I live in {}".format(area,age,name)) #default sequence is considered

# reordering the default sequence
#                                                                     0   1    2
print("My name is {2} and I am {1} years old and I live in {0}".format(area,age,name)) #default sequence is considered


# latest use
# using f-string


print("My name is {name} and I am {age} years old and I live in {area}") #default sequence is considered
print(f"My name is {name} and I am {age} years old and I live in {area}") #default sequence is considered



# HW
'''
A. use .format() to print below statement using the numerical values stored in variables

a = 100
b = 200
c = 300

The price of coke is 300 , spice is 100 and vcr is 200

Shyam has scored 300 in science , 200 in Physics and 300 in Maths


B. use f-string to print  below statement using the numerical values stored in above variables

The price of coke is 300 , spice is 100 and vcr is 200

Sameer has scored 300 in science , 200 in Physics and 300 in Maths


'''

