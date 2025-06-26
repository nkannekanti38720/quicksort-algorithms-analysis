def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Pivot selection (last element)
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]  # Elements less than pivot
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Test the deterministic quicksort
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original Array:", arr)
    sorted_arr = quicksort(arr)
    print("Sorted Array (Deterministic Quicksort):", sorted_arr)
