import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

types = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    types[ext.upper()] = mt

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# For each of the Q filenames, display on a line the corresponding MIME type.
# If there is no corresponding type, then display UNKNOWN.

for i in range(q):
    fname = input()  # One file name per line.
    t = fname.rsplit('.', 1)[-1].upper()
    if t in types and "." in fname:
        print(types[t])
    else:
        print("UNKNOWN")