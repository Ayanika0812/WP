def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Target found at index mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)  # Search in left half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)  # Search in right half

# Taking input from the user
arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
arr.sort()  # Ensuring the array is sorted in ascending order
print("Sorted array:", arr)

target = int(input("Enter the number to search: "))

# Performing binary search
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")




""" Enter sorted numbers separated by spaces: 22 55 40 30 90 2
Sorted array: [2, 22, 30, 40, 55, 90]
Enter the number to search: 40
Element 40 found at index 3.
"""