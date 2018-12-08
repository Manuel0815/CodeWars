def add_binary(a,b):
    return bin(a+b)[2:]
    #return int(bin(a+b)[2:])

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "/":
        return value1 / value2
    else:
        return value1 * value2

def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        y+=1
        principal = principal + principal * interest * (1-tax)
    return y

def disemvowel(string):
    s = ""
    chars = ["A", "E", "I", "O", "U"]
    for c in string:
        if c.capitalize() not in chars:
            s += c
    return s

def is_triangle(a, b, c):
    l = [a, b, c]
    l.sort()
    if l[0] + l[1] <= l[2]:
        return False
    return True

def tower_builder(n_floors):
    l = []
    for n in range(1, n_floors+1):
        l.append(" "*(n_floors - n) + "*"*(n*2-1) + " "*(n_floors - n))
    return l

print tower_builder(3)

def find_short(s):
    l = -1
    for word in s.split(" "):
        if l == -1:
            l = len(word)
        elif l > len(word):
            l = len(word)
    return l # l: shortest word length

find_short("bitcoin take over the world maybe who knows perhaps")

def stray(arr):
    #same = arr[0] if arr.count(arr[0]) > 1 else arr[1]
    for n in arr:
        if arr.count(n) == 1:#n != same:
            return n

print stray([1, 1, 1, 1, 1, 1, 2])

def title_case(title, minor_words=""):
    titleCase = ""
    for word in title.lower().split(" "):
        if titleCase == "":
            titleCase += word.capitalize()
        else:
            if minor_words.lower().split(" ").count(word) == 0:
                titleCase += " " + word.capitalize()
            else:
                titleCase += " " + word
    return titleCase

print title_case('a clash of KINGS', 'a an the of')
print title_case('a clash of KINGS')

def dirReduc(arr):
    removed = True
    while removed == True:
        removed = False
        for x in range(0, len(arr)):
            if x+1 == len(arr): break
            if (arr[x] == "NORTH" and arr[x+1] == "SOUTH") or (arr[x+1] == "NORTH" and arr[x] == "SOUTH") or (arr[x] == "WEST" and arr[x+1] == "EAST") or (arr[x+1] == "WEST" and arr[x] == "EAST"):
                arr.pop(x)
                arr.pop(x)
                removed = True
                break
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
#a = ['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']
#should equal ['EAST', 'NORTH'
print dirReduc(a)

def find_uniq(arr):
    same = None
    if (arr[0] == arr[1]) or (arr[0] == arr[2]):
        same = arr[0]
    elif arr[1] == arr[2]:
        return arr[0]

    for n in arr:
        if n != same:
            return n   # n: unique integer in the array

print find_uniq([ 1, 1, 1, 2, 1, 1 ])
