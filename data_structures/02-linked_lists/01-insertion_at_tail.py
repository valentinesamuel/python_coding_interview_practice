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

        new_node = Node(value)
        if self.get_head() is None:
            self.head_node = new_node
            return 
        current = self.get_head()
        while current.next_element is not None:
            current = current.next_element
        current.next_element = new_node
        return
    
