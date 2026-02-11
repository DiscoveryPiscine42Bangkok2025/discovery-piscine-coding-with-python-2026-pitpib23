#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1,len(sys.argv)):
        print(sys.argv[i].lower())

#chmod 744 downcase_it.py
#./downcase_it.py | cat -e
#./downcase_it.py "LUCIOLE" | cat -e
#./downcase_it.py 'This exercise is quite easy!' | cat -e