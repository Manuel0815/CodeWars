import sys
import math

def inc_grid_pos(grid, cur_x, cur_y):
    grid[cur_y][cur_x] += 1
    return grid

def move(grid, cur_x, cur_y, dir):
    grid = inc_grid_pos(grid, cur_x, cur_y)
    if dir == '^':
        cur_y -= 1
    elif dir == '>':
        cur_x += 1
    elif dir == 'v':
        cur_y += 1
    else: # dir == '<'
        cur_x -= 1
    return grid, cur_x, cur_y

def can_move(grid, cur_x, cur_y, h, w, dir):
    if dir == '>' and cur_x < w - 1 and grid[cur_y][cur_x + 1] != '#':
        return True
    elif dir == 'v' and cur_y < h - 1 and grid[cur_y + 1][cur_x] != '#':
        return True
    elif dir == '<' and cur_x > 0 and grid[cur_y][cur_x - 1] != '#':
        return True
    elif dir == '^' and cur_y > 0 and grid[cur_y - 1][cur_x] != '#':
        return True
    else:
        return False

def rotate_dir(dir, clockwise):
    if not clockwise: # counter clockwise
        if dir == '>':
            return '^'
        elif dir == '^':
            return '<'
        elif dir == '<':
            return 'v'
        else: # dir == 'v'
            return '>'
    else:
        if dir == '>':
            return 'v'
        elif dir == 'v':
            return '<'
        elif dir == '<':
            return '^'
        else: # dir == '^'
            return '>'

'''
1. check if there is a wall at left/right side (defined via variable 'clockwise')
2. if there is no wall, move there
3. if there is a wall, try to move to direction dir (= rotated tmp_dir back)
4. if you cannot move there, rotate direction dir further, until you can move or realize you are trapped (tmp_dir == dir)
'''
def make_game_move(grid, cur_x, cur_y, h, w, dir, clockwise, game_over):
    tmp_dir = rotate_dir(dir, clockwise)
    clockwise = not clockwise 
    if (can_move(grid, cur_x, cur_y, h, w, tmp_dir)):
        grid, cur_x, cur_y = move(grid, cur_x, cur_y, tmp_dir)
    else:
        tmp_dir = rotate_dir(tmp_dir, clockwise)
        can = can_move(grid, cur_x, cur_y, h, w, tmp_dir)
        while not can and not game_over:
            tmp_dir = rotate_dir(tmp_dir, clockwise)
            if tmp_dir == dir:
                game_over = True
            can = can_move(grid, cur_x, cur_y, h, w, tmp_dir)
        if not game_over:
            grid, cur_x, cur_y = move(grid, cur_x, cur_y, tmp_dir)

    dir = tmp_dir
    return grid, cur_x, cur_y, dir, game_over

# input data
init_x, init_y = 0,0
w, h = [int(i) for i in input().split()]
grid = [[0 for x in range(w)] for y in range(h)] 
dir = ''
for i in range(h):
    line = input()
    for j in range(w):
        if str.isnumeric(line[j]) or line[j] != '#':
            grid[i][j] = 0
            if line[j] not in '0#':
                init_x = j
                init_y = i
                dir = line[j]
        else:
            grid[i][j] = '#'

side = input() # L or R

cur_x = init_x
cur_y = init_y

game_over = False

# check if there is a wall at desired side.
# if there is no wall, you have to move there to keep following wall
clockwise = True
if (side == 'L'):
    clockwise = False

grid, cur_x, cur_y, dir, game_over = make_game_move(grid, cur_x, cur_y, h, w, dir, clockwise, game_over)

while not (init_x == cur_x and init_y == cur_y) and not game_over:
    grid, cur_x, cur_y, dir, game_over = make_game_move(grid, cur_x, cur_y, h, w, dir, clockwise, game_over)

for i in range(h):
    l = ""
    for j in range(w):
        l += str(grid[i][j])
    print(l)