T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split()) # N : Sample의 길이, K : PassCode의 길이
    Sample = list(map(int, input().split()))
    PassCode = list(map(int, input().split()))
    # print(t, N, K, Sample, PassCode)

    make_it = 1
    Perfect_index = [0]
    cnt = 0 # 1. len 대신 시간 복잡도를 줄이기 위해서, cnt를 한다.

    for i in PassCode:
        for j in range(Perfect_index[-1], N): # 3. 처음부터 순회할 필요가 없으니, 찾은 인덱스 다음 값부터 찾자
            if i == Sample[j]:
                if not Perfect_index:
                    Perfect_index.append(j)
                    cnt += 1
                    break
                elif Perfect_index and Perfect_index[-1] < j:
                    Perfect_index.append(j)
                    cnt += 1
                    break
        else: # 4. j가 다 돌 때까지 i != Sample[j] 인 경우 나오는 탈출구를 만들어줘야함.
            break

        if cnt == K: # 2. 길이가 같으면 탈출함으로써, 시간 복잡도를 줄이는 방법
            break


    # print(Perfect_index)

    if K != cnt:
        make_it = 0

    print(f'#{t} {make_it}')