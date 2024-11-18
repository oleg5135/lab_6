import math

x = float(input("Введіть значення x: "))

# Спосіб 1: Розгалуження в скороченій формі
if x <= -1:
    y1 = x + math.log10(abs(math.cos(5 * x))) + math.exp((1 / x) + x)
elif -1 < x < 0.4:
    y1 = x + math.sqrt((2 - x)**3) - math.tan(x)
else:  # x >= 0.4
    y1 = x + math.sin(5 * x) - math.sqrt(abs(1 - x))

# Спосіб 2: Розгалуження в повній формі
if x <= -1:
    y2 = x + math.log10(abs(math.cos(5 * x))) + math.exp((1 / x) + x)
else:
    if -1 < x < 0.4:
        y2 = x + math.sqrt((2 - x)**3) - math.tan(x)
    else:  # x >= 0.4
        y2 = x + math.sin(5 * x) - math.sqrt(abs(1 - x))

print("y1 = ", y1)
print("y2 = ", y2)
