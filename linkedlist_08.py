import collections
from typing import List, Deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)



def isPalindrome(head: ListNode) -> bool:
    arr = []

    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    while len(arr) > 1:
        if arr.pop(0) != arr.pop():
            return False

    return True


def isPalindrome2(head: ListNode) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True




# 8 15 reverse-linked-list
def reverseList(head: ListNode) -> ListNode:

    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            print(prev.val)
            return prev

        ndext, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

# Test Code


l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2, 3, 4]:
    l2.append(num)


# assert isPalindrome(l1.head)
# assert not isPalindrome(l2.head)

reverseList(l2.head)
