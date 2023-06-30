from LinkedListClass import Node, LinkedList as linked_list

def union(list1, list2):
    """
    PROBLEM: Given two lists, A and B, the union is the list that contains elements or objects that belong to either A, B, or to both. Given two lists, A and B, the intersection is the largest list which contains all the elements that are common to both the sets.
    
    The union function will take two linked lists and return their union.
    The intersection function will return all the elements that are common between two linked lists.

    Input: Two linked lists.

    Output: A list containing the union of the two lists.

    Example Input: 
    list1 = 10->20->80->60
    list2 = 15->20->30->60->45

    Example Output:
    union = 10->20->80->60->15->30->45

    APPROACH:
    - Initial thoughts: We can link the head of the second list to the tail of the first list and remove duplicates.

    - Plan: 
        - iterate to the end of list 1
        - link it to the head of list2
        - remove any duplicates that might exist between the merged list
    """
    if list1.get_head() is None:
        return
    
    curr = list1.get_head()
    while curr.next_element:
        curr = curr.next_element
    curr.next_element = list2.get_head()

    list1.remove_duplicates()

    return list1

def intersection(list1, list2):
    """
    PROBLEM: Given two lists, A and B, the intersection is the largest list which contains all the elements that are common to both the sets.
    
    The intersection function will return all the elements that are common between two linked lists.

    Input: Two linked lists.

    Output: A list containing the intersection of the two lists.

    Example Input: 
    list1 = 10->20->80->60
    list2 = 15->20->30->60->45

    Example Output:
    intersection = 20->60

    APPROACH:
    - Initial thoughts: we can use a hashmap to find the previously encountered values

    - Plan: 
        - load all the elements of list1 into the hasmap and check each element of list2 against the hashmap.
        - create a new linked list to return
        - if it exists, then it is an intersectory node
        OR
        - we simply list1 and search for all elements in list2.
        - if any of these values are found in list2, it is added to the result linked list. This is less effective
    """
    if list1.get_head is None and list1 is None:
        return

    register = {}
    curr = list1.get_head()
    while curr:
        register[curr.data] = 1
        curr = curr.next_element
    
    res = linked_list()

    curr = list2.get_head()
    while curr:
        if curr.data in register:
            res.insert_at_tail(curr.data)
        curr = curr.next_element
    return res