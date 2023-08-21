def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

lst = [3, 2, 1, 5, 4]
selection_sort(lst)  # Calling selection sort function

# Printing Sorted lst
print("Sorted lst: ", lst)
