#Implementation max
def max(a, b, c):@\onslide<2->@
    if a > b:
        if a > c:
            return a
        else:
            return c@\onslide<3->@
    else:
        if c > b:
            return c
        else:
            return b
