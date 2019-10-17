import sys
import math
import random

# Deliver more amadeusium to hq (left side of the map) than your opponent. Use radars to find amadeusium but beware of traps!

# height: size of the map
width, height = [int(i) for i in input().split()]

NONE = -1
ROBOT_ALLY = 0
ROBOT_ENEMY = 1
HOLE = 1
RADAR = 2
TRAP = 3
AMADEUSIUM = 4


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pos):
        return abs(self.x - pos.x) + abs(self.y - pos.y)


class Entity(Pos):
    def __init__(self, x, y, type, id):
        super().__init__(x, y)
        self.type = type
        self.id = id


class Robot(Entity):
    def __init__(self, x, y, type, id, item):
        super().__init__(x, y, type, id)
        self.item = item

    def is_dead(self):
        return self.x == -1 and self.y == -1

    def is_alive(self):
        return not self.is_dead()

    @staticmethod
    def move(x, y, message=""):
        print(f"MOVE {x} {y} {message}")

    @staticmethod
    def wait(message=""):
        print(f"WAIT {message}")

    @staticmethod
    def dig(x, y, message=""):
        print(f"DIG {x} {y} {message}")

    @staticmethod
    def request(requested_item, message=""):
        if requested_item == RADAR:
            print(f"REQUEST RADAR {message}")
        elif requested_item == TRAP:
            print(f"REQUEST TRAP {message}")
        else:
            raise Exception(f"Unknown item {requested_item}")
    
    def find_nearest_amadeusium(self, grid, player_advantage):
        shortest_dist = -1
        target = None
        for c in grid.cells: 
            if c.amadeusium != '?' and int(c.amadeusium) > 0 and ((not c.has_trap() and player_advantage) or not c.has_hole()):
                if shortest_dist == -1 or shortest_dist > c.distance(Pos(self.x, self.y)):
                    shortest_dist = c.distance(Pos(self.x, self.y))
                    target = Pos(c.x, c.y)
        return target

    def find_nearest_n_amadeusium(self, grid, amount):
        shortest_dist = -1
        target = None
        for c in grid.cells: 
            if c.amadeusium != '?' and int(c.amadeusium) == amount and not c.has_hole():
                if shortest_dist == -1 or shortest_dist > c.distance(Pos(self.x, self.y)):
                    shortest_dist = c.distance(Pos(self.x, self.y))
                    target = Pos(c.x, c.y)
        return target

    def get_nearest_amadeusium_before_request(self, grid, item, player_advantage):
        shortest_dist = 4
        target = None
        for c in grid.cells:
            if c.amadeusium != '?' and int(c.amadeusium) > 0 and ((not c.has_trap() and player_advantage) or not c.has_hole()):
                if shortest_dist == -1 or shortest_dist > c.distance(Pos(self.x, self.y)):
                    shortest_dist = c.distance(Pos(self.x, self.y))
                    target = Pos(c.x, c.y)
        if target is None:
            self.request(item)
        else:
            self.dig(target.x, target.y)

    def place_radar_at_next_spot(self, grid, ideal_radar_pos):
        if len(ideal_radar_pos) > 0:
            p = ideal_radar_pos.pop(0)
        else:
            p = self.get_random_pos(grid)
        while grid.get_cell(p.x, p.y).has_radar():
            if len(ideal_radar_pos) > 0:
                p = ideal_radar_pos.pop(0)
            else:
                p = self.get_random_pos(grid)
        self.dig(p.x, p.y)

    def get_random_pos(self, grid):
        x, y = random.randint(1, width - 1), random.randint(0, height - 1)
        while grid.get_cell(x, y).has_trap() or grid.get_cell(x, y).has_radar():
            x, y = random.randint(1, width - 1), random.randint(0, height - 1)
        return Pos(x, y)

    def go_to_nearest_cell_without_hole(self, grid):
        target = None
        shortest_dist = -1
        for c in grid.cells: 
            if not c.has_hole() and c.x > 2 and str(c.amadeusium) != '0' and not c.has_trap():
                if shortest_dist == -1 or shortest_dist > c.distance(Pos(self.x, self.y)):
                    shortest_dist = c.distance(Pos(self.x, self.y))
                    target = Pos(c.x, c.y)
        if target is not None:
            self.dig(target.x, target.y)
        else:
            self.wait()

class Cell(Pos):
    def __init__(self, x, y, amadeusium, hole):
        super().__init__(x, y)
        self.amadeusium = amadeusium
        self.hole = hole
        self.entity = 0

    def has_hole(self):
        return self.hole == HOLE

    def update(self, amadeusium, hole):
        self.amadeusium = amadeusium
        self.hole = hole

    def set_entity(self, entity):
        self.entity = entity

    def has_radar(self):
        return self.entity == RADAR

    def has_trap(self):
        return self.entity == TRAP

class Grid:
    def __init__(self):
        self.cells = []
        for y in range(height):
            for x in range(width):
                self.cells.append(Cell(x, y, 0, 0))

    def get_cell(self, x, y):
        if width > x >= 0 and height > y >= 0:
            return self.cells[x + width * y]
        return None


