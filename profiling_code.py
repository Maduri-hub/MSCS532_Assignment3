import time
import random
from deterministic_quicksort import deterministic_quicksort
from randomized_quicksort import randomized_quicksort

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(1, size + 1))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def generate_repeated_elements_array(size):
    return [random.randint(1, 10) for _ in range(size)]

def compare_algorithms():
    input_sizes = [100, 900]

    for size in input_sizes:
        print(f"\nArray size: {size}")

        random_array = generate_random_array(size)
        arr1 = random_array[:]
        arr2 = random_array[:]

        print("Randomly generated array")

        start = time.time()
        randomized_quicksort(arr1, 0, len(arr1) - 1)
        end = time.time()
        print(f"Randomized Quicksort (Random array): {end - start} seconds")

        start = time.time()
        deterministic_quicksort(arr2, 0, len(arr2) - 1)
        end = time.time()
        print(f"Deterministic Quicksort (Random array): {end - start} seconds")

        print()
        print("Already sorted array")

        # Already sorted array
        sorted_array = generate_sorted_array(size)
        arr1 = sorted_array[:]
        arr2 = sorted_array[:]

        start = time.time()
        randomized_quicksort(arr1, 0, len(arr1) - 1)
        end = time.time()
        print(f"Randomized Quicksort (Sorted array): {end - start} seconds")

        start = time.time()
        deterministic_quicksort(arr2, 0, len(arr2) - 1)
        end = time.time()
        print(f"Deterministic Quicksort (Sorted array): {end - start} seconds")

        print()
        print("Reverse-sorted array")

        reverse_sorted_array = generate_reverse_sorted_array(size)
        arr1 = reverse_sorted_array[:]
        arr2 = reverse_sorted_array[:]

        start = time.time()
        randomized_quicksort(arr1, 0, len(arr1) - 1)
        end = time.time()
        print(f"Randomized Quicksort (Reverse-sorted array): {end - start} seconds")

        start = time.time()
        deterministic_quicksort(arr2, 0, len(arr2) - 1)
        end = time.time()
        print(f"Deterministic Quicksort (Reverse-sorted array): {end - start} seconds")

        print()
        print("Array with repeated elements")

        repeated_elements_array = generate_repeated_elements_array(size)
        arr1 = repeated_elements_array[:]
        arr2 = repeated_elements_array[:]

        start = time.time()
        randomized_quicksort(arr1, 0, len(arr1) - 1)
        end = time.time()
        print(f"Randomized Quicksort (Repeated elements): {end - start} seconds")

        start = time.time()
        deterministic_quicksort(arr2, 0, len(arr2) - 1)
        end = time.time()
        print(f"Deterministic Quicksort (Repeated elements): {end - start} seconds")

        print("-----------------------------------------")

compare_algorithms()
