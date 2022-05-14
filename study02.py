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

    def Aprint(self):
        print("[", end="")
        current = self.head
        while current.next is not None:
            if str(type(current.data)) == "<class 'str'>":
                print(f"'{current.data}',", end="")
                current = current.next
                continue
            print(f"{current.data},", end="")
            current = current.next
        if str(type(current.data)) == "<class 'str'>":
            print(f"'{current.data}']")
        else:
            print(f"{current.data}]")




def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 정렬하기 위한 배열
    l = []

    # 데이터 배열에 담기
    while l1:  # linkedlist1
        l.append(l1.val)
        l1 = l1.next
    while l2:  # linkedlist2
        l.append(l2.val)
        l2 = l2.next

    node = None
    result = None
    # [1,1,2,3,4]
    # [1,1
    for val in sorted(l):  #값이들어있는 리스트를 정렬해서
        # node가 없을 때(빈 연결리스트이기 때문에), 새로운 node를 생성하고 result에 담는다.
        if not node:
            node = ListNode(val)
            result = node
        # node가 있을 때, 현재 node의 다음 node에 새로운 node를 생성하고 현재 node와 연결해준다.
        else:

            node.next = ListNode(val)
            node = node.next

    return result


l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2, 3, 4]:
    l2.append(num)


mergeTwoLists()