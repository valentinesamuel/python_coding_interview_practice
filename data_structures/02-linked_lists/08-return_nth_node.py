from LinkedListClass import LinkedList as linked_list

def find_nth(lst, n):
    """
    PROBLEM: In the find_nth function, a certain N is specified as an argument. You simply need to return the node which is N spaces away from the None end of the linked list.

    Input: A linked list and a position N.

    Output: The value of the node n positions from the end. Returns -1 if n is out of bounds.

    Example Input: 
    LinkedList = 22->18->60->78->47->39->99 and n = 3

    Example Output:
    47

    APPROACH:
    - Initial thoughts: Take some time to flesh out the logic for your algorithm. Keep in mind that you need to return the data component of the specified node. This isn't a very tough exercise. All hard work should end on a good note.

    - Plan: 
        - check if the linked list is empty 
        - if the n is less than the length, return -1
        - to get the traversl stop point, we subtract the n from the length
        - we loop while the index is less than 0
        - then we return the curr.data
    """

    if lst.get_head() is None:
        return

    curr = lst.get_head()
    length = lst.length()

    if n > length:
        return -1

    index = (length - n) 

    while index > 0:
        curr = curr.next_element
        index -= 1
    
    return curr.data