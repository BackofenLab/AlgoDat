#Alternative implementation max
@\onslide<2->@
def max(a, b):
    if a > b:
        return a
    else:
        return b@\onslide<3->@

def maxTripel(a, b, c):
    return max(max(a,b),c)
