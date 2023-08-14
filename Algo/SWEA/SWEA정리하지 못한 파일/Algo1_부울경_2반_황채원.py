T = int(input())

di = [-1, 0, 1, 0] # 4방향을 모두 탐색
dj = [0, 1, 0, -1]

for t in range(1, T+1): # tc의 반복
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(t, N, arr)
    cnt = 0
    count = 0
    result = 0

    # arr을 돌면서, 상하좌우보다 값이 크면, result에 값을 더해줌
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:
                    count = 0
                    if arr[i+di[k]][j+dj[k]]:
                        count += 1
                        if arr[i][j] > arr[i+di[k]][j+dj[k]]:
                            cnt += 1
                        elif arr[i][j] == arr[i+di[k]][j+dj[k]]:
                            break
                        else:
                            break

            if cnt == count:
                result += 1

        print(f'#{t} {result}')