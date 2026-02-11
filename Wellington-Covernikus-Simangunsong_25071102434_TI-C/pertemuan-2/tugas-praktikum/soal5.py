import math

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Jarak =", jarak(1, 2, 7, 10))