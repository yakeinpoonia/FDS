# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)
        
        # Display array after each iteration
        print(f"Array after partition: {arr}")
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Partition function for Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Main program
marks = [87, 92, 77, 85, 94, 72, 69, 99, 65, 80]

# Sort the array using Quick Sort
while True:
    print("Original marks:", marks)
    quick_sort(marks, 0, len(marks) - 1)
    
    # Display top 5 scores
    print("Top 5 scores:", sorted(marks, reverse=True)[:5])
    break  # Exiting the loop after sorting and displaying
