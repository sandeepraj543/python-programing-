# condition : A condition is simply a statement that can be either true or false.

# age = 18

# if age >= 18:     #condition
#     print ("Your are elegible to vote")

# If statement: if condition is true, the block of code runs, otherwise it is skipped.

age = int(input("Enter your age: "))

if age >= 18: #condition
    print ("you are elegible to vote")

# print(" NOTIC: The candidate age is must be  morethan or equal to 18 ")

# if else statement: if condition is true, the block of code under if runs,
                   # otherwise the block of code under else runs. 

# age = int(input("Enter your age:"))

# if age >= 18:
#     print("You are elegible to vote")
# else:
#     print("you are not elegible to vote")

# if elif else statement: it condition is used when there are multiple conditions to check. 
                   # The first condition that is true will execute and the rest will be skipped. 

# marks = int(input("Enter your marks:"))

# if marks >= 90:
#     print("Grade A")

# elif marks >= 80:
#     print("Grade B")

# elif marks >= 70: 
#     print("Grade C")

# elif marks >= 60:
#     print("Grade D")

# else:
#     print("Improvement needed")

# list in python : A list is a built-in-data type that can store multiple items in a single variable,
                 # and the items are ordered and changeable. 

# student1 = ["sandeep", "23", "Btech"]
# student2 = ["akok", "25", "Btech"]
# print(student1)
# print(student2)

# Accessing of list items using index: - Each item in a list has an assigned index, index starts from 0.

# student = ["sandeep", "23", "Btech","selected"]

# print("first value of the list is", student[0])  # because index starts from 0.
# print(student[1])
# print(student[2])
# print("Total no of length in this list is", len(student))

# modifying list items: - we can modify the items of a list by referring to their index number.

# student = ["sandeep", "23", "Btech","selected"]
# print("original list",student)
# student[1:2] = ("25" ,"Mtech")   # or student[1]=25 modifycation
# print("modified list",student)

# list slicing:- we can return a range of items by specifying where to start and where to end the slice.

# marks = [45,56,85,95,78,86,65,32,25,94]
# print(marks[3:7]) # prints items from index 3 to index 6 (7 is not included)
# print(marks[2:8]) # prints items from index 2 to index 7 (8 is not included)

# Negative indexing :- Negative indexing means beginning from the end, -1 refers to the last item,
                    #  similarly -2 second last item and so on. 

# marks = [45,56,85,95,78,86,65,32,25,94]
# print(marks[-3:-1])

# list functions :- 

# marks = [45,56,85,95,78,86,65,32,25,94]

# # print(len(marks))
# # print(max(marks))
# # print(min(marks))

# marks.append(100)    # through append() we can add an item to the end of the list.
# print(marks)

# marks.sort()         # through sort() we can sort the list in accending order.
# print(marks)

# marks.reverse()      # through reverse() we can reverse the order of the list.
# print(marks)

# marks.insert(3,99)    # through insert() we can add an item at the specified index. 
# print(marks)

# # many more functions are there simply type list. and show here all functions.


# tuple in python :- a tuple is a built-in-data type that stores multiple values like a list, but 
                   # tuples are immutable, means we cannot change, add or remore if created.

# tuple1 = ("sandeep", 85, "ok", "correct")
# print(tuple1)

# tuple1[1]= 90  # this will give error because tuple is immutable.
# print(tuple1)

# empty tuple 

# emp_tuple = ()       # it react as an tuple
# sin_tuple = (2)      # only single tuple react as an integer.
# single_tuple = (2,)  # it react as an tuple
# dou_tuple = (2,5)    # it react as an tuple

# print(emp_tuple)
# print(type(emp_tuple))
# print(type(sin_tuple))  
# print(type(single_tuple))
# print(type(dou_tuple))

# tuple_a= ("aman","rohit","vikesh","rohan","rohit")

# print(tuple_a.index("rohit"))
# print(tuple_a.index("rohan"))

# print(tuple_a.count("rohit"))
# print(tuple_a.index("rohan"))