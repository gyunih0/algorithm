# 프로그래머스 - 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238
import math


def done(mid, times):
    people = 0

    for time in times:
        people += mid // time

    return people


def solution(n, times):
    answer = 0
    left, right = 0, math.ceil(n/len(times)) * max(times)

    while left <= right:

        mid = (left + right) // 2
        done_ppl = done(mid, times)

        if done_ppl < n:
            left = mid + 1

        else:
            answer = mid
            right = mid - 1

    return answer

n = 6
times = [7, 10]

print(solution(n, times))
