# String : anything that you enclosed between single or double quotation is considered a string.
name = "sandeep"
friend = "sohan"
another_friend = "rohan"
# fruit = "he said, "i want to eat an apple"  # here occur error because double cotation not apply
fruit = 'he said, "i want to eat an apple'  # this is the correct way to write this type of code

print(fruit)
print(name,friend, another_friend)

# if i want to multiple line of string 
# kisi v sentence ko likhna ho as itis tb ye bahut useful hota hai
fruit1 = '''he said', 
hii sandeep
hey i am a good boy
"I want to eat an apple.'''    # 3 (single/double cotation) """  """ or ''' '''
print(fruit1) 

indexing = "sandeep" 
print(indexing[0])
print(indexing[1])
print(indexing[2])
print(indexing[3])
print(indexing[4])
print(indexing[5])
print(indexing[6])
# print(indexing[7]) # this throw an error(index out of range)

# for loop with string
print("\nlets use a for loop\n")
for character in indexing:
    print(character)

print("\nlets use a for loop\n")
for character in fruit1:
    print(character)


