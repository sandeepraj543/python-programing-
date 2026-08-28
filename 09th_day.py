# Typecasting in python
# a = "1"
# b = "2"
# print(a + b); # output is 12 because of a and b both are string 
# print(int(a) + int(b)); # output is 3 because of typecasting

# two types of typecasting:

# 1. Explicit Conversion(Explicit type casting in python) 
# done by the programmer, manually as per the requirenment
# Ex = int(), float(), hex(), oct(), str() etc 

# String = "15"
# number = 10
# String_number = int(String)
# sum = String_number + number
# print("sum is", sum);


# 2. Implicit Conversion(Implicit type casting in python)

# One data type is converted into other by the python interpreter itself(automatically).
# python converts a smaller datatype into a higher datatype to prevent data loss.

a = 1.9
print(a);
print(type(a));

b = 8 
print(b);
print(type(b));

print(a + b);
print(type(a+b));