import sys
sys.stdin = open('input.txt')
# 다양한 풀이가 존재할 수 있음 (구현, DP, 백트레킹 etc)
# 문제 이해도가 쉬움

def shift_nums(nums, i, exchange):
    if i == exchange:
        return nums
    else:
        MAX = 0
        for j in range(len(nums)):
            if MAX == nums[j]:
                index = j
            elif MAX < nums[j] and nums[0] != nums[j]:
                MAX = nums[j]
                index = j

        if 0 <= index < len(nums):
            nums.insert(index, 0)
            pop_num = nums.pop(0)
            nums.insert(0, MAX)
            nums[index] = pop_num
            nums.pop(index + 1)
            i += 1
            return shift_nums(nums, i, exchange)

T = int(input())

for t in range(1, T+1):
    str_nums, str_exchange = input().split()

    exchange = int(str_exchange)
    nums = list(map(int, str_nums))

    shift_nums(nums, 0, exchange)

    result = ''.join(map(str, nums))
    print(f'#{t} {result}')