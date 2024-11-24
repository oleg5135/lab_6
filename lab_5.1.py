import math

def h(a: float, b: float) -> float:
    return math.pow(a, 2) - math.pow(b, 2)

g = float(input("g = "))
s = float(input("s = "))
c = (h(g + 1.0, s) + math.pow(h(g, s + 1.0), 2)) / (1.0 + math.pow(h(math.pow(g, 2), math.pow(s, 2)), 3))
print(f"c = {c}")
