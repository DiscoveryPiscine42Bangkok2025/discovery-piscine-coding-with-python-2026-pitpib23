#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    z = re.findall("z",string)
    if "z" in z:
        res = "".join(z)
        print(res)
    else: print("none")

#chmod 744 string_are_arrays.py
#./string_are_arrays.py | cat -e
#./string_are_arrays.py "The character Z is not found in this string" | cat -e
#./string_are_arrays.py "The character z is found in this string" | cat -e
#./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
