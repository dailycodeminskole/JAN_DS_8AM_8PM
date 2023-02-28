#################################################
#  28.02.2023 8.15AM
#################################################
#  TOPICS TO BE COVERED 
#  👉WHILE Loop...
#  👉Sets
#################################################

# revision


# for loop
# while loop
# eg. 1

for i in range(1,11):
    print(i)

# using while loop
# initialisation of the variable
# condition
# incerement/decremet/condition  that will terminate the loop
i=1
while i <11:
    print(i)
    i=i+1


# user should give input as 'quit' to exit from the game



# user_input = 'quit'
# while user_input =='quit': #this is always true
#     print("Bye-Bye") #infinite time it will be executed


# user_input= ''

# while user_input.casefold() !='quit': #this is always true
#     user_input = input("Enter 'quit' to exit the game:")

# print("Bye-Bye") #infinite time it will be executed

# SETS
print("******sets************")
# Sets
        #  set is an unorderd colletion of items
        #  no duplicates allowed in Sets
        # unique values only
        #  empty set is a dictionary data type

s1 = {'a','b','c','d','e','f','w','e','r','a','b','c','d','e','f'}
print(len(s1))
print(s1)


s2 = {11,22,33}
print(type(s2))

s3 = {11}
print(type(s3))


s4 = {} #empty set is a dictionary
print(type(s4))


s4 = {"a"} 
print(type(s4))
