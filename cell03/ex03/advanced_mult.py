#!/usr/bin/env python3

i = 0
j = 0
while i in range(11):
    print(f"Table de {i}: ",end = "")
    while j in range(11):
        if j == 10:
            print(f"{i * j}")
        else: print(f"{i * j}",end = " ")
        j += 1
    j = 0
    i += 1

#chmod 744 advanced_mult.py
#./advanced_mult.py

