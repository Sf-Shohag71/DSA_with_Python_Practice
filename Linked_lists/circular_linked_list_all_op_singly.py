class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current = self.head

        if not self.head:
            # List is empty
            new_node.next = new_node
            self.head = new_node
        else:
            if current.next != self.head:
                # Traverse linked list at the end
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def traverse(self):
        current = self.head
        if not self.head:
            print("Circular linked list is empty!!")
            return
        
        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                print("head:",current.data)
                # Reach the head again
                break


cli = CircularSinglyLinkedList()
cli.append(4)
cli.append(2)
cli.append(10)
cli.append(15)
cli.append(5)
cli.traverse()
            

