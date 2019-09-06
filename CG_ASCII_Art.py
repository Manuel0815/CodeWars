import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

l = int(input())     # width
h = int(input())     # height
t = input().upper()  # text

for i in range(h):
    row = input()
    tmp = ""
    for c in t:
        n = ord(c) - 65 if ord(c) - 65 >= 0 and ord(c) - 65 <= 25 else 26
        tmp = tmp + row[n * l : n * l + l]
    print(tmp)
