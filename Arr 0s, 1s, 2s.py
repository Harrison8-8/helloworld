def sort_array(arr):
    # Initialize pointers
    low, mid, high = 0, 0, len(arr) - 1

    # Loop until mid exceeds high
    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[mid] and arr[low] if current element is 0
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # Simply move the mid pointer
            mid += 1
        else:
            # Swap arr[mid] and arr[high] if current element is 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example usage
arr = [2, 0, 2, 1, 0, 1, 2]
sorted_arr = sort_array(arr)
print(sorted_arr)