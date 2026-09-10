class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_first(self):
        if self.head is None:
            print("The list is empty.")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def delete_node(self, del_node):
        if del_node is None or self.head is None:
            print("The node to be deleted is None or the list is empty.")
            return
        if del_node == self.head:
            self.head = del_node.next
        if del_node.next is not None:
            del_node.next.prev = del_node.prev
        if del_node.prev is not None:
            del_node.prev.next = del_node.next

    def delete_last(self):
        if self.head is None:
            print("The list is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next is not None:
            last = last.next
        if last.prev is not None:
            last.prev.next = None