from typing import List

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


def stock_price(prices: List[int]) -> List[int]:
    pass


