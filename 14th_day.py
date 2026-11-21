# conditional statement

# age = int(input("Enter your age:"))
# print("your age is:", age)

# conditional operators
# >, <, >=, <=, ==, !=

# print(age > 18)
# print(age < 18)
# print(age >= 18)
# print(age <= 18)
# print(age == 18)
# print(age != 18)

# if-else condition
 
# if(age>=18):
#     print("you can drive")
#     print("yes")
# else:
#     print("you can not drive")
#     print("no")
# print("this line is not the part of else block")

# if-elif else condition

# Example: 1

# applePrice = 10;
# budget = 200;
# if (budget - applePrice > 100):
#     print("Alexa, its ok you can buy")
# elif (budget - applePrice > 70):
#     print("Alexa, add 1kg apples to the cart")
# else:
#     print("Alexa, do not add apples to the cart.")
 

# Example: 2

# num = int(input("Enter the value of num: "))
# if (num < 0):
#     print("number is negative.")
# elif (num == 0):
#     print("number is zero.")
# elif (num > 20):
#     print("number is greater than 20")
# else:
#     print("number is positive.")

# print("I am happy now")

# nested if statement 

num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negative:")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1 to 10")
    elif (num > 10 and num <= 20):
        print("Number is between 11 to 20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")






