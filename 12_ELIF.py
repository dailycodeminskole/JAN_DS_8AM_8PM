#################################################
#  22.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
#  👉IF...
#  👉IF...ELSE
#  👉IF...ELIF...ELSE
#################################################

# revision

if 10>25:
    print("10 is greater number")
else:
    print("10 is the smaller one")


# Checking the string is a PALINDROME ?

# name = "MANISH"
name = "NAMAN"
name = "MADAM"

print(name)
print(name[0])
print(name[1])
print(name[::-1])

if name==name[::-1]:
    print("Given word is a Palindrome")
else:
    print("Given word is not a Palindrome")


sentence = "Do geese see God"

if sentence.casefold()==sentence[::-1].casefold(): #checking after making the sent lowercase
    print("Given sentence is a Palindrome")
else:
    print("Given sentence is not a Palindrome")


list_v = ['a', 'e', 'i', 'o', 'u']

element = 'p'
# element = 'a'
# checking boolean value of the element
#  using membership operator
#  IN , NOT IN

print(element in list_v)

if element in list_v:
    print("Element is present in the list")
else:
    print("Element is not present in the list")



pass_students = ["Ramesh","Suresh","Mukesh","Jenish","Saket"]

student = "Saket"

if student in pass_students:
    print("Congrats!!!")
else:
    print("Try again")


if student not in pass_students: #FALSE bool value
    print("Congrats!!!")
else:
    print("Try again")



# checking if a numer is pos , neg , zero

num = 41
num = -41
num = 0

if num >0:
    print("The num is positive")
elif num < 0:
    print("number is neg")
else:
    print("The number is ZERO")

# checking the grade of student


marks = 74
marks = 84
marks = 94

if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("FAIL")



# membership operator

list_num = [11,22,33,44,55,66]

if 22 in list_num:
    print("Present")
else:
    print("Not Present")