class Game:
    def __init__(self):
        self.grid = Grid()
        self.my_score = 0
        self.enemy_score = 0
        self.radar_cooldown = 0
        self.trap_cooldown = 0
        self.radars = []
        self.traps = []
        self.my_robots = []
        self.enemy_robots = []
        self.ideal_radar_pos = []

    def reset(self):
        self.radars = []
        self.traps = []
        self.my_robots = []
        self.enemy_robots = []
        self.ideal_radar_pos = []
        self.ideal_radar_pos.append(Pos(5, 3))
        self.ideal_radar_pos.append(Pos(5, 11))
        self.ideal_radar_pos.append(Pos(10, 7))
        self.ideal_radar_pos.append(Pos(15, 3))
        self.ideal_radar_pos.append(Pos(15, 11))
        self.ideal_radar_pos.append(Pos(20, 7))
        self.ideal_radar_pos.append(Pos(25, 3))
        self.ideal_radar_pos.append(Pos(25, 11))
        self.ideal_radar_pos.append(Pos(20, 0))
        self.ideal_radar_pos.append(Pos(29, 7))
        self.ideal_radar_pos.append(Pos(20, 14))
        self.ideal_radar_pos.append(Pos(10, 0))
        self.ideal_radar_pos.append(Pos(10, 14))

def count_alive_robots(robots):
    return len([x for x in robots if x.is_alive()])

game = Game()

# game loop
while True:
    # my_score: Players score
    game.my_score, game.enemy_score = [int(i) for i in input().split()]
    for i in range(height):
        inputs = input().split()
        for j in range(width):
            # amadeusium: amount of amadeusium or "?" if unknown
            # hole: 1 if cell has a hole
            amadeusium = inputs[2 * j]
            hole = int(inputs[2 * j + 1])
            game.grid.get_cell(j, i).update(amadeusium, hole)
    # entity_count: number of entities visible to you
    # radar_cooldown: turns left until a new radar can be requested
    # trap_cooldown: turns left until a new trap can be requested
    entity_count, game.radar_cooldown, game.trap_cooldown = [int(i) for i in input().split()]

    game.reset()

    for i in range(entity_count):
        # id: unique id of the entity
        # type: 0 for your robot, 1 for other robot, 2 for radar, 3 for trap
        # y: position of the entity
        # item: if this entity is a robot, the item it is carrying (-1 for NONE, 2 for RADAR, 3 for TRAP, 4 for AMADEUSIUM)
        id, type, x, y, item = [int(j) for j in input().split()]

        if type == ROBOT_ALLY:
            game.my_robots.append(Robot(x, y, type, id, item))
        elif type == ROBOT_ENEMY:
            game.enemy_robots.append(Robot(x, y, type, id, item))
        elif type == TRAP:
            game.traps.append(Entity(x, y, type, id))
            game.grid.get_cell(x, y).set_entity(TRAP)
        elif type == RADAR:
            game.radars.append(Entity(x, y, type, id))
            game.grid.get_cell(x, y).set_entity(RADAR)

    c_radars = len(game.radars)
    for i in range(len(game.my_robots)):
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)
        if game.my_robots[i].item == AMADEUSIUM: # go to base
            game.my_robots[i].move(0, game.my_robots[i].y)
        elif game.my_robots[i].item == RADAR: # place radar to next optimal spot which is not already occupied by radar
            game.my_robots[i].place_radar_at_next_spot(game.grid, game.ideal_radar_pos)
        elif game.my_robots[i].item == TRAP:
            # place trap at nearest cell with exactly 2 amadeusium
            target = game.my_robots[i].find_nearest_n_amadeusium(game.grid, 2)
            if target is not None: # go to nearest amadeusium
                game.grid.get_cell(target.x, target.y).set_entity(TRAP)
                game.my_robots[i].dig(target.x, target.y)
            else:
                game.my_robots[i].go_to_nearest_cell_without_hole(game.grid)
        elif c_radars < 10 and game.radar_cooldown == 0:
            game.my_robots[i].get_nearest_amadeusium_before_request(game.grid, RADAR, count_alive_robots(game.my_robots) > count_alive_robots(game.enemy_robots) + 1)
            game.radar_cooldown = 1
        elif game.trap_cooldown == 0 and game.my_score % 3:
            game.my_robots[i].get_nearest_amadeusium_before_request(game.grid, TRAP, count_alive_robots(game.my_robots) > count_alive_robots(game.enemy_robots) + 1)
            game.trap_cooldown = 1
        else:
            target = game.my_robots[i].find_nearest_amadeusium(game.grid, count_alive_robots(game.my_robots) > count_alive_robots(game.enemy_robots) + 1)
            if target is not None: # go to nearest amadeusium
                game.grid.get_cell(target.x, target.y).amadeusium = int(game.grid.get_cell(target.x, target.y).amadeusium) - 1
                game.my_robots[i].dig(target.x, target.y)
            else:
                game.my_robots[i].go_to_nearest_cell_without_hole(game.grid)