#!/usr/bin/env python3

print("Enter a number")
num = int(input())
i = 0
for i in range(10):
    print(f"{i} x {num} = {i * num}")

#chmod 744 multiplication_table.py
#./multiplication_table.py