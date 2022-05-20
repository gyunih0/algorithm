
def fibo(n):

     # 종료조건
    if n < 3:
        return 1
    else:
        # 앞의 두 항의 함이 다음 항의 값이 된다.
        return fibo(n-1) + fibo(n-2)

def move_disk(num, start, end):
    print('{}번 원판을 {}에서 {}로 옮긴다.'.format(num, start, end))


def hanoi(num, start_peg, end_peg):
    hanoi_sub(num, start_peg, end_peg, 2)


def hanoi_sub(N, start_peg, end_peg, other_peg):
    if N == 1:
        move_disk(1, start_peg, end_peg)

    else:
        hanoi_sub(N-1, start_peg, other_peg, end_peg)
        move_disk(N, start_peg, end_peg)
        hanoi_sub(N-1, other_peg, end_peg, start_peg)

hanoi(3,1,3)


