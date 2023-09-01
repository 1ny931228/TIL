import sys
sys.stdin = open('sample_input(2).txt')

# (0,0)에서 우, 하 둘 중 하나로 갈 예정이다. 우측이나 아래 방향 중 작은 숫자로 이동하자
# grid를 벗어나지 않게 범위를 정해줘야한다.

def min_way(grid, i, j):
    if i == N - 1 and j == N - 1: # 도착점에 도착했을 때
        return grid[i][j]

    if i + 1 < N and j + 1 < N:
        right_sum = min_way(grid, i, j + 1)
        down_sum = min_way(grid, i + 1, j)
        return grid[i][j] + min(right_sum, down_sum)
    elif i + 1 < N:
        return grid[i][j] + min_way(grid, i + 1, j)
    elif j + 1 < N:
        return grid[i][j] + min_way(grid, i, j + 1)
    else:
        return float('inf')


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = min_way(grid, 0, 0)

    print(f'#{t} {result}')