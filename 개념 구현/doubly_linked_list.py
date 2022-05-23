from typing import List

class Node:
    def __init__(self, item, next = None, prev = None):
        self.item = item
        self.next = next
        self.prev = prev



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def insert_start(self, item):

        new_node = Node(item)
        if self.is_empty():

            self.head = new_node
            self.tail = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head

            self.tail = self.head
            self.head = new_node

    def insert_end(self, item):
        new_node = Node(item)
        self.tail.next = new_node
        new_node.prev = self.tail.next

        self.tail = new_node

    def print_all(self):
        if self.is_empty():
            return False

        result = '[head] '
        node = self.head

        while node:
            if not node.next:
                result += '[' + str(node.item) + '] [tail]'

            else:
                result += ('[' + str(node.item) + ']' + '<->')
            node = node.next

        print(result)


test = DoublyLinkedList()

test.insert_start(1)
test.insert_end(2)


test.print_all()