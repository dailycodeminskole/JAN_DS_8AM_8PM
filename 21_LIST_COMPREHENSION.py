#################################################
#  8.03.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
#  👉 LIST COMPREHENSION
#  👉 DICT  COMPREHENSION
#  👉 BREAK,CONTINUE,PASS
#################################################

# Core python syllabus completed
    # data types
    # conditional
    # loops

# Misc topics

# Functions
# Object oriented Programming (OOPs)



# LIST COMPREHENSION
# shorten the code length
# Eg 1 
list_num = [11,22,33,44,55]

for i in list_num:
    print(i*2)

print("using LIST COMPREHENSION ")
print([i*2 for i in list_num]) #compressed form 

# LIST COMPREHENSION with condition

print([i*2 for i in list_num if i%2==0])
print([i*2 for i in list_num if i%2==0 if i==22])


# Eg 2
fruits_list = ['apple', 'banana', 'cherry']

for i in fruits_list:
    print(i.upper())

print([i.upper() for i in fruits_list])





# DICT  COMPREHENSION

list_num = [11,22,33,44,55]
d = {x:x*2 for x in list_num }
print(d)

items_purchase = {
                    'milk' : 1,
                  'bread' : 2,
                  'eggs' : 3}


d= {key : value*80 for (key,value) in items_purchase.items()}
print(d)


print(type({12:24}))
print(type({12}))


# SET  COMPREHENSION
s1 = {i for i in "RAAAAAHUL"}
print(s1)




# BREAK
# CONTINUE
# PASS



num_list = [1,2,3,4,5,6,7,8,9]

for i in num_list:
    if i == 3:
        break #exit the loop
    print(i)


print("*******continue************")

for i in num_list:
    if i == 3:
        continue #skip the value
    print(i)


for i in num_list:
    pass