class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  
            return True
        else:
            return False

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def insert_at_tail(self, value):
        """
        PROBLEM: We need to insert a new object at the end of the linked list. You can naturally guess, that this newly added node will point to None as it is at the tail.

        Input: A linked list and an integer value.

        Output: The updated linked list with the value inserted.

        Example Input: 
        Linked List = 0->1->2
        integer = 3

        Example Output:
        Linked List = 0->1->2->3

        APPROACH:
        - Initial thoughts: We shold look for a way to add the node at the first place without losing pointers
        
        - Plan: 
            - check if the linked list is empty. If it is, assign the node to the be the head node of the linked list
            - if the list is not empty, get the head pointer of the list and iterate till the current node's pointer is None.
            - On every iteration, assign the next element of the current node to the current node
        """

        new_node = Node(value)
        if self.get_head() is None:
            self.head_node = new_node
            return 
        current = self.get_head()
        while current.next_element is not None:
            current = current.next_element
        current.next_element = new_node
        return
    
def test_insert_at_tail():
    # Test Case 1: Inserting into an empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    assert linked_list.print_list() == True

    # Test Case 2: Inserting into a non-empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    assert linked_list.print_list() == True

    # Test Case 3: Inserting multiple values into an empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    assert linked_list.print_list() == True

    # Test Case 4: Inserting multiple values into a non-empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    linked_list.insert_at_tail(4)
    assert linked_list.print_list() == True

    # Test Case 5: Inserting a value at the tail of a large list
    linked_list = LinkedList()
    for i in range(1, 10):
        linked_list.insert_at_tail(i)
    assert linked_list.print_list() == True

    # Test Case 6: Inserting a negative value at the tail
    linked_list = LinkedList()
    linked_list.insert_at_tail(-1)
    linked_list.insert_at_tail(-2)
    linked_list.insert_at_tail(-3)
    assert linked_list.print_list() == True

    print("\n\n💯💯All test cases passed!💯💯\n\n")

test_insert_at_tail()