#################################################
#  2.03.2023 8.15AM
#################################################
#  TOPICS TO BE COVERED 
#  👉Operations in Sets
#  👉Dictionary
#################################################

# revision


s1 = {11,22,33,44}
s2 = {"a","e","i","o","u"}
s3 = {11,22,33,"a","e","i"}

s4 = {} #dcit

s5 =  set() #to create a blank set , typecasting 

# accesssing/retrieving  set items using for loop

for i in s3:
    print(i)



# methods in a set

s3.add("o") #inplace change
print(s3)

s7 = {7,77,777}

s3.update(s7)
print(s3)

s8 = [9,99,999]
s3.update(s8) # we can update with other iteables also
print(s3)


# remove : will give error if element is missing
# discard : no error even if the element is absent 

s3.remove(999)
print(s3)

s3.discard(1000)

s3.pop()
print(s3)

s3.pop()
print(s3)


# operations on sets !!!


e = {0,2,4,6,8,10}
o = {0,1,3,5,7,9}
o1 = {3,5}

print(e.union(o))
print(e.intersection(o))
print(e.intersection(o1)) #blank set
print(o.intersection(o1)) 
print(o.difference(o1)) 
print(o.symmetric_difference(o1)) 

print(o1.issubset(o))
print(o1.issubset(e))


# Dictionary Intro :

# why we need a Dictionary
# problems with the list
#  we have to refer the INDEX value for any operations
# different list for same related data 

students_name = ['Samir','Saket','Sanjeev','Suresh']
print(students_name[0])
print(students_name[2])
students_name[3]= "Sumit"
print(students_name)

students_marks = [84,87,89,97]


student_info = {'Samir' : 84,
                'Saket' : 87,
                'Sanjeev' : 89,
                'Suresh' : 97}

print(student_info)


# Role of keys :
# keys are index for a dictionary
# to access any value we have to use the keys
# keys are customised indexing 

print(student_info["Suresh"])
print(student_info["Saket"])


# are dictionary ordered ?
# yes but after Python 3.7