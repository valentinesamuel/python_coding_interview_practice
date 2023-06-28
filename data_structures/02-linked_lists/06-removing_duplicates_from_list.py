from LinkedListClass import LinkedList as linked_list

def remove_duplicates(lst):
    if not lst.get_head():
        return
    register = {}
    curr = lst.get_head()
    follower = lst.get_head()

    while curr:
        if not curr.data in register:
            register[curr.data] = 1
            follower = curr
            curr = curr.next_element
        else:
            follower.next_element = curr.next_element
            curr = curr.next_element
    return lst