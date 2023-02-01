from linkedlist import LinkedList, list_traversal


def reverse_sublist(head, start, finish):
    sublist_head = head
    for _ in range(start):
        sublist_head = sublist_head.next

    # Reverses sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    
    return head


def main():
    list1 = LinkedList()
    items = [1, 3, 5, 7, 9, 11, 13, 15]
    for i in items:
        list1.add_node_to_rear(i)

    reversed_list = reverse_sublist(list1.head, 4, 6)
    list_traversal(reversed_list)


if __name__ == '__main__':
    main()