import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]  # Swap pivot with the last element
    pivot = arr[-1]
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]
    return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)

# Test the randomized quicksort
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original Array:", arr)
    sorted_arr = randomized_quicksort(arr)
    print("Sorted Array (Randomized Quicksort):", sorted_arr)
