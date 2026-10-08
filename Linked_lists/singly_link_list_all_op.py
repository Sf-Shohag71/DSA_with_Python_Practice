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
        # If the linked list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 3. Insert at a specific position
    # Position starts from 0
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        # Insert at beginning
        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head

        # Move to the node before the desired position
        for _ in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next

        if current is None:
            print("Position out of range")
            return

        new_node = Node(data)

        new_node.next = current.next
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

# Insert Nodes at specific positions
linked_list.insert_at_position(50, 2)  # Insert 50 at position 2

# Display the linked list
linked_list.display()