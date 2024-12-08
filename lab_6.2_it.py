def bubble_sort_descending(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

mas = [10, 11, 32, 2, 212]
print("Початковий масив:", mas)
sorted_mas = bubble_sort_descending(mas)
print("Відсортований масив:", sorted_mas)
