class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        new_node.next = self.head
        new_node.prev = self.tail

        self.head.prev = new_node
        self.tail.next = new_node

        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        new_node.prev = self.tail
        new_node.next = self.head

        self.tail.next = new_node
        self.head.prev = new_node

        self.tail = new_node

    # 3. Insert at a specific position
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Invalid position")

        length = self.size()

        if position > length:
            raise IndexError("Position out of range")

        if position == 0:
            self.insert_at_beginning(data)
            return

        if position == length:
            self.insert_at_end(data)
            return

        # Move to the node currently at the desired position
        current = self.head

        for _ in range(position):
            current = current.next

        new_node = Node(data)
        previous_node = current.prev

        new_node.prev = previous_node
        new_node.next = current

        previous_node.next = new_node
        current.prev = new_node

    # 4. Delete from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            raise IndexError("List is empty")

        # If there is only one node
        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next

        self.head.prev = self.tail
        self.tail.next = self.head

    # 5. Delete from the end
    def delete_from_end(self):
        if self.tail is None:
            raise IndexError("List is empty")

        # If there is only one node
        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.prev

        self.tail.next = self.head
        self.head.prev = self.tail

    # 6. Delete at a specific position
    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Invalid position")

        length = self.size()

        if position >= length:
            raise IndexError("Position out of range")

        if position == 0:
            self.delete_from_beginning()
            return

        if position == length - 1:
            self.delete_from_end()
            return

        current = self.head

        for _ in range(position):
            current = current.next

        previous_node = current.prev
        next_node = current.next

        previous_node.next = next_node
        next_node.prev = previous_node

    # 7. Search for a value
    # Returns the first matching position, or -1
    def search(self, value):
        if self.head is None:
            return -1

        current = self.head
        position = 0

        while True:
            if current.data == value:
                return position

            current = current.next
            position += 1

            if current == self.head:
                break

        return -1

    # 8. Update a node at a specific position
    def update(self, position, new_data):
        if position < 0:
            raise IndexError("Invalid position")

        current = self.head
        index = 0

        while current is not None and index < position:
            current = current.next

            # Stop after one complete cycle
            if current == self.head:
                break

            index += 1

        if current is None or index != position:
            raise IndexError("Position out of range")

        current.data = new_data

    # 9. Display forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" <-> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")

    # 10. Display backward
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

        print("(back to tail)")

    # 11. Calculate the number of nodes
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

    # 12. Check whether the list is empty
    def is_empty(self):
        return self.head is None

    # 13. Reverse the list
    def reverse(self):
        if self.head is None:
            return

        current = self.head

        while True:
            # Save the original next node
            next_node = current.next

            # Swap the previous and next references
            current.prev, current.next = current.next, current.prev

            # Move using the original next reference
            current = next_node

            if current == self.head:
                break

        # The old tail becomes the new head
        self.head, self.tail = self.tail, self.head

    # 14. Clear the list
    def clear(self):
        self.head = None
        self.tail = None


cdll = CircularDoublyLinkedList()

# Insert at the end
cdll.insert_at_end(10)
cdll.insert_at_end(20)
cdll.insert_at_end(30)

print("Forward:")
cdll.display_forward()

print("\nBackward:")
cdll.display_backward()