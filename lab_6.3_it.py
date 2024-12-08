def find_max_even_integer(mas):
    max_el = None
    for i in range(len(mas)):
        if (mas[i] % 2 == 0 and isinstance(mas[i], int) and 
                (max_el is None or mas[i] > max_el)):
            max_el = mas[i]
    return max_el

mas = [3, 7, 10, 22, 35, 18, 42, 11, 52, 54, 60.0]
print("Масив:", mas)
max_even_integer = find_max_even_integer(mas)
print("Максимальний парний цілий елемент:", max_even_integer)
