import math

N = int(input("Введіть значення N: "))

# 1. Цикл while
S_while = 0
i = 1
while i <= N:
    S_while += math.sqrt(1 + (math.cos(i)**2) * math.sin(i)) / (1 + (math.sin(i)**2) * math.cos(i))
    i += 1
print("Результат (while):", S_while)

# 2. Цикл do-while (емуляція)
S_dowhile = 0
i = 1
while True:
    S_dowhile += math.sqrt(1 + (math.cos(i)**2) * math.sin(i)) / (1 + (math.sin(i)**2) * math.cos(i))
    i += 1
    if i > N:
        break
print("Результат (do-while):", S_dowhile)

# 3. Цикл for (інкремент)
S_for_inc = 0
for i in range(1, N + 1):
    S_for_inc += math.sqrt(1 + (math.cos(i)**2) * math.sin(i)) / (1 + (math.sin(i)**2) * math.cos(i))
print("Результат (for, інкремент):", S_for_inc)

# 4. Цикл for (декремент)
S_for_dec = 0
for i in range(N, 0, -1):
    S_for_dec += math.sqrt(1 + (math.cos(i)**2) * math.sin(i)) / (1 + (math.sin(i)**2) * math.cos(i))
print("Результат (for, декремент):", S_for_dec)
