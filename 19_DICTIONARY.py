#################################################
#  2.03.2023 8.15AM
#################################################
#  TOPICS TO BE COVERED 
#  👉Dictionary
#  👉Dictionary Methods
#################################################

# HW 
# 2. Checking for common elements between two lists:
fruits1 = ["apple", "banana", "orange", "pear"]
fruits2 = ["banana", "kiwi", "pear", "watermelon"]
# HINT: convert the List into sets first


fruits1 = set(fruits1)
fruits2 = set(fruits2)

print(fruits1.intersection(fruits2))


# 
student_info = {
    'name' : "Rakesh",
    'age' : 24,
    'area' : "Pune",
    'subjects' : ['Phy','Chem','Maths'],

}

# Key should always be an immutable data type
# valuse field can be anything permitted in python

# creating a dictionary

dict_a = {'a' : 1, 'b' : 2 , 'c' : 3}
print(type(dict_a))
print(dict_a)


dict_b = dict(a=1,b=2,c=3) #using constructor
print(dict_b)

dict_c = dict(zip(['a','b','c'],[1,2,3])) #through LIST
print(dict_c)

dict_d = dict([("a",1),("b",2),("c",3)]) # Through tuple pair
print(dict_d)


# accessing a dictionay using []

student_info = {
    'name' : "Rakesh",
    'age' : 24,
    'area' : "Pune",
    'subjects' : ['Phy','Chem','Maths',['Python','JS','c']],

}

print(student_info['name'])
print(student_info['area'])
print(student_info['subjects'])
print(student_info['subjects'][2])
print(student_info['subjects'][0])
print(student_info['subjects'][3][2])


# dictionary methods

# copy

student_info_copy = student_info.copy()
print(student_info_copy)

# accessing dict using get()
print(student_info.get('name'))
print(student_info.get('age'))
print(student_info.get('subjects'))

# 
print("****************")
print(student_info.keys()) # list of keys
print(student_info.values()) # list of values 
print(student_info.items()) # return a key : value pair tuple

# update at the end only 

student_info.update({"pincode" : 400093})
print(student_info)

student_info.update({"result" : 'Pass'})
print(student_info)


# HW

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

