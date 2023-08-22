T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split()) # N : Sample의 길이, K : PassCode의 길이
    Sample = list(map(int, input().split()))
    PassCode = list(map(int, input().split()))
    # print(t, N, K, Sample, PassCode)

    make_it = 1
    Perfect_index = []

    for i in range(K):
        for j in range(N):
            if PassCode[i] == Sample[j]:
                Perfect_index.append(j)
                break


    print(Perfect_index)
    for k in range(len(Perfect_index)):
        if 0 <= k < len(Perfect_index) - 1:
            if Perfect_index[k] > Perfect_index[k + 1]:
                make_it = 0

    print(f'#{t} {make_it}')