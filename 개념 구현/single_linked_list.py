from typing import List


class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next


# single linkedlist
# insert_start / insert_end / insert_after / delete_start / delete_end / delete_after
# is_empty(?) / print_all
# get_node
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False

        return True

    def get_node(self, index):
        count = 0
        node = self.head

        while count < index:
            count += 1
            node = node.next

        return node

    def insert_start(self, item):
        if self.is_empty():
            self.head = Node(item)
            return

        else:
            start = self.head
            self.head = Node(item)
            self.head.next = start

    def insert_end(self, item):

        node = self.head

        while node.next:
            node = node.next

        node.next = Node(item)

    def insert_after(self, index, item):

        new_node = Node(item)
        node = self.get_node(index)

        new_node.next = node.next
        node.next = new_node

    def delete_start(self):
        if self.is_empty():
            return False

        self.head = self.head.next

    def delete_end(self):
        if self.is_empty():
            return False

        node = self.head

        while node.next.next:
            node = node.next

        node.next = None

    def delete_after(self, index):

        node = self.get_node(index)
        node.next = node.next.next

    def print_all(self):
        if not self.head:
            return False

        result = ''
        node = self.head

        while node:
            if not node.next:
                result += '[' + str(node.item) + ']'
            else:
                result += ('[' + str(node.item) + ']' + '->')
            node = node.next

        print(result)


test = LinkedList()

test.insert_start(1)
test.insert_start(2)
test.insert_end(3)
test.insert_end(4)
test.print_all()

test.insert_after(1, 0)
test.print_all()

test.delete_after(1)
test.print_all()