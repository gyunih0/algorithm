from collections import deque
from typing import List, Dict

'''
baekjoon #9012
'''


def is_vps(vps: str) -> str:
    stack = []
    opener = '('

    for char in vps:
        if char is opener:  # char = '('
            stack.append(char)
        else:  # char = ')'
            if stack:
                stack.pop()
            else:  # )
                return 'NO'
    # check if stack is not empty
    if stack:
        return 'NO'
    else:
        return 'YES'


# num = int(input())
# for i in range(num):
#     vps = input()
#     print(is_vps(vps))


'''
baekjoon # 1874
'''

def stack_sequence(input_count: int) -> Dict:
    stack = []  # stack
    status = []  # + or -
    current = 1  # current number

    result = {'status': status,
              'is_correct': True}

    for i in range(input_count):
        num = int(input())

        while current <= num:
            stack.append(current)
            current += 1
            status.append('+')

        if stack[-1] == num:
            stack.pop()
            status.append('-')

        else:
            result['is_correct'] = False
            break

    result['stack'] = stack
    return result


# input_count = int(input())
# result = stack_sequence(input_count)
#
# if result['is_correct'] == False:
#     print('NO')
# else:
#     for i in result['status']:
#         print(i)


'''
baekjoon # 4949
'''

def is_balanced(s: str) -> bool:
    stack = []
    opener = '({['
    closer = ')}]'
    pair = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in opener:
            stack.append(char)

        elif char in closer:
            if stack[-1] == pair(char):
                stack.pop()
    return

# while True:
#     string = input()
#
#
#     if string == '.':
#         break


'''
baekjoon # 2164
'''

def test_problem_queue(num: int) -> int:
    queue = deque([i for i in range(1, num+1)])
    # print(queue)
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
        # print(queue)
    return queue.popleft()

# num = int(input())
# print(test_problem_queue(num))


'''
beakjoon # 1966
'''

test_cases = int(input())

for _ in range(test_cases):
    n, m = list(map(int, input().split(" ")))
    imp = list(map(int, input().split(" ")))
    idx = list(range(len(imp)))
idx[m] = 'target'

# 순서
order = 0

for x in imp:
    if x == max(imp):
        order += 1

        if idx[0] == 'target':
            print(order)
            break
        else:
            imp.pop(0)
            idx.pop(0)

    else:
        imp.append(imp.pop(0))
        idx.append(idx.pop(0))

