class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Append nodes at the beginning
    def insert_at_begining(self, data):
        new_node = Node(data)

        # if list is empty
        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return

        # if list isn't empty
        new_node.next = self.head
        new_node.prev = self.tail
        self.head.prev = new_node
        self.tail.next = new_node
        self.head = new_node

    # Display forward
    def displayForward(self):
        if self.head is None:
            print("List is empty!!")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next

            if current == self.head:
                break

        print(f"(back to head: {current.data})")

cdll = CircularDoublyLinkedList()
cdll.insert_at_begining(10)
cdll.insert_at_begining(20)
cdll.insert_at_begining(30)
cdll.insert_at_begining(5)
cdll.displayForward()

