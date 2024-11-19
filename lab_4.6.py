import math

# While
S = 0
i = 1
while i <= 10:
    k = 1
    P = 1
    while k <= i:
        P *= k / i
        k += 1
    S += (1 + P) / math.pow(i, 2)
    i += 1
print(f"While: {S:.5f}")

# For (++ variant)
S = 0
for i in range(1, 11):
    P = 1
    for k in range(1, i + 1):
        P *= k / i
    S += (1 + P) / math.pow(i, 2)
print(f"For(++): {S:.5f}")

# Do-while simulation in Python
S = 0
i = 1
while True:
    k = 1
    P = 1
    while k <= i:
        P *= k / i
        k += 1
    S += (1 + P) / math.pow(i, 2)
    i += 1
    if i > 10:
        break
print(f"Do-while: {S:.5f}")

# For (-- variant)
S = 0
for i in range(10, 0, -1):
    P = 1
    for k in range(i, 0, -1):
        P *= k / i
    S += (1 + P) / math.pow(i, 2)
print(f"For(--): {S:.5f}")
