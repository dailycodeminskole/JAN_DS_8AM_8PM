#################################################
#  17.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
#  👉Tuples
#  👉Tuples Methods
#  👉Tuples unpacking
#################################################
# Revision
# Methods in Lists

list_fruits = ['apple','orange','guava','banana']

# adding elemnts in a list
# append :  add element at the end
# insert : add element at the given index
# extend : merge the existing list


list_fruits.append("Pineapple") #inplace append
print(list_fruits)

list_fruits.insert(0,"Stawberry")
print(list_fruits)

list_cit = ['lemon','orange']
list_cit.extend(list_fruits)
print(list_cit)


# counting,index,sort
print(list_cit.count("orange"))
print(list_cit.index("orange"))


list_cit.sort()
print(list_cit)


list_elements = ['s','t','u','a','d','f']
list_elements.sort() #sorted alphbatically
print(list_elements)


list_elements.sort(reverse=True) #sorted alphbatically
print(list_elements)


# Below code will give TypeError
# list_mix = ['a','d','f',12,123,11]
# list_mix.sort() #sorted alphbatically
# print(list_mix)


# sorting a list with different datatypes and special char
list_mix = ['a','d','f','12','123','11',"T","#","$"]
list_mix.sort() #sorted alphbatically
print(list_mix)

# deleting items from a list
list_mix = ['a','d','f','12','123','11',"T","#","$"]

print("***************")
list_mix.pop() # remove the last element 
print(list_mix)

list_mix.pop() # remove the last element 
print(list_mix)

list_mix.pop() # remove the last element 
print(list_mix)

list_mix.pop(0) # remove the  element at given index position
print(list_mix)

list_mix.pop(2) # remove the  element at given index position
print(list_mix)


del(list_mix)# this will completly delete the list
# print(list_mix)


# TUPLES
# immutable datatype : can not be changed, has fingerprint , hashable type
# LIST is a mutable datatype , can be changed , no fingerprint, unhashable type 

tup_fruits = ('apple','orange','guava','banana')
print(type(tup_fruits))
print(tup_fruits)


# accessing elements in a tuple

print(tup_fruits[0])
print(tup_fruits[-1])
print(tup_fruits[0:3]) #sliced output will alos be a tuple


# methods in a tuple

print(tup_fruits.count("apple")) # number of instances of the element
print(tup_fruits.index("apple")) # index position of the element 

# unpacking a tuple
tup_fruits = ('apple','orange','guava','banana')

print(tup_fruits[0])
print(tup_fruits[1])
print(tup_fruits[2])

a = tup_fruits[0]
b = tup_fruits[1]
c = tup_fruits[2]

print(a)
print(b)
print(c)

# unpacking a tuple
a , b , c ,d = tup_fruits 


print(a)
print(b)
print(c)
print(d)
