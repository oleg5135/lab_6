def countWays(m, x, y, z, depth, level):
    # Виведення рівня рекурсії та глибини
    print(f"Depth: {depth}, Level: {level}")

    # Якщо сума m дорівнює 0, це означає, що ми знайшли спосіб сплати
    if m == 0:
        return 1

    # Якщо сума m стала від'ємною, цей шлях не підходить
    if m < 0:
        return 0

    # Рекурсивний підрахунок способів для номіналів x, y, z
    return (
        countWays(m - x, x, y, z, depth + 1, level) +
        countWays(m - y, x, y, z, depth + 1, level + 1) +
        countWays(m - z, x, y, z, depth + 1, level + 2)
    )


# Основна програма
x = int(input("Введіть номінал x: "))
y = int(input("Введіть номінал y: "))
z = int(input("Введіть номінал z: "))
m = int(input("Введіть суму m: "))

# Виклик функції з початковими depth і level
ways = countWays(m, x, y, z, 1, 0)

# Виведення результату
print(f"Кількість способів сплатити {m} копійок: {ways}")
