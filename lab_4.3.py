# Введення значень
xp = float(input("xp = "))
xk = float(input("xk = "))
dx = float(input("dx = "))
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Виведення заголовка таблиці
print("--------------------------------")
print("|{:>5} |{:>7} |".format("x", "F"))
print("--------------------------------")

x = xp
while x <= xk:
    if x + c < 0 and a != 0:
        F = -a * (x ** 2) - b
    elif x + c > 0 and a == 0:
        F = (x - a) / (x - c)
    else:
        F = x / c + c / x

    # Виведення значень у таблицю
    print("|{:>5.2f} |{:>7.3f} |".format(x, F))

    x += dx

print("--------------------------------")
