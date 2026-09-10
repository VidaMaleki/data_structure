class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The previous node must not be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Usage:
sll = SinglyLinkedList()
sll.add_to_first(1)
sll.add_to_end(3)
sll.insert_after(sll.head, 2)
sll.print_list()