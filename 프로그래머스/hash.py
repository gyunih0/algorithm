from typing import List

# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def phone(phone_book: List) -> bool:
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break

    return answer

    # 접두사에 없다면
