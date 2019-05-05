"Collection of well-known sorting algorithms"

import numpy as np

def main():
    arr = np.random.randint(1,1001,1000)
    test = arr.copy()
    Selection_Sort(test)
    is_Sorted(test, "Selection Sort")
    test = arr.copy()
    Bubble_Sort(test)
    is_Sorted(test, "Bubble Sort")
    test = arr.copy()
    Insertion_Sort(test)
    is_Sorted(test, "Insertion Sort")
    test = arr.copy()
    Merge_Sort(test)
    is_Sorted(test, "Merge Sort")
    test = arr.copy()
    Quick_Sort(test, 0, len(test)-1)
    is_Sorted(test, "Quick Sort")

def Selection_Sort(arr):
    size = len(arr)
    for i in range(size):
        minIndex = i
        for j in range(i+1, size):
            minIndex = j if arr[j] < arr[minIndex] else minIndex
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def Bubble_Sort(arr):
    size = len(arr)
    swapped = False
    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
        else:
            swapped = False

def Insertion_Sort(arr):
    size = len(arr)
    for i in range(1, size):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j] = arr[i]

def Merge_Sort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        left = arr[:m]
        right = arr[m:]
        Merge_Sort(left)
        Merge_Sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def Quick_Sort(arr, low, high):
    if low < high:
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        pivot_Index = i
        Quick_Sort(arr, low, pivot_Index-1)
        Quick_Sort(arr, pivot_Index+1, high)

def is_Sorted(arr, type):
    sorted = 0
    if(all(arr[i] <= arr[i+1] for i in range(len(arr)-1))):
        sorted = 1
    if sorted:
        print("Array is sorted: " + type)
    else:
        print("Array not sorted: " + type)

if __name__ == "__main__":
    main()