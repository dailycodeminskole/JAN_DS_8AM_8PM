#################################################
#  27.02.2023 8.15AM
#################################################
#  TOPICS TO BE COVERED 
#  👉WHILE Loop...
#################################################

# remaining for loop topic

# Nested loop
# outer loop
# inner loop


for i in range(1,11):
    for j in range(1,11):
        print("Multiplication table of {0} is {1}*{2} = {3}".format(i,i,j,i*j ))
        # product = i*j
        # print(product)



# no use in datascience

for i in range(5):
    for j in range(i+1):
        print(j*"*")





#WHILE loop

# syntax
# while expression/condition:
#     code


for i in range(5):
    print("I will attend the class")


# eg 1
print("using while loop")
i = 0
while i < 5:
    print("I will attend the class")
    i = i +1


# eg 2 
# checking the input to be an integer

# value = "five"


valid_input = False
while not valid_input:

    value = input("Enter a 3digit code number:")
    if value.isdigit():
        valid_input = True
        print("Value is a number")
    else:
        print("Value is not  a number")
