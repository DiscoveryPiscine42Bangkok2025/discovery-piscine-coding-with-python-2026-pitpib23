#!/usr/bin/env python3

import sys

def greetings(name=None):
    if name == None:
        print("Hello, noble stranger.")
    elif isinstance(name,str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")
    
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)


# chmod 744 greetings_for_all.py
# cat greetings_for_all.py | cat -e
# 
