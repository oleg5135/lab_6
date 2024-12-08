from random import *

def appent_mas(size, areey=[]):
    if len(areey) == size:
        return areey
    
    item = randint(0, 20)
    areey.append(item)

    return appent_mas(size, areey)

mass = appent_mas(10)
print(mass)

def max_even_element(array, n=None, max_even=None):
    if n is None:
        n = len(array) - 1

    if n < 0:
        return max_even

    if array[n] % 2 == 0 and isinstance(array[n], int) and (max_even is None or array[n] > max_even):
        max_even = array[n]

    return max_even_element(array, n - 1, max_even)

result = max_even_element(mass)
print(f"Найбільший парний елемент: {result}")