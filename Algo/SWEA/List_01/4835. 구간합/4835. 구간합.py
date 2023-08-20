import sys
sys.stdin = open('sample_input(2).txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums_list = list(map(int, input().split()))

    # print(t, N, M, nums_list)

    sum_list = []

    for i in range(N-M+1):
        k = i + M
        SUM = 0
        for l in nums_list[i:k]:
            SUM += l
        sum_list.append(SUM)

    ans = max(sum_list) - min(sum_list)
    print(f'#{t} {ans}')
