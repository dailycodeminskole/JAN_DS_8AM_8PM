#################################################
#  23.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
#  👉For Loop...
#################################################

# revision
print(range(1,11))
print(type(range(1,11)))
print(list(range(1,11)))
print(list(range(10,101,10)))


for i in range(10,101,10):
    print(i)


for i in range(10,101,10):
    print(i**2)

# Eg 1
fruits = ['apple','banana','grapes','orange']
print(fruits[0])
print(len(fruits[0]))
print(len(fruits[1]))

lenght = [] #to store the lenght of each element
for i in fruits:
    # print(len(i))
    lenght.append(len(i))

print(lenght)


# Eg2.

num = [-1,-2,-5,8,7,12,-19]

# developing the logic
if 10 > 0:
    print("number is positive")
else:
    print("number is negative")



for i in num:
    if i > 0:
        print("number is positive")
    else:
        print("number is negative")

num_pos = []
num_neg = []

for i in num:
    if i > 0:
        num_pos.append(i)
    else:
        num_neg.append(i)

print(num_pos)
print(num_neg)


# Eg 3


list_num = [12,45,78,44,13,16,15,47]
list_even = []
list_odd = []
print(bool(12%2==0))

for i in list_num:
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)

print(list_even)
print(list_odd)



# Eg 4.
# Nested loop
# outer loop
# inner loop


for i in range(1,11):
    for j in range(1,11):
        product = i*j
        print(product)



