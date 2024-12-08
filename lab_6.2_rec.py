from random import randint

def generate_array(size, arrey=[]):
    if len(arrey) == size:
        return arrey
    arrey.append(randint(0, 50))
    return generate_array(size, arrey)

def bubble_sort_recursive(mas, n=None):
    if n is None:
        n = len(mas)
    if n == 1:
        return mas
    for i in range(n - 1):
        if mas[i] < mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return bubble_sort_recursive(mas, n - 1)

mas = generate_array(10)
print("Згенерований масив:", mas)
sorted_mas = bubble_sort_recursive(mas)
print("Відсортований масив:", sorted_mas)
