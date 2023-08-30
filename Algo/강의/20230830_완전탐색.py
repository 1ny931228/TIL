def f(i, N, card): # i 이전에 고른 개수, N개에서 K개를 고르는 순열
    global cnt
    if i == N: # 순열 완성 : K개를 모두 고른 경우
        cnt += 1
        print(cnt, p)
        return
    else: # card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0: # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0


card = list(map(int, input()))
used = [0] * 6 # 이미 사용한 카드인지 표시
p = [0] * 6
f(0, 6)


# 5개 숫자 중 3개만 고르는 경우
card = [1, 2, 3, 4, 5]
N = 5 # N개의 숫자에서
K = 3 # K개의 숫자를 고르는 경우
used = [0] * 5 # 이미 사용한 카드인지 표시
p = [0] * 3
f(0, 5, 3)
cnt = 0