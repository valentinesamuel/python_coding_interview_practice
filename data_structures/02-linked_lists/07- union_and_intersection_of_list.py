from LinkedListClass import Node, LinkedList as linked_list

def union(list1, list2):
    """
    PROBLEM: Given two lists, A and B, the union is the list that contains elements or objects that belong to either A, B, or to both. Given two lists, A and B, the intersection is the largest list which contains all the elements that are common to both the sets.
    
    The union function will take two linked lists and return their union.
    The intersection function will return all the elements that are common between two linked lists.

    Input: Two linked lists.

    Output: A list containing the union of the two lists. A list containing the intersection of the two lists.

    Example Input: 
    list1 = 10->20->80->60
    list2 = 15->20->30->60->45

    Example Output:
    union = 10->20->80->60->15->30->45
    intersection = 20->60

    APPROACH:
    - Initial thoughts: We can link the head of the second list to the tail of the first list and remove duplicates. And for the intersection, we can use a hashmap to find the previously encountered values

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