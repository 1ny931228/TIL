di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

for t in range(1, int(input())+1):
    N, P = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # print(t, N, P, grid)

    kill_v = []

    for i in range(N):
        for j in range(N):
            SUM = grid[i][j]
            for k in range(4):
                for l in range(1, P+1):
                    ni = i + l * di[k]
                    nj = j + l * dj[k]
                    if 0 <= ni < N and 0 <= nj <N:
                        SUM += grid[ni][nj]
            kill_v.append(SUM)
    kill_v.sort()

    ans = kill_v[-1]

    print(f'#{t} {ans}')