x = float(input("x = "))

if x <= -4:
    y = -2
else:
    if -4 < x <= 0:
        y = x / 4
    else:
        if 0 < x <= 2:
            y = x ** 2
        else:
            y = -(x / 2) + 5

print(f"y = {y}")
