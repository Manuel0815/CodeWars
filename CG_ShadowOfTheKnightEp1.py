import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x_low = 0
x_high = w
x_next = x0

y_low = 0
y_high = h
y_next = y0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if ('U') in bomb_dir:
        y_high = y_next
        y_next = int(y_next - (y_next - y_low) / 2)
    elif ('D') in bomb_dir:
        y_low = y_next
        y_next = int(y_next + (y_high - y_next) / 2)

    if ('L') in bomb_dir:
        x_high = x_next
        x_next = int(x_next - (x_next - x_low) / 2)
    elif ('R') in bomb_dir:
        x_low = x_next
        x_next = int(x_next + (x_high - x_next) / 2)

    # the location of the next window Batman should jump to.
    print(str(x_next) + " " + str(y_next))