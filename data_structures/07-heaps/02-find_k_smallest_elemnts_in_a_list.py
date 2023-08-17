from DS_Classes.MinHeapClass import MinHeap

def findKSmallest(lst, k):
    """
    PROBLEM: Implement a function findKSmallest(lst,k) that takes an unsorted integer list as input and returns the “k” smallest elements in the list using a Heap. The minHeap class that was written in Min Heap (Implementation) is prepended to this exercise so feel free to use it! Have a look at the illustration given for a clearer picture of the problem.

    Input: A heap.

    Output: Returns K smallest items in the heap

    Example Input:
    lst = [9,4,7,1,-2,6,5]
    k = 3

    Example Output:
    [-2,1,4]

    APPROACH:
    - Initial thoughts: None

    - Plan: 
        - from I to K, remove min from the heap
    """
    mh = MinHeap()
    mh.buildHeap(lst)
    kSmallest = []
    for i in range(k):
        kSmallest.append(mh.removeMin())
    return kSmallest