#!/usr/bin/env python3

ori_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [element + 2 for element in ori_array if element > 5]
print(ori_array)
print(set(new_array))

#chmod 744 play_with_array.py
#./play_with_array.py | cat -e