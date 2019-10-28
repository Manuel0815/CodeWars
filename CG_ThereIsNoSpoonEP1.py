import sys
import math

# Don't let the machines win. You are humanity's last hope...

w = int(input())  # the number of cells on the X axis
h = int(input())  # the number of cells on the Y axis
grid = [[{'r': None, 'b': None} for x in range(w)] for y in range(h)] 

for i in range(h):
    line = input()  # width characters, each either 0 or .
    for j in range(len(line)):
        grid[i][j]['c'] = str(line[j])
        if line[j] == '0':
            k = j - 1
            while k >= 0:
                if grid[i][k]['r'] == None and grid[i][k]['c'] == '0':
                    grid[i][k]['r'] = str(j) + ' ' + str(i)
                    k = 0
                k -= 1
            
            k = i - 1
            while k >= 0:
                if grid[k][j]['b'] == None and grid[k][j]['c'] == '0':
                    grid[k][j]['b'] = str(j) + ' ' + str(i)
                    k = 0
                k -= 1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# Three coordinates: a node, its right neighbor, its bottom neighbor
for i in range(h):
    for j in range(w):
        if grid[i][j]['c'] == '0':
            if grid[i][j]['r'] == None:
                grid[i][j]['r'] = '-1 -1'
            if grid[i][j]['b'] == None:
                grid[i][j]['b'] = '-1 -1' 
            print(str(j) + ' ' + str(i) + ' ' + grid[i][j]['r'] + ' ' + grid[i][j]['b'])