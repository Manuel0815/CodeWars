def presses(phrase):
    one_press = "ADGJMPTW 1#*"
    two_press = "BEHKNQUX0"
    three_press = "CFILORVY"
    four_press = "SZ234568"
    five_press = "79"

    c = 0
    for p in phrase.upper():
        if p in one_press:
            c += 1
        elif p in two_press:
            c+=2
        elif p in three_press:
            c+=3
        elif p in four_press:
            c+=4
        else:
            c+=5
    
    return c

x = presses("LOL")
print(x)