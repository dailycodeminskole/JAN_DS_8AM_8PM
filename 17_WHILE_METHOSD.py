#################################################
#  1.03.2023 8.15AM
#################################################
#  TOPICS TO BE COVERED 
#  👉Methods in Sets
#################################################
# doubt clearing
# pin = ""
# while pin != 'quit':
#     pin = input("Enter quit")
# print("Bye")


s4 = {} #empty set is a dictionary
print(type(s4))

s4 = {"a"}
print(type(s4))

#  blank set using set costructor

s1 =  set()
print(type(s1))

list_num = [1,7,8,9,41]
print(list_num)
print(type(list_num)) #list
print(set(list_num)) #type conversion
print(type(set(list_num))) # set


#  accesssing set items

set_fruits = {'apple','orange','guava','banana'}
print(set_fruits)
print(type(set_fruits))


# print(set_fruits[0]) #not possible  , error

# using for loop to print the items inside a set
# the output will be different in each case

for i in set_fruits:
    print(i)


# methods in a set

# adding elements in a set
# set_fruits[4] = "grapes" #TypeError


set_fruits.add("Grapes")
print(set_fruits)

set_fruits.add("Kiwi")
print(set_fruits)


# adding multiple items using update()
set_veg = {"potato","onion","tomato"}

set_fruits.update(set_veg)
print(set_fruits)


list_flowers = ['a','b','c']

set_fruits.update(list_flowers) # we can use any iterable
# iterable  = list , tuple, sets
print(set_fruits)

# removing the elements

set_fruits.remove("orange")
print(set_fruits)


set_fruits.remove("onion")
print(set_fruits)

# removing non existent item ??
# set_fruits.remove("pineapple") # KeyError
# print(set_fruits)


set_fruits.discard("pineapple")
print(set_fruits)


# using pop()

print(set_fruits.pop())
print(set_fruits)


print(set_fruits.pop())
print(set_fruits)


# print(set_fruits.pop("potato")) #takes no arguments
# print(set_fruits)


# set_fruits.remove('a', 'b') #takes exactly one argument 
# print(set_fruits)

# operations on sets !!!