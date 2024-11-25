import random
import time

def fillArray(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(4, 68)  # Генеруємо числа в діапазоні [4, 68]

def printArray(arr):
    for value in arr:
        print(value, end=" ")
    print()

def processArray(arr):
    count = 0
    total_sum = 0
    for i in range(len(arr)):
        if not (arr[i] % 2 == 0 or arr[i] % 13 == 0):  # Якщо елемент не кратний 2 або 13
            count += 1
            total_sum += arr[i]
            arr[i] = 0  # Замінюємо елемент на 0
    return count, total_sum

# Основна програма
random.seed(time.time())  # Ініціалізація генератора випадкових чисел

myArray = [0] * 23  # Масив із 23 елементів, ініціалізованих 0
fillArray(myArray)

print("Original Array: ")
printArray(myArray)

count, total_sum = processArray(myArray)

print(f"Count of elements satisfying the criteria: {count}")
print(f"Sum of elements satisfying the criteria: {total_sum}")
print("Modified Array: ")
printArray(myArray)
