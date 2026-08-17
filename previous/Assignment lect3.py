# mini project: emoji converter 

msg = input("Enter your message through any number (0-9):")
msg = msg.replace("0","😁")
msg = msg.replace("1","😊")
msg = msg.replace("2","😍")
msg = msg.replace("3","😇")
msg = msg.replace("4","❤️")
msg = msg.replace("5","🌟")
msg = msg.replace("6","🙏")
msg = msg.replace("7","😒")
msg = msg.replace("8","👌")
msg = msg.replace("9","🥰")

print(msg)

# write a program that takes a sentence and print-
# total character , uppercase version , lowercase version 

sentence = input ("Enter a sentence:")
print("Total characters in these sentence are :", len(sentence))
print("Uppercase version of the sentence is :", sentence.upper())
print("Lowercase version of the sentence is :", sentence.lower())
