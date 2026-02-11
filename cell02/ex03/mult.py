#!/usr/bin/env python3

print("Enter the first number:")
first_num = int(input())
print("Enter the second number:")
second_num = int(input())

result = first_num * second_num
print(f"{first_num} x {second_num} = {result}")

if result == 0:
    print("This number is both positive and negative.")
elif result < 0:
    print("This number is negative.")
elif result > 0:
    print("This number is positive.")

#chmod 744 mult.py
#./mult.py