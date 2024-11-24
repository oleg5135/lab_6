import math

def S(x, eps):
    n = 0
    a = 1.0
    s = a
    while True:
        n += 1
        a = A(x, n, a)
        s += a
        if abs(a) <= eps:
            break
    return s, n  # Повертаємо значення S і кількість ітерацій n

def A(x, n, a):
    R = ((-1.0) * x * x) / (2.0 * n * (2.0 * n - 1.0))
    a *= R
    return a

# Основна програма
xp = float(input("xp = "))
xk = float(input("xk = "))
dx = float(input("dx = "))
eps = float(input("eps = "))

print("-------------------------------------------")
print(f"| {'x':>7} | {'cos(x)':>10} | {'S':>7} | {'n':>5} |")
print("-------------------------------------------")

x = xp
while x <= xk:
    s, n = S(x, eps)  # Обчислюємо значення S та кількість ітерацій n
    print(f"| {x:7.2f} | {math.cos(x):10.5f} | {s:7.5f} | {n:5} |")
    x += dx

print("-------------------------------------------")
