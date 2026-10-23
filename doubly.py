class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # 3. Insert at a given position (zero-indexed)
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Invalid position")

        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head

        # Move to the node before the insertion position
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next

        if current is None:
            raise IndexError("Position out of range")

        new_node = Node(data)

        # Connect the new node
        new_node.prev = current
        new_node.next = current.next

        if current.next is not None:
            current.next.prev = new_node
        else:
            self.tail = new_node

        current.next = new_node

    # Display the list from head to tail
    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    # Display the list from tail to head
    def display_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_position(25, 2)  # Insert 25 at position 2


dll.display_forward()
dll.display_backward()