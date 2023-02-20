#################################################
#  20.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
#  👉Operators
#################################################

'''
Control flow in Python required understanding of
> Operators
> Boolean interpretation of the statements True/False

Logical operators
AND , OR ,NOT | Truthy values
Identity operators
IS , NOT IS 
Membership operators
IN , NOT IN 

'''

print(10>5)
print(10>500)

a = 300
b = 500

# print(a=b) #this is assignment and not comparison operator
print(a==b) #this is comparison operator


c = 900
d = 1000

# Logical operators

'''
AND		
Staement1	    Staement1	Output
TRUE	        TRUE	    TRUE
TRUE	        FALSE	    FALSE
FALSE	        TRUE	    FALSE
FALSE	        FALSE	    FALSE



OR		
Staement1	    Staement1       Output	
TRUE	        TRUE	        TRUE
TRUE	        FALSE	        TRUE
FALSE	        TRUE	        TRUE
FALSE	        FALSE	        FALSE


NOT	
Staement	Output
TRUE	    FALSE
FALSE	    TRUE

'''



#       F   and T = F
print(a>b and c<d)

#       F   or  T = T
print(a>b or c<d)



# Membership operators

list_vowels = ['a', 'e', 'i', 'o', 'u']

print("a" in list_vowels) # will have a boolean output
print("z" in list_vowels) # will have a boolean output
print("z" not in list_vowels) # will have a boolean output
print("o" not in list_vowels) # will have a boolean output


# Practical cases of AND and OR operators

#eg 1
# checking if a person is eligible to vote or not
age = 25 #age of person
citizen =  "N" # the status of citizenship
can_vote =  "N"

# we can form below statement 
# (age = 25 #age of person) and  (citizen =  "N" # the status of citizenship) = (can_vote =  "N")

# Checking if we can employ a person , whose age is >= 18
#Eg 2 

Person_age  = 18
qualification = "D" #we can assume that adiploma holder's age >=18
Employable = "Y"

# we can form below statement  
# (Person_age  = 18) or (qualification = "D") = (Employable = "Y")


# boolean outputs of datatypes

print("*******************")
print(bool([12])) # value
print(bool([])) #empyt 
print(bool("")) #empty
print(bool())

# Tomorrow
# Flow control statements
# If
# If...else











