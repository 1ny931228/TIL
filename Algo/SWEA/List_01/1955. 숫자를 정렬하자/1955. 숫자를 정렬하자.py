import sys
sys.stdin = open('input (1).txt')

for t in range(1, int(input())+1):
    input()
    nums_list = list(map(int, input().split()))

    # print(t, nums_list)

    nums_list.sort()

    print(f'#{t}', *nums_list)

