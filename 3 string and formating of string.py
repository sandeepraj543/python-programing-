# string

# str1 = ' hello sandeep '
# str2 = " hello sandeep "
# str3 = """ hello sandeep """
# str4 = ''' hello sandeep '''

# print(str1, str2, str3, str4)

# string concatenation 

# str1 = " hiii sandeep "
# str2 = " hello sandeep "
# print(str1 + "  " + str2)

# length of string

# str1 = "sandeep"
# str2 = "hello sandeep"
# print(len(str1))
# print(len(str2))

# index = it is a sequence of numbers that represent positions of characters in a string. 
# string are immutable, "means" we cannot change the characters of a string by using index. 

# str1 = "hello saumya mam"
# print(str1[3])
# print(str1[9])

# write a python program to take a users name as input and print 
# 1st character , last character and length of the name.

# name = input("enter your name:")
# print("1st character:", name[0])
# print("last character:", name[-1])
# print("length of name:", len(name))

# slicing of string

# string[start : end]  # end index is not including  

# str1 = "sandeepkumarverma"
# print(str1[0:7])
# print(str1[7:12])

# negative indexing = it is used to access the characters from the end of the string.

# negative_str = "sandeepkumarverma"
# print(negative_str[-6:-2]) 

# write a program that takes your favourite fruit name as input 
#                 and prints the middle 3 character and last 2 character

# fruit_name = input("enter your favourite fruit name: ")
# middle_index = len(fruit_name) // 2
# print("middle 3 characters :", fruit_name[middle_index-1:middle_index+2])
# print("last 2 characters :", fruit_name[-2:])

# string methods 

# str = "hello sandeep kumar verma"
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.find("kumar"))
# print(str.replace("sandeep","Raj"))
# print(str.count("a"))

# write a program to take a string as input and print the given question.

# sentence = input("enter a sentence: ")
# print("The given sentence in lowercase is:", sentence.lower())
# print(sentence.replace(" ",","))

# formatting of string

# name = "sandeep kumar verma"
# age = 24

# name = input("enter your name:")
# age = input("enter your age:")
# print(f"my name is {name} and i am {age} years old.")  # using (f) for formating.

# escape sequence
# print("hello mam")
# print("hello\n mam")
# print("hello\t mam")
# print("hello\' mam")
# print("hello\'' mam")
# print("hello\''' mam")