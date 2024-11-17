import math

# Введення значень R1, R2 і x
R1 = float(input("Введіть значення R1: "))
R2 = float(input("Введіть значення R2: "))
x = float(input("Введіть значення x: "))

# Розгалуження для обчислення y
if x <= -R1:
    y = x + 3 * R1
elif -R1 < x <= 0:
    y = math.sqrt(R1**2 - x**2)
elif 0 < x <= R2:
    y = math.sqrt(R2**2 - (x - R2)**2)
elif R2 < x <= 6:
    y = -R2
else:  # x > 6
    y = -R2

# Виведення результату
print(f"При x = {x}, R1 = {R1}, R2 = {R2}, значення y = {y}")
