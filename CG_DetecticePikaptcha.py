import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
grid = [[0 for x in range(w)] for y in range(h)] 
for i in range(h):
    line = input()
    for j in range(w):
        grid[i][j] = line[j]

for i in range(h):
    for j in range(w):
        if grid[i][j] != '#':
            c = 0
            if i > 0 and grid[i-1][j] != '#':
                c+=1
            if i < h - 1 and grid[i+1][j] != '#':
                c+=1
            if j > 0 and grid[i][j-1] != '#':
                c+=1
            if j < w - 1 and grid[i][j+1] != '#':
                c+=1
            grid[i][j] = c
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

for i in range(h):
    l = ""
    for j in range(w):
        l += str(grid[i][j])
    print(l)