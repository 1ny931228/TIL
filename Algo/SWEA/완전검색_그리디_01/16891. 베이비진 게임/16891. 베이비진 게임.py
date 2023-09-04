import sys
sys.stdin = open('sample_input(4).txt')

cnt = 0
def f(i, N, cards): # i 이전에 고른 개수, N개에서 K개를 고르는 순열
    global cnt
    if i == N: # 순열 완성 : K개를 모두 고른 경우
        print(p)
        return
    else:
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이면
                p[i] =cards[j]
                used[j] = 1
                f(i+1, N, cards)
                used[j] = 0
def babygin(): # 함수명은 역할이 하나인 것이 최고이다. isWinner이라고 지으면 역할이 하나인 뚜렷한 함수가 된다. 
    pass
T = int(input())

for t in range(1, T+1):
    cards = list(map(int, input().split()))

    # print(t, cards)

    player1 = []
    player2 = []

    used = [0] * 6
    p = [0] * 6

    for i in range(len(cards)):
        if i == 0 or i % 2 == 0: # if i % 2
            player1.append(cards[i])
        elif i % 2 == 1:
            player2.append(cards[i])

    # print(player1, player2)
    f(0, 6, cards)

    # print(cards)

    print(f'#{t} {WoL}')


