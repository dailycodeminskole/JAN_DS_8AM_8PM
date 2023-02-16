#################################################
#  17.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
# 👉LISTS
#################################################

#HW
x = '''Jana gana mana adhinayaka jaya he
Bharata bhagya vidhata
Panjaba Sindha Gujarata Maratha
Dravida Utkala Banga
Vindhya Himachala Yamuna Ganga
Uchchhala jaladhi taranga
Tava subha name jage,
tava subhasisa mage,
gahe tava jaya gatha.
Jana gana mangala dayaka jaya he
Bharata bhagya vidhata.
Jaya he, jaya he,
jaya he,
jaya jaya jaya jaya he'''

# 1. count how many time "jaya/Jaya" appeared
# 2. Replace Bharata with India
# 3. Find 1st occurance of Bharata
# 4. store every word in x in a LIST and observe the items in the list .

'''
print(x.count("jaya"))
print(x.count("Jaya"))

print(x.casefold().count("jaya"))

print(x.replace("Bharata","India"))

print(x.find("Bharata"))
print(x.index("Bharata"))

print(x.split(" "))
'''

# Accessing a list
#                   0       1       2      3        4
#                  -5       -4      -3     -2      -1
students_name = ['Amar','Akash','Anuj','Amit','Aniket']
print(students_name)
print(students_name[3]) #Amit
print(students_name[4]) #Amit
print(students_name[-1]) #using negative indexing



print(students_name[0:3]) #Slicing
print(students_name[:])  #default start:end

# print(students_name[-3:-5])  #Slicing with neg INdexing
print(students_name[-5:-2])  #Slicing with neg INdexing



# List Methods
students_name = ['Amar','Akash','Anuj','Amit','Aniket']
# append , to add item at the end of the list


students_name.append("Amol") # this is inplace method, will append the original list
print(students_name.append("Amol")) #None
print(students_name) # this will be the updated list


# insert
# .insert(indexPosition , Item)
students_name.insert(0,"Zakir")
print(students_name)

students_name.insert(2,"Nimesh") # the existing item will get shifted to one right position
print(students_name)

# extend
students_name2 = ['Samir','Saket','Sanjeev','Suresh']

print("*************")
students_name.extend(students_name2) #inplace changes
print(students_name) # the original list is now having both lists combined
print(students_name2)# 2nd list will not be affected 


# index , will return the index position of the item

print(students_name.index("Zakir"))
print(students_name.index("Nimesh"))

students_name.append("Zakir")
print(students_name)
print(students_name.index("Zakir")) #1st occurance


# count

print(students_name.count("Zakir"))# number of occurances

# sort
print("*************")
print(students_name.sort()) #None
print(students_name)

students_name.sort(reverse=True) # to print in reverse order
print(students_name)


# reverse
students_name2 = ['Samir','Saket','Sanjeev','Suresh']
students_name2.reverse()
print(students_name2)


list_vovwel = ['e','i','a','o','u']
list_vovwel.reverse() #will revers the items based on index position
print(list_vovwel)

# pop

# del