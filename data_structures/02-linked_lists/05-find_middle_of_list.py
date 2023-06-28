from LinkedListClass import LinkedList as linked_list

def find_mid(lst):

    if not lst.get_head():
        return
    trav = 0
    length = lst.length()
    if length % 2 == 0:
        trav = length // 2
    else:
        trav = (length // 2) + 1
    i = 1
    curr = lst.get_head()
    while i < trav:
        curr = curr.next_element
        i+=1
    return curr.data