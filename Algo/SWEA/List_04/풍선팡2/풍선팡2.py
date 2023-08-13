import sys
sys.stdin = open('input1.txt')

T = int(input())

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    MAX = 0

    for i in range(N):
        for j in range(M):
            SUM = 0
            SUM += arr[i][j]
            for k in range(4):
                if 0 <= i + di[k] < N and 0 <= j + dj[k] < M:
                    SUM += arr[i + di[k]][j + dj[k]]
                    if SUM > MAX:
                        MAX = SUM

    print(f'#{t} {MAX}')