# 4835
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_min = sum_max = sum(lst[:M])

    for i in lst:
        ind = lst.index(i)
        if sum_min > sum(lst[ind:ind+M]):
            sum_min = sum(lst[ind:ind+M])
        if sum_max < sum(lst[ind:ind+M]):
            sum_max = sum(lst[ind:ind+M])

    print(sum_max)
    print(sum_min)

    ans = sum_max - sum_min

    print(f'#{t} {ans}')

# 1208
T = 10

for t in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    max = 0
    min = 9999999

    m_lst = []

    for height in lst:
        if max < height:
            max = height

        if min > height:
            min = height
            # for _ in lst:
            #     max - 1 = min + 1
            #         if max - min <= 1:
            #             break

    dif = max - min
    print(dif)
    # print(f'#{t} {dif}')


    # 2001

    T = int(input())  # input뒤, print를 하면, 문자이기때문에 정수형으로 바꿔줘야 한다.

    for t in (1, T + 1):  # 우리는 답을 #1와 같은 형식으로 도출하기 위해서, 범위를 1부터 T+1로 지정한다.
        N, M = map(int, input().split())  # N의 의미는 리스트가 해당 문제안에 몇개가 있는 지 알려주는 녀석이다.
        lst = [list(map(int, input().split())) for _ in range(N)]
        # input으로 리스트를 받아와서 공백으로 문자를 나눠준 뒤, map으로 모든 문자를 정수형으로 변환해준다. 그리고 그것을 눈으로 보이는 값으로
        # 남기기위해서, list로 변환해준 뒤, N개 만큼 반복해서 list로 묶어준다.

        row = N  # 행은 그 문제 안에 리스트 갯수와 같다.
        col = len(lst[0])  # 열은 하나의 리스트 안에 몇개의 원소가 있는 지와 같다.

        s = lst[i][j]
        print(s)

        # for i in range(row):
        #     for j in range(col):
        #         if 0 <= i < M and 0 <= j < M:
        #             s += lst[i][j]

    # 파리퇴치
