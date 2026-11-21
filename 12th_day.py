# String slicing and operation
names = "sandeep, sohan, mohan, Gopal"
print(len(names))

print(names[0:5]) # 0 to (5-1=4)tak ka sabhi character print ker dega 
print(names[ :5]) # python bydefault zero add kr leta hai
print(names[2:6]) 

my_name = "sandeep"
len1 = len(my_name)
print("In my name", len1, "letters present.")

fruit = "mango"
print(fruit)
print(len(fruit))

print(fruit[0:5])
# both line are similar
print(fruit[ :5])

print(fruit[0:-3]) 
# similar as given just below
print(fruit[0:len(fruit)-3]) # python actually aise kaam krta hai

#print(fruit[-1:-3]) # ye shi nhi hai

print(fruit[-3:-1]) 
# ye code aise me kaam ker rha hai
print(fruit[len(fruit)-3:len(fruit)-1]) 

# quick quiz
nm = "Harry"
print(nm[-4:-2]) # ans is ar
# explanation
print(nm[len(nm)-4 : len(nm)-2])