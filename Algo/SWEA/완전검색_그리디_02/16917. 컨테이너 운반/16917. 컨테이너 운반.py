import sys
sys.stdin = open('sample_input(2).txt')
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split())) # N개의 화물 무게
    ti = list(map(int, input().split())) # M개의 트럭의 적재용량

    result = 0

    print(f'#{t} {result}')