from random import randint

def generate_filtered_array(size):
    array = []
    while len(array) < size:
        item = randint(-20, 37)
        if item < 0 or item % 5 == 0:
            array.append(item)
    return array

mas = generate_filtered_array(22)
print(mas)
