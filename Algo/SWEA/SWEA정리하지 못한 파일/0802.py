T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    MAX = MIN = lst[0]
    MAX_index = MIN_index = 0

    for i in range(N):
        if lst[i] > MAX:
            MAX = lst[i]
            for j in range(N):
                if MAX == lst[j]:
                    if i < j:
                        MAX_index = j
                    else:
                        MAX_index = i
        if lst[i] < MIN:
            MIN = lst[i]
            for j in range(N):
                if MIN == lst[j]:
                    if i < j:
                        MIN_index = i
                    else:
                        MIN_index = j

    result = MAX_index - MIN_index
    print(f'#{t} {result}')