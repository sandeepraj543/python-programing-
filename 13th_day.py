# string methods
# strings are immutable
str1 = "Sandeep"
print(len(str1))
print(str1.upper()) # SANDEEP
print(str1.lower())

str2 = "!!!!sandeepkr!!!!!!!!!!!"
print(str2)
print(str2.rstrip("!")) # ye sirf baad bale string ko strip krta hai
print(str2.replace("kr", "kumar")) # multiple "kr" hota tb savi ko replace kr deta

str3 = "!!!!! sandeep kumar @@@@@"
print(str3)
print(str3.split(" ")) 

blogheading = "introduction to js"
print(blogheading.capitalize()) # convert 1st letter in capital letter

blogheading = "intRoducTion tO jS"
print(blogheading.capitalize()) # pura sentence ko analysice krke correct ker deta hai

str4 = "Welcome to the Console"
print((str4.center(50))) # apne aage 50 character space free ker dega
print(len(str4.center(50)))
print(len(str4))

str5 = "hii sandeep HII hello sandeep"
print(str5.count("sandeep"))   # ye count krke batata hai ki diya hua string kitni baar a rha hai
print(str5.count("hii"))

str6 = "Welcome to the console !!!"
print(str6.endswith("!!!"))       # boolean type me result show krega True/False
print(str6.endswith(" hii "))     # boolean type me result show krega True/False

print(str6.endswith("to", 4, 10))  # 4 se 10 ke bitch me (to) a rha hai

str7 = "He's name is Dan. He is an honest man."
print(str7.find("is"))   # jhaha v first time string match krega oha ka string return kr dega
print(str7.find("isss"))   # nhi match krne per (-1) return ker dega 

print(str7.index("is"))     # ye v index return krta hai first time match hone per 
#print(str7.index("isss"))   # nhi match krne per error show krega 

# agar aap confirm hai ki wo string mil skta hai tbhi aap index use kre otherwise find is better option 

str8 = "Welcometotheconsole" 
print(str8.isalnum())  # it returns true if entire strings consists with A-Z, a-z, 0-9.

str8 = "Welcome to the console" 
print(str8.isalnum())  # it returns false if entire strings not consists with A-Z, a-z, 0-9.

str9 = "welcome"
print(str9.isalpha())   # isalpha() returns true if the entire strings consists of A-Z,a-z.

str9 = "welcome000"
print(str9.isalpha())   # isalpha() returns False if the any other number, punctuatios or characters are present.

str9 = "welcome365"
print(str9.isalpha()) 

str9 = "welcome,,,"
print(str9.isalpha()) 

str10 = "hello world"
print(str10.islower())   # kya savi character lower case me hai tb true return krega

string10 = "HELLO world"
print(string10.islower()) 

str11 = " we wish you a Marry Christmas\n "
print(str11.isprintable())     # (\n) printable nhi hai eslea False return krega   

str12 = "         "   # es black ko maine spacebaar ki help se di hai
print(str12.isspace())

str13 = "           "   # es blank ko maine TAB key ki help se di hai
print(str13.isspace())

str14 = "World Health Organization"     #True
print(str14.istitle()) 

str15 = "World health organization"     #false
print(str15.istitle())

str16 = "Python is a interpreted language"
print(str16.startswith("Python"))      # yes ye python string se start ho rha hai 

print(str16.swapcase())     # ye uppercase ko lowercase me convert ker deta hai

str17 = "His name is Dan. Dan is an honest man."
print(str17.title())






