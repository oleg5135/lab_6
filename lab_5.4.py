import math

def S0(K, N):
    s = 0
    for i in range(K, N + 1):
        s += (math.sin(i) * math.cos(i)) / (1.0 + math.pow(math.sin(i), 2))
    return s

def S1(K, N, i):
    if i > N:
        return 0
    else:
        return (math.sin(i) * math.cos(i)) / (1.0 + math.pow(math.sin(i), 2)) + S1(K, N, i + 1)

def S2(K, N, i):
    if i < K:
        return 0
    else:
        return (math.sin(i) * math.cos(i)) / (1.0 + math.pow(math.sin(i), 2)) + S2(K, N, i - 1)

def S3(K, N, i, t):
    t = t + (math.sin(i) * math.cos(i)) / (1.0 + math.pow(math.sin(i), 2))
    if i >= N:
        return t
    else:
        return S3(K, N, i + 1, t)

def S4(K, N, i, t):
    t = t + (math.sin(i) * math.cos(i)) / (1.0 + math.pow(math.sin(i), 2))
    if i <= K:
        return t
    else:
        return S4(K, N, i - 1, t)

# Основна програма
K = int(input("K = "))
N = int(input("N = "))

print(f"(iter) S0 = {S0(K, N):.5f}")
print(f"(rec up ++) S1 = {S1(K, N, K):.5f}")
print(f"(rec up --) S2 = {S2(K, N, N):.5f}")
print(f"(rec down ++) S3 = {S3(K, N, K, 0):.5f}")
print(f"(rec down --) S4 = {S4(K, N, N, 0):.5f}")
