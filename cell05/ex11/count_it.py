#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    print(f"parameters: {len(sys.argv)-1}")
    for i in range(1,len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")

#chmod 744 count_it.py
#./count_it.py | cat -e
#./count_it.py "Game" "of" "Thrones" | cat -e