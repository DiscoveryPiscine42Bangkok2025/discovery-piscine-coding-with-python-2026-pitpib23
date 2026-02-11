#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    i = len(sys.argv)-1
    while i > 0:
        print(sys.argv[i])
        i -= 1

#chmod 744 aff_rev_params.py
#./aff_rev_params.py | cat -e
#./aff_rev_params.py "coucou" | cat -e
#./aff_rev_params.py "Python" "piscine" "hello" | cat -e