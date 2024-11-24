import math

def f(x):
    if abs(x) >= 1:
        return math.cos(x / 2) / (1 + math.pow(math.sin(x), 2))
    else:
        S = 0
        i = 0
        a = 1
        S = a
        while i < 6:
            i += 1
            R = (2 * i * (2 * i - 1)) / ((3 * i - 2) * (3 * i - 1) * (3 * i))
            a *= R
            S += a
        return S

# Основна програма
yp = float(input("yp = "))
yk = float(input("yk = "))
n = int(input("n = "))

dp = (yk - yp) / n
y = yp

while y <= yk:
    z = f(1 + math.pow(y, 2)) + math.pow(f(f(1) + math.pow(f(math.pow(y, 2)), 2)), 2)
    print(f"{y:.2f} {z:.5f}")
    y += dp
