import sys
sys.stdin = open('sample_input(2)(1).txt')

for t in range(1, int(input())+1):
    colors = int(input())
    color_grid = [list(map(int, input().split())) for _ in range(colors)]

    grid = [[0] * 10 for _ in range(10)]

    # print(color_grid[-1][-1])
    cnt = 0

    for cg in color_grid:
        i, j = cg[0], cg[1]
        k, l = cg[2], cg[3]
        if cg[-1] == 1:
            for a in range(i, k+1):
                for b in range(j, l+1):
                    grid[a][b] += 1

        else:
            for a in range(i, k + 1):
                for b in range(j, l + 1):
                    grid[a][b] += 2

    for a in range(10):
        for b in range(10):
            if grid[a][b] == 3:
                cnt += 1

    print(f'#{t} {cnt}')
