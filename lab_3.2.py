# Введення значень a, b, c, x
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
c = float(input("Введіть значення c: "))
x = float(input("Введіть значення x: "))

# Спосіб 1: Розгалуження в скороченій формі
if c < 0 and x != 0:
    F1 = -a * x - c
elif c > 0 and x == 0:
    F1 = (x - a) / -c
else:
    F1 = (b * x) / (c - a)

print("\n1) Значення F (скорочена форма):", F1)

# Спосіб 2: Розгалуження в повній формі
if c < 0 and x != 0:
    F2 = -a * x - c
else:
    if c > 0 and x == 0:
        F2 = (x - a) / -c
    else:
        F2 = (b * x) / (c - a)

print("2) Значення F (повна форма):", F2)
