import math


def solution1(n, a, b):
    if a > b:  # a, b를 순서대로 정렬 -> pivot을 기준으로 값을 비교하기 위해서
        a, b = b, a

    while n >= 2:  # 가장 밑단의 리프 노드 수, a,b 두 사람이 라운드를 진행하기 때문에 2 이상이어야한다.
        pivot = (1 + n) / 2  # 중심선 설정

        if a < pivot < b:  # pivot이 a 와 b 사이에 있는 경우
            return math.log2(n)

        else:  # a, b 모두 pivot 앞으로
            if a > pivot and b > pivot:  # a, b 모두 pivot보다 뒤에 있는 경우
                a, b = a - int(pivot), b - int(pivot)  # pivot의 앞으로 대칭 이동 시켜준다.

            n = n / 2  # 반으로 줄이기


print(solution1(8, 4, 7))


def solution2(n, a, b):
    answer = 0
    while a != b:  # a = b 일 때 까지
        answer += 1  # 라운드 수

        # 다음 번호로 이동
        a = (a+1) // 2
        b = (b+1) // 2

    return answer

print(solution2(8, 4, 7))