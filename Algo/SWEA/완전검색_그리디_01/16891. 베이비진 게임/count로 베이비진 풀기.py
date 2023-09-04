import sys
sys.stdin = open('sample_input(4).txt')

def isWinner(counts, index):
    if counts[index] == 3:# triplet 검사
        return 1
    for i in (index, index-1, index-2): # run 검사
        if 0 <= i <= 7 and counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            return 1

T = int(input())

for t in range(1, T+1):
    cards = list(map(int, input().split()))

    cnt_player1 = [0] * 10 # player1이 받은 카드가 숫자당 몇개인지 알 수 있는 리스트를 만들기
    cnt_player2 = [0] * 10

    # player에게 카드 나눠주기

    result = 0

    for i in range(len(cards)):
        if i % 2 == 0:
            cnt_player1[cards[i]] += 1
            if isWinner(cnt_player1, cards[i]):
                result = 1
                break


        else:
            cnt_player2[cards[i]] += 1
            if isWinner(cnt_player2, cards[i]):
                result = 2
                break

    # print(cnt_player1, 1)
    # print(cnt_player2, 2)

    print(f'#{t} {result}')