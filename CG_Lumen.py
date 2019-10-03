import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = int(input())

grid = [['' for x in range(n)] for y in range(n)]
result_grid = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    grid[i] = input().split(" ")

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for y in range(n):
    for x in range(n):
        if grid[y][x] == 'C':
            result_grid[y][x] = l
            for i in range(n):
                for j in range(n):
                    if abs(i - y) <= l and abs(j - x) <= l:
                        result_grid[i][j] = max(result_grid[i][j], l - max(abs(i - y), abs(j - x)))

print(sum([result_grid[i].count(0) for i in range(n)]))