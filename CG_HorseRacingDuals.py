import sys
import math

horses = []
n = int(input())
smallest_diff = -1

for i in range(n):
    horses.append(int(input()))

horses.sort()

for i in range(1, len(horses)):
    diff = abs(horses[i] - horses[i-1])
    if diff < smallest_diff or smallest_diff == -1:
        smallest_diff = diff

print(str(smallest_diff))