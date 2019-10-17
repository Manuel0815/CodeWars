import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
landing_zone_y, landing_zone_x_start, landing_zone_x_end = 0,0,0
tmp_y = -1
tmp_x = -1
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    if land_y == tmp_y:
        landing_zone_y = land_y
        landing_zone_x_start = tmp_x
        landing_zone_x_end = land_x
        # break
    tmp_y = land_y
    tmp_x = land_x

landing_zone_x_center = (landing_zone_x_start + landing_zone_x_end) / 2

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    power_new = 0
    if v_speed <= -40:
        power_new = 4

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print("-10" + " " + str(power_new))