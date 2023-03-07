#################################################
#  7.03.2023 8.15AM
#################################################
#  TOPICS TO BE COVERED 
#  👉Dictionary Methods
#################################################

# HW discussion
'''
1 . create a dictionary using zip function with 
keys_list = ['apple', 'banana', 'cherry']
values_list = [1, 2, 3]

2. create a dictionary using tuple pair 
('red', 1), ('green', 2), ('blue', 3)

3. update below dict with (4 ,'pear')
fruit_dict = {
  1: "apple",
  2: "banana",
  3: "cherry"
}

4. print list of keys , vales and iteams in below dict
user_dict = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "hiking", "yoga"]
  }

'''


keys_list = ['apple', 'banana', 'cherry']
values_list = [1, 2, 3]
dict_fruits = dict(zip(keys_list,values_list))
print(dict_fruits)


dict_color= dict([('red', 1), ('green', 2), ('blue', 3)])
print(dict_color)

fruit_dict = {
  1: "apple",
  2: "banana",
  3: "cherry"
}

fruit_dict.update({4 :'pear'})
print(fruit_dict)



# vIMP
user_dict = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "hiking", "yoga"]
  }

print(user_dict.keys())
print(user_dict.values())
print(user_dict.items())

# Methods 

# setdefault()
# setdefault() = get() + update()


# print(user_dict['city'])
print(user_dict.get('city','The key is not present')) # we can print  a custom msg using get()
user_dict.update({'city':'Pune'})
print(user_dict)

print(user_dict.setdefault(('name')))
# print(user_dict.setdefault('result')) #behaves like get() , if the key is absent
print(user_dict.setdefault('result','fail')) #behaves like update() , if the key is absent , it will create one

print(user_dict)


# 

fruit_dict = {
  1: "apple",
  2: "banana",
  3: "cherry"
}


print(fruit_dict.get('4','Somethion went wrong'))
print(fruit_dict.setdefault('4',"KIWI"))


fruit_dict.update({4:"Guava"})
print(fruit_dict)

print(fruit_dict.setdefault('5','mango'))
print(fruit_dict)



# removing elements

print(fruit_dict.popitem()) #last elemt in the dictionary
print(fruit_dict)

fruit_dict.update({2:"BANANA"})
print(fruit_dict)

print(fruit_dict.popitem())
print(fruit_dict)


print(fruit_dict.pop(2))
print(fruit_dict)

fruit_dict.clear()
print(fruit_dict)

del(fruit_dict)
# print(fruit_dict)

# INITIALISING A DICT

# fromkeys()

list_admission = ['ramesh','suresh','prakas','jenish']
# list_score = [0,0,0,0]
score = 100
score = [100,89,58,99]
score = "NA"

# print(dict(zip(list_admission,list_score)))

print(dict.fromkeys(list_admission))
print(dict.fromkeys(list_admission,score))



#  using for loop to retrieve 
# keys
# values
# items



list_admission = ['ramesh','suresh','prakas','jenish']

for i in list_admission:
    print(i)


student_info = {
    'name' : "Rakesh",
    'age' : 24,
    'area' : "Pune",
    'subjects' : ['Phy','Chem','Maths',['Python','JS','c']],

}


print(student_info.keys())


for i in student_info.keys():
    print(i)

print(student_info.values())

for i in student_info.values():
    print(i)



print(student_info.items())

for key,value in student_info.items():
    print(key,value)