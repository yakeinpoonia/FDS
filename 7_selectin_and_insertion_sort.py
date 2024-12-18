# Function to perform Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"After iteration {i + 1}: {arr}")

# Function to perform Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"After iteration {i}: {arr}")

# Menu function with a while loop for continuous interaction
marks = []
n = int(input("Enter the number of students: "))

# Input marks for students
for i in range(n):
    mark = int(input(f"Enter the marks of student {i + 1}: "))
    marks.append(mark)

while True:
    print("\nMenu:")
    print("1. Sort marks using Selection Sort")
    print("2. Sort marks using Insertion Sort")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nSelection Sort:")
        selection_sort(marks.copy())  # Using a copy to keep original list intact
    elif choice == '2':
        print("\nInsertion Sort:")
        insertion_sort(marks.copy())  # Using a copy to keep original list intact
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
