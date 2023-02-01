from linkedlist import LinkedList

def merge(head1, head2):
    curr1, prev1 = head1, head1
    curr2 = head2
    while curr1 is not None:
        if curr1.data < curr2.data:
            prev1 = curr1
            curr1 = curr1.next
        else:
            # Operations with the second list
            merge_node = curr2  # Temporary External Reference
            curr2 = curr2.next  # Advance the pointer to the next node
            
            # Operations to link to the first list
            merge_node.next = curr1  # Link 
            prev1.next = merge_node  # UnLink

            if curr2 is None:
                break

    # Since we are merging list2 into list1, any elements leftover 
    # in list2 after the complete traversal of list1 should be appended
    # to the end of list1 as these elements are greater than all the 
    # elements in the list1. Hence,the sortedness is preserved.
    if curr2 is not None:
        prev1.next = curr2

    return head1


def list_traversal(head):
    curr_node = head
    item_str = 'Head -->'
    count = 0
    while curr_node is not None:
        item_str = item_str + str(curr_node.data) + '-->'
        curr_node = curr_node.next
        count = count + 1
    print(item_str)
    return count


def main():
    list1 = LinkedList()
    items = [1, 3, 5, 7, 9]
    for i in items:
        list1.add_node_to_rear(i)

    list2 = LinkedList()
    items = [2, 4, 6, 8, 10]
    for i in items:
        list2.add_node_to_rear(i)

    merged_list = merge(list1.head, list2.head)
    
    list1.traversal()
    list2.traversal()
    list_traversal(merged_list)


if __name__ == '__main__':
    main()

