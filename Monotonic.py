def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False
        if arr[i] > arr[i - 1]:
            decreasing = False

    return increasing or decreasing


# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [13,1, 2, 2, 3, 4]
arr5= [5, 4, 3, 2,3,4,5,]

print(is_monotonic(arr1))  # Output: True
print(is_monotonic(arr2))  # Output: True
print(is_monotonic(arr3))  # Output: True
print(is_monotonic(arr5))  # Output: True


