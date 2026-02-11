#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
for i in range(3):
    print(f"In {(i + 1) * 10} years, you'll be {(i + 1) * 10 + age} years old.")

#chmod 744 age.py
#./ age.py