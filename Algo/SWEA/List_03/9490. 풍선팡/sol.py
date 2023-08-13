import sys
sys.stdin = open('input1.txt')

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(t, N, M, arr)
    MAX = 0

    for i in range(N):
        for j in range(M):
            SUM = arr[i][j]
            # print(SUM, 1)
            for k in range(4):
                for l in range(1, arr[i][j] + 1):
                    if 0 <= i + l * di[k] < N and 0 <= j + l * dj[k] < M:
                        # print(i + l * di[k], j + l * dj[k])
                        SUM += arr[i + l * di[k]][j + l * dj[k]]
                    if SUM > MAX:
                        MAX = SUM

    print(f'#{t} {MAX}')


