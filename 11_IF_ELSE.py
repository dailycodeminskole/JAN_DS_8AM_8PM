#################################################
#  21.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
#  👉IF...ELSE
#################################################


# checking boolean output of an expression/statement

print(1)
print(bool(1)) #checking bool value of 1
print(bool(0)) #checking bool value of 0


print(bool("1")) #checking bool value of string 1
print(bool("0")) #checking bool value of string 0
print(bool("")) #checking bool value of ""

# Examples of if..else..

# Syntax
# if Expression:
    # code
# else:
    # code


num1 = 100
num2 = 200

print(num1>num2) #checking boolean outputs
print(num1<num2) #checking boolean outputs


if num1<num2:
    print(num2 ,"is the greater number")


num1 = 100
num2 = 100
if num1==num2:
    print( "Both numbers are equal")


#
num1 = 25
num2 = 33

if num1>num2:
    print("num1 is greater number")
else:
    print("num1 is smaller number")


# 
# marks  = 40
marks  = 35

if marks>=40:
    print("Congrats !!! you have passed the exam")
else:
    print("Better luck next time")


# Checking even/odd num

num1 = 13
num2 = 14


print(num1%2==0)
print(num2%2==0)


if num1%2==0:
    print("This is an even number")
else:
    print("This is an odd number")


if num2%2==0:
    print("The number is even")
else:
    print("The number is odd ")

# checking the password strength
# password length >= 8

pass1 = "abc@12345"
pass2 = 123
if len(pass1)>= 8:
    print("Strong Password")
else:
    print("Weak Password")


if len(str(pass2))>= 8: #converting the int to string 
    print("Strong Password")
else:
    print("Weak Password")



# given year is a century
# same logic a sfindin even and odd number
year = 2001

if year%100==0:
    print("Year is a century")
else:
    print("Year is not a century")

# to be discussed tomorrow
# Checking the string is a PALINDROME ?

name = "NAMAN"
