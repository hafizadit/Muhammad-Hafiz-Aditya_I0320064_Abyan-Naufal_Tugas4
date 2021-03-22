# !/usr/bin/python

a = 60    # 60 = 0011 1100
b = 13    # 13 = 0000 1101
c = 0

c = a & b   # And, 12 = 0000 1100
print("Line 1 - value of c is", c,", Binary :",format(c,'08b'))

c = a | b   # Or, 61 = 0011 1101
print("Line 2 - value of c is", c,", Binary :",format(c,'08b'))

c = a ^ b   # Xor, 49 = 0011 0001
print("Line 3 - value of c is", c,", Binary :",format(c,'08b'))

c = ~a;     # Not, -61 = -0111101
print("Line 4 - value of c is", c,", Binary :",format(c,'08b'))

c = a << 2  # >>, 240 = 1111 0000
print("Line 5 - value of c is", c,", Binary :",format(c,'08b'))

c = a >> 2  # <<, 15 = 0000 1111
print("Line 6 - value of c is", c,", Binary :",format(c,'08b'))