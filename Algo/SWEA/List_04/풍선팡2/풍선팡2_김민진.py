T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    pollen_list = []

    for i in range(N):
        for j in range(M):
            total = 0

            for d in range(-1, 2):
                if 0 <= i + d < N:
                    total += arr[i + d][j]
                if 0 <= j + d < M:
                    total += arr[i][j + d]

            total -= arr[i][j]
            pollen_list.append(total)

    print(f'#{t} {max(pollen_list)}')