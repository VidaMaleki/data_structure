class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def delete_first(self):
        if self.head is None:
            print("The list is empty.")
            return
        self.head = self.head.next

    def delete_after(self, prev_node):
        if prev_node is None or prev_node.next is None:
            print("The previous node is None or it has no next node.")
            return
        prev_node.next = prev_node.next.next

    def delete_last(self):
        if self.head is None:
            print("The list is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

# Usage:
# sll = SinglyLinkedList()
# # ... (add some elements)
# sll.delete_first()
# sll.delete_after(sll.head)
# sll.delete_last()
# sll.print_list()