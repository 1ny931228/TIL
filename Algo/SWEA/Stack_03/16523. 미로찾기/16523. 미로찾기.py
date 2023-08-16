import sys
sys.stdin = open('sample_input.txt')

def find_way(x,y):

    if arr[0][y] == '3':
        return 0

    if arr[N-1][y] == '2':
        try_up = find_way(x-1, y)
        if try_up == '0':
            return try_up
        elif try_up == '1':
            try_east = find_way(x, y+1)
            if try_east == '0':
                return try_east
            elif try_east == '1':
                try_west = find_way(x, y-1)
                return try_west
                if try_west == '0':
                    return try_west
                else:
                    return try_up

    else:
        return 1

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # print(t, N, arr)

    result = 1
    for i in range(N):
        for j in range(N):
            if 0 <= i < N and 0 <= j < N:
                print(find_way(i, j))


    # print(f'#{t} {result}')