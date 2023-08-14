"""#1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1): # i 구간의 마지막 인덱스
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}', *arr)

#input() 1 1줄씩 입력받는다
#input() 2 str 문자열으로 받는다.

#2
T = int(input())    # 테스트케이스 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = 1000000
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]

    ans = max_v - min_v
    print(f'#{tc} {ans}')

#3 minmax
T = int(input())    # 테스트케이스 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    max_v = arr[0]
    min_v = 1000000
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]

    ans = max_v - min_v
    print(f'#{tc} {ans}')

# 3
T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    min_id = 0 # 최소값의 인덱스
    max_id = 0

    for i in range(1, N):
        if lst[min_id] > lst[i]:
            min_id = i
        if lst[max_id] <= lst[i]:
            max_id = i

    abs(max_id - min_id)

    ans = max_id - min_id
    if ans < 0:
        ans * -1
    else:
        ans

# 4 9386
T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = input().split('0')

# 5 view
T = int(input())

for t in range(1, T+1):
    lst = list(map(int, input().split()))
    N = len(lst)

    for i in range(2, N-2):
        if lst[i] > lst[i-2] and lst[i] > lst[i-1] and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
            max_height = lst[i]
            for j in range(-2, 3):
                if j == 0:
                    continue
                if lst[i-j] > max_height:
                    max_height = lst[i-j]
            result += buildingHeight[i] - max_height

    print(f'#{t}{result}')
"""

 # 4835
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_lst = lst[0:M]
    sum_min = sum(sum_lst)
    sum_max = sum(sum_lst)

    for i in lst:
        if sum_min > sum(lst[i:i + M - 1]):
            sum_min = sum(lst[i:i + M - 1])
        if sum_max < sum(lst[i:i + M - 1]):
            sum_max = sum(lst[i:i + M - 1])

    ans = sum_max - sum_min

    print(f'#{t} {ans}')