import math

# Введення значень xp, xk, dx
xp = float(input("xp = "))
xk = float(input("xk = "))
dx = float(input("dx = "))

# Виведення заголовку таблиці
print(f"{'-' * 25}")
print(f"| {'x':^7} | {'y':^10} |")
print(f"{'-' * 25}")

x = xp
while x <= xk:
    A = abs(4 * x - 1)
    if x < 0:
        B = math.pow(x, 7) - 2 * x
    elif x >= 3:
        B = math.pow(x, 4) + math.exp(math.pow(x, 2) + 3)
    else:
        B = math.atan((math.exp(x) + 1) / 8)
    
    y = A + B
    print(f"| {x:7.2f} | {y:10.3f} |")
    x += dx

print(f"{'-' * 25}")
