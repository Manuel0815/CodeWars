import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


cells = []

def get_cell_value(cell):
    if "val" in cell:
        return cell["val"]

    arg_1 = cell.get("arg_1")
    if "$" in arg_1:
        arg_1 = get_cell_value(cells[int(arg_1[1:])])

    arg_2 = cell.get("arg_2")
    if "$" in arg_2:
        arg_2 = get_cell_value(cells[int(arg_2[1:])])

    op = cell.get("operation")
    if op == "ADD":
        cell["val"] = int(arg_1) + int(arg_2)
    elif op == "MULT":
        cell["val"] = int(arg_1) * int(arg_2)
    elif op == "SUB":
        cell["val"] =  int(arg_1) - int(arg_2)
    elif op == "VALUE":
        cell["val"] =  int(arg_1)

    return cell["val"]

n = int(input())
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    cells.append({"operation": operation, "arg_1": arg_1, "arg_2": arg_2})

for i in range(n):
    print(str(get_cell_value(cells[i])))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)