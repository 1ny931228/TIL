import sys
sys.stdin = open('input1.txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    pang_list = []

    for i in range(N):
        for j in range(M):
            total = 0
            for d in range(-1, 2):
                if 0 <= i + d < N:
                    total += grid[i + d][j]
                if 0 <= j + d < M:
                    total += grid[i][j + d]
            total -= grid[i][j]
            pang_list.append(total)
    result = max(pang_list)

    print(f'#{t} {result}')