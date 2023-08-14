T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    MAX = MIN = sum(lst[:M])

    for i in range(N):
        if MAX < sum(lst[i:i+M]):
            MAX = sum(lst[i:i+M])
        if MIN > sum(lst[i:i+M]):
            MIN = sum(lst[i:i+M])

    result = MAX - MIN

    print(f'#{t} {result}')
