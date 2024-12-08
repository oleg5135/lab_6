from random import randint

def generate_array(size):
    return [randint(-10, 10) for _ in range(size)]

def calculate_sum_of_odd(array):
    return sum(item for item in array if item % 2 != 0)

def find_first_negative(array):
    for index, value in enumerate(array):
        if value < 0:
            return index
    return None

def find_last_negative(array):
    for index in range(len(array) - 1, -1, -1):
        if array[index] < 0:
            return index
    return None

def calculate_sum_between_negatives(array, first_index, last_index):
    if first_index is not None and last_index is not None and first_index != last_index:
        return sum(array[first_index + 1:last_index])
    return None

def replace_small_values(array):
    return [0 if abs(value) <= 1 else value for value in array]

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
