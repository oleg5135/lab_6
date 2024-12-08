from random import randint

mas = [10, 11, 32, 2, 212]  # Початковий масив
print("Початковий масив", mas)
# Бульбашкове сортування за спаданням
n = len(mas)
for i in range(n):
    for j in range(n - 1):
        if mas[j] < mas[j + 1]:  # Змінюємо знак порівняння для сортування за спаданням
            mas[j], mas[j + 1] = mas[j + 1], mas[j]  # Міняємо елементи місцями

print("Відсортованйи масив", mas)  # [32, 11, 10, 2]

# Функція для генерації масиву
def generate_array(size, arrey=[]):
    if len(arrey) == size:  # База рекурсії: якщо масив заповнений
        return arrey
    
    item = randint(0, 50)  # Генеруємо випадкове число
    arrey.append(item)  # Додаємо його до масиву

    return generate_array(size, arrey)  # Рекурсивно додаємо наступний елемент

# Функція для рекурсивного бульбашкового сортування
def bubble_sort_recursive(mas, n=None):
    if n is None:
        n = len(mas)  # Встановлюємо початкову довжину масиву

    if n == 1:  # База рекурсії: якщо залишився 1 елемент, масив відсортований
        return mas

    for i in range(n - 1):  # Проходимо масив до n-1 елемента
        if mas[i] < mas[i + 1]:  # Сортуємо за спаданням
            mas[i], mas[i + 1] = mas[i + 1], mas[i]  # Міняємо місцями

    return bubble_sort_recursive(mas, n - 1)  # Рекурсивно сортуємо решту масиву

# Генеруємо масив
mas = generate_array(10)  # Наприклад, масив із 10 елементів
print("Згенерований масив:", mas)

# Сортуємо масив
sorted_mas = bubble_sort_recursive(mas)
print("Відсортований масив:", sorted_mas)