import sys
sys.stdin = open('input1.txt')

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_pang = 0

    for i in range(N):
        for j in range(M):
            SUM = grid[i][j]
            a = grid[i][j]
            for k in range(1, a+1):
                for dx, dy in direction:
                    ni = i + k * dx
                    nj = j + k * dy
                    if 0 <= ni < N and 0 <= nj < M:
                        SUM += grid[ni][nj]
                        if SUM > max_pang:
                            max_pang = SUM

    print(f'#{t} {max_pang}')
