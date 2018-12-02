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