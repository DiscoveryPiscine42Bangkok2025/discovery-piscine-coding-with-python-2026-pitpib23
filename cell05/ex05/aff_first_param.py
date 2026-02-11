#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    print(sys.argv[1])

#chmod 744 aff_first_param.py
#./aff_first_param.py | cat -e
#./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e