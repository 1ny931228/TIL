import sys
sys.stdin = open('sample_input.txt')

T = int(input())
di = [-1, 0, 1, 0]

def find_way(x, y):
    for x in range(N):
        for y in range(N):
            if 0 <= x < N and 1 <= y < N-1:
                if MAP[x][y] =='1':
                    return 0

                if MAP[0][y] == '3':
                    return 1

                if
                else:
                    return 0

for t in range(1, T+1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]

    # print(t, N, MAP)

    for i in range(N):
        for j in range(N):
            print(MAP[i][j] == 2)

            result = find_way(i, j)


    print(f'#{t} {result}')
