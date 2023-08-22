def selection_sort(arr: list):
    """
    param (lst): List of integers
    """
    for i in range(len(arr)):
       # find the smallest element in unstorted list
        min = i
        for j in range(i+1, len(arr)):
        # find any other smallest element in the unstorted list
            if arr[j] < arr[min]:
                min = j
        # if there is, perform a swap
        arr[min], arr[i] = arr[i], arr[min]


lst = [3, 2, 1, 5, 4]
selection_sort(lst)


print("Sorted lst: ", lst)
