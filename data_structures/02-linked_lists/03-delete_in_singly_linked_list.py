from DS_Classes.LinkedListClass import LinkedList as linked_list
import sys
sys.path.append('../DS_Classes/')

def delete(value):
    """
    PROBLEM: we can pass a particular value that we want to delete from the list. The node containing this value could be anywhere in the list. It is also possible that such a node may not exist at all.Therefore, we would have to traverse the whole list until we find the value which needs to be deleted. If the value doesn't exist, we do not need to do anything.

    Input: A linked list and an integer to be deleted.

    Output: True if the value is deleted. Otherwise, False.

    Example Input: 
    LinkedList = 3->2->1->0
    integer = 2

    Example Output:
    Linked List = True

    APPROACH:
    - Initial thoughts: We shold look for a way to safely delete the node. We can try to serach for it to make sure it exists

    - Plan: 
        - check if the linked list is empty or if the node to be deleted is the head node. If so, delete accordingly and return true
        - If we are able to search for the the node, then we can go ahead to initialize the fast and slow pointer.
        - For every node, if the node's data is the value that we are looking for, then we can delete and return true.
        - Else we move the slow pointer and the update the fast pointer.
        - The last node does not get checked because it's next_element is None. SO we have to check for this and return True is deletion is possible.
    """
    if not linked_list.get_head():
        return
    if linked_list.get_head().data == value:
        linked_list.delete_at_head()
        return True

    if linked_list.search(value):
        current = linked_list.get_head()
        follower = current
        while current.next_element:
            if current.data == value:
                follower.next_element = current.next_element
                return True
            follower.next_element = current
            current = current.next_element
        if current.data == value:
            follower.next_element = current.next_element
            return True
        return False
    return False
