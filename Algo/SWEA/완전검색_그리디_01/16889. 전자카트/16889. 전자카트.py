import sys
sys.stdin = open('sample_input(1).txt')
# min_energy를 찾는 재귀함수
def find_min_energy(MAP, N, cnt, min_energy, visited):
    if cnt == N:
        return min_energy

    min_val = float('inf')

    for i in range(N):
        if i not in visited:
            for j in range(N):
                if MAP[i][j] < min_val and MAP[i][j] != 0:
                    min_val = MAP[i][j]
                    next_visited = visited.copy()
                    next_visited.add(i)
                    next_energy = min_energy + min_val
                    next_map = [row[:] for row in MAP]
                    set_to_zero(next_map, j)
                    result = find_min_energy(next_map, N, cnt + 1, next_energy, next_visited)
                    min_energy = min(min_energy, result)

    return min_energy

# 특정열을 0으로 만드는 함수
def set_to_zero(MAP, col_index):
    for row in MAP:
        row[col_index] = 0

# 2번째로 작은 수 찾기
def find_second_smallest(row):
    smallest = float('inf')  # 무한대로 초기화
    second_smallest = float('inf')  # 무한대로 초기화

    for num in row:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest

T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # print(t, N, MAP)
    min_energy = float('inf')
    visited = set()

    result = find_min_energy(MAP, N, 0, 0, visited)

    print(f'#{t} {result}')



