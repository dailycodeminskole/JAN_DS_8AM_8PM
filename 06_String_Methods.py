#################################################
#  14.02.2023 8.00PM
#################################################
#  TOPICS TO BE COVERED 
# 👉String Methods
#################################################
# HW Soln

sentence = " My email ID is nikhil.pune@yahoo.com $"
print(sentence[0])
print(sentence[-12])
print(sentence[-11:-6])
print(sentence[-1])
print(sentence[0::4])
print(sentence[::-1])

# What are methods
# methods vs functions

name =  "ANU"
print(name) #function , independent 
print(name.lower()) #methods , requires certain variable/object


# String methods

print(name.title()) # Title case

# casefold()	Converts string into lower case
print(name.lower()) #  lower case , soft conversion , works good for Eng only
print(name.casefold()) # lower  case , aggressive for any language



# count()	Returns the number of times a specified value occurs in a string
sentence = " My email ID is nikhil.pune@yahoo.com $"
print(sentence.count("@"))
print(sentence.count(".com"))
print(sentence.count("i"))

print(sentence.casefold().count("i")) #we can use method over other method



# find()	Searches the string for a specified value and returns the position of where it was found
print(sentence.find("$"))
print(sentence.find("@"))
print(sentence.find(" ")) #first instance only
print(sentence.find("#")) #return -1 if charcter is not there



# index()	Searches the string for a specified value and returns the position of where it was found

print(sentence.index("$"))
print(sentence.index("@"))
print(sentence.index(" ")) #first instance only
# print(sentence.index("#")) # break the code #ValueError

# replace()	Returns a string where a specified value is replaced with a specified value
sentence = " My email ID is nikhil.pune@yahoo.com $"

print(sentence.replace("email", "MailBox"))
print(sentence.replace("$", ""))


# strip()	Returns a trimmed version of the string

print(sentence)
print(sentence.strip())
print(len(sentence))
print(len(sentence.strip()))


# split()	Splits the string at the specified separator, and returns a list
print(sentence.split("@")) # op will be a list
print(sentence.split(" ")) # op will be a list