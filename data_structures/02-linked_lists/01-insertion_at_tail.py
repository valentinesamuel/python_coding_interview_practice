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
        if (self.head_node is None):
            return True
        else:
            return False

    def print_list(self):
        if (self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def search(self, value):
        """
        PROBLEM: To search for a specific value in a linked list, there is no other approach but to traverse the whole list until we find the desired value. In that sense, the search operation in linked lists is similar to the linear search in normal lists or arrays - all of them take O(n) amount of time.

        Input: A linked list and an integer to be searched.

        Output: True if the integer is found. False otherwise.

        Example Input: 
        Linked List = 5->90->10->4  
        Integer = 4

        Example Output:
        True

        APPROACH:
        - Initial thoughts: Since we have to look at every node. When we get to each node, we should check if the value we are looking for is in that node's data store

        - Plan: 
            - On every node, check if the node that we are looking for is the node that is that data store
            - If it is, then we return true else we return false.
            - An edge case is to check the last node before we return false since we did not check it in the loop because the last node's next_element points to null
        """

        if self.get_head() == None:
            return False
        current = self.get_head()
        while current.next_element:
            if current.data == value:
                return True
            current = current.next_element
        if current.data == value:
            return True
        return False

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

    def delete(self, value):
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
        if not self.get_head():
            return
        if self.get_head().data == value:
            self.delete_at_head()
            return True

        if self.search(value):
            current = self.get_head()
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

    def delete_at_head(self):
        first_element = self.get_head()
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return


def test_linked_list():
    # Test Case 1: Inserting into an empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    assert linked_list.search(1) == True
    assert linked_list.search(2) == False
    assert linked_list.print_list() == True

    # Test Case 2: Inserting into a non-empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    assert linked_list.print_list() == True
    assert linked_list.search(1) == True
    assert linked_list.search(2) == True
    assert linked_list.search(3) == True
    assert linked_list.search(4) == False

    # Test Case 3: Inserting multiple values into an empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    assert linked_list.print_list() == True
    assert linked_list.search(1) == True
    assert linked_list.search(2) == True
    assert linked_list.search(3) == True
    assert linked_list.search(4) == False

    # Test Case 4: Inserting multiple values into a non-empty list
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    linked_list.insert_at_tail(4)
    assert linked_list.print_list() == True
    assert linked_list.search(1) == True
    assert linked_list.search(2) == True
    assert linked_list.search(3) == True
    assert linked_list.search(4) == True
    assert linked_list.search(5) == False

    # Test Case 5: Inserting a value at the tail of a large list
    linked_list = LinkedList()
    for i in range(1, 10):
        linked_list.insert_at_tail(i)
    assert linked_list.print_list() == True
    for i in range(1, 10):
        assert linked_list.search(i) == True
    assert linked_list.search(10) == False

    # Test Case 6: Inserting a negative value at the tail
    linked_list = LinkedList()
    linked_list.insert_at_tail(-1)
    linked_list.insert_at_tail(-2)
    linked_list.insert_at_tail(-3)
    assert linked_list.print_list() == True
    assert linked_list.search(-1) == True
    assert linked_list.search(-2) == True
    assert linked_list.search(-3) == True
    assert linked_list.search(0) == False

    print("\n\n💯💯All test cases passed!💯💯\n\n")


test_linked_list()
