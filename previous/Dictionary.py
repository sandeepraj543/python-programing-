# Dictionary : A dict is a built-in data type in python used to store data in key-value pairs. 

# Student = {
#     "name" : "sandeep kumar verma.",
#     "city" : "nawada.",
#     "pin-code" : "805124",
#     "roll-number" : "06"
# }

# print(type(Student))

# print(Student["name"])
# print(Student["city"])
# print(Student["pin-code"])
# print(Student["roll-number"])


# dictonary in python last keys are valid, dictonary ignore the previous keys 

# Student = {
#     "name" : "sandeep kumar verma.",
#     "city" : "nawada.",
#     "pin-code" : "805124",
#     "roll-number" : "06",
#     "name" : "verma jii", # over-right
#     "city" : "Bihar"   # over-right
# }

# # print the whole dictonary value
# print(Student)

# # print the specific data which i want
# print(Student["name"]) 
# print(Student["city"])

# # update the dictonary value/keys outside in dictonary
# Student["city"] = "patna" 

# # create a new dictionary value
# Student["country"] = "india"

# # print the updated value
# print(Student["city"])
# print(Student["country"])

# print(Student)
# # if you want to remove any key/value then use pop commend
# Student.pop("name") 
# print(Student)

# # dictionay methods 
# print(Student.keys())
# print(Student.values())
# print(Student.items())
# print(Student.copy())

# nested methode
# example : 1

# profile = {
#     "username" : "sandeep kumar verma",
    
#     "details" : {
#         "phone_no": "9632587410",
#         "ista_id" : "sandeep",
#         "age" : "24"
#     }
# }

# print(profile["username"])
# print(profile["details"]["phone_no"])
# print(profile["details"]["ista_id"])

# example: 2 

# Mygf = {
#     "username" : "Rajnandani kumari",
#     "nick_name" : "patlu",

#     "All Details" : {
#         "contect_no" : "9632587410",
#         "F_name" : "kalua",
#         "M_name" : "pyari_devi",
#         "Brothers" : "3",
#         "Sister" : "0",
#         "Home_town" : "lakhisarai",
#         "State" : "Bihar",
#         "capital" : "india"
#     }
# }

# print(Mygf)

# question_no- 01
# create a dictionay named Marks to store marks of 3 subjects. Add the subjects one by one and print the final dictionary.

# Marks = {
#     "math" : "88",
#     "science" : "85",
#     "english" : "90"
# }
# print(Marks)

# sets in python : A set is a collection of unordered and unique items. sets automatically remove duplicate elements and are written using curly braces{}

# food = {"paneer", "chole", "sandwitch", "aalu-paratha", "paneer"}
# print(type(food))
# print(food)
# food.add("samosa")
# print(food)

language = {"python", "java", "c++", "R", "python", "PYTHON"}
print(type(language))
print(language)
language.add("c")
print(language)
language.remove("PYTHON")
print(language)
language.pop() # remove the upper element from the set
print(language)


# creating empty set
empty_set = set()
print(type(empty_set))






