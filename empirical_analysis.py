import random
import time

# Iterative version of Quicksort
def quicksort_iterative(arr):
    # Create a stack for the indices of the subarrays
    stack = [(0, len(arr) - 1)]

    # Run the loop while there are subarrays to process
    while stack:
        start, end = stack.pop()
        
        if start >= end:
            continue  # No need to process subarrays of length 0 or 1
        
        pivot_index = partition(arr, start, end)  # Partition the array and get the pivot index
        
        # Push the subarrays onto the stack
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

    return arr

def partition(arr, start, end):
    pivot = arr[end]  # Use the last element as the pivot
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:  # Elements smaller than pivot move to the left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot into its correct position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# Randomized Quicksort (Random pivot, iterative version)
def randomized_quicksort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()
        
        if start >= end:
            continue
        
        pivot_index = random.randint(start, end)
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]  # Swap the random pivot with the last element
        pivot_index = partition(arr, start, end)
        
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

    return arr

# Function to test the performance of both sorting algorithms
def test_quicksort_versions():
    input_sizes = [10, 100, 1000, 5000, 10000]  # Different input sizes for testing
    distributions = ['random', 'sorted', 'reverse_sorted']  # Different types of input distributions

    # Loop through different sizes and distributions
    for size in input_sizes:
        for dist in distributions:
            if dist == 'random':
                arr = random.sample(range(size), size)  # Random array
            elif dist == 'sorted':
                arr = list(range(size))  # Sorted array
            else:
                arr = list(range(size, 0, -1))  # Reverse sorted array

            # Test deterministic quicksort (iterative version)
            start_time = time.time()
            quicksort_iterative(arr.copy())  # Copy to avoid sorting the same array twice
            print(f"Deterministic Quicksort ({dist}, size {size}): {time.time() - start_time:.6f} seconds")

            # Test randomized quicksort (iterative version)
            start_time = time.time()
            randomized_quicksort(arr.copy())  # Copy to avoid sorting the same array twice
            print(f"Randomized Quicksort ({dist}, size {size}): {time.time() - start_time:.6f} seconds")

# Run the empirical analysis
if __name__ == "__main__":
    test_quicksort_versions()
