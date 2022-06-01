# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
# not yet
def solution(gems):
    dic = {}
    gem_type = set(gems)

    start = end = 0


    while end < len(gems):
        if gems[end] not in dic:
            dic[gems[end]] = 1
        else:
            dic[gems[end]] += 1
        end += 1

        if len(dic) == len(gem_type):
            while start < end:
                if dic[gems[start]] > 1:
                    dic[gems[start]] -= 1
                    start += 1

                else:
                    break

    answer = [start + 1, end + 1]

    return answer
    # # end 설정
    # while len(dic) < len(gem_type):
    #
    #     if gems[end] not in dic:
    #         dic[gems[end]] = 1
    #
    #     else:
    #         dic[gems[end]] += 1
    #
    #     end += 1
    # print(dic)
    #
    # # start 설정
    # while start < end:
    #     dic[gems[start]] -= 1
    #     if dic[gems[start]] == 0:
    #         break
    #
    #     start += 1
    #
    # answer = [start+1, end]
    # print(dic)
    #
    # return answer


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])