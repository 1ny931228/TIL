import sys
sys.stdin = open('sample_input(4).txt')

T = int(input())

def babygin(counts, index):
    if counts[index] == 3:
        return 1
    # print(index, index-1, index-2)
    for i in (index, index-1, index-2):
        if 0 <= i <= 7 and counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            return 1
    return 0


for t in range(1, T+1):
    lst = list(map(int,input().split()))
    countP1 = [0] * 10
    countP2 = [0] * 10

    result = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            # print(lst[i], 1)
            # print(countP1, 1)
            countP1[lst[i]] += 1
            # print(countP1, 2)
            if babygin(countP1,lst[i]):
                result = 1
                break
        else:
            # print(lst[i])
            countP2[lst[i]] += 1
            if babygin(countP2,lst[i]):
                result = 2
                break

    print(f'#{t} {result}')