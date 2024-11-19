import math

# Введення даних
xp = float(input("xp = "))
xk = float(input("xk = "))
dx = float(input("dx = "))
eps = float(input("eps = "))

print("-" * 43)
print(f"| {'x':^5} | {'cos(x)':^9} | {'S':^9} | {'n':^3} |")
print("-" * 43)

x = xp
while x <= xk:
    n = 0
    a = 1
    S = a

    while abs(a) > eps:
        n += 1
        R = ((-1.0) * x * x) / (2.0 * n * (2.0 * n - 1.0))
        a *= R
        S += a

    print(f"| {x:7.2f} | {math.cos(x):9.5f} | {S:9.5f} | {n:^3} |")
    x += dx

print("-" * 43)
