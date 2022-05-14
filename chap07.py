from typing import List

# 9 - 1 Brute-Force
def threeSum1(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # 브루트 포스
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results

# 9 - 2 two pointer
def threeSum2(nums: List[int]) -> List[int]:
    results = []
    nums.sort()
    print(nums)

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1

            else:  # 정답 추가 및 중복 스킵
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return results


def threeSum2_set(nums: List[int]) -> List[int]:
    results = []
    nums = list(set(nums))
    nums.sort()

    print(nums, len(nums))

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1

            else:  # 정답 추가 및 중복 스킵

                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return results


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum1(nums))
print(threeSum2(nums))
print(threeSum2_set(nums))

# 10 - 1 pair 생성해서 합 구하기
def arrayPairSum1(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for num in nums:
        pair.append(num)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


# 10 - 2 짝수 번째 수의 합 (0부터 시작)
def arrayPairSum2(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):  # i = index, n = num
        if i % 2 == 0:
            sum += n

    return sum

# 10 - 3 Using python method
def arrayPairSum3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

nums = [1, 4, 3, 2]
print(arrayPairSum1(nums))
print(arrayPairSum2(nums))
print(arrayPairSum3(nums))



test = [1, 1, 2, 3]
test = set(test)
test_list = list(test)
print(test_list)