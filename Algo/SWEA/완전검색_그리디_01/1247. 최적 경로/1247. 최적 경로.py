import sys
sys.stdin = open('input.txt')

MIN = float('inf')

def min_distance(i, j, visit):
    global MIN
    if visit == N + 2:
        print(MIN)
        return
    else:
        measure = abs(x[i] - x[j]) + abs(y[i] - y[j])
        if MIN > measure:
            MIN = measure
        min_distance(i + 1, i, visit + 1)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    destination = list(map(int, input().split()))

    x = []
    y = []
    distance = 0

    # print(N, distance)
    for i in range((N + 2) * 2):
        if i == 0:
            x.append(destination[i])
        elif i % 2 == 0:
            x.append(destination[i])
        else:
            y.append(destination[i])

    # print(t, x, y)
    min_distance(0 ,0, 0)
    # print(MIN)

    print(f'#{t} {distance}')