import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
ghost_legs = [[0 for x in range(w)] for y in range(h)] 
for i in range(h):
    line = input()
    for c in range(w):
        ghost_legs[i][c] = line[c]

for lane in range(w): # each column
    if ghost_legs[0][lane] != " ": # path to follow
        start = ghost_legs[0][lane] # first char of result
        for row in range(1, h): # follow path down
            if ghost_legs[row][lane] != "|": # end found, print result
                print(start + ghost_legs[row][lane])
            elif lane < (w-1) and ghost_legs[row][lane+1] == "-": # change lane, go right
                lane += 3
                # while ghost_legs[row][lane] == "-":
                #     lane += 1
            elif lane > 0 and ghost_legs[row][lane-1] == "-": # change lane, go left
                lane -= 3
                # while ghost_legs[row][lane] == "-":
                #     lane -= 1
        
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)