class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def search(self, data):
        current = self.head
        position = 0
        while current is not None:
            if current.data == data:
                print(f"Found {data} at position {position}")
                return True
            current = current.next
            position += 1
        print(f"{data} not found")
        return False


ll = LinkedList()

ll.append(5)
ll.append(10)
ll.append(15)
ll.append(20)

print("Linked List: ")
ll.display()

print("\nSearch Element in the Linked List: ")
ll.search(11)
ll.search(20)
