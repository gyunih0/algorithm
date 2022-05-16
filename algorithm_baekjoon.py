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


input_count = int(input())
result = stack_sequence(input_count)

if result['is_correct'] == False:
    print('NO')
else:
    for i in result['status']:
        print(i)

