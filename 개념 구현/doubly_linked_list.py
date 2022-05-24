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
        self.size = 0

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
            self.head.prev = new_node  # new_node <- head
            new_node.next = self.head  # new_node -> head

            self.tail = self.head
            self.head = new_node

            # tail <-> head
            self.head.prev = self.tail
            self.tail.next = self.head

            self.size += 1

    def insert_end(self, item):
        new_node = Node(item)

        new_node.next = self.head  # new_node -> head
        self.head.prev = new_node  # new_node <- head

        self.tail.next = new_node  # tail -> new_node
        new_node.prev = self.tail.next  # tail <- new_node

        self.tail = new_node

        self.size += 1

    def insert_after(self, index, item):

        new_node = Node(item)

        if index >= self.size:
            print('Out of Index')
            return False

        # if index >= self.size / 2:  # index 가 tail 쪽이면
        #     node = self.tail
        #     for _ in range(self.size - index):
        #         node = node.prev
        #
        #     new_node.next = node
        #     new_node.prev = node.prev
        #     node.prev.next = new_node
        #     node.prev = new_node

            # self.size += 1







    def print_all(self):
        if self.is_empty():
            return False

        result = '[head] '
        node = self.head

        for i in range(self.size + 1):
            if i == self.size:
                result += '[' + str(node.item) + '] [tail]'

            else:
                result += ('[' + str(node.item) + ']' + '<->')
            node = node.next

        print(result)


test = DoublyLinkedList()

test.insert_start(1)
test.insert_end(2)
test.insert_end(3)
test.insert_end(4)

test.insert_after(2, 0)
test.print_all()