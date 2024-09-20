# Corrected code with proper logic

def bubble(li):
    li1 = li.copy()
    for i in range(len(li) - 1):
        for j in range(1, len(li) - i):
            if li1[j - 1] > li1[j]:
                li1[j - 1], li1[j] = li1[j], li1[j - 1]
    return li1

def selection(li1):
    li = li1.copy()
    for i in range(len(li) - 1):
        min_idx = i  # Start from the first unsorted element
        for j in range(i + 1, len(li)):  # Find the minimum element
            if li[j] < li[min_idx]:
                min_idx = j
        # Swap the minimum element with the first unsorted element
        li[i], li[min_idx] = li[min_idx], li[i]
    return li

def insertion(li):
    li1 = li.copy()
    for i in range(1, len(li1)):  # Start from the second element
        value = li1[i]
        j = i - 1
        while j >= 0 and li1[j] > value:
            li1[j + 1] = li1[j]  # Move the element one position forward
            j -= 1
        li1[j + 1] = value  # Insert the value in its correct position
    return li1

def shell(arr1):
    arr = arr1.copy()
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def partition(li, s, e):
    pivot = li[s]
    count = 0
    for i in range(s + 1, e + 1):
        if li[i] < pivot:
            count += 1
    pos = s + count
    li[pos], li[s] = li[s], li[pos]

    i, j = s, e
    while i < j:
        while i < pos and li[i] < pivot:
            i += 1
        while j > pos and li[j] >= pivot:
            j -= 1
        if i < j:
            li[i], li[j] = li[j], li[i]
    return pos

def quick(li, s, e):
    if s >= e:
        return
    pos = partition(li, s, e)
    quick(li, s, pos - 1)
    quick(li, pos + 1, e)

# def quick(li, s, e):
#     if s < e:
#         pos = partition(li, s, e)
#         quick(li, s, pos - 1)  # Recursively sort elements before pivot
#         quick(li, pos + 1, e)  # Recursively sort elements after pivot

# Test
li = [12, 54, -324, 657, 1, 45]
li1 = li.copy()

print("Bubble Sort:", bubble(li))
print("Selection Sort:", selection(li))
print("Insertion Sort:", insertion(li))
quick(li1, 0, len(li1) - 1)
print("Quick Sort:", li1)
print("Shell Sort:", shell(li))
