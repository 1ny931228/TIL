import sys
sys.stdin = open('input1.txt')

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_pang = 9999999999

    for i in range(N):
        for j in range(M):
            sum_pang = 0
            sum_pang += grid[i][j]
            for dx, dy in direction:
                ni = dx + i
                nj = dy + j
                if 0 <= ni < N and 0 <= nj < M:
                    sum_pang += grid[ni][nj]
                    if min_pang > sum_pang:
                        min_pang = sum_pang
    print(f'#{tc} {min_pang}')


