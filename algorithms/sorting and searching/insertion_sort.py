def insertio_sort(arr):

    for i in range(1, len(arr)):
        # get the current number to be sorted
        key = arr[i]

        # get the amount of backward spaces to shift
        j = i - 1

        # perform the backward movement while there is
        # still space and the current sorted element is 
        # than the jth element
        while j >= 0 and arr[j] > key:
         # perform the backward shift
            arr[j + 1] = arr[j]
            j -= 1
        # put the current sorted element into the empty space
        arr[j + 1] = key
