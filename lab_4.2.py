import math

# Введення початкових даних
xp = float(input("Введіть X_поч (початкове значення x): "))
xk = float(input("Введіть X_кін (кінцеве значення x): "))
dx = float(input("Введіть dX (крок): "))

# Виведення заголовка таблиці
print("x\t\t\t\t\t y")
print("-" * 30)

# Цикл для обчислення значень y на заданому інтервалі
x = xp
while x <= xk:
    if x <= -1:
        y = x + math.log10(abs(math.cos(5 * x))) + math.exp(-1 / x)
    elif -1 < x < 0.4:
        y = x + math.sqrt((2 - x)**3) - math.tan(x)
    else:  # x >= 0.4
        y = x + math.sin(5 * x) - math.sqrt(abs(1 - x))
    
    # Виведення результатів з табуляцією
    print(f"{x:.4f}\t\t\t {y:.4f}")
    x += dx

print("-" * 30)
