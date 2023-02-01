

# Addition of elements to the front
# Addition of elements to the rear

# Removal
#   - with a specific value
#   - specific index from head
#   - first element
#   - last element
#   - middle element

# Create a LinkedList for elements <1, 3, 5, 7, 9>

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_to_front(self, value):
        new_node = Node(value)
        temp = self.head
        self.head = new_node
        new_node.next = temp

    def add_node_to_rear(self, value):
        new_node = Node(value)
        if self.head is not None:
            last_node = self.get_last_node()
            last_node.next = new_node
        else:
            self.head = new_node

    def get_last_node(self):
        node = self.head
        while node is not None:
            if node.next is None:
                return node
            else: 
                node = node.next
        
    def traversal(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node  = curr_node.next

    def unordered_search(self, target):
        curr_node = self.head
        while curr_node is not None and curr_node.data != target:
            curr_node = curr_node.next
        return curr_node is not None

    def prepending_node(self, target):
        new_node = Node(target)
        new_node.next = self.head
        self.head = new_node

    def removing_node(self, target):
        prev_node = None
        
    def list_traversal(self):
        curr_node = self.head
        item_str = 'Head -->'
        count = 0
        while curr_node is not None:
            item_str = item_str + str(curr_node.data) + '-->'
            curr_node = curr_node.next
            count = count + 1
        print(item_str)
        return count

    def remove_first_node(self):
        temp = self.head
        self.head = temp.next
        return temp.data

    def remove_last_node(self):
        node = self.head
        while(node.next is not None):
            prev_node = node
            node = node.next
        prev_node.next = None
        return node.data
        
    def remove_node_by_value(self, value):
        curr_node = self.head
        while(curr_node is not None):
            prev_node = curr_node
            curr_node = curr_node.next
            
            if(curr_node.data == value):
                temp = curr_node
                next_node = curr_node.next
                prev_node.next = next_node
                return temp.data

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
    
def create_linked_list():
    ll_obj = LinkedList()
    items = [1, 3, 5, 7, 9]
    for i in items:
        ll_obj.add_node_to_front(i)
    
    # Print the list object created
    print("Adding new items to the front")
    ll_obj.list_traversal()
    

    # Add items to the rear
    ll_obj = LinkedList()
    items = [1, 3, 5, 7, 9]
    for i in items:
        ll_obj.add_node_to_rear(i)
    
    print("Adding items to the rear end")
    ll_obj.list_traversal()


def remove_nodes():
    ll_obj = LinkedList()
    items = [1, 3, 5, 7, 9]
    for i in items:
        ll_obj.add_node_to_front(i)
    
    # Print the list object created
    print("Adding new items to the front")
    ll_obj.list_traversal()

    ll_obj.remove_first_node()

    print("After removing first item")
    ll_obj.list_traversal()

    ll_obj.remove_last_node()
    print("After removing last node")
    ll_obj.list_traversal()

    ll_obj.remove_node_by_value(5)
    print("After removing node with value 5")
    ll_obj.list_traversal()
    

if __name__ == '__main__':
    # create_linked_list()
    remove_nodes()
    

