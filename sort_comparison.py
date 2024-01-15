import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def test_algorithms(arr_100, arr_1000):
    print("| Algorithm      | 100 elements    |  1000 elements  |")
    print("| --------------- | --------------- | ---------------- |")

    # Merge Sort
    merge_sort_time_100 = timeit.timeit(lambda: merge_sort(arr_100.copy()), number=1000)
    merge_sort_time_1000 = timeit.timeit(
        lambda: merge_sort(arr_1000.copy()), number=1000
    )
    print(
        f"| Merge Sort      | {merge_sort_time_100:.8f} sec | {merge_sort_time_1000:.8f} sec |"
    )

    # Insertion Sort
    insertion_sort_time_100 = timeit.timeit(
        lambda: insertion_sort(arr_100.copy()), number=1000
    )
    insertion_sort_time_1000 = timeit.timeit(
        lambda: insertion_sort(arr_1000.copy()), number=1000
    )
    print(
        f"| Insertion Sort  | {insertion_sort_time_100:.8f} sec | {insertion_sort_time_1000:.8f} sec |"
    )

    # Timsort (Python's built-in sorting algorithm)
    timsort_time_100 = timeit.timeit(lambda: sorted(arr_100.copy()), number=1000)
    timsort_time_1000 = timeit.timeit(lambda: sorted(arr_1000.copy()), number=1000)
    print(
        f"| Timsort         | {timsort_time_100:.8f} sec | {timsort_time_1000:.8f} sec |"
    )


if __name__ == "__main__":
    random.seed(42)
    test_array_100 = [random.randint(1, 1000) for _ in range(100)]
    test_array_1000 = [random.randint(1, 1000) for _ in range(1000)]

    test_algorithms(test_array_100, test_array_1000)
