import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

index = 0
closestTemp = None

n = int(raw_input())  # the number of temperatures to analyse
arr = raw_input().split()
for i in arr:
    i = int(i)
    # t: a temperature expressed as an integer ranging from -273 to 5526
    if (closestTemp == None) or (abs(i) < abs(closestTemp)) or (abs(closestTemp) == abs(i) and i > 0 and closestTemp < 0):
        closestTemp = i

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages...

print closestTemp or 0