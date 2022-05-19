import collections
from typing import List


# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909
def is_vps(s: str) -> bool:
    stack = []
    opener = '('

    for char in s:
        if char is opener:
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


# 주식 가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
def stock_price(prices: List[int]) -> List[int]:

    stack = []
    answer = [0]*len(prices)

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer


# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

def printer(priorities: List[int], location: int) -> int:
    answer = 0
    from collections import deque

    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


    # answer = 0
    # q = collections.deque([(i,v) for i,v in enumerate(priorities)])
    #
    # while q:
    #     item = q.popleft()
    #     if q and max()

def printer_2(priorities: List[int], location: int) -> int:
    queue = collections.deque([(i, p) for i,p in enumerate(priorities)])
    answer = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer +=1
            if cur[0] == location:
                return answer



#
# priorities = [2, 1, 3, 2]
# location = 2
# print(printer_2(priorities, location))
# print(printer(priorities, location))

# 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

def max_min(s: str) -> str:
    l = list(map(int, s.split(' ')))
    answer = '{} {}'.format(min(l), max(l))
    return answer

# test = "1 2 3 4"
# print(max_min(test))

# 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def progress(progresses: List[int], speeds: List[int]):

    # 입력 List를 Deque로 형변환
    progressQ = collections.deque(progresses)
    speedQ = collections.deque(speeds)

    answer = []
    day = 0
    count = 0  # 한번에 완료되는 누적 count
    while len(progressQ):  # 일이 남아 있는 동안
        # day ++ 해주면서 가장 앞작업이 100을 넘긴다면 -> progressQ, speedQ를 popleft()해주고
        # count ++ 해준다

        if progressQ[0] + speedQ[0] * day >= 100:  # 가장 앞작업 완료 할 때
            progressQ.popleft()
            speedQ.popleft()
            count += 1
        else:
            if count > 0:
                # count 초기화
                answer.append(count)
                count = 0
            day += 1

    answer.append(count)  # 마지막 count 추가
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]


print(progress(progresses, speeds))

def progress_2(progresses: List[int], speeds: List[int]):

    complete = [0] * len(progresses)
    answer = []
    while len(progresses):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        i = 0
        while i < len(progresses):
            print(i, complete)
            if progresses[i] >= 100:
                complete[i] += 1
            i += 1

        count = 0
        for temp in complete:
            if temp != 0:
                count += 1
            if count == len(complete):
                temp = 0
                for i in range(len(complete) - 1):
                    if complete[i] < complete[i + 1]:
                        temp += 1
                    else:
                        answer.append(temp)
                        temp = 0


                # return complete



        print(answer)


print(progress_2(progresses, speeds))