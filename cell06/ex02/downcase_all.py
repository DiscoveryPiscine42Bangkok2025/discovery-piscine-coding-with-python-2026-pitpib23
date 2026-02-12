#!/usr/bin/env python3

import sys

def downcase_it(tmp):
    res = tmp.lower()
    return res

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))

# chmod 744 downcase_all.py
# ./downcase_all.py
# ./downcase_all.py "HELLO WORLD" "I understood Arrays well!"