import math

# Введення значень
R = float(input("Введіть радіус R: "))
x = float(input("Введіть координату x: "))
y = float(input("Введіть координату y: "))

# Перевірка для півкола
in_semi_circle = (x**2 + y**2 <= R**2) and (x >= 0) and (y >= 0)

# Перевірка для трикутника
in_triangle = (y >= -R) and (y <= (-R / R) * x) and (x >= 0)

# Перевірка, чи точка належить будь-якій із областей
if in_semi_circle or in_triangle:
    print("Точка належить зафарбованій області (yes)")
else:
    print("Точка не належить зафарбованій області (no)")
