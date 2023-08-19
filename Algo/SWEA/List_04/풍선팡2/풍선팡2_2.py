import sys
sys.stdin = open('input1.txt')

di = [-1, 0, 1, 0] # d = [(0,1), (1,0), (0,-1), (-1,0)]
dj = [0, 1, 0, -1]

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    MAX = 0 # max_pang = 0
    # 완전 탐색
    for i in range(N):
        for j in range(M):
            SUM = 0
            SUM += grid[i][j]
            for k in range(4): # for dx, dy in direction: ni, nj = i + dx, j + dy
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    SUM += grid[ni][nj]
                if MAX < SUM:
                    MAX = SUM

    print(f'#{t} {MAX}')