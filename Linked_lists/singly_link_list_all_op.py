class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Add node with the given data at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Add node with the given data at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def display(self):
        """Display the linked list."""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", " -> ".join(map(str, elements) if elements else "Empty List"))

# Insert nodes at the end of the linked list
linked_list = SinglyLinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(5)
linked_list.insert_at_end(25)
linked_list.insert_at_end(15)

# Insert at the beginning
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(40)
linked_list.display()