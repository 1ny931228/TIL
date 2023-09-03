import sys
sys.stdin = open('input.txt')

nums = list(map(int, list(input())))

# print(nums)

SUM = 0

for num in nums:
    SUM += num

print(SUM)