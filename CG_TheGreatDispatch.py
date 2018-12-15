import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



box_count = int(raw_input())
for i in xrange(box_count):
    weight, volume = [float(j) for j in input().split()]

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print "0 0 0 0 0 ..."

# each truck 100 volume
# boxes between 100 and 3300
# weight 0 to 100
# volume 0 to 26