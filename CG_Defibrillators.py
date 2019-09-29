import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def clean_input(inp):
    return float(inp.replace(",", "."))


lon = clean_input(input())
lat = clean_input(input())
n = int(input())

d = None
closest_defib = None

for i in range(n):
    defib = input().split(";")
    lon_defib = clean_input(defib[4])
    lat_defib = clean_input(defib[5])

    x = (lon_defib - lon) * math.cos((lat + lat_defib) / 2)
    y = lat_defib - lat
    d_tmp = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) * 6371

    if d == None or d_tmp < d:
        d = d_tmp
        closest_defib = defib[1]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# 1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217

print(closest_defib)
