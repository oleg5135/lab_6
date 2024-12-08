from random import randint

def generate_array(size, array=None):
    if array is None:
        array = []
    if len(array) == size:
        return array
    array.append(randint(-10, 10))
    return generate_array(size, array)

def calculate_sum_of_odd(array, index=0, total=0):
    if index == len(array):
        return total
    if array[index] % 2 != 0:
        total += array[index]
    return calculate_sum_of_odd(array, index + 1, total)

def find_first_negative(array, index=0):
    if index == len(array):
        return None
    if array[index] < 0:
        return index
    return find_first_negative(array, index + 1)

def find_last_negative(array, index=None):
    if index is None:
        index = len(array) - 1
    if index < 0:
        return None
    if array[index] < 0:
        return index
    return find_last_negative(array, index - 1)

def calculate_sum_between_negatives(array, first_index, last_index, current_index=None, total=0):
    if first_index is None or last_index is None or first_index == last_index:
        return None
    if current_index is None:
        current_index = first_index + 1
    if current_index >= last_index:
        return total
    total += array[current_index]
    return calculate_sum_between_negatives(array, first_index, last_index, current_index + 1, total)

def replace_small_values(array, index=0):
    if index == len(array):
        return array
    if abs(array[index]) <= 1:
        array[index] = 0
    return replace_small_values(array, index + 1)

def main():
    n = int(input("Введіть довжину масиву: "))
    array = generate_array(n)

    first_negative = find_first_negative(array)
    last_negative = find_last_negative(array)
    sum_between_negatives = calculate_sum_between_negatives(array, first_negative, last_negative)

    print("Масив:", array)
    print("Сума непарних елементів:", calculate_sum_of_odd(array))
    print("Індекс першого від'ємного елемента:", first_negative if first_negative is not None else "Відсутній")
    print("Індекс останнього від'ємного елемента:", last_negative if last_negative is not None else "Відсутній")
    print("Сума елементів між першим і останнім від'ємними:", sum_between_negatives if sum_between_negatives is not None else "Недостатньо від'ємних елементів")
    print("Масив із заміненими елементами:", replace_small_values(array))

main()
