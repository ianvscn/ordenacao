import random
import time
import psutil

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def counting_sort(arr):
    output = [0] * len(arr)
    count = [0] * (max(arr) + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def generate_test_data(size, order):
    if order == "random":
        return random.sample(range(size * 10), size)
    elif order == "ascending":
        return list(range(size * 10))
    elif order == "descending":
        return list(range(size * 10, 0, -1))
    elif order == "constant":
        return [5] * size
    elif order == "partially_ascending":
        ascending_part = list(range(int(size * 0.9) * 10))
        random_part = random.sample(range(int(size * 0.1) * 10, size * 10), int(size * 0.1))
        return ascending_part + random_part

def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # Em megabytes

def run_sorting_algorithm(algorithm, data):
    start_memory = get_memory_usage()
    start_time = time.time()

    algorithm(data)

    end_time = time.time()
    end_memory = get_memory_usage()

    execution_time = end_time - start_time
    memory_usage = end_memory - start_memory

    return execution_time, memory_usage

if __name__ == "__main__":
    orders = ["random", "ascending", "descending", "constant", "partially_ascending"]
    sizes = [100000, 500000, 1500000, 2000000, 3000000]

    for order in orders:
        print(f"Order: {order}")
        for size in sizes:
            data = generate_test_data(size, order)

            # Bubble Sort
            bubble_time, bubble_memory = run_sorting_algorithm(bubble_sort, data.copy())
            print(f"Bubble Sort - Size: {size}, Time: {bubble_time:.6f} seconds, Memory: {bubble_memory:.2f} MB")

            # Selection Sort
            selection_time, selection_memory = run_sorting_algorithm(selection_sort, data.copy())
            print(f"Selection Sort - Size: {size}, Time: {selection_time:.6f} seconds, Memory: {selection_memory:.2f} MB")

            # Insertion Sort
            insertion_time, insertion_memory = run_sorting_algorithm(insertion_sort, data.copy())
            print(f"Insertion Sort - Size: {size}, Time: {insertion_time:.6f} seconds, Memory: {insertion_memory:.2f} MB")

            # Merge Sort
            merge_time, merge_memory = run_sorting_algorithm(merge_sort, data.copy())
            print(f"Merge Sort - Size: {size}, Time: {merge_time:.6f} seconds, Memory: {merge_memory:.2f} MB")

            # Quick Sort
            quick_time, quick_memory = run_sorting_algorithm(quick_sort, data.copy())
            print(f"Quick Sort - Size: {size}, Time: {quick_time:.6f} seconds, Memory: {quick_memory:.2f} MB")

            # Counting Sort
            counting_time, counting_memory = run_sorting_algorithm(counting_sort, data.copy())
            print(f"Counting Sort - Size: {size}, Time: {counting_time:.6f} seconds, Memory: {counting_memory:.2f} MB")

            print("--------")