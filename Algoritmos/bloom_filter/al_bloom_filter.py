import math
import mmh3  # Asegúrate de tener instalada la biblioteca mmh3 (pip install mmh3)

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.bit_array = [False] * size
        self.hash_functions = hash_functions

    def add(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            self.bit_array[index] = True

    def __contains__(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            if not self.bit_array[index]:
                return False
        return True

# Ejemplo de uso
if __name__ == "__main__":
    # Tamaño del filtro de Bloom y número de funciones hash
    size = 10
    num_hash_functions = 3

    # Creamos el filtro de Bloom
    bloom_filter = BloomFilter(size, [hash, mmh3.hash, lambda x: hash(x) + mmh3.hash(x)])

    # Agregamos elementos al filtro
    elementos = ["apple", "banana", "cherry", "date"]
    for elemento in elementos:
        bloom_filter.add(elemento)

    # Verificamos la pertenencia de un elemento
    elemento_a_verificar = "banana"
    if elemento_a_verificar in bloom_filter:
        print(f"'{elemento_a_verificar}' probablemente está en el conjunto.")
    else:
        print(f"'{elemento_a_verificar}' definitivamente no está en el conjunto.")
