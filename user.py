# Program: Username & Password Gen
# Author: R
# Creation Date: 1-9-2021
#!/usr/bin/env python3

import random

print("Username & Password Generator\n"),
print("The options are:\n"),
user_option = ["[1] Username", "[2] Password"]

for option in user_option:
    print(option)
    print()
question = input("Select option: ")

if question == "1":
    user = []
    with open("names.txt", "r") as f:
        user = f.readlines()
        print("How about?:", random.choice(user)),

elif question == "2":
    password = []
    with open("rockyou.txt", "r", encoding="utf8") as f:
        password = f.readlines()
        print("How about?:", random.choice(password)),

else:
    print("Topic entered not in the list!")
    print("Goodbye")
    exit()
