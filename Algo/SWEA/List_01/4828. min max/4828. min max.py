import sys
sys.stdin = open('sample_input.txt')

for t in range(1, int(input())+1):
    input()
    nums_list = list(map(int, input().split()))

    nums_list.sort()

    ans = nums_list[-1] - nums_list[0]

    print(f'#{t} {ans}')