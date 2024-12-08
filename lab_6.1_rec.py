from random import randint

def generate_array(size, array=[]):
    if len(array) == size:
        return array

    item = randint(-20, 37)

    if item < 0 or item % 5 == 0:
        array.append(item)

    return generate_array(size, array)

result = generate_array(22)
print(result)