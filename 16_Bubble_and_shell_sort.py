def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        print(f"Iteration {i + 1}: {arr}")  # Display array before each iteration
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f"Final sorted array: {arr}")


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    iteration = 1
    while gap > 0:
        print(f"Gap: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        print(f"Iteration {iteration}: {arr}")
        iteration += 1
        gap //= 2
    print(f"Final sorted array: {arr}")

# Main Program
while True:
    print("\nMenu:")
    print("1. Input student percentages")
    print("2. Sort using Bubble Sort")
    print("3. Sort using Shell Sort")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter the number of students: "))
        percentages = []
        for i in range(n):
            percentage = float(input(f"Enter percentage of student {i + 1}: "))
            percentages.append(percentage)
        print("\nOriginal Array:", percentages)

    elif choice == 2:
        if 'percentages' in locals():
            print("\nBubble Sort:")
            bubble_sort(percentages[:])  # Pass a copy of the array to preserve original order
        else:
            print("Please input percentages first.")

    elif choice == 3:
        if 'percentages' in locals():
            print("\nShell Sort:")
            shell_sort(percentages[:])
        else:
            print("Please input percentages first.")

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")