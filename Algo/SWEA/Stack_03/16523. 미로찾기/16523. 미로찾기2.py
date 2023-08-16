import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def find_way(x, y):
    for x in range(N):
        for y in range(N):
            if 0 <= x < N and 1 <= y < N-1:
                if MAP[0][y] == '3':
                    return 1

                if MAP[N-1][y] == '2':
                    try_up = find_way(x-1, y)
                    if try_up == '0':
                        return try_up
                    else:
                        try_east = find_way(x, y+1)
                        if try_east == '0':
                            return try_east
                        else:
                            try_west = find_way(x, y-1)
                            if try_west == '0':
                                return try_west
                            else:
                                return 0
                else:
                    return 0

for t in range(1, T+1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]

    # print(t, N, MAP)

    for i in range(N):
        for j in range(N):
            result = find_way(i, j)


    print(f'#{t} {result}')
