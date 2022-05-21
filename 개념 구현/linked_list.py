from typing import List


class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next


# single linkedlist
# insert_start / insert_end / insert_after / delete_start / delete_end / delete_after
# is_empty(?) / print_all
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False

        return True

    def insert_start(self, item):
        if self.is_empty():
            self.head = Node(item)
            return

        else:
            start = self.head
            self.head = Node(item)
            self.head.next = start

    def insert_end(self, item):  # insert_start / insert_end
        if self.is_empty():
            self.head = Node(item)
            return

        node = self.head

        while node.next:
            node = node.next

        node.next = Node(item)

    def delete_start(self):  # delete
        if self.is_empty():
            return False

        self.head = self.head.next

    def delete_end(self):
        if self.is_empty():
            return False

        node = self.head

        while node:
            node = node.next
            pass

    def print_all(self):
        if not self.head:
            return False

        result = ''
        node = self.head

        while node:
            if not node.next:
                result += str(node.item)
            else:
                result += (str(node.item) + '->')
            node = node.next

        print(result)





test  = LinkedList()

test.insert_start(1)
test.insert_start(2)
test.insert_end(3)
test.print_all()
test.delete_start()
test.print_all()

test.delete_end()