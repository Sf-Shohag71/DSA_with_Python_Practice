class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        
        new_node.next = self.head
        new_node.prev = self.tail

        self.head.prev = new_node
        self.tail.next = new_node

        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        new_node.prev = self.tail
        new_node.next = self.head

        self.head.prev = new_node
        self.tail.next = new_node
        self.tail = new_node

    # Count number of Nodes in the linked list
    def size(self):
        if self.head is None:
            return 0

        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break

        return count
    # Insert at position without using insert_at_beginning or insert at the end
    def insert_at_position(self, data, position):

        if position < 0:
            raise IndexError("Invalid position")

        new_node = Node(data)

        # Case 1: Empty linked list
        if self.head is None:
            if position != 0:
                raise IndexError("Invalid position")

            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node
            return

        # Case 2: Insert at beginning
        if position == 0:
            new_node.next = self.head
            new_node.prev = self.tail

            self.head.prev = new_node
            self.tail.next = new_node

            self.head = new_node
            return

        # Case 3: Traverse to the previous node
        current = self.head
        count = 0

        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1

        # Case 4: Validate position
        if count != position - 1:
            raise IndexError("Invalid position")

        # Case 5: Insert at the end
        if current == self.tail:
            new_node.next = self.head
            new_node.prev = self.tail

            self.tail.next = new_node
            self.head.prev = new_node

            self.tail = new_node
            return

        # Case 6: Insert in the middle
        new_node.next = current.next
        new_node.prev = current

        current.next.prev = new_node
        current.next = new_node
  
        
    def display_forward(self):
        if self.head is None:
            print("List is empty!")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next

            if current == self.head:
                break

        print(f"({current.data}-back to head)")

    def display_backward(self):
        if self.tail is None:
            print("List is empty")
            return
        current = self.tail
        while True:
            print(current.data, end=" <-> ")
            current = current.prev

            if current == self.tail:
                break

        print(f"({current.data}-back to head)")

cdl = CircularDoublyLinkedList()
list_size = cdl.size()
print(list_size)

cdl.insert_at_beginning(50)
cdl.insert_at_beginning(9)
cdl.insert_at_end(5)
cdl.insert_at_position(80, 2)
cdl.display_forward()
cdl.display_backward()

list_size = cdl.size()
print(list_size)
