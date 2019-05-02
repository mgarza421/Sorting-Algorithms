"Collection of well-known sorting algorithms"

import numpy as np

def main():
    arr = np.random.randint(1,1001,1000)
    test = arr
    Selection_Sort(test)
    Bubble_Sort(test)

    for i in range(999):
        sorted = False if test[i] > test[i+1] else True
    if sorted:
        print("Array is sorted")

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
    for i in range(size-1):
        for j in range(i+1, size-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        else:
            swapped = False

if __name__ == "__main__":
    main()