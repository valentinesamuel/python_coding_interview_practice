from DS_Classes.MaxHeapClass import MaxHeap


def findKLargest(lst, k):
    """
    PROBLEM: Implement a function findKLargest(lst,k) that takes an unsorted integer list as input and returns the k largest elements in the list using a Max Heap. The maxHeap class that was written in Max Heap (Implementation) is prepended in this exercise so feel free to use it! Have a look at the illustration given for a clearer picture of the problem. Implement a function findKlargest() which takes a list as input and finds the “k” largest elements in the list using a Max-Heap. An illustration is also provided for your understanding.

    Input: A heap.

    Output: Returns K largest items in the heap

    Example Input:
    lst = [9,4,7,1,-2,6,5]
    k = 3

    Example Output:
    [9,7,6]

    APPROACH:
    - Initial thoughts: None

    - Plan: 
        - from I to K, remove max from the heap
    """
    mh = MaxHeap()
    mh.buildHeap(lst)
    kLargest = []
    for i in range(k):
        kLargest.append(mh.removeMax())
    return kLargest
