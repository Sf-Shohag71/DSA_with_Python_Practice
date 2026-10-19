class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
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

    # 4. Delete from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        self.head = self.head.next

        # Python automatically handles memory cleanup
        del temp

    # 5. Delete from the end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head

        # Find the second-last node
        while current.next.next is not None:
            current = current.next

        current.next = None

    # 6. Delete from a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position < 0:
            print("Invalid position")
            return

        # Delete first node
        if position == 0:
            self.delete_from_beginning()
            return

        current = self.head

        # Move to the node before target
        for _ in range(position - 1):
            if current is None:
                print("Position out of range")
                return

            current = current.next

        if current is None or current.next is None:
            print("Position out of range")
            return

        temp = current.next

        current.next = temp.next

        del temp

    # 7. Search for a value
    def search(self, value):
        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return position

            current = current.next
            position += 1

        return -1

    # 8. Update a node
    def update(self, position, new_data):
        if position < 0:
            print("Invalid position")
            return

        current = self.head

        for _ in range(position):
            if current is None:
                print("Position out of range")
                return

            current = current.next

        if current is None:
            print("Position out of range")
            return

        current.data = new_data

    # 9. Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # 10. Count the number of nodes
    def size(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # 11. Reverse the linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    # 12. Delete all nodes
    def clear(self):
        self.head = None

    # 13. Check whether list is empty
    def is_empty(self):
        return self.head is None


# ==========================================
# Example usage
# ==========================================

if __name__ == "__main__":

    linked_list = SinglyLinkedList()

    # Insert at beginning
    linked_list.insert_at_beginning(30)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(10)

    print("After inserting at beginning:")
    linked_list.display()

    # Insert at end
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    print("\nAfter inserting at end:")
    linked_list.display()

    # Insert at position
    linked_list.insert_at_position(25, 2)

    print("\nAfter inserting 25 at position 2:")
    linked_list.display()

    # Search
    position = linked_list.search(40)

    print("\nPosition of 40:", position)

    # Update
    linked_list.update(2, 100)

    print("\nAfter updating position 2 to 100:")
    linked_list.display()

    # Delete from beginning
    linked_list.delete_from_beginning()

    print("\nAfter deleting from beginning:")
    linked_list.display()

    # Delete from end
    linked_list.delete_from_end()

    print("\nAfter deleting from end:")
    linked_list.display()

    # Delete at position
    linked_list.delete_at_position(1)

    print("\nAfter deleting position 1:")
    linked_list.display()

    # Size
    print("\nSize of list:", linked_list.size())

    # Reverse
    linked_list.reverse()

    print("\nAfter reversing:")
    linked_list.display()

    # Check empty
    print("\nIs list empty?", linked_list.is_empty())