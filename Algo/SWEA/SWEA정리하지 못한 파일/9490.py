T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    row = N
    col = M

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    max_v = 0

    for i in range(row):
        for j in range(col):
            s = lst[i][j]
            for k in range(4):
                for s_v in range(1, lst[i][j] + 1):
                    ni, nj = i + s_v * di[k], j + s_v * dj[k]
                    if 0 <= ni < row and 0 <= nj < col:
                        s += lst[ni][nj]
                    if max_v < s:
                        max_v = s


    print(f'#{t} {max_v}')