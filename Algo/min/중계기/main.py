T = int(input())

for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N+1)]

    repeater_dot = []
    home_dot = []

    for i in range(N+1):
        for j in range(N+1):
            if grid[i][j] == 2:
                (y, x) = i, j
                repeater_dot.append((y, x))
            elif grid[i][j] == 1:
                (hy, hx) = i, j
                home_dot.append((hy, hx))

    # print(repeater_dot, home_dot)
    MAX = 0

    for y, x in repeater_dot:
        for hy, hx in home_dot:
            D = (hy - y) ** 2 + (hx - x) ** 2
            # print(f'{t} {D}')
            if D > MAX:
                MAX = D
    result = int(-(- MAX ** 0.5 // 1))

    print(f'#{t} {result}')

