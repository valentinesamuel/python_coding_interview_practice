def convertMax(maxHeap):
    """
    PROBLEM: Implement a function convertMax(maxHeap) which will convert a binary Max-Heap into a binary Min-Heap. Where maxHeap is a list which is given in the maxHeap format, i.e, the parent is greater than its children.

    Input: A max heap.

    Output: Returns a min heap

    Example Input:
    maxHeap = [9,4,7,1,-2,6,5]

    Example Output:
    result = [-2,1,5,9,4,6,7]

    APPROACH:
    - Initial thoughts: I thought that if i could traverse to find a node, i can possibly, keep track of all the nodes that i have gone through

    - Plan: 
        - for every index from the last root node to the root node
        - call heapify in them
    """
    n = len(maxHeap)
    for i in range(n//2-1, -1, -1):
        heapify(maxHeap, n, i)
    return maxHeap


def heapify(heap, length, index):
    """    
        - For heapify-ing
        - get the current index, left and right index
        - if left is within bounds and the left value is less than the current value,
            - let the current index be the left index
        - if right is within bounds and the right value is less than the current value,
            - let the current index be the right index
        - if current and the index does not match
            - swap the current and index index values
            - and recursively heapify from the current value
    """
    curr = index
    left = 2 * index + 2
    right = 2 * index + 1

    if index < length and heap[left] < heap[curr]:
        curr = left
    if index < length and heap[right] < heap[curr]:
        curr = right
    if curr != index:
        heap[curr], heap[index] = heap[index], heap[curr]
        heapify(heap, length, curr)
