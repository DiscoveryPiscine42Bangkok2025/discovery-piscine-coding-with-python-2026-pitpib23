#!/usr/bin/env python3

import sys
import re

if len(sys.argv) < 3:
    print("none")
else:
    print(len(re.findall(sys.argv[1],sys.argv[2])))

#chmod 744 scan_it.py
#./scan_it.py | cat -e
#./scan_it.py "the" | cat -e
#./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
