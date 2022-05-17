from typing import List
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None
        self.len = 0

    def push(self, item):
        self.last = Node(item, self.last)
        self.len += 1

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

# for _ in range(stack.len):
#     print(stack.pop())


# 9 - 20
def is_stack_mine(s: str) -> bool:
    stack = []
    pair = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    openers = '({['
    closers = ')}]'
    for char in s:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if stack:
                opener = stack[-1]
                if pair[opener] == char:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False
    else:
        return True


def is_stack(s: str) -> bool:
    stack = []
    pair = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in pair:
            stack.append(char)
        elif not stack or pair[char] != stack.pop():
            return False

    return len(stack) == 0


# test = input()
# print(is_stack(test))


# 9 - 21

def removeDuplicateLetters(s: str) -> str:
    stack = []


    print(s)
test1 = 'bcabc'
test2 = 'cbacdcbc'
removeDuplicateLetters(test2)
# 9 - 22 Daily Temperatures

def dailyTemperatures(T: List[int]) ->List[int]:
    result = [0]*len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result

# T = [73, 74, 75, 71, 69, 72, 76, 73]
# print(dailyTemperatures(T))


