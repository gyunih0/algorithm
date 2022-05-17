from collections import deque


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, item):
        if not self.front:
            self.front = Node(item, None)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(item, None)

    def dequeue(self):
        if not self.front:
            return None

        node, self.front = self.front, self.front.next

        return node.item

    def is_empty(self):
        return self.front is None


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())


# 9 - 23 implement-stack-using-queues

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, item):
        self.q.append(item)

        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# q_stack = MyStack()
# q_stack.push(1)
# q_stack.push(2)
# q_stack.push(3)
#
# assert q_stack.pop() == 3

# 9 - 24 implement-queue-using-stacks
class MyQueue_mine:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print('before', self.stack)
        for i in range(len(self.stack)-1):
            self.stack[i], self.stack[-1] = self.stack[-1], self.stack[i]
            print('sorting', self.stack)
        print('After', self.stack)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def empty(self):
        return len(self.stack) == 0

# q = MyQueue_mine()
# q.push(1)
# q.push(2)
# q.push(3)
#
# print(q.pop())
# print(q.pop())
# print(q.pop())

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, item):
        self.input.append(item)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while not self.input:
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self):
        return self.output == [] and self.input == []

# 9 - 25

class CircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.q = [None] * size
        self.front = 0
        self.rear = 0


    def enqueue(self, item):
        if self.q[self.rear] is None:
            self.q[self.rear] = item
            print(self.rear, 'Enqueue')
            self.rear = (self.rear + 1) % self.size

        else:
            print("Full")

    def dequeue(self):
        if self.q[self.front]:
            self.q[self.front] = None
            print(self.front, 'Dequeue')
            self.front = (self.front + 1) % self.size

        else:
            print('No Item')


    def print(self):
        print(self.q, self.front, self.rear)



# q = CircularQueue(6)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.print()
# q.dequeue()
# q.print()
# q.dequeue()
# q.print()
# q.dequeue()
# q.print()
# q.enqueue(4)
# q.print()
# q.enqueue(5)
# q.enqueue(6)
# q.print()
# q.enqueue(7)
# q.print()
# q.enqueue(7)
# q.print()
# q.enqueue(7)
# q.print()
# q.enqueue(7)
# q.print()
# q.dequeue()
# q.print()



class MyQueue(object):
    def __init__(self):
        " 어떻게 class를 init 할 수 있을지 채워주세요 "
        self.q = []


    def peek(self):
        " 3번 기능(print)에 해당합니다. "
        if not self.q:
            return False
        return self.q[-1]

    def pop(self):
        " 2번 기능(dequeue)에 해당합니다. "
        return self.q.pop()

    def put(self, value):
        " 1번 기능(enqueue)에 해당합니다. "
        if not self.q:
            self.q.append(value)
        else:
            self.q.insert(0, value)


queue = MyQueue()
t = int(input())

for line in range(t):
    # test_case.txt 파일에 적혀있는 값이 줄 별로 읽혀집니다.
    # 예를 들어, 1 42는 ['1', '42'] 가 됩니다. map 함수는 1과 42에 각각 int 함수를 적용시킵니다.
    values = map(int, input().split())
    # 하지만 map 이 적용된 values는 바로 위의 기능을 수행하지 않습니다. 이때까지는 map object 형태입니다.
    # list가 적용되면 비로서 values 는 [1,42] 가 됩니다.
    values = list(values)

    # values[0]는 어떤 기능을 수행할지에 대한 값입니다.
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())