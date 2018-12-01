def tower_builder(n_floors):
    l = []
    for n in range(1, n_floors+1):
        l.append(" "*(n_floors - n) + "*"*(n*2-1) + " "*(n_floors - n))
    return l

print tower_builder(3)