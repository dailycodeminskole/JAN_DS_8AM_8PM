#################################################
#  16.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
# 👉LISTS
#################################################

# revision string methods
# methods vs functions

print("Hello World")
name = "SAKET"
print(name.lower())

# String methods
print(name.casefold()) #aggressive

quote = "The number 5 is the number of the Lucky"
small = quote.casefold()
print(small)
print(small.count("the"))


print(quote.casefold().count("the")) # method over method

# print(quote.find(5)) # Error  TypeError
print(quote.find("5"))

print(quote.index("5"))


print(quote.find("@")) #return -1 , if character is missing
print("I am Running")
# print(quote.index("@")) # this will break the code if char is missing
print("I am Running")

line = "This is x and y"
print(line.replace("x" , "p"))

name = "                      z"
print(name)
print(len(name))
print(name.strip())
print(len(name.strip()))


num = "1110222033304440555"
print(num.split("0"))

acc_num = "1173.111.081.999"
print(acc_num.split("."))



# Intro to list
# creating a list using constructor/type casting

even_num = "123"
print(even_num)
print(type(even_num))


num = list(even_num)
print(type(num))

print(num)


name = "CHINMAY"
print(list(name))


# direct way by writing the items inside a square bracket

list_odd = [1,3,5,7,9]
print(type(list_odd))
print(list_odd)

ans = str(list_odd)
print(ans)
print(type(ans))
print(ans)

z = []
print(z)
print(type(z))

z = [""]
print(z)
print(type(z))

z = [" "]
print(z)
print(type(z))