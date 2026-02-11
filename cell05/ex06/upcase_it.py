#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1,len(sys.argv)):
        print(sys.argv[i].upper())

#chmod 744 upcase_it.py
#./upcase_it.py "initiation" | cat -e
#./upcase_it.py 'This exercise is quite easy!' | cat -e