import sys
import math

message = input()
binary_message = ''
for c in message:
    binary = bin(ord(c))[2:]
    while len(binary) < 7:
        binary = '0' + binary
    binary_message += binary

result = ""
c_bits = 0
last_bit = None
for bit in binary_message:
    if last_bit == None:
        last_bit = bit
        c_bits = c_bits + 1
        if last_bit == "0":
            ch = "00 "
        else:
            ch = "0 "
    else:
        if last_bit == bit:
            c_bits = c_bits + 1
        else:
            result = result + ch + c_bits*"0" + " "
            last_bit = bit
            c_bits = 1
            if last_bit == "0":
                ch = "00 "
            else:
                ch = "0 "

result = result + ch + c_bits*"0"
print(result)