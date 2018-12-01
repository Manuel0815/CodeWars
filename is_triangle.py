def is_triangle(a, b, c):
    l = [a, b, c]
    l.sort()
    if l[0] + l[1] <= l[2]:
        return False
    return True

print is_triangle(1, 1, 3)