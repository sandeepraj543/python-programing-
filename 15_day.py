# Exercise 2 : Good morning sir according to time

import time
timestamp = (time.strftime('%H:%M:%S'))  # ye current time batane ke lea hai
print(timestamp)

timestamp = time.strftime('%H') # ye sirf current hour batane ke lea
print(timestamp)

timestamp = time.strftime('%M') # ye sirf current minute batane ke lea
print(timestamp)

timestamp = time.strftime('%S') # ye sirf current second batane ke lea
print(timestamp)

hour = int(time.strftime('%H')) # time ko integer me convert kr lea

if 5 <= hour < 12:
    print("Good morning, Sir! Have a great day.")
elif 12 <= hour < 17:
    print("Good afternoon, Sir! Hope you are doing well.")
elif 17 <= hour < 21:
    print("Good evening, Sir! Welcome back.")
else:
    print("Good night, Sir! Have a peaceful night.")













