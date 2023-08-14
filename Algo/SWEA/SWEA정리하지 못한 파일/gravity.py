T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    new_lst = sorted(lst)

    MAX = new_lst[-1]
    MAX_index = lst.index(MAX)

    for i in range(N):
        if MAX == lst[i]:
            result = N - MAX_index - i - 1
        else:
            result = N - MAX_index

    print(result)
    #
    # MAX = max(lst)
    # MAX_index = lst.index(MAX)
    #
    # next_MAX =
    # next_MAX_idex =
    # # print(f'#{t} {}')