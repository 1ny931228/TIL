import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_catch = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_catch = 0
            for k in range(M):
                for l in range(M):
                    sum_catch += grid[i+k][j+l]
                if max_catch < sum_catch:
                    max_catch = sum_catch

    print(f'#{t} {max_catch}')

