#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for arg in args:
        if not arg.endswith("ism"):
            print(arg + "ism")

# chmod 744 append_it.py
# ./append_it.py | cat -e
# ./append_it.py "parallel" "egoism" "human" | cat -e

