import random

def generate_random_array(size):
    # Generar un array de 'size' elementos con números aleatorios
    return [random.randint(1, 1000) for _ in range(size)]

def deterministic_quick_sort(array, lowlest, highlest):
    if lowlest < highlest:
        pivot_index = partition_right(array, lowlest, highlest)
        deterministic_quick_sort(array, lowlest, pivot_index - 1)
        deterministic_quick_sort(array, pivot_index + 1, highlest)

def partition_right(array, lowlest, highlest):
    pivot = array[highlest]
    pointer = lowlest - 1

    for j in range(lowlest, highlest):
        if array[j] <= pivot:
            pointer = pointer + 1
            (array[pointer], array[j]) = (array[j], array[pointer])

    (array[pointer + 1], array[highlest]) = (array[highlest], array[pointer + 1])

    return pointer + 1

random_array_size = random.randint(10, 50)
random_array = generate_random_array(random_array_size)

print("Array sin ordenar:")
print(random_array)

deterministic_quick_sort(random_array, 0, len(random_array) - 1)  # Llamada a la función con los índices apropiados

print("Array ordenado:")
print(random_array)

