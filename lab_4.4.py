xp = float(input("xp = "))
xk = float(input("xk = "))
dx = float(input("dx = "))

print("-----------------------------------")
print("|{:^7}|{:^10}|".format("x", "y"))
print("-----------------------------------")

x = xp
while x <= xk:
    if x <= -4:
        y = -2
    elif -4 < x <= 0:
        y = x / 4
    elif 0 < x <= 2:
        y = x ** 2
    else:
        y = -(x / 2) + 5

    print("|{:7.2f}|{:10.3f}|".format(x, y))
    x += dx

print("-----------------------------------")
