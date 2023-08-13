import sys
sys.stdin = open('sample_input(2)(1).txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(t, N, arr)


    MAP = [[0] * 10 for _ in range(10)]
    # print(MAP)

    for i in range(N):
        x, y = arr[i][0], arr[i][1]
        k, l = arr[i][2], arr[i][3]
        if arr[i][-1] == 1:
            for a in range(x, k+1):
                for b in range(y, l + 1):
                    MAP[a][b] += 1
                    # print(MAP, 1)
        elif arr[i][-1] == 2:
            for a in range(x, k+1):
                for b in range(y, l + 1):
                    MAP[a][b] += 2

    result = 0

    for i in range(10):
        for j in range(10):
            if MAP[i][j] == 3:
                result += 1

    print(f'#{t} {result}')