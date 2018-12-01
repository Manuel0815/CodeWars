def disemvowel(string):
    s = ""
    chars = ["A", "E", "I", "O", "U"]
    for c in string:
        if c.capitalize() not in chars:
            s += c
    return s

print disemvowel ("This website is for losers LOL!")