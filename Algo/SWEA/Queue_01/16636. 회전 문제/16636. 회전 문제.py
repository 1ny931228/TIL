import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    for _ in range(M):
        add_num = Q.pop(0)
        Q.append(add_num)

    print(f'#{t} {Q[0]}')