import math

# Введення значення N
N = int(input("N = "))
res = 1.0

# Цикл While
i = N
while i <= 10:
    res *= (i + 1 / (math.pow(i, 2))) / math.sqrt(1 + math.exp(1 / i))
    i += 1
print(f"While: {res}")

# Цикл Do-While (імітація в Python)
i = N
res = 1.0
while True:
    res *= (i + 1 / (math.pow(i, 2))) / math.sqrt(1 + math.exp(1 / i))
    i += 1
    if i > 10:
        break
print(f"Do-While: {res}")

# Цикл For (з i++)
res = 1.0
for i in range(N, 11):
    res *= (i + 1 / (math.pow(i, 2))) / math.sqrt(1 + math.exp(1 / i))
print(f"For(++): {res}")

# Цикл For (з i--)
res = 1.0
for i in range(10, N - 1, -1):
    res *= (i + 1 / (math.pow(i, 2))) / math.sqrt(1 + math.exp(1 / i))
print(f"For(--): {res}")
