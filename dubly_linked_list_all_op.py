
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
        index = 0

        while current is not None and index < position:
            current = current.next
            index += 1

        if current is None:
            if index == position:
                self.insert_at_end(data)
                return
            raise IndexError("Position out of range")

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

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    # 5. Delete from the end
    def delete_from_end(self):
        if self.tail is None:
            raise IndexError("List is empty")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    # 6. Delete at a given position (zero-indexed)
    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Invalid position")

        if self.head is None:
            raise IndexError("List is empty")

        if position == 0:
            self.delete_from_beginning()
            return

        current = self.head
        index = 0

        while current is not None and index < position:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Position out of range")

        if current == self.tail:
            self.delete_from_end()
            return

        current.prev.next = current.next
        current.next.prev = current.prev

    # 7. Search for a value
    # Returns its first position, or -1 if not found
    def search(self, value):
        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return position

            current = current.next
            position += 1

        return -1

    # 8. Update a value at a given position
    def update(self, position, new_data):
        if position < 0:
            raise IndexError("Invalid position")

        current = self.head
        index = 0

        while current is not None and index < position:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Position out of range")

        current.data = new_data

    # 9. Display from head to tail
    def display_forward(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    # 10. Display from tail to head
    def display_backward(self):
        current = self.tail

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")

    # 11. Get the number of nodes
    def size(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # 12. Check whether the list is empty
    def is_empty(self):
        return self.head is None

    # 13. Reverse the list in place
    def reverse(self):
        current = self.head

        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    # 14. Clear the list
    def clear(self):
        self.head = None
        self.tail = None


# Create a doubly linked list and perform operations

dll = DoublyLinkedList()

# Insert values
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

dll.display_forward()
# 10 <-> 20 <-> 30 <-> None

dll.display_backward()
# 30 <-> 20 <-> 10 <-> None

# Insert at the beginning
dll.insert_at_beginning(5)
# 5 <-> 10 <-> 20 <-> 30

# Insert 15 at index 2
dll.insert_at_position(15, 2)
# 5 <-> 10 <-> 15 <-> 20 <-> 30

# Search
print(dll.search(20))  # 3
print(dll.search(99))  # -1

# Update the value at index 2
dll.update(2, 17)
# 5 <-> 10 <-> 17 <-> 20 <-> 30

# Delete at index 1
dll.delete_at_position(1)
# 5 <-> 17 <-> 20 <-> 30

# Delete from beginning and end
dll.delete_from_beginning()
dll.delete_from_end()
# 17 <-> 20

print(dll.size())      # 2
print(dll.is_empty())  # False

# Reverse
dll.reverse()
dll.display_forward()
# 20 <-> 17 <-> None

# Clear everything
dll.clear()
print(dll.is_empty())  # True