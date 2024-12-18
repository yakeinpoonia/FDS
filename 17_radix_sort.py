# Custom max function
def max(arr):
    # Initialize the first element as the maximum
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num  # Update max_val if a larger number is found
    return max_val

# Counting Sort Function
def counting_sort(arr, exp):
    n = len(arr)  # Get the length of the array
    output = [0] * n  # Create an output array to store sorted elements
    count = [0] * 10  # Create a count array to store the frequency of digits (0-9)

    # Count the occurrences of digits at the current place value (exp)
    for i in range(n):
        index = arr[i] // exp  # Get the digit at the current place value
        count[index % 10] += 1  # Increment the count for that digit

    # Update the count array by adding the previous counts
    for i in range(1, 10):
        count[i] += count[i - 1]  # Modify the count array to store actual positions

    # Build the output array by placing elements in their sorted positions
    for i in range(n - 1, -1, -1):  # Traverse from end to start for stable sorting
        index = arr[i] // exp  # Get the digit at the current place value
        output[count[index % 10] - 1] = arr[i]  # Place the element in the output array
        count[index % 10] -= 1  # Decrement the count for that digit

    # Copy the sorted elements from the output array back to the original array
    for i in range(n):
        arr[i] = output[i]  # Copy the elements back into the original array

# Radix Sort Function
def radix_sort(arr):
    max_val = max(arr)  # Find the maximum number in the array using the custom max function

    # Perform counting sort for every digit starting from the least significant digit
    exp = 1  # Start with the least significant digit (1s place)
    while max_val // exp > 0:  # Continue sorting until we've sorted all digits
        counting_sort(arr, exp)  # Sort the array based on the current digit
        exp *= 10  # Move to the next place value (10s, 100s, etc.)

    return arr  # Return the fully sorted array

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Sorted array:", radix_sort(arr))  # Output: [2, 24, 45, 66, 75, 90, 170, 802]