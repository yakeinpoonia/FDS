# Binary Search 
def binary_search(arr, x):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
    return -1

# Linear Search 
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Sentinal Search
def sentinal_seaarch(arr, x):
    n = len(arr)
    last = arr[n-1]
    arr[n-1] = x

    i = 0
    while arr[i]!=x:
        i+=1

    arr[n-1] = last

    if i<n-1 or arr[n-1] == x:
        return i
    return -1

# Fibonacci Search
def fibonacci_search(arr, x):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fibM = fib2 + fib1

    while fibM < n:
        fib2 = fib1
        fib1 = fibM
        fibM = fib2 + fib1

    offset = -1

    while fibM > 1:
        i = min(offset+fib2, n-1)
        if arr[i] < x:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif arr[i] > x:
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return i
    
    if fib1 and arr[offset + 1] == x:
        return offset + 1
    
    return -1